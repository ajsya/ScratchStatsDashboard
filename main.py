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
# cloud = session.connect_scratch_cloud(project_id)
# client = cloud.requests()

# turbowarp cloud login
cloud_tw = sa.get_tw_cloud(1276436782, purpose="Updates cloud variable to display accurate user stats in the project", contact=contact_info)
client = cloud_tw.requests()

user = sa.get_user("ajsya")

time_since_last_fetch = 0

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

    now_time = "{0} @ {1}".format(today.strftime("%m/%d/%y"), current_time.strftime("%H:%M"))

    print("DONE!")
    global time_since_last_fetch
    time_since_last_fetch = time.time()

    global previous_fetch
    previous_fetch = (totalViews, totalLoves, totalFavorites, followers, messageCount, now_time)
    return totalViews, totalLoves, totalFavorites, followers, messageCount, now_time

@client.request
def ping(): #called when client receives request
    print("Ping request received")
    return "pong" #sends back 'pong' to the Scratch project

@client.request
def get_data(): #called when client receives request
    print("Data request received")

    time_now = time.time()
    if time_now - time_since_last_fetch > 2400: # if it's been more than 20 minutes since the last data fetch, fetch new data
        print("Data is outdated, fetching new data...")
        try:
            data = fetch_data()
            print(data)
            encoded = encode_list(list(data))  # Encode a list
            print(encoded)

            return encoded
        except Exception as e:
            print(f"Error occurred while fetching data: {e}. Sending current data...")
            return encode_list(list(previous_fetch))
    else:
        print("Data is up to date, sending current data...")
        return encode_list(list(previous_fetch))

@client.event
def on_ready():
    print("Request handler is running")

client.start(thread=True) # thread=True is an optional argument. It makes the cloud requests handler run in a thread