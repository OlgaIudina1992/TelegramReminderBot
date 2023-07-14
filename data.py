import requests as rq
import pandas as pd
import time
from datetime import datetime, timedelta

#employee productivity reminders -> sent at specified times by a manager using GoogleSheets
#careful, this is a forever function
while True:
    sheet_id = "1lUa0aZ2VJzyogYztGEXq2eIrWosxnoJDuETbpKKJHo4"
    bot_id = "your ID here"
        
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"
    df = pd.read_csv(url)
    df.set_index("employee_tel_id")
    df["schedule_datetime"] = pd.to_datetime(df["schedule_datetime"], dayfirst=True)

    #get the employee and task info
    current_time = pd.Timestamp.now()
    relevant_user = df.loc[(df.schedule_datetime == current_time)]["employee_tel_id"][1] #if you have id
    relevant_task = df.loc[(df.schedule_datetime == current_time)]["task_id"][1] #assign the task /reminder to be sent

    # if no id -> get the id from here. The user has to have used /start to begin conversation with the bot
    #res = rq.get(f"https://api.telegram.org/bot{bot_id}/getUpdates")

    #plug into the bot

    def send_task():        
        user_id = relevant_user
        message = f"The manager says: {relevant_task}"
        address_url = f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={user_id}&text={message}"

        return rq.get(address_url).json()

    send_task()
