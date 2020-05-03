from peewee import *

db = PostgresqlDatabase('contacts', user='postgres', password='',host='localhost',port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contacts(BaseModel):
    id = AutoField()
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    phone_number = BigIntegerField()

db.create_tables([Contacts])

