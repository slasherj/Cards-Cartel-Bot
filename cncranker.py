import discord
import datetime

# I will probably change this to a command bot and not client bot at some point, but have not figured out when -Slash

# Variables for Client

adminlist = [164529707335942144]

client = discord.Client()

# Functions

class Match:
    def __init__(self, player1, player2, caster1, caster2, date = datetime.datetime.now().replace(microsecond=0), bans = None):
        # all players are to be strings, possibly user id if we @ them, I could see issues returning this in the future, constantly @ them
        self.player1 = player1
        self.player2 = player2
        self.caster1 = caster1
        self.caster2 = caster2
        # self.date must be a datetime object
        self.date = datetime.datetime(hour = date[0:1], month = date[3:4], day = date[6:7], year = date[9:10]) # in the format 23:01/05/2021 or 'hours (2 digit):month (2 digit) /day (2 digit) /year (4 digit)'
        # used if we include banned factions, cards, ect, TODO
        self.bans = bans
    def timetomatch(self):
        curtime = datetime.datetime.now().replace(microsecond=0)
        # difference returns datetime object, in str format of % days, %h:%m:%s
        difference = self.date - curtime
        return difference
    def remindplayers(self):
        # TODO
        pass
    def remindcasters(self):
        #TODO
        pass
    def remindall(self):
        #TODO
        pass

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
    if msg.author.id != 0 and msg.author.bot is not True:
        if msg.content.startswith('!next' or '!matchdate' or 'getdate'):
            msg.channel.send('pass') # Whatever closest match date is, will implement later TODO
    # Admin Commands
    if msg.author.id in adminlist:
        if msg.content.startswith('!create'):
            #TODO
            pass

client.run('KEY GOES HERE, REMOVED TO KEEP MY OAUTH2 SAFE')