from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Products, Item

app = Flask(__name__)

engine = create_engine('sqlite:///products.db', connect_args = {'check_same_thread': False}, echo = True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Fake Restaurants
# restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

# restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


# Fake Menu Items
# items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
# item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}
# items = []


'''@app.route('/products/<int:products_id>/menu/JSON')
def productsJSON(products_id):
    products = session.query(Products).filter_by(id=products_id).one()
    items = session.query(Item).filter_by(
        products_id=products_id).all()
    return jsonify(Items=[i.serialize for i in items])


@app.route('/products/<int:products_id>/item/<int:item_id>/JSON')
def ItemJSON(products_id, item_id):
    Item = session.query(Item).filter_by(id=item_id).one()
    return jsonify(Item=Item.serialize)

@app.route('/products/JSON')
def productsJSON():
    products = session.query(Products).all()
    return jsonify(products=[r.serialize for r in products])'''


# Show all restaurants
@app.route('/')
@app.route('/products/')
def showProducts():
    products = session.query(Products).all()
    # return "This page will show all my restaurants"
    return render_template('products.html', products=products)


# Create a new restaurant
@app.route('/products/new/', methods=['GET', 'POST'])
def newProducts():
    if request.method == 'POST':
        newProducts = Products(name=request.form['name'])
        session.add(newProducts)
        session.commit()
        return redirect(url_for('showProducts'))
    else:
        return render_template('newProducts.html')
    # return "This page will be for making a new restaurant"

# Edit a restaurant


@app.route('/products/<int:products_id>/edit/', methods=['GET', 'POST'])
def editProducts(products_id):
    editedProducts = session.query(
        Products).filter_by(id=products_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedProducts.name = request.form['name']
            return redirect(url_for('showProducts'))
    else:
        return render_template(
            'editProducts.html', products=editedProducts)

    # return 'This page will be for editing restaurant %s' % restaurant_id

# Delete a restaurant


@app.route('/products/<int:products_id>/delete/', methods=['GET', 'POST'])
def deleteProducts(products_id):
    productsToDelete = session.query(
        Products).filter_by(id=products_id).one()
    if request.method == 'POST':
        session.delete(productsToDelete)
        session.commit()
        return redirect(
            url_for('showProducts'))
    else:
        return render_template(
            'deleteProducts.html', products=productsToDelete)
    # return 'This page will be for deleting restaurant %s' % restaurant_id


# Show a restaurant menu
@app.route('/products/<int:products_id>/')
@app.route('/products/<int:products_id>/menu/')
def showMenu(products_id):
    products = session.query(Products).filter_by(id=products_id).one()
    items = session.query(Item).filter_by(
        products_id=products_id).all()
    return render_template('item.html', items=items, products=products)
    # return 'This page is the menu for restaurant %s' % restaurant_id

# Create a new menu item


@app.route(
    '/products/<int:products_id>/menu/new/', methods=['GET', 'POST'])
def showItems(products_id):
    product = session.query(Products).filter_by(id = products_id).one()
    if request.method == 'POST':
        newItem = Item(name=request.form['name'], description=request.form[
                           'description'], price=request.form['price'],  products_id=products_id)
        session.add(newItem)
        session.commit()

        return redirect(url_for('showMenu', products_id=products_id))
    else:
        return render_template('newItem.html', products_id=products_id)

    #return render_template('newItem.html', products=products)
    # return 'This page is for making a new menu item for restaurant %s'
    # %restaurant_id

# Edit a menu item


@app.route('/products/<int:products_id>/<int:menu_id>/edit',
           methods=['GET', 'POST'])
def editMenuItem(products_id, menu_id):
    editedItem = session.query(Item).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['name']
        if request.form['price']:
            editedItem.price = request.form['price']
        
        session.add(editedItem)
        session.commit()
        return redirect(url_for('showMenu', products_id=products_id))
    else:

        return render_template(
            'edititem.html', products_id=products_id, item_id=menu_id, item=editedItem)

    # return 'This page is for editing menu item %s' % menu_id

# Delete a menu item


@app.route('/products/<int:products_id>/menu/<int:menu_id>/delete',
           methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    itemToDelete = session.query(Item).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showMenu', products_id=products_id))
    else:
        return render_template('deleteitem.html', item=itemToDelete)
    # return "This page is for deleting menu item %s" % menu_id


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)
