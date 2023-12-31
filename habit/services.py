# import logging
# import os
#
# import requests
# from django.utils.timezone import now
#
# from KW7_habits import settings
# from config.config import TLG_TOKEN, LOG_FILE_NAME
# from habit.models import SenderDailyLog, Habit
#
#
# def cleaning_logs():
#     """Cleaning daily logs
#         this task must be run one time per day"""
#     SenderDailyLog.objects.all().delete()
#     actual_habits = Habit.objects.all()
#     for habit in actual_habits:
#         tmp = SenderDailyLog(habit_id=habit, daily_status=SenderDailyLog.CREATE)
#         tmp.save()
#
#
# def send_telegram_message_rev_b():
#     """Send telegram message via request.
#        You need make schedule for sending in Admin panel """
#
#     logfile = os.sep.join([str(settings.BASE_DIR), LOG_FILE_NAME])
#     print("logfile:", logfile)
#     logging.basicConfig(level=logging.INFO, filename=logfile, filemode="w")
#     actual_habits_create = Habit.objects.filter(senderdailylog__daily_status=SenderDailyLog.CREATE)
#     logging.info(f"{actual_habits_create}")
#     actual_habits = actual_habits_create.filter(creator__telegram_username__isnull=False)
#     logging.info(f"{actual_habits}")  # print(actual_habits)
#     for habit in actual_habits:
#         if habit.time <= now().time():
#             print("I gonna send", habit, "to tlg_id", habit.creator.telegram_username)
#             logging.info(f"I gonna send {habit} to tlg_id {habit.creator.telegram_username}")
#             message = f"I remind you:at {habit.time} " \
#                       f"for {habit.title} you need to do {habit.action} in {habit.place}."
#             url = f"https://api.telegram.org/bot{TLG_TOKEN}/sendMessage" \
#                   f"?chat_id={habit.creator.telegram_username}&text={message}"
#             response = requests.get(url)
#             if response.status_code == 200:
#                 # content = json.loads(response.text)
#                 habit.senderdailylog.daily_status = SenderDailyLog.SENT
#                 habit.senderdailylog.save()
#                 # habit.save()
#             # print("API response is:", response.status_code)
#             logging.info(f"API response is: {response.status_code}")
#         else:
#             # print("the time has not yet come for", habit)
#             logging.info(f"the time has not yet come for {habit}")
