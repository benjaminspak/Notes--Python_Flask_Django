### Using Databases with Python

##### Peewee ORM

+ ORM = Object Relational Mapping

```
pip install peewee
```

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

```bash

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

##### 

+ .create() - creates a new instance all at once
+ .create_tables() - creates a table entry
+ .select() - finds records in a table
+ .save() - updates an existing row in the database
+ .get() - finds a single record in a table
+ .delete_instance() - deletes a single record from the table
+ .order_by() - specify how to sort the records
+ if __name__ == '__main__' - a common pattern for making code only run when the script is run and not when it's imported.

```python
# student.py
from peewee import *
db = SqliteDatabase('students.db')

class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db

students = [
    {'username': 'kennethlove',
    'points': 4888},
    {'username': 'chalkers',
    'points': 11922}
    {'username': 'joykesten2',
    'points': 7363}
    {'username': 'craigsdennis',
    'points': 4079}
    {'username': 'davemcfarland',
    'points': 14717},
]


def add_students():
    for student in students:
        try:  # Create a new user with points in the DB.
            Student.create(username=student['username'],
                            points=student['points'])
        except IntegrityError:  # If the student record already exists, get the record & update their points, then, save the record.
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()

def top_student():  # Select all entries from the student table. Then, sort from largest to smallest points. Then, get the first (greatest) result.
    student = Student.select().order_by(Student.points.dec()).get()
    return student

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print("Our top student right now is: {0.username}".format(top_student()))


```

##### More Models Practice

```python
#!/usr/bin/env python3
import datetime
from peewee import *

db = SqliteDatabase('journal.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)  # We do not need the parens on now, because functions set to default values auto execute.

    class Meta():
        database = db

def initialize():
    """ Create the database and table if they don't exist. """
    db.connect()
    db.create_tables([Entry], safe=True)

def menu_loop():
    """ Show the menu. """

def add_entry():
    """ Add an entry. """

def view_entries():
    """ View previous entries. """

def delete_entry():
    """ Delete an entry. """

if __name__ == '__main__':
    initialize()
    menu_loop()

```

##### Text Input Methods
+ CharField() - Specify the length of characters to be entered
+ TextField() - A non specific length of characters

#### Capturing Inputs from the CLI
+ sys - a Python module that contains functionality fron interacting with the system
+ sys.stdin - a Python object that represents the standard input stream. In most cases, this will be the keyboard
