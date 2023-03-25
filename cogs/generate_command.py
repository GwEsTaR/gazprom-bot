import disnake
from disnake.ext import commands
from assets import functions as funct

class GenerateCommands(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(dm_permission=False, name='generate-image')
    async def generate_image(self, inter, prompt: str):
        await inter.response.defer()
        try:
            image_url = funct.generate_image(prompt)
            await inter.edit_original_message(image_url)
        except: await inter.edit_original_message('Ник читай')


def setup(bot:commands.Bot):
    bot.add_cog(GenerateCommands(bot))