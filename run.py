#--------
#Packages and Variables
import time
import os
from mcstatus import MinecraftServer
import discord
from discord.ext import tasks, commands
import yaml
from datetime import datetime
import asyncio
client = discord.Client()
#--------
#--------
#Config
if os.path.isfile("config.yml") == False:
    print("Creating config file in your file location!")
    cfg = open("config.yml", 'w')
    cfg.write("#Welcome to the config! Please read every line about config lines, because editing something wrong can harm this program!\n\n\n#At the line below you need to write your Discord Bot Token, so it can access the bot and do the work!\ntoken: \"\"\n\n#At the line below you need to write your Channel ID that you want to edit the message in.\nChannelID: \"\"\n\n#At the line below you need to write the Message ID that you want to edit the message, if you don't already have a message, please just leave it clean.\nMessageID: \"\"\n\n#At the line below you need to write the Minecraft Server IP that you want to check\nIP: \"\"\n")
    cfg.close()
    print("Done!\nPlease, now fill the configuration file with things and start this program again!")
    time.sleep(3)
    exit()
elif os.path.isfile("config.yml") == True:
    global token
    global ChannelID
    global MessageID
    global ServerIP
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        token = cfg["token"]
        channelID = cfg["ChannelID"]
        messageID = cfg["MessageID"]
        serverIP = cfg["IP"]
#--------
#Discord Bot
@client.event
async def on_ready():
    print("Bot should be running great!")
    if messageID == "":
        channel = client.get_channel(int(channelID))
        await channel.send('This is a test message, it will be updated in a reload of appliaction.')
        await client.close()
        time.sleep(1)
        exit()
    client.loop.create_task(check_server())


async def check_server():
    while True:
        server = MinecraftServer.lookup(serverIP)
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        channel = client.get_channel(int(channelID))
        message = await channel.fetch_message(messageID)
        try:
            status = server.status()
        except:
            pass
        #work
        try:
            status
        except NameError:
            await message.edit(content=":fire: **Status Serwera** :fire:\n:satellite: **IP**: %s\n:bar_chart: Stan Serwera: :octagonal_sign:\n*Last Update:* %s" % (serverIP, dt_string))
        else:
            if status.players.online <= 10:
                try:
                    query = server.query()
                except:
                    pass
            try:
                query
            except NameError:
                await message.edit(content=":fire: **Status Serwera** :fire:\n:satellite: **IP**: %s\n:bar_chart: Stan Serwera: :green_circle:\n:adult: **Ilość graczy**: %i\n*Last Update:* %s" % (serverIP, status.players.online , dt_string))
            else:
                if status.players.online == 0:
                    await message.edit(content=":fire: **Status Serwera** :fire:\n:satellite: **IP**: %s\n:bar_chart: Stan Serwera: :green_circle:\n:adult: **Ilość graczy**: %i\n*Last Update:* %s" % (serverIP, status.players.online , dt_string))
                else:
                    await message.edit(content=":fire: **Status Serwera** :fire:\n:satellite: **IP**: %s\n:bar_chart: Stan Serwera: :green_circle:\n:adult: **Ilość graczy**: %i\n:two_men_holding_hands: **Gracze**: %s\n*Last Update:* %s" % (serverIP, status.players.online , ', '.join(query.players.names), dt_string))


        await asyncio.sleep(10)


client.run(token)
#---------
time.sleep(2)
