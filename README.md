# ScratchStatsDashboard
Python Server code for Scratch project to show your Scratch Stats automatically without having to manually update it all the time. **Updates both the Turbowarp and Scratch Cloud**

## Dependencies
See requirements.txt

```bash
$ pip install -r requirements.txt
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

## Configure

Open _.env_. Edit the four variables in the file.

# 1. USERNAME
Username for a Scratch account that will act as a bot to automatically update the cloud variables. The account you provide does not have to have Scratcher status, however, do not use your main account. You will be logged out very time the program runs.
# 2. PASSWORD
Password of the bot account
# 3. PROJECT_ID
ID of your Scratch Project that you remixed that the program will be updating the cloud variables of.
# 4. CONTACT_INFO
Some sort of contact info for the Turbowarp devs.

Save the file and run it. You should be done! Let me know if you have any errors or problems setting it up. Please run this program at your own risk and be considerate of the scratch servers.
