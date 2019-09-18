import pickle
import json
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

from settings import POSTGRES_DB_STRING

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


def persist_settings_to_db(from_file):
    with open(from_file, "rb") as f:
        settings = pickle.load(f)

    for user in settings['user_data']:
        db_user = session.query(UserSettings).filter_by(chat_id=user)
        options = json.dumps(settings['user_data'][user])
        if db_user.first():
            db_user.update(values={UserSettings.user_settings: options})
            session.commit()
        else:
            entry = UserSettings(chat_id=user, user_settings=options)
            try:
                session.add(entry)
                session.commit()
            except:
                session.rollback()
