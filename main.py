import telebot
from telebot import types

bot = telebot.TeleBot('5865897537:AAGIxhx7N0ciaAckuLDaPPOhwUQ4aWmKWAE')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    photo_btn = types.InlineKeyboardButton('Мои фотографии', callback_data='photo')
    voice_btn = types.InlineKeyboardButton('Мои голосовые', callback_data='voice')
    source_btn = types.InlineKeyboardButton('Репозиторий с проектом', callback_data='source')
    markup.row(photo_btn, voice_btn)
    markup.row(source_btn)
    bot.send_message(message.chat.id,
                     'Приветствую! Это телеграм бот для тестового задания для Яндекс Практикума. '
                     'Зовут меня Муратшин Борис, мне 19 лет, учусь на 3 курсе УрФУ ИРИТ-РТФ, бакалавриат.'
                     '\nЕсли хотите узнать, как я выгляжу, моё главное увлечение, мои голосовые сообщения на разные'
                     ' темы или получить ссылку на репозиторий, нажмите на соответствующую кнопку.', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_query(callback):
    if callback.data == 'photo':
        markup = types.InlineKeyboardMarkup()
        selfie_btn = types.InlineKeyboardButton('Моё селфи', callback_data='photo_selfie')
        school_btn = types.InlineKeyboardButton('Фотография с 11 класса', callback_data='photo_school')
        markup.row(selfie_btn, school_btn)
        bot.send_message(callback.message.chat.id, 'Вообще я не люблю фотографироваться, но несколько фотографий'
                                                   ' себя-любимого я всё же имею. Какую именно фотографию вы хотите'
                                                   ' посмотреть?', reply_markup=markup)
    elif callback.data == 'photo_selfie':
        bot.send_message(callback.message.chat.id, 'Фотография сделана на горе Азов, Свердловская область, 2023 год')
    elif callback.data == 'photo_school':
        bot.send_message(callback.message.chat.id, 'Школа!')
    elif callback.data == 'voice':
        bot.send_message(callback.message.chat.id, 'Голосовуха')
    elif callback.data == 'source':
        bot.send_message(callback.message.chat.id, 'Гитхаб')


bot.infinity_polling()
