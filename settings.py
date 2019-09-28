from os import environ


# Bot specific settings
BOT_ACTIONS = [
    'minprice',
    'maxprice',
    'minfloor',
    'maxfloor',
    'minsurface',
    'maxsurface',
    'minrooms',
    'maxrooms',
]
BOT_ACTIONS_TO_HUMAN = {
    'minprice': 'Minimum price: ',
    'maxprice': 'Maximum price: ',
    'minfloor': 'Lowest floor: ',
    'maxfloor': 'Highest floor: ',
    'minsurface': 'Minimum surface (in sqm) ',
    'maxsurface': 'Maximum surface (in sqm) ',
    'minrooms': 'Minimum number of rooms: ',
    'maxrooms': 'Maximum number of rooms: ',
}
BOT_TOKEN = environ.get('BOT_TOKEN')

# DB persistence settings
WITH_DB_PERSISTENCE = True
PERSISTENCE_FILE = 'settings.pickle'

POSTGRES_USER = environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = environ.get('POSTGRES_PORT')
POSTGRES_DB = environ.get('POSTGRES_DB')
POSTGRES_DB_STRING = 'postgres://{user}:{password}@{host}:{port}/{db}'.format(
  user=POSTGRES_USER,
  password=POSTGRES_PASSWORD,
  host=POSTGRES_HOST,
  port=POSTGRES_PORT,
  db=POSTGRES_DB
)
