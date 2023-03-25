import disnake
from disnake.ext import commands

bot = commands.InteractionBot(
    intents = disnake.Intents.all(),
    owner_id= 322985216484573186,
    activity = disnake.Activity(name = 'Ждёт рекодинга', type=disnake.ActivityType.watching),
    status = disnake.Status.idle,
    reload=True
)

#cog
bot.load_extension('cogs.generate_command')

token = open('token', 'r').readline()
bot.run(token)