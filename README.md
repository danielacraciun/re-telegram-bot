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
So make sure to set these in the environment by using: `.env`

The bot also allows you to see current settings with: `/settings`

Clear a setting with: `/clear <action>`

Persist your current settings and start receiving events with `/subscribe`

Set it and forget it with: `nohup python bot.py &` or just `python bot.py`

Send following commands to botfather with `/setcommands`:
```
setminprice - Minimum price for a rental
setmaxprice - Maximum price for a rental
setminsurface - Minimum surface for a rental
setmaxsurface - Maximum surface for a rental
setminrooms - Minimum number of rooms for a rental
setmaxrooms - Maximum number of rooms for a rental
setminfloor - Minimum floor level for a rental
setmaxfloor - Maximum surface for a rental
settings - See current settings
clear - Clear setting for given attribute
subscribe - Start getting rentals according to settings
unsubscribe - Stop getting rentals
```
