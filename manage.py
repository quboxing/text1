from flask_script import Manager
from zhuhanshu import app
from exts import db
from models import User,Text
from flask_migrate import MigrateCommand,Migrate
manager=Manager(app)
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)
if __name__=='__main__':
    manager.run()
