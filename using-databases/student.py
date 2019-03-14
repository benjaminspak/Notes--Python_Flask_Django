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