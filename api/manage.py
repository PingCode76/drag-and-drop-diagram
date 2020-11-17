#from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import app, db


manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()



# error [root] Error: Can't locate revision identified by 'xxxxxxxx'   :   DROP TABLE  alembic_version CASCADE; 