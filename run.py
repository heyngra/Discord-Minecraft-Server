#--------
#Packages and Variables
import time
import os
import secrets
try:
    from mcstatus import MinecraftServer
    import discord
    from discord.ext import tasks, commands
    import yaml
    from datetime import datetime
    import asyncio
except ModuleNotFoundError:
    if os.path.isfile("installpackages.py") == True:
        if os.name == "nt":
            os.system("installpackages.py")
        else:
            os.system("python3 installpackages.py")
        print("Zainstalowano nową wersję")
        time.sleep(2)
        exit()
    else:
        print("Jesteś pewien, że pobrałeś najnowszą wersję programu?")
client = discord.Client()
#--------
#Config
if os.path.isfile("config.yml") == False:
    print("Creating config file in your file location!")
    cfg = open("config.yml", 'w', encoding="utf-8")
    cfg.write("#Welcome to the config! Please read every line about config lines, because editing something wrong can harm this program!\n\n\n#At the line below you need to write your Discord Bot Token, so it can access the bot and do the work!\ntoken: \"\"\n\n#At the line below you need to write your Channel ID that you want to edit the message in.\nChannelID: \"\"\n\n#At the line below you need to write the Message ID that you want to edit the message, if you don't already have a message, please just leave it clean.\nMessageID: \"\"\n\n#At the line below you need to write the Minecraft Server IP that you want to check\nIP: \"\"\n\n#Server status message:\nServerStatus: \"Status Serwera\"\n\n#Is online:\nIsOnline: \"Stan serwera\"\n\n#Currently Playing\nPlayerAmount: \"Ilość graczy\"\n\n#Players\nPlayers: \"Gracze\"\n\n#Last Updated\nLastUpdated: \"Last update\"")
    cfg.close()
    print("Done!\nPlease, now fill the configuration file with things and start this program again!")
    time.sleep(3)
    exit()
elif os.path.isfile("config.yml") == True:
    global token, ChannelID, MessageID, ServerIP, ServerStatus, IsOnlline, PlayerAmount, Players, LastUpdated
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        token = cfg["token"]
        channelID = cfg["ChannelID"]
        messageID = cfg["MessageID"]
        serverIP = cfg["IP"]
        ServerStatus = cfg["ServerStatus"]
        IsOnline = cfg["IsOnline"]
        PlayerAmount = cfg["PlayerAmount"]
        Players = cfg["Players"]
        LastUpdated = cfg["LastUpdated"]

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
        randomcode = secrets.token_urlsafe(24)
        server = MinecraftServer.lookup(serverIP)
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        channel = client.get_channel(int(channelID))
        message = await channel.fetch_message(messageID)
        try:
            globals()["status_%s" % randomcode] = server.status()
        except Exception as e:
            pass
            #print(e) #Remove comment if you want to check logs
        #work
        if "status_%s" % randomcode in globals():
            if globals()["status_%s" % randomcode].players.online <= 10:
                try:
                    globals()["query_%s" % randomcode] = server.query()
                except:
                    pass
            if "query_%s" % randomcode in globals():
                if globals()["status_%s" % randomcode].players.online == 0:
                    await message.edit(content=":fire: **%s** :fire:\n:satellite: **IP**: %s\n:bar_chart: %s: :green_circle:\n:adult: **%s**: %i\n*%s:* %s" % (ServerStatus, serverIP, IsOnline, PlayerAmount, globals()["status_%s" % randomcode].players.online, LastUpdated, dt_string))
                else:
                    await message.edit(content=":fire: **%s** :fire:\n:satellite: **IP**: %s\n:bar_chart: %s: :green_circle:\n:adult: **%s**: %i\n:two_men_holding_hands: **%s**: %s\n*Last Update:* %s" % (ServerStatus, serverIP, IsOnline, PlayerAmount, globals()["status_%s" % randomcode].players.online, Players, ', '.join(globals()["query_%s" % randomcode].players.names), dt_string))
            else:
                await message.edit(content=":fire: **%s** :fire:\n:satellite: **IP**: %s\n:bar_chart: %s: :green_circle:\n:adult: **%s**: %i\n*%s:* %s" % (ServerStatus, serverIP, IsOnline, PlayerAmount, globals()["status_%s" % randomcode].players.online, LastUpdated, dt_string))
        else:
            await message.edit(content=":fire: **%s** :fire:\n:satellite: **IP**: %s\n:bar_chart: %s: :octagonal_sign:\n*%s:* %s" % (ServerStatus, serverIP, IsOnline, LastUpdated, dt_string))


        await asyncio.sleep(10)


client.run(token)
#---------
time.sleep(2)
