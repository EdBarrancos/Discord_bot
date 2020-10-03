# Discord_bot

## Author

Eduardo Barrancos, Me :)

## Objective

Manage Dungeons and Dragons functionalities in a channel

## Using

At the moment I'm not keeping this bot online full time, but you are free to. __I did not test if this method works. If it doesn't, feel free to email me eduardobarrancos11488@gmail.com__

### Step One

Go to this [repo page](https://github.com/EdBarrancos/The_GM) and Clone Or Download the Zip, just pressed the green button with a down arrow on it saying "Code" and then Press "Download Zip"

### Step Two

Follow the steps in <a href="https://discordpy.readthedocs.io/en/latest/discord.html" target="_blank">Create a Bot</a>

Tick, in the Permissions part at least **Manage Roles**, **Manage Channels**, **View Channels**, **Send Messages**, **Manage Messages** and **Add Reactions**.

### Step Three

Copy the Bot Token. Go to the file [Bot.py](./bot.py) and change the line *TOKEN = config('TOKEN')* To *TOKEN = "Paste the Token here"*

### Step Four

Open a Terminal. Go to the directory of the repo and run the command *python3 bot.py*

### Functions

#### Category and Channel Creation

It creates a category for DnD where it will operate

It creates a "announcement" channel within that category

#### Commands

- !help

If You need any help with any of the commands, besides the help given in this README

- !ping

Pong!

- !add nbrs

sum(nbrs)

- !roll NdX [OPTIONS]

Rolls N dice of X type according to OPTIONS
