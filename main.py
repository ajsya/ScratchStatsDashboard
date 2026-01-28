import scratchattach as sa
import requests, json
import time, pytz
from datetime import datetime, date
import string
import os
from dotenv import load_dotenv

ALL_CHARS = list(string.ascii_uppercase + string.ascii_lowercase +
                 string.digits + string.punctuation + ' ')

def encode(text, default=" "):
        text = str(text)
        number = ""
        for i in range(0, len(text)):
            try:
                char = text[i]
                index = str(ALL_CHARS.index(char) + 1)
                if int(index) < 10:
                    index = '0' + index
            except ValueError:
                index = str(ALL_CHARS.index(default) + 1)
                if int(index) < 10:
                    index = '0' + index
            number += index
        return number

def encode_list(data, default=" "):
    encoded = ""
    for i in data:
        encoded += f"{encode(i, default=default)}00"
    return encoded

load_dotenv()

# login info of an scratch account with cloud access
username = os.environ['USERNAME']
password = os.environ['PASSWORD']

project_id = os.environ['PROJECT_ID'] # the project to connect to
contact_info = os.environ['CONTACT_INFO'] # to be included with TurboWarp cloud connection

# scratch cloud login
session = sa.login(username, password)
cloud = session.connect_scratch_cloud(project_id)

# turbowarp cloud login
cloud_tw = sa.get_tw_cloud(project_id, purpose="Updates cloud variable to display accurate user stats in the project", contact=contact_info)

user = sa.get_user("ajsya")

def fetch_data():
    print("Fetching data...")

    projectData = requests.get('https://scratchinfo.quuq.dev/api/v1/users/ajsya/projectStats').json()
    print("Project data fetched.")

    totalViews = projectData['totalViews']
    totalLoves = projectData['totalLoves']
    totalFavorites = projectData['totalFaves']

    userData = requests.get("https://scratchinfo.quuq.dev/api/v1/users/ajsya/info?mode=all").json()
    print("User data fetched.")

    followers = userData['followers']

    messageCount = user.message_count()

    tz = pytz.timezone('EST') 
    current_time = datetime.now(tz)
    today = date.today()

    time = "{0} @ {1}".format(today.strftime("%m/%d/%y"), current_time.strftime("%H:%M"))

    print("DONE!")
    return totalViews, totalLoves, totalFavorites, followers, messageCount, time

def send_data(to_send):
    print("Sending data to cloud...")
    try:
        cloud.set_var("Cloud", to_send)
        print("Data sent to Scratch cloud.")
    except Exception as e:
        print(f"Error occurred while sending to scratch cloud servers: {e}. Trying TurboWarp cloud...")
    # Try TurboWarp cloud
    try:
        cloud_tw.set_var("Cloud", to_send)
        print("Data sent to TurboWarp cloud.")
    except Exception as e:
        print(f"Error occurred while sending to TurboWarp cloud servers: {e}.")
    
    return

def main():
    while True:
        data = fetch_data()
        print(data)
        encoded = encode_list(list(data))  # Encode a list
        print(encoded)

        send_data(encoded)

        sleepTime = 3600*2  # 2 hour delay between updates, can be changed based on user's popularity.
        print(f"Updating again in {sleepTime/3600} hours...")
        time.sleep(sleepTime)  # 3 hour delay between updates, can be changed based on user's popularity.

main()