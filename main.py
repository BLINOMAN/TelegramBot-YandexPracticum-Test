import telebot
from telebot import types

bot = telebot.TeleBot('5865897537:AAGIxhx7N0ciaAckuLDaPPOhwUQ4aWmKWAE')
start_markup = types.InlineKeyboardMarkup()
start_btn = types.InlineKeyboardButton('На главную', callback_data='start')
start_markup.row(start_btn)


@bot.message_handler(commands=['start'])
def start(message):
    file = open('photos/photo_main.png', 'rb')
    bot.send_photo(message.chat.id, file,
                   'Приветствую! Это телеграм бот для тестового задания для Яндекс Практикума. '
                   'Зовут меня Муратшин Борис, мне 19 лет, учусь на 3 курсе УрФУ ИРИТ-РТФ, бакалавриат.\n\n'
                   'Если хотите узнать, как я выгляжу, моё главное увлечение, мои голосовые сообщения на разные '
                   'темы или получить ссылку на репозиторий, нажмите на соответствующую кнопку.'
                   '\n/photos - Мои фотографии'
                   '\n/hobby  - О моем увлечении'
                   '\n/voices - Голосовые сообщения'
                   '\n/github - ссылка на репозиторий на Github')


@bot.message_handler(commands=['photos'])
def photos(message):
    markup = types.InlineKeyboardMarkup()
    selfie_btn = types.InlineKeyboardButton('Мое селфи', callback_data='photo_selfie')
    school_btn = types.InlineKeyboardButton('Фотография со школы', callback_data='photo_school')
    markup.row(selfie_btn, school_btn)
    bot.send_message(message.chat.id,
                     'Вообще я не люблю фотографироваться, но несколько фотографий себя-любимого я всё же имею. Какую '
                     'именно фотографию вы хотите посмотреть?',
                     reply_markup=markup)


@bot.message_handler(commands=['hobby'])
def hobby(message):
    file = open('photos/photo_hobby.jpeg', 'rb')
    bot.send_photo(message.chat.id, file,
                   'Моим самым любимым увлечением являются походы. За последние 4 годы я сходил в походы самой разной '
                   'сложности и дальности. Был и на сплавах, и в горах, на озерах, реках. Выходы на природу позволяют '
                   'мне отдохнуть от душного города и запечатлеть природу в самое  разное время года. А после того, '
                   'как у меня появился личный автомобиль, мне стала интересна еще одна категория походов – авто '
                   'походы, суть которых заключается в поездках по разным местам нашей страны на автомобиле.\n\nНа '
                   'приложенной фотографии - поход на Тальков  камень, Сысерть',
                   reply_markup=start_markup)


@bot.message_handler(commands=['voices'])
def voices(message):
    markup = types.InlineKeyboardMarkup()
    voice1_btn = types.InlineKeyboardButton('Бабушка и ChatGPT', callback_data='voice_1')
    voice2_btn = types.InlineKeyboardButton('SQL и NoSQL', callback_data='voice_2')
    voice3_btn = types.InlineKeyboardButton('Про первую любовь', callback_data='voice_3')
    markup.row(voice1_btn, voice2_btn, voice3_btn)
    bot.send_message(message.chat.id,
                     'Я подготовил для вас 3 разных аудио рассказов на разные темы. Первое сообщение – как я объясняю '
                     'своей бабушке, что такое ChatGPT. Во втором – я кратко объясняю главные различия между SQL и '
                     'NoSQL. В последнем я рассказываю историю о первой любви. Выберите, которое вы хотите послушать.',
                     reply_markup=markup)


@bot.message_handler(commands=['github'])
def github(message):
    bot.send_message(message.chat.id, '<a href="github.com">Репозиторий с проектом</a>',
                     parse_mode='html',
                     reply_markup=start_markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_query(callback):
    if callback.data == 'start':
        start(callback.message)
    elif callback.data == 'photo_selfie':
        file = open('photos/photo_selfie.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file,
                       'Гора Азов, Свердловская область, 2023 год',
                       reply_markup=start_markup)
    elif callback.data == 'photo_school':
        file = open('photos/photo_school.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file,
                       'Гимназия №94, Екатеринбург, 2021 год',
                       reply_markup=start_markup)
    elif callback.data == 'voice_1':
        bot.send_message(callback.message.chat.id, 'БАБКА!!!!!!!!!!!!!!!!', reply_markup=start_markup)
    elif callback.data == 'voice_2':
        bot.send_message(callback.message.chat.id, 'БАЗЫДАННЫХ!!!!!!!!!!!', reply_markup=start_markup)
    elif callback.data == 'voice_3':
        bot.send_message(callback.message.chat.id, 'ЛЮБОВЬ!!!!!!!!!!!!!!!', reply_markup=start_markup)


bot.infinity_polling()
