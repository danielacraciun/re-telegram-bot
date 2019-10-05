import pickle
import json
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

from settings import POSTGRES_DB_STRING, PERSISTENCE_FILE

engine = sa.create_engine(POSTGRES_DB_STRING)
base = declarative_base()


class UserSettings(base):
    __tablename__ = 'telegram_bot_user_settings'

    chat_id = sa.Column(sa.Integer, nullable=False, primary_key=True)
    user_settings = sa.Column(sa.String)


def get_postgres_session():
    base.metadata.create_all(engine)
    Session = sa.orm.sessionmaker(engine)
    return Session()


session = get_postgres_session()


def update_or_create_user_options(user, options):
    db_user = session.query(UserSettings).filter_by(chat_id=user)

    if db_user.first():
        db_user.update(values={UserSettings.user_settings: options})
        session.commit()
        return True
    else:
        entry = UserSettings(chat_id=user, user_settings=options)
        try:
            session.add(entry)
            session.commit()
        except:
            session.rollback()
        return False


def persist_settings_to_db(user):
    with open(PERSISTENCE_FILE, "rb") as f:
        settings = pickle.load(f)

    options = json.dumps(settings['user_data'].get(user), {})
    update_or_create_user_options(user, str(options))
