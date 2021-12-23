# ScratchStatsDashboard
Python Server code for Scratch project to show your Scratch Stats automatically without having to manually update it all the time.

## Requirements
- scratchconnect
- requests
- python-dotenv

```bash
$ pip install -r requirments.txt
```

## How to setup / remix guide
### Scratch
1. Remix the Scratch Project: https://scratch.mit.edu/projects/619760935/
2. Delete the cloud variable, it should be called _Cloud_.
3. Create a new cloud variable. **IMPORTANT:** it must be called _Cloud_ for the program to work.
4. Feel free to mess around with the colors in the project. Make it your own!

### Python
Follow these commands closely to ensure that your program works correctly:

Clone the repository.
```bash
$ git clone https://github.com/ajsya/ScratchStatsDashboard.git
```

Install the requirements:

**Mac/Linux**
```bash
$ python3 -m pip install -r requirements.txt
```
**Windows**
```bash
$ pip install -r requirements.txt
```

Open _.env_. Edit the two variables in the file. These are your bot account's username and password. The account you provide does not have to have Scratcher status, however, do not use your main account since ever time the program is ran you will be logged out.

Open _main.py_. Edit the two settings at the top of the program. These should be the username of the Scratch acount you want the program to get the stats for and update the project with, and the id of your project that you want the cloud variables updated in (the one you just created earlier).

Save the file and run it. You should be done! Let me know if you have any errors or problems setting it up. Please run this program at your own risk.
