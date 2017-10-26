import os

from app import create_app, db
from app.models import City, Country, Continent, add_data_from_csv
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
  return dict(app=app, db=db, Country=Country, City=City)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command('add_csv', add_data_from_csv)

if __name__ == '__main__':
  manager.run()