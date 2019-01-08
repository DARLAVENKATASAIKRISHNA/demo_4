from flask import Flask
app = Flask(_name_)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Products, item

engine = create_engine('sqlite:///products.db')
Base.metadata.bind 

@app.route('/')
@app.route('/hello')
def Helloworld():
    return "Hello World"

if _name_ == '_main_':
    app.debug = True
    app.run(host = '0.0.0.0',port= 5000)

