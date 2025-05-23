# Databases with SQLAlchemy

This is an example of how to work with databases (in this example we use a SQLite database) using the SQLAlchemy Python package. The example hows how to set up a database for tracking financial transactions in several accounts (account movements).

## Creating models

In the following example we want to create:

- A `User` model.
- Each `User` may have various `Account`s.
- The `Account` is associated to a single user.
- Each `Account` has many `Movement`s. These represent the transactions of currency in and out of each account.
- Each `Movement` belongs to a single `Account`.
- Each `Movement` may be categorized with a `Category` and a `Subcategory`.
- The `Subcategory` cannot repeat for the same `Category`.

```python
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    accounts = relationship("Account", back_populates="user", cascade="all, delete-orphan")


class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="accounts")

    movements = relationship("Movement", back_populates="account", cascade="all, delete-orphan")


class Movement(Base):
    __tablename__ = "movements"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    description = Column(String)
    debit = Column(Float)
    credit = Column(Float)
    
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    account = relationship("Account", back_populates="movements")

    category_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    category = relationship("Category", back_populates="movements")

    subcategory_id = Column(Integer, ForeignKey('subcategories.id'), nullable=True)
    subcategory = relationship("Subcategory", back_populates="movements")

    shared = Column(Boolean, default=False, nullable=False)


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    subcategories = relationship("Subcategory", back_populates="category", cascade="all, delete-orphan")
    movements = relationship("Movement", back_populates="category")


class Subcategory(Base):
    __tablename__ = "subcategories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="subcategories")

    movements = relationship("Movement", back_populates="subcategory")

    # Make so a subcategory cannot repeat within a category but can across categories
    __table_args__ = (
        UniqueConstraint('name', 'category_id', name='uix_name_category'),
    )
```


## Connecting to the database

Let's connect to the database now. In the following, we if the database already exists and if it doesn't, we create it.

```python
from pathlib import Path
from sqlalchemy.orm import sessionmaker


db_path = Path('database.db')

first_time = not db_path.exists()  # False if DB exist, otherwise True (first time connecting)

engine = create_engine(f"sqlite:///{db_path}", echo=False)

# If this is the first time connecting create all tables
if first_time:
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()
```


## Adding data to the database

Adding a single `User`. The code avoids adding a user if another exists with the same name.

```python
USERNAME = 'John'

user = session.query(User).filter_by(name=USERNAME).first()  # returns None if no user with name John exists.

# Add user if it doesn't exist
if not user:
    user = User(name=USERNAME)
    session.add(user)
    print(f"Created User <{user.name}>.")
```

Adding rows from a Pandas dataframe. We assume `Account`s, `Category`s, and `Subcategory`s have already been added.

```python 
# We assume we have a dataframe called df

for i, row in df.iterrows():
    # Find account
    account = session.query(Account).filter_by(name=row['Account']).first()

    # Find category and subcategory
    if pd.isna(row["Category"]):  # We want NaN values in the dataframe to translate to NULL values in the database
        category = None
        subcategory = None

    else:
        category = session.query(Category).filter_by(name=row["Category"]).first()
    
        if pd.isna(row["Subcategory"]):
            subcategory = None
        else:
            subcategory = session.query(Subcategory).filter_by(name=row["Subcategory"], category=category).first()

    # Create movement
    movement = Movement(
            date=row['Date'],
            description=row['Description'],
            debit=row['Debit'],
            credit=row['Credit'],
            account=account,
            category=category,
            subcategory=subcategory
        )
    session.add(movement)

# Commit all new items to the database. Including the user from above,
session.commit()
```

## References

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)
