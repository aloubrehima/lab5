from peewee import *

db = SqliteDatabase('peewee.sqlite')

# Define the Peewee model for the database table
class Record(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.name}, {self.country}, {self.catches}'


db.connect()
db.create_tables([Record])

janne_mustonen = Record(name = 'Janne Mustonen', country = 'Finland', catches = '98')
janne_mustonen.save()

ian_stewart = Record(name = 'Ian Stewart', country = 'Canada', catches = '94')
ian_stewart.save()

aaron_gregg = Record(name = 'Aaron Greg', country = 'Canada', catches = '88')
aaron_gregg.save()

chad_taylor = Record(name = 'Chad Taylor', country = 'USA', catches = '78')
chad_taylor.save()

def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    records = Record.select()
    for record in records:
        print('record')


def search_by_name():
    name = input("Enter a name to search: ")
    record = Record.select().where(Record.name == name).first()
    if record:
        print(record)
    else:
        print('Record not found')


def add_new_record():
    name = input("Enter the new name: ")
    country = input("Enter the country: ")
    catches = int(input("Enter the number of catches: "))
    try:
        Record.create(name=name, country=country, catches=catches)
        print("Record added!")
    except IntegrityError:
        print("Record already exists.")


def edit_existing_record():
    name = input("Enter the name of the record to edit: ")
    record = Record.select().where(Record.name == name).first()
    if record:
        new_catches = int(input("Enter the new number of catches: "))
        record.catches = new_catches
        record.save()
        print("Record edited successfully.")
    else:
        print("Record not found. Cannot edit.")


def delete_record():
    name = input("Enter the name of the record to delete: ")
    record = Record.select().where(Record.name == name).first()
    if record:
        record.delete_instance()
        print("Record deleted successfully.")
    else:
        print("Record not found. Cannot delete.")


if __name__ == '__main__':
    main()

