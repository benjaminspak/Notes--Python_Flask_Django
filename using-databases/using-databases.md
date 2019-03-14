### Using Databases with Python

##### Peewee ORM

+ ORM = Object Relational Mapping
+ pip install peewee
+ Models in Peewee are Python classes
    + Each column in the table is a attribute on the model class.

```python
# student.py
from peewee import *
db = SqliteDatabase('students.db')

class Student(Model):
    username = CharField(max_length=255, uniquie=True)
    points = IntegerField(default=0)

    class Meta:
        database = db

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)

```

Looking into the database.

```

$ python student.py
# Creates student.db

$ sqlite3 students.db
# Accesses the database vs sqlite

# Exploring the database
sqlite> .tables
student
sqlite> select * from student;
sqlite>  # We've entered nothing so the return is blank.
sqlite> .exit  # To exit sqlite3
```

##### Making Queries

+ .create() - creates a new instance all at once.
+ .select() - finds records in a table.
+ .save() - updates an existing row in the database.
+ .get() - finds a single record in a table.
+ .delete_instance() - deletes a single record from the table.
+ .order_by() - specify how to sort the records.
+ if __name__ == '__main__' - a common pattern for making code only run when the script is run and not when it's imported.

```python
# student.py
from peewee import *
db = SqliteDatabase('students.db')

class Student(Model):
    username = CharField(max_length=255, uniquie=True)
    points = IntegerField(default=0)

    class Meta:
        database = db

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()

students = [
    {'username': 'kennethlove',
    'points': 4888},
    {'username': 'chalkers',
    'points': 11913},
    {'username': 'joykesten2',
    'points': 7363},
    {'username': 'craigsdennis',
    'points': 4079},
    {'username': 'davemcfarland',
    'points': 14717}
]

# Create a user entry in a database for each student in the students list.
def add_students():
    for student in students:
        Student.create(username=student['username'],
                        points=student['points'])

```