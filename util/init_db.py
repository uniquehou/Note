from apps.models import *
from Note.settings import settings
from peewee import MySQLDatabase

def main():
    database = MySQLDatabase(**settings['db'])
    database.create_tables([Note, ])
    database.close()

if __name__ == '__main__':
    main()
