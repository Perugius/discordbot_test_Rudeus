import hikari
from datetime import datetime
from pytz import timezone

# initialize needed time zones for !time command
na_east = timezone('US/Eastern')
na_west = timezone('America/Los_Angeles')
germany = timezone('Europe/Berlin')
greece = timezone('Europe/Athens')
uk = timezone('Europe/London')

# region list for time zones command !time.regions
regions = [["eu", "de", "fr", "germany", "france", "europe"], ["gr", "greece"], ["pa", "pennsylvania", "na.east", "na"], ["na.west", "lv", "la"], ["uk", "london"]]
timezones = [germany, greece, na_east, na_west, uk]

#enter Discord bot token here
bot = hikari.GatewayBot(token='')


# function to message time when prompted with !time.region
@bot.listen(hikari.GuildMessageCreateEvent)
async def return_time(event):
    # check if message was by bot, if so ignore
    if event.is_bot:
        return
    # check if command type is !time.region
    if event.content.startswith("!time."):

        # check which region is being requested by iterating matching(!) regions[] and timezones[] and output date/time
        for i in range(0, len(timezones)):
            if event.content[6:] in regions[i]:
                await event.message.respond(datetime.now(timezones[i]).strftime("Time: %H:%M:%S Date: %Y-%m-%d"))
                return
        await event.message.respond("Specify correct region.\nAvailable regions are: eu, gr, na.west, na.east, uk")

        # inneficient? way of doing same thing
        # if event.content[6:] in regions[0]:
        #     await event.message.respond(datetime.now(germany).strftime("Time: %H:%M:%S Date: %Y-%m-%d"))
        # elif event.content[6:] in regions[1]:
        #     await event.message.respond(datetime.now(greece).strftime("Time: %H:%M:%S Date: %Y-%m-%d"))
        # elif event.content[6:] in regions[2]:
        #     await event.message.respond(datetime.now(na_east).strftime("Time: %H:%M:%S Date: %Y-%m-%d"))
        # elif event.content[6:] in regions[3]:
        #     await event.message.respond(datetime.now(na_west).strftime("Time: %H:%M:%S Date: %Y-%m-%d"))
        # elif event.content[6:] == regions[4]:
        #     await event.message.respond(datetime.now(uk).strftime("Time: %H:%M:%S Date: %Y-%m-%d"))
        # else:
        #     await event.message.respond("Specify correct region.\nAvailable regions are: eu, gr, na.west, na.east, uk")

bot.run()

