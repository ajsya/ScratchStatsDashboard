import scratchconnect, requests, os, json, time
from dotenv import load_dotenv

load_dotenv()

username = os.environ['USERNAME']
password = os.environ['PASSWORD']

login = scratchconnect.ScratchConnect(username, password)
user = login.connect_user(username="ajsya")
project = login.connect_project(581011441) # Connect the project

def data():
        user.update_data()

        views = user.total_views()
        loves = user.total_loves_count()
        favs = user.total_favourites_count()
        followers = user.followers_count()

        messages = user.messages_count()

        r = requests.get('https://scratchdb.lefty.one/v3/user/info/ajsya')
        data = r.json()

        rank_country = data['statistics']['ranks']['country']['followers']
        rank_global = data['statistics']['ranks']['followers']

        return views, loves, favs, followers, rank_country, rank_global, messages

while True:
    variables = project.connect_cloud_variables()
    
    #print(data())
    encoded = variables.encode_list(list(data()))  # Encode a list

    variables.set_cloud_variable(variable_name='cloud_variable', value=encoded)
    print('Updated Data Sent!')

    time.sleep(3600) #an hour delay between updates, can be changed based on user's popularity.
