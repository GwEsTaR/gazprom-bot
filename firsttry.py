import discord
import disnake
from disnake.ext import commands
import torch
import diffusion

bot = commands.Bot(command_prefix='/')

model = diffusion.load_model(device='cpu')

@bot.command(name='generate')
async def generate_command(ctx: disnake.Message):

    num_steps = 1000
    batch_size = 1
    size = 256
    channels = 3

    z = torch.randn(batch_size, channels, size)

    with torch.no_grad():
        generated_images = diffusion.generate(model, z, num_steps=num_steps)

        image = disnake.File(generated_images[0].clamp(0, 1).cpu().numpy())
        await ctx.send(file=image)

bot.run('MTA3MzQ4MDIxMjk4NzI1Mjc2Ng.G5xMUl.6gqH7JnrS7tHnNXuqTsP7qE7UJIQ_XdxIWiNSc')