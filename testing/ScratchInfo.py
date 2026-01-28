import requests
import json

userData = requests.get("https://scratchinfo.quuq.dev/api/v1/users/ajsya/info?mode=all").json()
print(userData['followers'])

projectData = requests.get('https://scratchinfo.quuq.dev/api/v1/users/ajsya/projectStats').json()
print(projectData)

totalViews = projectData['totalViews']
totalLoves = projectData['totalLoves']
totalFavorites = projectData['totalFavorites']