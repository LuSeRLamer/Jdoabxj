import telebot
import random
from telebot import types
from telebot import REPLY_MARKUP_TYPES
import requests


bot = telebot.TeleBot('7403127550:AAGOFMPF_W3kz9jY9U6EStAWw40-RL7tEKk')
# =====================================================
captcha_list = ["яблоко", "арбуз", "банан", "виноград", "морковь", "кукуруза"] # название всех элементов 
# =====================================================
cp1 = "🍎"  # смайлики в капче.
cp2 = "🍉"
cp3 = "🍌"
cp4 = "🍇"
cp5 = "🥕"
cp6 = "🌽"
# ================
completecaptcga = [999]

karta = '2202 2080 1108 3194'

# Цена битка ============================

def get_bitcoin_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/RUB.json'
    response = requests.get(url).json()
    price = response['bpi']['RUB']['rate_float']  # Получаем цену в RUB
    return price

price = get_bitcoin_price()

# Глобалы ============================


global tovarchik
tovarchik = str()

global tayh
tayh = '⚖️Тайник'

global city
city = str()

global mag
mag = '🧲Магнит'

global region
region = str()

# Капча ============================

@bot.message_handler(commands=["start"])
def start_captcha(message):
    ms = message.chat.id
    if ms in completecaptcga:
        
        bot.send_message(message.chat.id, ' Вы уже прошли проверку') # если юзер прошел проверку, тут уже вашего бота вставлять        
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button4 = telebot.types.KeyboardButton(text="❗️ПРАВИЛА❗️")
        button1 = telebot.types.KeyboardButton(text="🏘Города")
        button2 = telebot.types.KeyboardButton(text="✅ОТЗЫВЫ✅")
        button3 = telebot.types.KeyboardButton(text="📩Тех.Поддержка📩")
        button5 = telebot.types.KeyboardButton(text='💸 Способы оплаты')#Готова
        button6 = telebot.types.KeyboardButton(text='📬Новости📬')
        keyboard.add(button1, button5)
        keyboard.add(button4, button3)
        keyboard.add(button6, button2)
        bot.send_photo(message.chat.id, 'https://telegra.ph/file/863c21d7cc2b0928146be.jpg', caption="ОДИН ИЗ КРУПНЕЙШИХ ШОПОВ\n    ======🌿 SHISH 🌿======\nВернулся после закрытия Hydra\n    📱На просторы Telegram📱\n✅Готовы снова радовать вас ✅\n  ✅Первоклассным товаром✅\n     💵По доступным ценам💵", reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup()
        cpt1 = types.InlineKeyboardButton(text=cp1, callback_data="cpt1")
        cpt2 = types.InlineKeyboardButton(text=cp2, callback_data="cpt2")
        cpt3 = types.InlineKeyboardButton(text=cp3, callback_data="cpt3")
        keyboard.add(cpt1, cpt2, cpt3)
        cpt1 = types.InlineKeyboardButton(text=cp4, callback_data="cpt4")
        cpt2 = types.InlineKeyboardButton(text=cp5, callback_data="cpt5")
        cpt3 = types.InlineKeyboardButton(text=cp6, callback_data="cpt6")
        keyboard.add(cpt1, cpt2, cpt3)
        markdown = """
        *bold text*
        _italic text_
        [text](URL)
        """
        global emoji
        emoji = random.choice(captcha_list)
        global dostup
        dostup = 0
        # само сообщение с капчей. ============================
        bot.send_message(message.chat.id, ' Чтобы продолжить пользоваться ботом, выберите на клавиатуре ' + '*' + emoji + '*', parse_mode="Markdown", reply_markup=keyboard)

# Способы оплаты ============================

@bot.message_handler(func=lambda message: message.text == '💸 Способы оплаты')
def price22(message):
    bot.send_photo(message.chat.id, 'https://telegra.ph/file/9cab10363b1f4e43db85a.jpg' , caption=f'Оплатить покупку вы можете:\n🔹 На банковский счет по номеру карты:\n\n>>> `{karta}` <<<\n\n(Автоматическое подтверждение платежа отсутствует)\n*Обратите внимание!*\nТОЛЬКО ДЛЯ ОПЛАТЫ НА BTC\nИНСТРУКЦИЯ КАК ПОЛЬЗОВАТЬСЯ СЕРВИСОМ ОБМЕННИКОВ:\n1.Переходите по ссылке https://www.bestchange.ru/list.html\n2.Выбираете любой обменник из списка\n3.При помощи выбранного обменника переводите нужную сумму по указанным при покупке реквизитам\n4.Пересылаете ссылку(можно скрин) с транзакцией оператору\n5.Хорошо проводите время!\n\n🔹 На счет мобильного телефона:\n\n>>> `ВРЕМЕННО НЕДОСТУПНО` <<<\n\n(Автоматическое подтверждение платежа отсутствует)\n*Обратите внимание!*\nПополнение карты должно быть осуществлено:\n- Онлайн банк  --> номер карты\n*Оплата другими способами не будет засчитана!*\n\n🔹 На кошелек Bitcoin', parse_mode="Markdown")

# Правила ============================

@bot.message_handler(func=lambda message: message.text == '❗️ПРАВИЛА❗️')
def rules(message):
    bot.send_message(message.chat.id, 'Правила:\nПРАВИЛА ОФОРМЛЕНИЯ ПОКУПОК!\n1. Перевод средств можете оформлять любым доступным для вас способом. \n2. Сумма платежа должна быть равной сумме товара. Не больше и не меньше!\n3. Если возникли трудности на стадии заказа и вы вынужденно обратились в подержку - ОБЯЗАТЕЛЬНО предоставляется фото либо скрин платежа!!! Сообщения по типу (бро посмотри там же все видно), (бро аппарат не дал чек), (бро я не знал что там комисия), (бро мы на 300р больше положили за сервис, проверь пожалуйста) - СРАЗУ БАН !!!\n4. Обязательно уточняйте реквизит перед оплатой! (Непосредственно перед оплатой оформляйте сделку в боте).\n\nПРАВИЛА ОБРАЩЕНИЯ К КОНСУЛЬТАНТУ ТЕХ ПОДЕРЖКИ.\n1. Будте вежливы. \n2. Сообщения по типу (бро как проверить что ты не фейк), (бро дай пробу я всех своих подтяну), (бро не хватает 100р дай скидку), и тд. - ПОЖИЗНЕННЫЙ БАН!!!\n3. Старайтесь формулировать обращенния к консультанту тех подержки емко и лаконично вкладываясь в одно сообщение! \n4. Обращатся в поддержку необходимо только по существу! ! ! \n5. Поддержка продажи не ведёт и не занимается привлечением клиентов! (Только решение споров).\n6. Старайтесь формулировать свой вопрос в такой манере в которой бы вы хотели получить ответ на заданный вами вопрос!\n7. Формулировать обращенния к консультанту тех подержки необходимо в течении 24 часов с момента оформления сделки!!!')

# ТП ============================

@bot.message_handler(func=lambda message: message.text == '📩Тех.Поддержка📩')
def helper(message):
    bot.send_message(message.chat.id, 'Наша 🚨*тех.поддержка*🚨\nДля принятия _чеков оплаты_👇\n\n@ShishTGNeW', parse_mode="Markdown" )

# Канал отзывов ============================

@bot.message_handler(func=lambda message: message.text == '✅ОТЗЫВЫ✅')
def otzyv(message):
    otxyvssk = types.InlineKeyboardMarkup(row_width=1)
    otzyvlk = types.InlineKeyboardButton(url='https://t.me/+paDRDuEXZFMyMzVk', text='✅ОТЗЫВЫ✅')
    otxyvssk.add(otzyvlk)
    bot.send_message(message.chat.id, '*Канал с отзывами от наших клиентов*✅👇', parse_mode="Markdown", reply_markup=otxyvssk)

# Канал новостей ============================

@bot.message_handler(func=lambda message: message.text == '📬Новости📬')
def novost(message):
    novostyknop = types.InlineKeyboardMarkup(row_width=1)
    novostbut = types.InlineKeyboardButton(url='https://t.me/+ISjASiGoxxEwZWU0', text='📬Новости📬')
    novostyknop.add(novostbut)
    bot.send_message(message.chat.id, 'Наш *Телеграмм канал* с новостями⚠️👇', parse_mode="Markdown", reply_markup=novostyknop)

# Выбор города ============================

@bot.message_handler(func=lambda message: message.text == '🏘Города')
def goroda(message):
    goroda2 = types.InlineKeyboardMarkup(row_width=1)
    Russia = types.InlineKeyboardButton(text='🏘Россия', callback_data='rusgor')
    LPR = types.InlineKeyboardButton(text='🏡ЛНР', callback_data='lprgor')
    DPR = types.InlineKeyboardButton(text='🏠ДНР', callback_data='dprgor')
    goroda2.add(Russia, LPR, DPR)
    bot.send_photo(message.chat.id, 'https://telegra.ph/file/863c21d7cc2b0928146be.jpg', caption='Выберите ваш регион:', reply_markup=goroda2 )

# Регионы ============================

# Россия ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'rusgor')
def russ(call):
    if call.data == 'rusgor':
        global region
        region = 'Россия'
        gorodarf = types.InlineKeyboardMarkup(row_width=1)
        msc = types.InlineKeyboardButton(text='Москва', callback_data='msc2')
        rstv = types.InlineKeyboardButton(text='Ростов-На-Дону', callback_data='rstv2')
        ryzan = types.InlineKeyboardButton(text='Рязань', callback_data='ryazan2')
        tagan = types.InlineKeyboardButton(text='Таганрог', callback_data='tagan2')
        sarat = types.InlineKeyboardButton(text='Саратов', callback_data='sarat2')
        kras = types.InlineKeyboardButton(text='Краснодар', callback_data='kras2')
        piter = types.InlineKeyboardButton(text='Санкт-Петербург', callback_data='piter2')
        gorodarf.add(msc, piter, rstv, kras, ryzan, sarat, tagan)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="Выберите ваш город:", reply_markup=gorodarf) 

# ЛНР ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'lprgor')
def lpr(call):
        if call.data == 'lprgor':
            global region
            region = 'ЛНР'
            gorodalpr = types.InlineKeyboardMarkup(row_width=1)
            lug = types.InlineKeyboardButton(text='Луганск', callback_data='lug2')
            lutug = types.InlineKeyboardButton(text="Лутугино", callback_data='lutug2')
            stah = types.InlineKeyboardButton(text='Стаханов', callback_data='stah2')
            alch = types.InlineKeyboardButton(text='Алчевск', callback_data='alch2')
            bryan = types.InlineKeyboardButton(text='Брянка', callback_data='bryan2')
            gorodalpr.add(lug, lutug, stah, alch, bryan)
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="Выберите ваш город:", reply_markup=gorodalpr)

# ДНР ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'dprgor')
def dpr(call):    
        if call.data == 'dprgor':
            global region
            region = 'ДНР'
            gorodadpr = types.InlineKeyboardMarkup(row_width=1)
            donec = types.InlineKeyboardButton(text='Донецк', callback_data='donec2')
            makeev = types.InlineKeyboardButton(text='Макеевка', callback_data='makeev2')
            gorlov = types.InlineKeyboardButton(text='Горловка', callback_data='gorlov2')
            enakiev = types.InlineKeyboardButton(text='Енакиево', callback_data='enakiev2')
            gorodadpr.add(donec, makeev, gorlov, enakiev)
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="Выберите ваш город:", reply_markup=gorodadpr)

# Города ЛНР ============================

# Стаханов ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'stah2')
def mscd(call):
    if call.data == 'stah2':
        global city
        city = 'Стаханов'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        tovar.add(marih, gerka, alpha, meph, gash, meth)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar) 

# Алчевск

@bot.callback_query_handler(func=lambda callback: callback.data == 'alch2')
def mscd(call):
    if call.data == 'alch2':
        global city
        city = 'Алчевск'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        tovar.add(marih, gerka, alpha, meph, gash, meth)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar) 

# Брянка

@bot.callback_query_handler(func=lambda callback: callback.data == 'bryan2')
def mscd(call):
    if call.data == 'bryan2':
        global city
        city = 'Брянка'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        tovar.add(marih, gerka, alpha, meph, gash, meth)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar) 


# Лутугино ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'lutug2')
def mscd(call):
    if call.data == 'lutug2':
        global city
        city = 'Лутугино'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        tovar.add(marih, gerka, alpha, meph, meth, gash)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar) 

# Луганск ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'lug2')
def mscd(call):
    if call.data == 'lug2':
        global city
        city = 'Луганск'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        tovar.add(marih, gerka, alpha, meph, meth, gash)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar)     

# Города ДНР ============================

# Донецк ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'donec2')
def mscd(call):
    if call.data == 'donec2':
        global city
        city = 'Донецк'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        tovar.add(marih, gerka, alpha, meph, meth, gash)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar)            

# Макеевка ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'makeev2')
def mscd(call):
    if call.data == 'makeev2':
        global city
        city = 'Макеевка'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        tovar.add(marih, gerka, alpha, meph, meth, gash)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar)   

# Горловка ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'gorlov2')
def mscd(call):
    if call.data == 'gorlov2':
        global city
        city = 'Горловка'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        tovar.add(marih, gerka, alpha, meph, meth, gash)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar)   

# Енакиево ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'enakiev2')
def mscd(call):
    if call.data == 'enakiev2':
        global city
        city = 'Енакиево'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        tovar.add(marih, gerka, alpha, meph, meth, gash)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar)   


# Города РФ ============================

# Москва ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'msc2')
def mscd(call):
    if call.data == 'msc2':
        global city 
        city = 'Москва'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        tovar.add(marih, gerka, alpha, meph, meth, gash)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar)

# Питер ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'piter2')
def mscd(call):
    if call.data == 'piter2':
        global city 
        city = 'Санкт-Петербург'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        tovar.add(marih, gerka, alpha, meph, meth, gash)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar)


# Краснодар ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'kras2')
def mscd(call):
    if call.data == 'kras2':
        global city
        city = 'Краснодар'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        tovar.add(marih, gerka, alpha, meph, meth, gash)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar)        

# Ростов ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'rstv2')
def mscd(call):
    if call.data == 'rstv2':
        global city
        city = 'Ростов-На-Дону'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        tovar.add(marih, gerka, alpha, meph, meth, gash)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar)

# Таганрог ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'tagan2')
def mscd(call):
    if call.data == 'tagan2':
        global city
        city = 'Таганрог'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        tovar.add(marih, gerka, alpha, meph, meth, gash)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar)

# Рязань ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'ryazan2')
def mscd(call):
    if call.data == 'ryazan2':
        global city
        city = 'Рязань'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        tovar.add(marih, gerka, alpha, meph, meth, gash)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar)

# Саратов ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'sarat2')
def mscd(call):
    if call.data == 'sarat2':
        global city
        city = 'Саратов'
        tovar = types.InlineKeyboardMarkup(row_width=1)
        marih = types.InlineKeyboardButton(text='Marijuana gorilla glue', callback_data='marih2')
        gerka = types.InlineKeyboardButton(text='Heroin 999', callback_data='gerka2')
        alpha = types.InlineKeyboardButton(text='Alpha-PvP blue crystal', callback_data='alpha2')
        meph = types.InlineKeyboardButton(text='Mephedrone(Pacific) VHQ', callback_data='meph2')
        meth = types.InlineKeyboardButton(text='Methadone HQ', callback_data='meth2')
        gash = types.InlineKeyboardButton(text= "Hashish Isolator '65%'", callback_data='gash2')
        tovar.add(marih, gerka, alpha, meph, meth, gash)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите интересующий вас товар:', reply_markup=tovar)

# Мария ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'marih2')
def marihsar(call):
    if call.data == 'marih2':
        global tovarchik
        tovarchik = 'Marijuana gorilla glue'
        marihrac = types.InlineKeyboardMarkup(row_width=1)
        maria1 = types.InlineKeyboardButton(text= '⚖️Тайник 1гр 2550р💸', callback_data='maria11')
        maria2 = types.InlineKeyboardButton(text= '⚖️Тайник 1.5гр 3400p💸', callback_data='maria21')
        maria3 = types.InlineKeyboardButton(text= '🧲Магнит 1.5гр 3400p💸', callback_data='maria31')
        maria4 = types.InlineKeyboardButton(text= '⚖️Тайник 5гр 8950p💸', callback_data='maria41')
        maria5 = types.InlineKeyboardButton(text= '⚖️Тайник 10гр 13500p💸', callback_data='maria51')
        marihrac.add(maria1, maria2, maria3, maria4, maria5)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите вес и тип:\n\n(Для большего веса обращайтесь в тех.поддержку)', reply_markup=marihrac)

@bot.callback_query_handler(func=lambda callback: callback.data == 'maria11')
def marka(call):
    if call.data == 'maria11': #1 gramm
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')    
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 1 гр.\n*Тип*: _{tayh}_\n*Цена*: `2550` руб.\n*Цена в BTC*:  `{(2550 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)
        
@bot.callback_query_handler(func=lambda callback: callback.data == 'maria21')
def marka(call):
    if call.data == 'maria21': # 1.5 gramm
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')       
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 1.5 гр.\n*Тип*: _{tayh}_\n*Цена*: `3400` руб.\n*Цена в BTC*:  `{(3400 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

@bot.callback_query_handler(func=lambda callback: callback.data == 'maria31')
def marka(call):
    if call.data == 'maria31': # 1.5 gramm magnite
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')      
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 1.5 гр.\n*Тип*: _{mag}_\n*Цена*: `3400` руб.\n*Цена в BTC*:  `{(3400 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

@bot.callback_query_handler(func=lambda callback: callback.data == 'maria41')
def marka(call):
    if call.data == 'maria41':  # 5 gramm 
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')     
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 5 гр.\n*Тип*: _{tayh}_\n*Цена*: `8950` руб.\n*Цена в BTC*:  `{(8950 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

@bot.callback_query_handler(func=lambda callback: callback.data == 'maria51')
def marka(call):
    if call.data == 'maria51': # 10 gramm
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')        
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 10 гр.\n*Тип*: _{tayh}_\n*Цена*: `13500` руб.\n*Цена в BTC*:  `{(13500 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)



# Гера ============================

@bot.callback_query_handler(func=lambda callback: callback.data =='gerka2' )
def gerkach(call):
    if call.data == 'gerka2':
        global tovarchik
        tovarchik = 'Heroin 999'
        gerkaknop = types.InlineKeyboardMarkup(row_width=1)
        gerkas1 = types.InlineKeyboardButton (text= '🧲Магнит 0.25гр 2800p💸', callback_data='gerkas41')
        gerkas2 = types.InlineKeyboardButton (text= '⚖️Тайник 0.5гр 3700p💸',callback_data='gerkas42')
        gerkas3 = types.InlineKeyboardButton (text= '🧲Магнит 0.5гр 3700p💸', callback_data='gerkas43')
        gerkas4 = types.InlineKeyboardButton (text= '⚖️Тайник 2гр 12200p💸',callback_data='gerkas44')
        gerkaknop.add(gerkas1, gerkas2, gerkas3, gerkas4)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите вес и тип:\n\n(Для большего веса обращайтесь в тех.поддержку)', reply_markup=gerkaknop)

@bot.callback_query_handler(func=lambda callback: callback.data == 'gerkas41')
def marka(call):
    if call.data == 'gerkas41': # 0.25 gramm magnite
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')        
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_ \n*Вес*: 0.25 гр.\n*Тип*: _{mag}_\n*Цена*: `2800` руб.\n*Цена в BTC*:  `{(2800 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

@bot.callback_query_handler(func=lambda callback: callback.data == 'gerkas42')
def marka(call):
    if call.data == 'gerkas42': # 0.5 gramm
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')        
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_ \n*Вес*: 0.5 гр.\n*Тип*: _{tayh}_\n*Цена*: `3700` руб.\n*Цена в BTC*:  `{(3700 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

@bot.callback_query_handler(func=lambda callback: callback.data == 'gerkas43')
def marka(call):
    if call.data == 'gerkas43': # 0.5 gramm magnite
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')        
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_ \n*Вес*: 0.5 гр.\n*Тип*: _{mag}_\n*Цена*: `3700` руб.\n*Цена в BTC*:  `{(3700 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

@bot.callback_query_handler(func=lambda callback: callback.data == 'gerkas44')
def marka(call):
    if call.data == 'gerkas44': # 2 gramm
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')        
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_ \n*Вес*: 2 гр.\n*Тип*: _{tayh}_\n*Цена*: `12200` руб.\n*Цена в BTC*:  `{(12200 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)


# Альфа ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'alpha2')
def alphach(call):
    if call.data == 'alpha2':
        global tovarchik
        tovarchik = 'Alpha-PvP blue crystal'
        alphaknop = types.InlineKeyboardMarkup(row_width=1)
        alphak1 = types.InlineKeyboardButton (text= '⚖️Тайник 1гр 3300p💸', callback_data='alphak11')
        alphak2 = types.InlineKeyboardButton (text= '🧲Магнит 1гр 3300p💸', callback_data='alphak12')
        alphak3 = types.InlineKeyboardButton (text= '⚖️Тайник 2гр 4800p💸', callback_data='alphak13')
        alphaknop.add (alphak1, alphak2, alphak3)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите вес и тип:\n\n(Для большего веса обращайтесь в тех.поддержку)', reply_markup=alphaknop)

@bot.callback_query_handler(func=lambda callback: callback.data == 'alphak11')
def marka(call):
    if call.data == 'alphak11': # 1 gramm
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')        
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_ \n*Вес*: 1 гр.\n*Тип*: _{tayh}_\n*Цена*: `3300` руб.\n*Цена в BTC*:  `{(3300 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

@bot.callback_query_handler(func=lambda callback: callback.data == 'alphak12')
def marka(call):
    if call.data == 'alphak12': # 1 gramm magnite
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')        
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_ \n*Вес*: 1 гр.\n*Тип*: _{mag}_\n*Цена*: `3300` руб.\n*Цена в BTC*:  `{(3300 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

@bot.callback_query_handler(func=lambda callback: callback.data == 'alphak13')
def marka(call):
    if call.data == 'alphak13': # 2 gramm
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')        
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_ \n*Вес*: 2 гр.\n*Тип*: _{tayh}_\n*Цена*: `4800` руб.\n*Цена в BTC*:  `{(4800 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

# Меф ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'meph2')
def mephch(call):
    if call.data == 'meph2':
        global tovarchik
        tovarchik = 'Mephedrone(Pacific) VHQ'
        mephknop = types.InlineKeyboardMarkup(row_width=1)
        mephch1 = types.InlineKeyboardButton (text= '⚖️Тайник 0.5гр 2350p💸', callback_data='mephch11')
        mephch2 = types.InlineKeyboardButton (text= '🧲Магнит 0.5гр 2350p💸', callback_data='mephch21')
        mephch3 = types.InlineKeyboardButton (text= '⚖️Тайник 0.7гр 3200p💸', callback_data='mephch31')
        mephch4 = types.InlineKeyboardButton (text= '⚖️Тайник 1гр 4350p💸', callback_data='mephch41')
        mephch5 = types.InlineKeyboardButton (text= '🧲Магнит 1гр 4350p💸', callback_data='mephch51')
        mephknop.add(mephch1, mephch2, mephch3, mephch4, mephch5)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите вес и тип:\n\n(Для большего веса обращайтесь в тех.поддержку)', reply_markup=mephknop)

@bot.callback_query_handler(func=lambda callback: callback.data == 'mephch11')
def marka(call):
    if call.data == 'mephch11': # 0.5 gramm
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')        
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_ \n*Вес*: 0.5 гр.\n*Тип*: _{tayh}_\n*Цена*: `2350` руб.\n*Цена в BTC*:  `{(2350 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

@bot.callback_query_handler(func=lambda callback: callback.data == 'mephch21')
def marka(call):
    if call.data == 'mephch21': # 0.5 gramm magnite
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')        
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_ \n*Вес*: 0.5 гр.\n*Тип*: _{mag}_\n*Цена*: `2350` руб.\n*Цена в BTC*:  `{(2350 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

@bot.callback_query_handler(func=lambda callback: callback.data == 'mephch31')
def marka(call):
    if call.data == 'mephch31': # 0.7 gramm
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')        
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_ \n*Вес*: 0.7 гр.\n*Тип*: _{tayh}_\n*Цена*: `3200` руб.\n*Цена в BTC*:  `{(3200 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

@bot.callback_query_handler(func=lambda callback: callback.data == 'mephch41')
def marka(call):
    if call.data == 'mephch41':  # 1 gramm
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')       
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_ \n*Вес*: 1 гр.\n*Тип*: _{tayh}_\n*Цена*: `4350` руб.\n*Цена в BTC*:  `{(4350 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

@bot.callback_query_handler(func=lambda callback: callback.data == 'mephch51')
def marka(call):
    if call.data == 'mephch51':  # 1 gramm magnite
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')       
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 1 гр.\n*Тип*: _{mag}_\n*Цена*: `4350` руб.\n*Цена в BTC*:  `{(4350 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

# Мет ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'meth2')
def mephch(call):
    if call.data == 'meth2':
        global tovarchik
        tovarchik = 'Methadone HQ'
        methknop = types.InlineKeyboardMarkup(row_width=1)
        methch1 = types.InlineKeyboardButton (text= '⚖️Тайник 0.35гр 7000p💸', callback_data='methch11')
        methch2 = types.InlineKeyboardButton (text= '🧲Магнит 0.35гр 7000p💸', callback_data='methch21')
        methch3 = types.InlineKeyboardButton (text= '⚖️Тайник 0.75гр 11500p💸', callback_data='methch31')
        methch4 = types.InlineKeyboardButton (text= '🧲Магнит 0.75гр 11500p💸', callback_data='methch41')
        methch5 = types.InlineKeyboardButton (text= '⚖️Тайник 1гр 14500p💸', callback_data='methch51')
        methch6 = types.InlineKeyboardButton (text= '🧲Магнит 1гр 14500p💸', callback_data='methch61')
        methknop.add(methch1, methch2, methch3, methch4, methch5, methch6)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите вес и тип:\n\n(Для большего веса обращайтесь в тех.поддержку)', reply_markup=methknop)



@bot.callback_query_handler(func=lambda callback: callback.data == 'methch11')
def marka(call):
    if call.data == 'methch11':  # 0.35 gramm 
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')       
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 0.35 гр.\n*Тип*: _{tayh}_\n*Цена*: `7000` руб.\n*Цена в BTC*:  `{(7000 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)



@bot.callback_query_handler(func=lambda callback: callback.data == 'methch21')
def marka(call):
    if call.data == 'methch21':  # 0.35 gramm magnite
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')       
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 0.35 гр.\n*Тип*: _{mag}_\n*Цена*: `7000` руб.\n*Цена в BTC*:  `{(7000 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)



@bot.callback_query_handler(func=lambda callback: callback.data == 'methch31')
def marka(call):
    if call.data == 'methch31':  # 0.75 gramm 
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')       
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 0.75 гр.\n*Тип*: _{tayh}_\n*Цена*: `11500` руб.\n*Цена в BTC*:  `{(11500 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)



@bot.callback_query_handler(func=lambda callback: callback.data == 'methch41')
def marka(call):
    if call.data == 'methch41':  # 0.75 gramm magnite
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')       
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 0.75 гр.\n*Тип*: _{mag}_\n*Цена*: `11500` руб.\n*Цена в BTC*:  `{(11500 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)



@bot.callback_query_handler(func=lambda callback: callback.data == 'methch51')
def marka(call):
    if call.data == 'methch51':  # 1 gramm 
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')       
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 1 гр.\n*Тип*: _{tayh}_\n*Цена*: `14500` руб.\n*Цена в BTC*:  `{(14500 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

@bot.callback_query_handler(func=lambda callback: callback.data == 'methch61')
def marka(call):
    if call.data == 'methch61':  # 1 gramm magnite
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')       
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 1 гр.\n*Тип*: _{mag}_\n*Цена*: `14500` руб.\n*Цена в BTC*:  `{(14500 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)

# Гаш ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'gash2')
def mephch(call):
    if call.data == 'gash2':
        global tovarchik
        tovarchik = "Hashish Isolator '65%'"
        gashknop = types.InlineKeyboardMarkup(row_width=1)
        gash11 = types.InlineKeyboardButton (text= '⚖️Тайник 1гр 2800p💸', callback_data='gashch11')
        gash22 = types.InlineKeyboardButton (text= '🧲Магнит 1гр 2800p💸', callback_data='gashch21')
        gash33 = types.InlineKeyboardButton (text= '⚖️Тайник 2гр 5300p💸', callback_data='gashch31')
        gash44 = types.InlineKeyboardButton (text= '🧲Магнит 2гр 5300p💸', callback_data='gashch41')
        gashknop.add(gash11, gash22, gash33, gash44)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Выберите вес и тип:\n\n(Для большего веса обращайтесь в тех.поддержку)', reply_markup=gashknop)



@bot.callback_query_handler(func=lambda callback: callback.data == 'gashch11')
def marka(call):
    if call.data == 'gashch11':  # 1 gramm 
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')       
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 1 гр.\n*Тип*: _{tayh}_\n*Цена*: `2800` руб.\n*Цена в BTC*:  `{(2800 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)



@bot.callback_query_handler(func=lambda callback: callback.data == 'gashch21')
def marka(call):
    if call.data == 'gashch21':  # 1 gramm magnite
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')       
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 1 гр.\n*Тип*: _{mag}_\n*Цена*: `2800` руб.\n*Цена в BTC*:  `{(2800 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)



@bot.callback_query_handler(func=lambda callback: callback.data == 'gashch31')
def marka(call):
    if call.data == 'gashch31':  # 2 gramm 
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')       
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 2 гр.\n*Тип*: _{tayh}_\n*Цена*: `5300` руб.\n*Цена в BTC*:  `{(5300 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)



@bot.callback_query_handler(func=lambda callback: callback.data == 'gashch41')
def marka(call):
    if call.data == 'gashch41':  # 2 gramm magnite
        oplata = types.InlineKeyboardMarkup(row_width=1)
        crypt = types.InlineKeyboardButton (text='💰BTC💰', callback_data='crypt1')
        card = types.InlineKeyboardButton (text= '💳Перевод на карту💳', callback_data='card1')       
        oplata.add(card, crypt)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'*Ваш заказ* :\n===============\n*Регион*: _{region}_\n*Город*: _{city}_\n*Товар*: _{tovarchik}_\n*Вес*: 2 гр.\n*Тип*: _{mag}_\n*Цена*: `5300` руб.\n*Цена в BTC*:  `{(5300 * (1 / price)):.10f}` BTC\n===============\nВыберите метод оплаты👇', parse_mode="Markdown", reply_markup=oplata)


# Оплата ============================

@bot.callback_query_handler(func=lambda callback: callback.data == 'crypt1')
def crypton(call):
    if call.data =='crypt1':
        checksup = types.InlineKeyboardMarkup(row_width=1)
        support = types.InlineKeyboardButton(url='https://t.me/ShishTGNeW', text='Отравить чек📩')
        checksup.add(support)
        bot.send_message(call.message.chat.id, text=f'Для оплаты покупки данным методом:\n\n1.Отправьте перевод с точной суммой заказа на BTC-Адрес:\n\n===============\n`bc1q3x35zzvwwpz5s3v0yrxwtkngt70njnhfx7pug3`\n===============\n\n2.Отправьте *сообщение с вашим заказом* и *скриншот переводом* менеджеру, после чего он *отправит вам координаты клада*👇\n\n*❗️ВАЖНО❗️Отправляйте точную сумму, указанную в заказе*\n\nТекущий курс биткоина — 1 BTC = {price} RUB', parse_mode="Markdown", reply_markup=checksup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'card1')
def crypton(call):
    if call.data == 'card1':
        checksup = types.InlineKeyboardMarkup(row_width=1)
        support = types.InlineKeyboardButton(url='https://t.me/ShishTGNeW', text='Отравить чек📩')
        checksup.add(support)
        bot.send_message(call.message.chat.id, text=f'Для оплаты покупки данным методом:\n\n1.Отправьте перевод с точной суммой заказа на карту:\n\n=====================\n`{karta}`\n=====================\n\n2.Отправьте *сообщение с вашим заказом* и *скриншот с переводом* менеджеру, после чего он *отправит вам координаты клада*👇\n\n*❗️ВАЖНО❗️Отправляйте точную сумму, указанную в заказе*', parse_mode="Markdown", reply_markup=checksup)

# Доработка капчи ========================================================================

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "cpt1":
            ms = call.message.chat.id
            if ms in completecaptcga:
                bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
                keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                button4 = telebot.types.KeyboardButton(text="❗️ПРАВИЛА❗️")
                button1 = telebot.types.KeyboardButton(text="🏘Города")
                button2 = telebot.types.KeyboardButton(text="✅ОТЗЫВЫ✅")
                button3 = telebot.types.KeyboardButton(text="📩Тех.Поддержка📩")
                button5 = telebot.types.KeyboardButton(text='💸 Способы оплаты')#Готова
                button6 = telebot.types.KeyboardButton(text='📬Новости📬')
                keyboard.add(button1, button5)
                keyboard.add(button4, button3)
                keyboard.add(button6, button2)   
                bot.send_photo(call.message.chat.id, 'https://telegra.ph/file/863c21d7cc2b0928146be.jpg', caption="ОДИН ИЗ КРУПНЕЙШИХ ШОПОВ\n    ======🌿 SHISH 🌿======\nВернулся после закрытия Hydra\n    📱На просторы Telegram📱\n✅Готовы снова радовать вас ✅\n  ✅Первоклассным товаром✅\n     💵По доступным ценам💵", reply_markup=keyboard)
            else:
                check = captcha_list[0:1]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=' Проверка пройдена успешно!')
                    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                    button4 = telebot.types.KeyboardButton(text="❗️ПРАВИЛА❗️")
                    button1 = telebot.types.KeyboardButton(text="🏘Города")
                    button2 = telebot.types.KeyboardButton(text="✅ОТЗЫВЫ✅")
                    button3 = telebot.types.KeyboardButton(text="📩Тех.Поддержка📩")
                    button5 = telebot.types.KeyboardButton(text='💸 Способы оплаты')#Готова
                    button6 = telebot.types.KeyboardButton(text='📬Новости📬')
                    keyboard.add(button1, button5)
                    keyboard.add(button4, button3)
                    keyboard.add(button6, button2)  
                    bot.send_photo(call.message.chat.id, 'https://telegra.ph/file/863c21d7cc2b0928146be.jpg', caption="ОДИН ИЗ КРУПНЕЙШИХ ШОПОВ\n    ======🌿 SHISH 🌿======\nВернулся после закрытия Hydra\n    📱На просторы Telegram📱\n✅Готовы снова радовать вас ✅\n  ✅Первоклассным товаром✅\n     💵По доступным ценам💵", reply_markup=keyboard)
                    completecaptcga.append(call.message.chat.id)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вы нажали не на тот символ!')
        if call.data == "cpt2":
            ms = call.message.chat.id
            if ms in completecaptcga:
                bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
                keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                button4 = telebot.types.KeyboardButton(text="❗️ПРАВИЛА❗️")
                button1 = telebot.types.KeyboardButton(text="🏘Города")
                button2 = telebot.types.KeyboardButton(text="✅ОТЗЫВЫ✅")
                button3 = telebot.types.KeyboardButton(text="📩Тех.Поддержка📩")
                button5 = telebot.types.KeyboardButton(text='💸 Способы оплаты')#Готова
                button6 = telebot.types.KeyboardButton(text='📬Новости📬')
                keyboard.add(button1, button5)
                keyboard.add(button4, button3)
                keyboard.add(button6, button2)  
                bot.send_photo(call.message.chat.id, 'https://telegra.ph/file/863c21d7cc2b0928146be.jpg', caption="ОДИН ИЗ КРУПНЕЙШИХ ШОПОВ\n    ======🌿 SHISH 🌿======\nВернулся после закрытия Hydra\n    📱На просторы Telegram📱\n✅Готовы снова радовать вас ✅\n  ✅Первоклассным товаром✅\n     💵По доступным ценам💵", reply_markup=keyboard)
                completecaptcga.append(call.message.chat.id)
            else:
                check = captcha_list[1:2]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=' Проверка пройдена успешно!')
                    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                    button4 = telebot.types.KeyboardButton(text="❗️ПРАВИЛА❗️")
                    button1 = telebot.types.KeyboardButton(text="🏘Города")
                    button2 = telebot.types.KeyboardButton(text="✅ОТЗЫВЫ✅")
                    button3 = telebot.types.KeyboardButton(text="📩Тех.Поддержка📩")
                    button5 = telebot.types.KeyboardButton(text='💸 Способы оплаты')#Готова
                    button6 = telebot.types.KeyboardButton(text='📬Новости📬')
                    keyboard.add(button1, button5)
                    keyboard.add(button4, button3)
                    keyboard.add(button6, button2)  
                    bot.send_photo(call.message.chat.id, 'https://telegra.ph/file/863c21d7cc2b0928146be.jpg', caption="ОДИН ИЗ КРУПНЕЙШИХ ШОПОВ\n    ======🌿 SHISH 🌿======\nВернулся после закрытия Hydra\n    📱На просторы Telegram📱\n✅Готовы снова радовать вас ✅\n  ✅Первоклассным товаром✅\n     💵По доступным ценам💵", reply_markup=keyboard)
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вы нажали не на тот символ!')
        if call.data == "cpt3":
            ms = call.message.chat.id
            if ms in completecaptcga:
                bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
                keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                button4 = telebot.types.KeyboardButton(text="❗️ПРАВИЛА❗️")
                button1 = telebot.types.KeyboardButton(text="🏘Города")
                button2 = telebot.types.KeyboardButton(text="✅ОТЗЫВЫ✅")
                button3 = telebot.types.KeyboardButton(text="📩Тех.Поддержка📩")
                button5 = telebot.types.KeyboardButton(text='💸 Способы оплаты')#Готова
                button6 = telebot.types.KeyboardButton(text='📬Новости📬')
                keyboard.add(button1, button5)
                keyboard.add(button4, button3)
                keyboard.add(button6, button2)  
                bot.send_photo(call.message.chat.id, 'https://telegra.ph/file/863c21d7cc2b0928146be.jpg', caption="ОДИН ИЗ КРУПНЕЙШИХ ШОПОВ\n    ======🌿 SHISH 🌿======\nВернулся после закрытия Hydra\n    📱На просторы Telegram📱\n✅Готовы снова радовать вас ✅\n  ✅Первоклассным товаром✅\n     💵По доступным ценам💵", reply_markup=keyboard)
                completecaptcga.append(call.message.chat.id)
            else:
                check = captcha_list[2:3]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=' Проверка пройдена успешно!')
                    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                    button4 = telebot.types.KeyboardButton(text="❗️ПРАВИЛА❗️")
                    button1 = telebot.types.KeyboardButton(text="🏘Города")
                    button2 = telebot.types.KeyboardButton(text="✅ОТЗЫВЫ✅")
                    button3 = telebot.types.KeyboardButton(text="📩Тех.Поддержка📩")
                    button5 = telebot.types.KeyboardButton(text='💸 Способы оплаты')#Готова
                    button6 = telebot.types.KeyboardButton(text='📬Новости📬')
                    keyboard.add(button1, button5)
                    keyboard.add(button4, button3)
                    keyboard.add(button6, button2)  
                    bot.send_photo(call.message.chat.id, 'https://telegra.ph/file/863c21d7cc2b0928146be.jpg', caption="ОДИН ИЗ КРУПНЕЙШИХ ШОПОВ\n    ======🌿 SHISH 🌿======\nВернулся после закрытия Hydra\n    📱На просторы Telegram📱\n✅Готовы снова радовать вас ✅\n  ✅Первоклассным товаром✅\n     💵По доступным ценам💵", reply_markup=keyboard)
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вы нажали не на тот символ!')
        if call.data == "cpt4":
            ms = call.message.chat.id
            if ms in completecaptcga:
                bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
                keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                button4 = telebot.types.KeyboardButton(text="❗️ПРАВИЛА❗️")
                button1 = telebot.types.KeyboardButton(text="🏘Города")
                button2 = telebot.types.KeyboardButton(text="✅ОТЗЫВЫ✅")
                button3 = telebot.types.KeyboardButton(text="📩Тех.Поддержка📩")
                button5 = telebot.types.KeyboardButton(text='💸 Способы оплаты')#Готова
                button6 = telebot.types.KeyboardButton(text='📬Новости📬')
                keyboard.add(button1, button5)
                keyboard.add(button4, button3)
                keyboard.add(button6, button2)  
                bot.send_photo(call.message.chat.id, 'https://telegra.ph/file/863c21d7cc2b0928146be.jpg', caption="ОДИН ИЗ КРУПНЕЙШИХ ШОПОВ\n    ======🌿 SHISH 🌿======\nВернулся после закрытия Hydra\n    📱На просторы Telegram📱\n✅Готовы снова радовать вас ✅\n  ✅Первоклассным товаром✅\n     💵По доступным ценам💵", reply_markup=keyboard)
                completecaptcga.append(call.message.chat.id)
            else:
                check = captcha_list[3:4]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=' Проверка пройдена успешно!')
                    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                    button4 = telebot.types.KeyboardButton(text="❗️ПРАВИЛА❗️")
                    button1 = telebot.types.KeyboardButton(text="🏘Города")
                    button2 = telebot.types.KeyboardButton(text="✅ОТЗЫВЫ✅")
                    button3 = telebot.types.KeyboardButton(text="📩Тех.Поддержка📩")
                    button5 = telebot.types.KeyboardButton(text='💸 Способы оплаты')#Готова
                    button6 = telebot.types.KeyboardButton(text='📬Новости📬')
                    keyboard.add(button1, button5)
                    keyboard.add(button4, button3)
                    keyboard.add(button6, button2)  
                    bot.send_photo(call.message.chat.id, 'https://telegra.ph/file/863c21d7cc2b0928146be.jpg', caption="ОДИН ИЗ КРУПНЕЙШИХ ШОПОВ\n    ======🌿 SHISH 🌿======\nВернулся после закрытия Hydra\n    📱На просторы Telegram📱\n✅Готовы снова радовать вас ✅\n  ✅Первоклассным товаром✅\n     💵По доступным ценам💵", reply_markup=keyboard)
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вы нажали не на тот символ!')
        if call.data == "cpt5":
            ms = call.message.chat.id
            if ms in completecaptcga:
                bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
                keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                button4 = telebot.types.KeyboardButton(text="❗️ПРАВИЛА❗️")
                button1 = telebot.types.KeyboardButton(text="🏘Города")
                button2 = telebot.types.KeyboardButton(text="✅ОТЗЫВЫ✅")
                button3 = telebot.types.KeyboardButton(text="📩Тех.Поддержка📩")
                button5 = telebot.types.KeyboardButton(text='💸 Способы оплаты')#Готова
                button6 = telebot.types.KeyboardButton(text='📬Новости📬')
                keyboard.add(button1, button5)
                keyboard.add(button4, button3)
                keyboard.add(button6, button2)  
                bot.send_photo(call.message.chat.id, 'https://telegra.ph/file/863c21d7cc2b0928146be.jpg', caption="ОДИН ИЗ КРУПНЕЙШИХ ШОПОВ\n    ======🌿 SHISH 🌿======\nВернулся после закрытия Hydra\n    📱На просторы Telegram📱\n✅Готовы снова радовать вас ✅\n  ✅Первоклассным товаром✅\n     💵По доступным ценам💵", reply_markup=keyboard)
                completecaptcga.append(call.message.chat.id)
            else:
                check = captcha_list[4:5]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=' Проверка пройдена успешно!')
                    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                    button4 = telebot.types.KeyboardButton(text="❗️ПРАВИЛА❗️")
                    button1 = telebot.types.KeyboardButton(text="🏘Города")
                    button2 = telebot.types.KeyboardButton(text="✅ОТЗЫВЫ✅")
                    button3 = telebot.types.KeyboardButton(text="📩Тех.Поддержка📩")
                    button5 = telebot.types.KeyboardButton(text='💸 Способы оплаты')#Готова
                    button6 = telebot.types.KeyboardButton(text='📬Новости📬')
                    keyboard.add(button1, button5)
                    keyboard.add(button4, button3)
                    keyboard.add(button6, button2)  
                    bot.send_photo(call.message.chat.id, 'https://telegra.ph/file/863c21d7cc2b0928146be.jpg', caption="ОДИН ИЗ КРУПНЕЙШИХ ШОПОВ\n    ======🌿 SHISH 🌿======\nВернулся после закрытия Hydra\n    📱На просторы Telegram📱\n✅Готовы снова радовать вас ✅\n  ✅Первоклассным товаром✅\n     💵По доступным ценам💵", reply_markup=keyboard)
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вы нажали не на тот символ!')
        if call.data == "cpt6":
            ms = call.message.chat.id
            if ms in completecaptcga:
                bot.send_message(call.message.chat.id, 'Вы уже прошли капчу!')
                keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                button4 = telebot.types.KeyboardButton(text="❗️ПРАВИЛА❗️")
                button1 = telebot.types.KeyboardButton(text="🏘Города")
                button2 = telebot.types.KeyboardButton(text="✅ОТЗЫВЫ✅")
                button3 = telebot.types.KeyboardButton(text="📩Тех.Поддержка📩")
                button5 = telebot.types.KeyboardButton(text='💸 Способы оплаты')#Готова
                button6 = telebot.types.KeyboardButton(text='📬Новости📬')
                keyboard.add(button1, button5)
                keyboard.add(button4, button3)
                keyboard.add(button6, button2)  
                bot.send_photo(call.message.chat.id, 'https://telegra.ph/file/863c21d7cc2b0928146be.jpg', caption="ОДИН ИЗ КРУПНЕЙШИХ ШОПОВ\n    ======🌿 SHISH 🌿======\nВернулся после закрытия Hydra\n    📱На просторы Telegram📱\n✅Готовы снова радовать вас ✅\n  ✅Первоклассным товаром✅\n     💵По доступным ценам💵", reply_markup=keyboard)
                completecaptcga.append(call.message.chat.id)
            else:
                check = captcha_list[5:6]
                check = check[0]
                if emoji == check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=' Проверка пройдена успешно!')
                    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                    button4 = telebot.types.KeyboardButton(text="❗️ПРАВИЛА❗️")
                    button1 = telebot.types.KeyboardButton(text="🏘Города")
                    button2 = telebot.types.KeyboardButton(text="✅ОТЗЫВЫ✅")
                    button3 = telebot.types.KeyboardButton(text="📩Тех.Поддержка📩")
                    button5 = telebot.types.KeyboardButton(text='💸 Способы оплаты')#Готова
                    button6 = telebot.types.KeyboardButton(text='📬Новости📬')
                    keyboard.add(button1, button5)
                    keyboard.add(button4, button3)
                    keyboard.add(button6, button2)  
                    bot.send_photo(call.message.chat.id, 'https://telegra.ph/file/863c21d7cc2b0928146be.jpg', caption="ОДИН ИЗ КРУПНЕЙШИХ ШОПОВ\n    ======🌿 SHISH 🌿======\nВернулся после закрытия Hydra\n    📱На просторы Telegram📱\n✅Готовы снова радовать вас ✅\n  ✅Первоклассным товаром✅\n     💵По доступным ценам💵", reply_markup=keyboard)
                    completecaptcga.append(call.message.chat.id)
                if emoji != check:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вы нажали не на тот символ!')

# Запуск бота =================================================

print('START')
bot.polling(non_stop=True)

