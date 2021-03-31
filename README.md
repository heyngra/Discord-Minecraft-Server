[Version]: <1.1>
# Discord-Minecraft-Server
With it you can make your own autoupdating message with stats on your Discord Server!
## Setup
1. Download the latest version from [releases](https://github.com/heyngra/Discord-Minecraft-Server/releases).
2. Open run.py file and wait until it closes.
3. Open the config file and fill it up. 
NOTE: Do not fill messageID, because you will collect it later. 
4. Run the app again. Copy the Message ID and fill it to config.
5. Run it again!

If you something goes wrong and application would crash, you should try open the app via cmd.exe and if there are any errors report them on the github.

## Debugging

After you found an error you probably want to report it. That's great!

Windows | Linux
-|-
Open cmd via writing `cmd` in explorer bar or press Win+R and write cmd.exe, then navigate to location of your file. | Run terminal and navigate to location of your file. |
After error show, copy the error message fron: `Traceback:` to `Error: ...`. | After error show, copy the error message fron: `Traceback:` to `Error: ...`. |
Open the issue page and create new issue. Write here your Windows' version and the thing copied. Wait for response. | Open the issue page and create new issue. Write here your Linux distribution and version and the thing copied. Wait for response. |

Please, be patient.





## How to collect data

1. To get token go to [discord.com/developers](https://discord.com/developers/applications). Create new application, then bot in it. Copy the **Token**
2. To get the channelID you need to enable the developer mode, then click on channel and copy the ID and insert.
3. To get messageID you need to make the same what you did in 2. but you need to get the ID of an message that will be send by running the bot without it.
4. To get the IP you just write the IP of an server you connect it. F.E. hypixel.net
![][Developer]

## Contribution

If you want to help in creating this application, thats cool!
Github Web | Github Desktop
-|-
Click edit on file you want to contribute. | Go to main page and click **Clone** button, then click **Open in Github Desktop** |
| Add edits and click create new branch | Mark you want to make changes to parent repository. | 
| | Open the file in normal editor then proceed to make changes  |
| Every click of **commit changes** after editing will create commit. Name it shortly, but recognizable. | After **all** changes create commit. Name it shortly, but recognizable. |
| After you are done making changes at the main page of your fork click **Create Pull Request** | After you are done making changes **push** your commits. |
| | Click **Create Pull Request.** |
Fill pull request with short title, description what you've changed and all information about it. | Fill pull request with short title, description what you've changed and all information about it. |
Wait for [@heyngra](https://github.com/heyngra) to merge it. | Wait for [@heyngra](https://github.com/heyngra) to merge it. |


## License
App above uses MIT License.



[Developer]: DeveloperMode.PNG "How to enable Developer"
