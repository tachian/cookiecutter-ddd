from flask.cli import with_appcontext
from {{cookiecutter.directory_name}}.app import db


@with_appcontext
def drop_create_tables():
    db.session.commit()
    db.drop_all()
    db.create_all()
    db.session.commit()
