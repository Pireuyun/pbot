import discord
import os
from discord.ext import commands
app = commands.Bot(command_prefix='')

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("새우잡이 배 탑승")
    await app.change_presence(status=discord.Status.online, activity=game)

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    await app.process_commands(message)
    if message.content == "윤영아 일하자":
        await message.channel.send("돔황챠!")
    if message.content == "로아와":
        await message.channel.send("https://loawa.com/stat")
    if message.content == "지도":
        await message.channel.send("https://lostark.inven.co.kr/dataninfo/world/")
    if message.content == "각인계산":
        await message.channel.send("https://mokoko.co.kr/searchacc")
    if message.content == "도와줘": #명령어 정리
        embed = discord.Embed(title="윤영이가 지금까지 배운 말", description="더 많은 말 가르치기 > 윤영#5009", color=0x62c1cc)
        embed.add_field(name="1️⃣ 지도", value="모코코 지도를 링크를 불러옵니다.", inline=False)
        embed.add_field(name="2️⃣ 로아와", value="로아와 링크를 불러옵니다.", inline=False)
        embed.add_field(name="3️⃣ 각인계산", value="각인 계산기 링크를 불러옵니다.", inline=False)
        embed.add_field(name="4️⃣ 공대모집 [내용]", value="공격대 모집을 돕습니다. [레이드 목표/날짜/시간]을 작성해주세요.", inline=False)
        await message.channel.send(embed=embed)

@app.command()
async def 공대모집(ctx, *, text): #공격대 모집 구문 5️⃣
    get = discord.Embed(title=(text),
                        description="공대장  ➡  {}".format(ctx.author.mention),
                        color=0xFFA7A7)
    get.add_field(name=" ✅ 공격대원 모집 중", value=" > 이모지를 눌러 공격대에 참여하세요!", inline=True)
    get.add_field(name="딜러", value="❤", inline=True)
    get.add_field(name="서폿", value="💛", inline=True)
    await ctx.message.delete()
    msg = await ctx.channel.send(embed=get)
    await msg.add_reaction("❤")
    await msg.add_reaction("💛")
    await msg.add_reaction("☑")
    b = set()
    c = set()
    try:
        def check(reaction, user):
            if str(reaction) == "❤":
                b.add(user.name)
            elif str(reaction) == "💛":
                c.add(user.name)
            return str(reaction) in ['☑'] and \
                   user == ctx.author and reaction.message.id == msg.id
        reaction, user = await app.wait_for('reaction_add', check=check)
        if (str(reaction) == '☑'):
            get = discord.Embed(title=(text), description="공대장  ➡  {}".format(ctx.author.mention), color=0xFFA7A7)
        get.add_field(name="💟 공격대원 모집 마감", value="> 지원해주신 분들 감사합니다!", inline=True)
        get.add_field(name="❤ 참여 딜러", value=f"> {','.join(b)}", inline=False)
        get.add_field(name="💛 참여 서폿", value=f"> {','.join(c)}", inline=False)
        await msg.clear_reactions()
        await msg.edit(embed=get)

    except: pass

token = os.environ["BOT_TOKEN"]   
app.run(token)
