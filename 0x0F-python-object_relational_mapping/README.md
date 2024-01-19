0x0F-python-object_relational_mapping

What ORM means
ORM stands for Object-Relational Mapping. It is a programming technique for converting data between incompatible type systems, such as converting data between a relational database and an object-oriented programming language. In the context of databases, an ORM allows you to interact with a database using the object-oriented paradigm of your programming language, abstracting away the underlying SQL queries.

How to map a Python Class to a MySQL table
Using an ORM like SQLAlchemy, you can map a Python class to a MySQL table. Here's a simplified example:

python
Copy code
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the Python class
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Create an SQLite database in memory (you can replace with your MySQL connection string)
engine = create_engine('sqlite:///:memory:')

# Create the table
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Use the User class to interact with the 'users' table
new_user = User(name='John Doe', age=30)
session.add(new_user)
session.commit()

# Query the database
queried_user = session.query(User).filter_by(name='John Doe').first()
print(queried_user.name, queried_user.age)
