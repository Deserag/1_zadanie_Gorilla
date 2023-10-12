import telebot
import asyncio
import time
from telebot import types
#подключенные библиотеки
bot = telebot.TeleBot("*****")# токен бота
nick = []
money = 1
money_user = []
doxod = 1
aksesuar = []
eda = 0
#переменные для хранения результатов игры
banan = 10
palka = 200
golden = 15000
palima = 100000
gorila = 5000
samka = 100000
#цена аксессуаров

#Запуск бота и доступ к функции /start /старт
@bot.message_handler(commands = ["start","старт","Старт","Start"])
def zapusk(message):
    bot.send_message(message.chat.id, f'==============\nПривет, я игровой бот Gorilla 😊.'
                                      f'\nЭто развлекательный бот, в котором вы можете "убить свое время", а так же веселится👌.'
                                      f'\nПожалуйста, ознакомтесь с ботом в "Помощь📋".'
                                      f'\nЕсли у вас не появились кнопки, то пропишите "Магазин".'
                                      f'\nЭто не проблема программиста, а самого месседжера.'
                                      f'\nПриятной игры,{message.from_user.username}\n==============')
    bot.register_next_step_handler(message, get_name)#начальное сообщение для запуска

#Меню с кнопками и присвоения всех новых переменных, таких как money,
@bot.message_handler(commands = ["start","старт","Старт","Start"])
def menu(message):
    WTC = 0
    FTC = 0
    money = 1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Магазин') #Кнопка открывает мазагин с аксессуарами
    item2 = types.KeyboardButton('Покормить Гориллу🍽') #Кнопка восстанавливает рейтинг
    item3 = types.KeyboardButton('Поиграть с гориллой⚽') #Кнопка добавляет деньги и рейтинг
    item4 = types.KeyboardButton('Профиль🐵') #Выводит профиль игрока
    item5 = types.KeyboardButton('Помощь') #Выводит функционал бота
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id,text = 'Выполнено',reply_markup=markup)

#Вывод кнопок для игры в бота.
@bot.message_handler()
def bot_message(message):
        global proverka
        proverka = 0
    # Переменная пользователя, в которой будут хранится его деньги/рейтинг.
        global money
    # Переменная, в которой будет хранится доход пользователя, с каждым новым аксессуаром он будет меняться.
        global doxod
    # Список аксессуаров пользователя.
        global aksesuar
    # Энергия пользователя.
        global eda
        global banan
        global palka
        global gold
        global palima
        global gorila
        global samka
        global money_user
    #переменные акссесуаров

#Кнопка "Магазин"
        if message.text == 'Магазин':
            proverka += 1
            n = open('Магазин.jpg','rb')
            bot.send_photo(message.chat.id,photo= n,caption='\n=========================='
                                             '\n'
                                             '\nАксессуары для вашей Гориллы:'
                                              f'\nБанан🍌: Стоимость {banan} монет, увеличивает доход на 1 монеты.\n'
                                               '\nПалка🪵: Стоимость - 200 монет, увеличивает доход на 10 монеты.\n'
                                               '\nЗолотой банан🌙: Стоимсоть - 15000 монет, увеличивает доход на 100 монет.\n'
                                               '\nПальма с бананами🌴🍌: Стоимтость - 100000 монет, увеличивает доход на 1000 монет.\n'
                                               '\nЭнергия гроилы" Стоимость 500 монет, увеличивает доход в 2 раза на 5 минут\n'
                                               '\nСамка горилы: Стоимость 350000 монет, увеличивает доход в 2 раза'
                                               '\n'
                                               '\n=========================='                             )#описание цены акссесуаров, выводящеейся сообщением
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Банан🍌')
            item2 = types.KeyboardButton('Палка🪵')
            item3 = types.KeyboardButton('Золотой банан🌙')
            item4 = types.KeyboardButton('Пальма с бананами🌴🍌')
            item5 = types.KeyboardButton('Энергия гориллы')
            item6 = types.KeyboardButton('Самка гориллы')
            back = types.KeyboardButton('назад🔙')
            markup.add(item1, item2, item3,item4,item5,item6, back)
            bot.send_message(message.chat.id,'Успешно',reply_markup=markup)
            proverka -= 1
        # Покупа аксессуара Банан для Гориллы.
        if message.text == 'Банан🍌':
            # Добавление на пользователя.
            telegram_id = str(message.from_user.id)
            # Проверка, хватает ли у пользователя денег.
            if money >= 10:
                # Вывод обратного сообщения.
                n = open('На покупку банана.jpg','rb')
                bot.send_photo(message.chat.id, photo=n,caption='Банан🍌 успешно приобретена.')
                # В список аксессуаров добавляется Банан.
                aksesuar.append('Банан🍌')
                # Вычет пользовательских сбережений для покупки (десять монет).
                money -= 10
                banan *= 2
                # Увеличение кол-ва денег с кнопки Поиграит с гориллой на одну монету.
                doxod += 1
                n = open('На покупку банана.jpg','rb')
                bot.send_photo(message.chat.id, photo=n, caption='К сожалению у вас не хватает средств💵 на покупку данного замечательного артефакта😭.')


        # Покупа аксессуара Пальма для Гориллы.
        if message.text == 'Палка🪵':
            # Добавляет на пользователя.
            telegram_id = str(message.from_user.id)
            # Проверка, хватает ли у пользователя денег.
            if money >= 200:
                # Вывод обратного сообщения.
                n = open('Палка.jpg','rb')
                bot.send_photo(message.chat.id, photo=n, caption='Палка🪵 успешно приобретена.')
                # В список аксессуаров добавляется Палка.
                aksesuar.append('Палка🪵')
                # Вычет пользовательских сбережений для покупки (пятьдесят монет).
                money -=200
                # Увеличение кол-ва денег с кнопки Поиграит с гориллой на две монеты.
                doxod += 10
            # Вывод ошибки
            else:
                n = open('Палка.jpg','rb')
                bot.send_photo(message.chat.id, photo=n, caption='К сожалению у вас не хватает средств💵 на покупку данного замечательного артефакта😭.')

        # Покупа аксессуара Золотой банан для Гориллы.
        if message.text == 'Золотой банан🌙':
            # Добавляет на пользователя.
            telegram_id = str(message.from_user.id)
            # Проверка, хватает ли у пользователя денег.
            if money >= 15000:
                # Вывод обратного сообщения.
                n = open('На золотой банан.jpg','rb')
                bot.send_photo(message.chat.id, photo=n, caption='Золотой банан🌙 успешно приобретен.')
                # В список аксессуаров добавляется Золотой банан.
                aksesuar.append('Золотой банан🌙')
                # Вычет пользовательских сбережений для покупки (двести монет).
                money -=15000
                # Увеличение кол-ва денег с кнопки Поиграит с гориллой на пять монеты.
                doxod += 100
            else:
                # Вывод ошибки.
                n = open('На золотой банан.jpg','rb')
                bot.send_photo(message.chat.id, photo=n, caption='К сожалению у вас не хватает средств💵 на покупку данного замечательного артефакта😭.')

        # Покупа аксессуара Пальма с бананами для Гориллы.
        if message.text == 'Пальма с бананами🌴🍌':
            # Добавляет на пользователя.
            telegram_id = str(message.from_user.id)
            # Проверка, хватает ли у пользователя денег.
            if money <= 100000:
                n = open('пальма с бананами.jpg','rb')
                # Вывод обратного сообщения.
                bot.send_photo(message.chat.id, photo=n,caption='Пальма с бананами🌴🍌успешно приобретена.')
                # В список аксессуаров добавляется Пальму с бананами.
                aksesuar.append('Пальма с бананами🌴🍌')
                # Вывод обратного сообщения.
                # Вычет пользовательских сбережений для покупки (тысяча монет).
                money += 100000
                # Увеличение кол-ва денег с кнопки Поиграит с гориллой на десять монеты.
                doxod += 1000
            else:
                # Вывод ошибки.
                n = open('пальма с бананами.jpg', 'rb')
                bot.send_photo(message.chat.id, photo=n, caption='К сожалению у вас не хватает средств💵 на покупку данного замечательного артефакта😭.')

        elif message.text == 'Энергия горилы':
            telegram_id = str(message.from_user.id)
            if money >= 500:
                n = open('Аксессуар кофе.jpg', 'rb')
                bot.send_photo(message.chat.id, photo=n, caption='Вы успешно купили горилу')
                money -= 500
                doxod *= 1.25
            else:
                n = open('Аксессуар кофе.jpg', 'rb')
                bot.send_photo(message.chat.id, photo=n, caption='К сожалению у вас не хватает средств💵 на покупку данного замечательного артефакта😭')

        elif message.text == 'Самка горилы':
            telegram_id = str(message.from_user.id)
            if money >= 100000:
                n = open('самка.jpg','rb')
                bot.send_photo(message.chat.id, photo=n, caption='Самка успешно приобретена')
                money -= 100000
                doxod*= 2
            else:
                n = open('самка.jpg', 'rb')
                bot.send_photo(message.chat.id, photo=n, caption='К сожалению у вас не хватает средств💵 на покупку данного замечательного артефакта😭')
        #Кнопка возвращения в меню.
        if message.text == 'назад🔙':
            menu(message)

        #Восстановление энергии на гориле через кнопку Покормить Гориллу.
        elif message.text == 'Покормить Гориллу🍽':
            proverka += 1
            n = open('Покормить гориллу.jpg', 'rb')
            # Вывод обратного сообщения после восстановления рейтинг.
            bot.send_photo(message.chat.id, photo=n,caption='Ваша горилла теперь сыта🙊.\nВы можете играть с ней!')
            # восстановление рейтинга.
            eda = 100000
            proverka -= 1
            # Вывод обратного сообщения после восстановления рейтинг.

         #кнопка Поиграть с Гориллой.
        elif message.text == 'Поиграть с гориллой⚽' or message.text == 'Поиграть с гориллой' :
           proverka += 1
           if eda <= 0: #Проверка энергии на наличие.
               n = open('Если горилла голодает.jpg','rb')
               bot.send_photo(message.chat.id, photo=n)
               bot.send_message(message.chat.id,'Ваша Горилла голодна🙊, покормите ее!!!') #Вывод ошибки в случае, если энергия закончилась.
               time.sleep(5)
           else:
                n = open('Поиграть с гориллой.jpg','rb')
                # В случае, если энергия у пользователя есть - вывод сообщения об успехе.
                bot.send_photo(message.chat.id, photo=n, caption= f'Вы успешно поиграли с Гориллой, она слегка улыбается 🐒\nВам начисленно {doxod}💎, всего у вас {money} 💎')
                money += doxod
           proverka -= 1


        #Кнопка Профиль.
        elif message.text == 'Профиль🐵' or message.text == 'профиль':
            proverka += 1
            dlina = len(aksesuar)
            n = open('На профиль.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=n,caption=f'Ваш рейтинг в игре: {money}\nВаши аксессуары:{dlina}')
            proverka -= 1

        #Кнопка помощи.
        elif message.text == 'Помощь' or message.text == 'помощь':
            proverka += 1
            n = open('Помощь.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=n, caption='Информация о боте:\n1.Нажимая на кнопку поиграть с Гориллой⚽ вы получаете рейтинг🏆 и деньги💎.'
                                             '\n\n2.Ваши деньги = вашему рейтингу, чем вы богаче, тем вы успешнее.'
                                             '\n\n3.В профиле вы можете увидеть ваш рейтинг и деньги, а так же аксессуары, которые у вас есть🐵.'
                                             '\n\n4.Для увеличения вашего дохода вы можете купить аксессуары для вашей Гориллы.'
                                             '\n\n5.Для игры с Гориллой вам нужно ее кормить🍽.')
            proverka -= 1
        else:
            bot.send_message(message.chat.id,'Такой команды нет, возможно вы ввели ее неправильно, или  попробуйте ввести другую')
        #Уменьшение количества энергии с каждой секундой, чтобы человек кормил гориллу .
        while time.time() == True:
            eda -= 1


def get_name(message):
    telegram_id = str(message.from_user.id)
    global user_name, nick
    user_name = message.text


#Запуск бота.
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(5)
