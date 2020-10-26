import time

import click

from backend.databases import Postgres
from backend.databases import postgres as postgres_models
from config import BaseConfig


@click.group()
def cli():
    pass


@cli.command(short_help='Get Users ')
def get_users():
    postgres_db = Postgres(uri=BaseConfig.POSTGRES_URI)

    while True:
        session = postgres_db.start_session()
        users = session.query(postgres_models.User).all()
        session.close()
        for u in users:
            print('User %s, name %s' % (u.id, u.name))
        time.sleep(5)
