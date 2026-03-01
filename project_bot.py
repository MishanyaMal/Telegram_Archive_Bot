import logging
import telebot

from config_reader import config
from handlers import commands

bot = telebot.TeleBot(
    token=config.BOT_TOKEN.get_secret_value()
)

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    commands.register_handlers(bot)

    return bot.polling(none_stop=True)

if __name__ == '__main__':
	main()
