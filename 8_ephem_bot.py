"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot2.log', level=logging.INFO)


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def say_planet(update, context):
    user_text = update.message.text
    planet = user_text.split()[1]
    if planet == 'Mercury':
        merc = ephem.Mercury('2024/23/05')
        constellation = ephem.constellation(merc)
        update.message.reply_text(constellation[1])
    if planet == 'Venus':
        ven = ephem.Venus('2024/23/05')
        constellation = ephem.constellation(ven)
        update.message.reply_text(constellation[1])
    if planet == 'Mars':
        mars = ephem.Mars('2024/23/05')
        constellation = ephem.constellation(mars)
        update.message.reply_text(constellation[1])
    if planet == 'Jupiter':
        jup = ephem.Jupiter('2024/23/05')
        constellation = ephem.constellation(jup)
        update.message.reply_text(constellation[1])
    if planet == 'Saturn':
        satu = ephem.Saturn('2024/23/05')
        constellation = ephem.constellation(satu)
        update.message.reply_text(constellation[1])
    if planet == 'Neptune':
        nep = ephem.Neptune('2024/23/05')
        constellation = ephem.constellation(nep)
        update.message.reply_text(constellation[1])
    else:
        update.message.reply_text('Введите правильное название планеты')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", say_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
