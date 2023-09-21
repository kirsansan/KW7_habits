import json

import requests

from config.config import TLG_TOKEN
from habit.models import SenderDailyLog, Habit


def cleaning_logs():
    """Cleaning daily logs
        this task must be run one time per day"""
    SenderDailyLog.objects.all().delete()
    actual_habits = Habit.objects.all()
    for habit in actual_habits:
        tmp = SenderDailyLog(habit_id=habit, daily_status=SenderDailyLog.CREATE)
        tmp.save()

def send_telegram_message_rev_B():
    """Send message via request
       you need make schedule to send in Admin panel """
    actual_habits = Habit.objects.filter(habit__senderdailylog__daily_status=SenderDailyLog.CREATE).filter(creator__telegram_username__isnull=False)
    print(actual_habits)
    for habit in actual_habits:
        # print(habit, habit.creator.telegram_username)
        url = f"""https://api.telegram.org/bot{TLG_TOKEN}
               /sendMessage?chat_id={habit.creator.telegram_username}
               &text=I remind you:at {habit.time} for {habit.title} you need to do {habit.action} in {habit.place}."""
        response = requests.get(url)
        if response.status_code == 200:
            content = json.loads(response.text)
            habit.senderdailylog.daily_status=SenderDailyLog.SENT
        print("API response is:", response)
        # print("API response content is:", content)



# if __name__ == '__main__':
#     #send_telegram_message_rev_B()
#     cleaning_logs()