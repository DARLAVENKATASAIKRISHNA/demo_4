from flask import Flask
app = Flask(__name__)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Products, Item

engine = create_engine('sqlite:///products.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/products/')
def productsMenu(products_id):
    products = session.query(Products).first()
    items = session.query(MenuItem).filter_by(products_id=products.id)
    return render_template('menu.html',products)
    #Task 1: Create route for newmenuItem function here
    @app.route('/products/<int:products_id>/new/',methods=['GET','POST'])
    def newMenuItem(products_id):
    	if request.method == 'POST':
    		newItem = MenuItem(name=request.form['name'],products_id = products_id)
    		session.add(newItem)
    		session.commit()
    	return redirect(url_for('productsMenu',restaurant_id=restaurant_id))

    	return "page to create a new menu item. Task 1 complete!"
    #Task 2:  Create route for editMenuItem function here
    @app.route('/restaurant/<int:restaurant_id/<int:menu_id>/edit/',methods='GET','POST')
    def editMenuItem(restaurant_id,menu_id):
    	editedItem = session.query(MenuItem).filter_by(id = menu_id).one()
    	if request.method == 'POST':
    		if request.form['name']:
    			editedItem.name = request.form['name']
    			session.add(editedItem)
    			session.commit()
    			return redirect(url_for['restaurantMenu',restaurant_id=restaurant_id])
    		else:
    			return render_template('editmenuitem.html',restaurant_id=restaurant_id,menu_id, i = editedItem)
     
     return "page to edit a new item.Task2 complete!"
    #Task 3:  Create a route for deleteMenuItem function here
    @app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/',methods=['GET','POST'])
    def deleteMenuItem(restaurant_id,menu_id):
    	itemToDelete = session.query(MenuItem).filter_by(id = menu_id).one()
    	if request.method == 'POST':
    		session.delete(itemToDelete)
    		session.commit()
    		return redirect(url_for('restaurantMenu',restaurant_id=restaurant_id)
    	else:
    		return render_template('deleteItem.html' i=itemToDelete)
        return "page to delete a new menu item. Task3 complete!" 	
if __name__ =='__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
