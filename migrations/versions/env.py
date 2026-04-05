from logging.config import fileConfig
from flask import current_app

from alembic import context
from app import db, create_app

config = context.config
fileConfig(config.config_file_name)

target_metadata = db.metadata

def run_migrations_online():
    app = create_app()

    with app.app_context():
        connectable = db.engine

        with connectable.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=target_metadata
            )

            with context.begin_transaction():
                context.run_migrations()

run_migrations_online()