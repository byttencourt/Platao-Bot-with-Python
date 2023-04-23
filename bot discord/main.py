import discord
from discord.ext import commands
import aiohttp

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Olá mundo! O bot está conectado uma cortesia de byttencourt.')

@bot.command()
async def platao(ctx: commands.Context, *, prompt: str):
    async with aiohttp.ClientSession() as session:
        payload = {
            "model": "text-davinci-003",
            "prompt": prompt,
            "temperature": 0.5,
            "max_tokens": 2000,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "best_of": 1,

        }
        headers = {"Authorization": f"Bearer {'SEUAPI_KEY'}"}
        async with session.post("https://api.openai.com/v1/completions", json=payload, headers=headers) as resp:
            response = await resp.json()
            embed = discord.Embed(title="Platao GPT responde:", description=response['choices'][0]['text'])
            embed.set_footer(text='https://chat.openai.com powered by byttencourt.')
            await ctx.reply(embed=embed)


bot.run('TOKEN')


