import json
import logging
import os

from celery import app, shared_task
from django.utils.timezone import now
# from telebot import TeleBot-P eventlet

from KW7_habits import settings
from config.config import TLG_TOKEN, TLG_CHAT_ID, LOG_FILE_NAME
from habit.models import Habit, SenderDailyLog

import requests

# from celery.utils.log import get_task_logger
# logger = get_task_logger(__name__)

#       Example working messaging via telebot
# @task
# def send_telegram_message(habit_pk):
#     """Send message via Telebot
#        you need make schedule to send in Admin panel """
#     habit = Habit.objects.get(pk=habit_pk)
#     if habit.creator.telegram_username:
#         telegram_bot = TeleBot(TLG_TOKEN)
#         message = f"I remind you:at {habit.time} for {habit.title} you need to do {habit.action} in {habit.place}."
#         telegram_bot.send_message(habit.creator.telegram_username, message)



@shared_task
def send_telegram_message_rev_b():
    """Send telegram message via request.
       You need make schedule for sending in Admin panel """

    logfile = os.sep.join([str(settings.BASE_DIR), LOG_FILE_NAME])
    print("logfile:", logfile)
    logging.basicConfig(level=logging.INFO, filename=logfile, filemode="w")
    actual_habits_create = Habit.objects.filter(senderdailylog__daily_status=SenderDailyLog.CREATE)
    logging.info(f"{actual_habits_create}")
    actual_habits = actual_habits_create.filter(creator__telegram_username__isnull=False)
    logging.info(f"{actual_habits}")  # print(actual_habits)
    for habit in actual_habits:
        if habit.time <= now().time():
            print("I gonna send", habit, "to tlg_id", habit.creator.telegram_username)
            logging.info(f"I gonna send {habit} to tlg_id {habit.creator.telegram_username}")
            message = f"I remind you:at {habit.time} for {habit.title} " \
                      f"you need to do {habit.action} in {habit.place}."
            url = f"https://api.telegram.org/bot{TLG_TOKEN}/sendMessage" \
                  f"?chat_id={habit.creator.telegram_username}&text={message}"
            response = requests.get(url)
            if response.status_code == 200:
                # content = json.loads(response.text)
                habit.senderdailylog.daily_status = SenderDailyLog.SENT
                habit.senderdailylog.save()
                # habit.save()
            # print("API response is:", response.status_code)
            logging.info(f"API response is: {response.status_code}")
        else:
            # print("the time has not yet come for", habit)
            logging.info(f"the time has not yet come for {habit}")
#
#
@shared_task
def cleaning_logs():
    """Cleaning daily logs
        this task must be run one time per day"""
    SenderDailyLog.objects.all().delete()
    actual_habits = Habit.objects.all()
    for habit in actual_habits:
        tmp = SenderDailyLog(habit_id=habit,
                             daily_status=SenderDailyLog.CREATE)
        tmp.save()


@shared_task
def printing_logs():
    """ Tiny task for juzz up celery log """
    print("uweee =)")
