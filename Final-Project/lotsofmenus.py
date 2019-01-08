from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Products, Base, Item

engine = create_engine('sqlite:///products.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for UrbanBurger


# Menu for Super Stir Fry
products2 = Products(name="Clothings")

session.add(products2)
session.commit()


Item1 = Item(name="T-shirt", description="it is used for feel comfort",
                     price="9000",products=products2)

session.add(Item1)
session.commit()

Item2 = Item(name="Jeans", description=" jeans pant",
 price="500",  products=products2)

session.add(Item2)
session.commit()

Item3 = Item(name="Shirts", description=" shirtsnormall ",
                     price="500", products=products2)

session.add(Item3)
session.commit()

Item4 = Item(name="Shorts ", description=" shorts for comfort ",
                     price="200", products=products2)

session.add(Item4)
session.commit()

Item5 = Item(name="sportswear", description=" sports wear t-shirt",
                     price="400", products=products2)

session.add(Item5)
session.commit()

Item6 = Item(name="Tourser", description=" tourser which is used for pants.",
                     price="500", products=products2)

session.add(Item6)
session.commit()


# Menu for Panda Garden
products1 = Products(name="Acessories")

session.add(products1)
session.commit()


Item1 = Item(name="Watches", description=" differnt watches",
                     price="8000", products=products1)

session.add(Item1)
session.commit()

Item2 = Item(name="Bags", description=" types of Bags",
                     price="7000", products=products1)

session.add(Item2)
session.commit()

Item3 = Item(name="Sunglasses", description=" Sunglasses",
                     price="8000",products=products1)

session.add(Item3)
session.commit()

Item4 = Item(name="Suitcase", description="it is typesof suitcases",
                     price="9000",products=products1)

session.add(Item4)
session.commit()

Item2 = Item(name="Wallet", description=" It is type of purses",
                     price="350", products=products1)

session.add(Item2)
session.commit()


# Menu for Thyme for that
products1 = Products(name="Westernwears ")

session.add(products1)
session.commit()


Item1 = Item(name="Scarves", description="Scarves which is used wear gents and ladies",
                     price="200",  products=products1)

session.add(Item1)
session.commit()

Item2 = Item(name="Belts", description="Belts",
                     price="500",  products=products1)

session.add(Item2)
session.commit()

Item3 = Item(name="Hand bags", description="hand bags",
                     price="500", products=products1)

session.add(Item3)
session.commit()

Item4 = Item(name="Hats" ,description="Hts wear of heads",
                     price="9500", products=products1)

session.add(Item4)
session.commit()



# Menu for Tony's Bistro
products1 = Products(name="Ladies Foot wear ")

session.add(products1)
session.commit()


Item1 = Item(name="Heels", description="heels ",
                     price="1395",products=products1)

session.add(Item1)
session.commit()

Item2 = Item(name="sportsladies", description="sports shoes",
                     price="495",products=products1)

session.add(Item2)
session.commit()

Item3 = Item(name="flipflops", description="ladies flipflops",
                     price="$6.95",products=products1)

session.add(Item3)
session.commit()



# Menu for Andala's
products1 = Products(name="LapTops")

session.add(products1)
session.commit()


Item1 = Item(name="Lenovo", description="lenovo which is one of the same brand",
                     price="46,000", products=products1)

session.add(Item1)
session.commit()

Item2 = Item(name="DELL", description="Dell which is one of the high cost laptop",
                     price="50,000", products=products1)

session.add(Item2)
session.commit()

Item3 = Item(name="HP", description="hp which is one of the brand in the laptop",
                     price="60,000", products=products1)

session.add(Item3)
session.commit()

Item4 = Item(name="acer", description="acer which is use",
                     price="16750",  products=products1)

session.add(Item4)
session.commit()

Item2 = Item(name="Apple", description="one of the brand in laptop",
                     price="700", products=products1)

session.add(Item2)
session.commit()


# Menu for Auntie Ann's
products1 = Products(name="Phone")

session.add(products1)
session.commit()

Item9 = Item(name="Samsung", description="samsung phone which is  gobal",
                     price="89900", products=products1)

session.add(Item9)
session.commit()


Item1 = Item(name="nokia", description="nokia Phone",
                     price="20099",  products=products1)

session.add(Item1)
session.commit()

Item2 = Item(name="MotoG3", description="Moto Phone its a type of phone ",
                     price="13000",  products=products1)

session.add(Item2)
session.commit()

Item3 = Item(name=" Miphone", description=" Miphone are also called as a RedmiNote5pro",
                     price="7550", products=products1)

session.add(Item3)
session.commit()

Item4 = Item(name="Lenova", description=" Lenova",
                     price="8950",products=products1)

session.add(Item4)
session.commit()

Item2 = Item(name="Appleiphone", description="Apple i phone",
                     price="9650",products=products1)

session.add(Item2)
session.commit()

Item10 = Item(name="Redmi", description="Redmi",
                      price="1799",products=products1)

session.add(Item10)
session.commit()


# Menu for Cocina Y Amor
products1 = Products(name="Home furniture")

session.add(products1)
session.commit()


Item1 = Item(name="Beds", description="Beds of home ",
                     price="5095",products=products1)

session.add(Item1)
session.commit()

Item2 = Item(name="Sofas", description="Sofas with smooth ",
                     price="7099",products=products1)

session.add(Item2)
session.commit()

products1 = Products(name="Wall Stickers")
session.add(products1)
session.commit()

Item1 = Item(name="Redwallstickers", description="wall stickers",
                     price="5095", products=products1)

session.add(Item1)
session.commit

Item1 = Item(name="Photowalls", description="Photowalls",
                     price="695",products=products1)

session.add(Item1)
session.commit()


Item1 = Item(name="Carpets and doormates", description="carpets and doormates which is used for living comfort",
                     price="425", products=products1)

session.add(Item1)
session.commit()


print ("added menu items!")
