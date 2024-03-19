import discord
from discord.ui import View, Select
from discord.ext import commands
from discord.utils import get

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print('-----봇이 준비되었습니다.-----')
    print(f'봇 이름: {bot.user}')
    print(f'봇 아이디: {bot.user.id}')
    print(f'봇이 참가한 서버 수: {len(bot.guilds)}')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("<https://github.com/201580ag>"))

@bot.command()
async def dropdown(ctx):
    select = Select(
        placeholder = "placeholder도 문구를 수정할 수 있어요",
        options = [
        discord.SelectOption(label="dropdown 1", description="1번 설명"),
        discord.SelectOption(label="dropdown 2", description="2번 설명"),
        discord.SelectOption(label="dropdown 3", description="3번 설명")
    ])

    async def my_callback(interaction):
        if select.values[0] == "dropdown 1":
            await interaction.response.send_message("1번 선택!")
        elif select.values[0] == "dropdown 2":
            await interaction.response.send_message("2번 선택!")
        elif select.values[0] == "dropdown 3":
            await interaction.response.send_message("3번 선택!")

    select.callback = my_callback
    view = View()
    view.add_item(select)

    await ctx.send("example dropdown", view = view)

bot.run('TOKEN')
