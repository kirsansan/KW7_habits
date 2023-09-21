import json

from celery.app import task, shared_task
from telebot import TeleBot

from KW7_habits import settings
from config.config import TLG_TOKEN, TLG_CHAT_ID
from habit.models import Habit, SenderDailyLog

import requests

#
# @task
# def send_telegram_message(habit_pk):
#     """Send message via Telebot
#        you need make schedule to send in Admin panel """
#     habit = Habit.objects.get(pk=habit_pk)
#     if habit.creator.telegram_username:
#         telegram_bot = TeleBot(TLG_TOKEN)
#         message = f"I remind you:at {habit.time} for {habit.title} you need to do {habit.action} in {habit.place}."
#         telegram_bot.send_message(habit.creator.telegram_username, message)
#
@shared_task
def send_telegram_message_rev_B():
    """Send message via request
       you need make schedule to send in Admin panel """

    url = f"https://api.telegram.org/bot{TLG_TOKEN}/sendMessage?chat_id={TLG_CHAT_ID}&text=<текст_отправляемого_сообщения>"
    response = requests.get(url)
    if response.status_code == 200:
        content = json.loads(response.text)
    print("API response is:", response)
    print("API response content is:", content)



@shared_task
def cleaning_logs():
    """Cleaning daily logs
        this task must be run one time per day"""
    SenderDailyLog.objects.all().delete()
    actual_habits = Habit.objects.all()
    for habit in actual_habits:
        tmp = SenderDailyLog(habit_id=habit, daily_status=SenderDailyLog.CREATE)
        tmp.save()
