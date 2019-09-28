import logging

from functools import partial
from telegram.ext import Updater, CommandHandler, PicklePersistence

from db_wrapper import persist_settings_to_db, update_or_create_user_options
from settings import PERSISTENCE_FILE, BOT_TOKEN, BOT_ACTIONS, BOT_ACTIONS_TO_HUMAN

logger = logging.getLogger(__name__)


def put(update, context, key, value):
    context.user_data[key] = value
    update.message.reply_text('{} set to {}'.format(key, value))


def set_attribute(update, context, attr):
    value = update.message.text.partition(' ')[2]
    if value:
        put(update, context, attr, int(value))
    else:
        update.message.reply_text('Usage: /set{} <value>'.format(attr))


def settings(update, context):
    ud = context.user_data
    msg = ''.join(['{}: {}\n'.format(BOT_ACTIONS_TO_HUMAN.get(k, ''), ud[k]) for k in ud.keys()]) if ud else 'No settings'
    update.message.reply_text(msg)


def clear(update, context):
    value = update.message.text.partition(' ')[2]
    if value:
        if context.user_data.get(value):
            context.user_data.pop(value)
        else:
            update.message.reply_text('{} not set'.format(value))
    else:
        update.message.reply_text('Usage: /clear <attribute>')

    update.message.reply_text('{} cleared'.format(value))


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def subscribe(update, context):
    current_user = update.message.chat_id
    persist_settings_to_db(current_user)
    update.message.reply_text(
        'Settings saved! You will receive rental ads with the given settings. '
        'If you change something, you need to run /subscribe again!'
    )


def unsubscribe(update, context):
    current_user = update.message.chat_id
    updated = update_or_create_user_options(current_user, {})
    msg = 'You have been unsubscribed.' if updated else 'You are not even subscribed!'
    update.message.reply_text(msg)


if __name__ == '__main__':
    logger.info('Starting up bot...')
    p = PicklePersistence(filename=PERSISTENCE_FILE, store_user_data=True)
    updater = Updater(BOT_TOKEN, use_context=True, persistence=p)
    dp = updater.dispatcher
    for action in BOT_ACTIONS:
        dp.add_handler(CommandHandler('set{}'.format(action), partial(set_attribute, attr=action)))

    dp.add_handler(CommandHandler('settings', settings))
    dp.add_handler(CommandHandler('clear', clear))
    dp.add_handler(CommandHandler('subscribe', subscribe))
    dp.add_handler(CommandHandler('unsubscribe', unsubscribe))
    dp.add_error_handler(error)

    logger.info('Done! Awaiting commands.')
    updater.start_polling()
    updater.idle()
