import telebot
import time
import threading

bot = telebot.TeleBot("TELEGRAM_BOT_TOKEN")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я напомню тебе об окончании бесплатного времени парковки! Команда /set установит таймер на 15 секунд.')

@bot.message_handler(commands=['set'])
def set_timer(message):
    bot.reply_to(message, "У тебя 15 бесплатных секунд. Дам знать, когда пора валить!")

    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

def send_reminders(chat_id):
    time.sleep(10)
    bot.send_message(chat_id, "Осталось 5 секунд! Оплати парковку или придется искать новое место.")
    time.sleep(5)
    bot.send_message(chat_id, "Время бесплатной парковки истекло. Валим отсюда!")

bot.polling(none_stop=True)
