# AirBnB console - MySQL

- [SQLAlchemy](#SQLAlchemy)

## SQLAlchemy

### Step 1: Installation
First, you need to install SQLAlchemy. You can do this using pip:
```sh
pip install SQLAlchemy
```
### Step 2: Connecting to a Database
To start using SQLAlchemy, you need to create an engine that manages the connection to the database. Here's an example of how to connect to a SQLite database:
```py
from sqlalchemy import create_engine

# Create an engine
engine = create_engine('sqlite:///example.db')
```

### Step 3: Defining a Schema
To define your database schema, you need to define Python classes that represent your database tables. Each class will inherit from declarative_base:
```py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Create a base class
Base = declarative_base()

# Define a User class that represents a table in the database
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create all tables in the engine
Base.metadata.create_all(engine)
```

### Step 4: Creating a Session
To interact with the database, you need to create a session. The session will be used to execute queries and persist changes to the database:
```py
from sqlalchemy.orm import sessionmaker

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
```

### Step 5: Adding Data to the Database
You can add data to the database by creating instances of your classes and adding them to the session:
```py
# Create a new user
new_user = User(name='John Doe', age=30)

# Add the user to the session
session.add(new_user)

# Commit the session to save the changes
session.commit()
```

### Step 6: Querying the Database
You can query the database to retrieve data using the session:

```py
# Query all users
users = session.query(User).all()
for user in users:
    print(user.name, user.age)

# Query a specific user
user = session.query(User).filter_by(name='John Doe').first()
print(user.name, user.age)
``` 

### Step 7: Updating Data
To update data in the database, modify the object and commit the changes:
```py
# Update a user's age
user = session.query(User).filter_by(name='John Doe').first()
user.age = 31

# Commit the session to save the changes
session.commit()
```

### Step 8: Deleting Data
To delete data from the database, remove the object from the session and commit the changes:
```py
# Delete a user
user = session.query(User).filter_by(name='John Doe').first()
session.delete(user)

# Commit the session to save the changes
session.commit()
```

### Full Example
Here's a complete example putting everything together:
```py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine
engine = create_engine('sqlite:///example.db')

# Create a base class
Base = declarative_base()

# Define a User class that represents a table in the database
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a new user
new_user = User(name='John Doe', age=30)

# Add the user to the session
session.add(new_user)

# Commit the session to save the changes
session.commit()

# Query all users
users = session.query(User).all()
for user in users:
    print(user.name, user.age)

# Update a user's age
user = session.query(User).filter_by(name='John Doe').first()
user.age = 31
session.commit()

# Delete a user
user = session.query(User).filter_by(name='John Doe').first()
session.delete(user)
session.commit()
```



