# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
# from flask_script._compat import text_type

from app import app
from models import db

# migrate = Migrate(app, db)
# manager = Manager(app)

# manager.add_command('db', MigrateCommand)


# if __name__ == '__main__':
#     manager.run()

from flask.cli import FlaskGroup
# from app import app 

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()

