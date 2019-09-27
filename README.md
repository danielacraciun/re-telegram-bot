# re-telegram-bot
real estate (but not only) notifications telegram bot 🤖

What it does?
Defines actions which concern real estate ad properties:
```
# Currently defined actions
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
```
and the bot takes slash commands like: `/setminprice 200`

Persists the values to a database defined in `settings.py`:
```
POSTGRES_USER = environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = environ.get('POSTGRES_PORT')
POSTGRES_DB = environ.get('POSTGRES_DB')
```
So make sure to set these in the environment by using: `export POSTGRES_USER=<your user`

The bot also allows you to see current settings with: `/settings`

Clear a setting with: `/clear <action>`

Persist your current settings and start receiving events with `/subscribe`

Set it and forget it with: `nohup python bot.py &`
