import discord
import discord.ext
from discord.ext import commands
import time
import asyncio
import os
import traceback

bot = commands.Bot(command_prefix="a9:", help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']
espotify = <:spotify:730688808252604457>


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(f"ヘルプは a9:help | 導入サーバー数: {len(bot.guilds)}"))
    
    #status=discord.Status.idle で退席状態に

async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
    
async def embox(title,description,color,message):
      embed = discord.Embed(title=title,description=description,color=color)
      await message.channel.send(embed=embed)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="ヘルプ", description="botを使用していただきありがとうございます！\n注:このbotは非公式です。\n　 アスファルト9公式のbotではありません。",color=0xce0042)
    embed.add_field(name="help", value="このコマンドです。",inline=False)
    embed.add_field(name="database", value="データの種類や、説明を表示します。",inline=False)
    embed.add_field(name="about", value="botについてや、botの招待リンクを確認できます。",inline=False)
    embed.add_field(name="ping", value="botのメッセージ送信速度をチェックします。",inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=["db"])
async def database(ctx):
    embed = discord.Embed(title="アスファルト9の全て", description="アスファルト9について、様々な情報を知ることができます。\n(実行は全て`a9:種類名`というように行ってください。)\n※`|`で区切られている項目はどちらでも実行可能です。",color=0xce0042)
    embed.add_field(name="情報の種類一覧:", value="全般 | general\nマシン | car | machine\nキャリア | career\nBGM")
    await ctx.send(embed=embed)

@bot.command(aliases=["general"])
async def 全般(ctx):
    embed = discord.Embed(title="アスファルト9の情報", description="アスファルト9について、様々な情報を知ることができます。\n(実行は全て`a9:情報名`というように行ってください。)",color=0xce0042)
    embed.add_field(name="情報一覧:", value="クレジット | credit\nトークン | token\nトレードコイン | tradecoin",inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=["career"])
async def キャリア(ctx):
    embed = discord.Embed(title="アスファルト9のキャリア", description="アスファルト9について、様々な情報を知ることができます。\n(実行は全て`a9:情報名`というように行ってください。)",color=0xce0042)
    embed.add_field(name="情報一覧:", value="情報が登録されていません",inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=["bgm"])
async def BGM(ctx):
    embed = discord.Embed(title="アスファルト9のBGM", description="\n(実行は全て`a9:bgm1`というように行ってください。)",color=0xce0042)
    embed.add_field(name="メニューBGM:", value="1. Black Wave - K.Flay\n2. Bottom Of The Deep Blue Sea - MISSIO\n3. Higher - Lemaitre feat. Maty Noyes",inline=False)
    embed.add_field(name="レースBGM:", value="データがありません",inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=["bgm1"])
async def BGM1(ctx):
    embed = discord.Embed(title="曲の情報", description="タイトル: Black Wave\nアーティスト: K.Flay",color=0xce0042)
    embed.add_field(name="聴く", value="espotify[Spotifyで再生](https://open.spotify.com/track/6B69v0kDUWJqWz1W3lNrz2?si=_aLo6QD8SlC1TbeSr9Ku4w)\n<:youtube:730692649543008406>[YouTubeで再生](https://youtu.be/kmKyh5_X4Hk)",inline=False)
    embed.set_thumbnail(url="https://images-na.ssl-images-amazon.com/images/I/710Mgh-CRfL._AC_SL1200_.jpg")
    await ctx.send(embed=embed)

@bot.command(aliases=["bgm2"])
async def BGM2(ctx):
    embed = discord.Embed(title="曲の情報", description="タイトル: Bottom Of The Deep Blue Sea\nアーティスト: MISSIO",color=0xce0042)
    embed.add_field(name="聴く", value="<:spotify:730688808252604457>[Spotifyで再生](https://open.spotify.com/track/6AvslIXIi9iaGvukefyVVK?si=Ng6YemZ4QWioV0LIATRGJA)\n<:youtube:730692649543008406>[YouTubeで再生](https://youtu.be/CFEBriOa1x0)",inline=False)
    embed.set_thumbnail(url="https://images-na.ssl-images-amazon.com/images/I/815A-o2cCoL._AC_SL1500_.jpg")
    await ctx.send(embed=embed)

@bot.command(aliases=["bgm3"])
async def BGM3(ctx):
    embed = discord.Embed(title="曲の情報", description="タイトル: Higher\nアーティスト: Lemaitre feat. Maty Noyes",color=0xce0042)
    embed.add_field(name="聴く", value="<:spotify:730688808252604457>[Spotifyで再生](https://open.spotify.com/track/2jIMtd2GaUesi6u3hO2Anb?si=GoY7EqZVQcCJDIpDs20GoA)\n<:youtube:730692649543008406>[YouTubeで再生](https://youtu.be/bsENfTmAdeI)",inline=False)
    embed.set_thumbnail(url="https://images-na.ssl-images-amazon.com/images/I/61HEvrDWn3L._AC_.jpg")
    await ctx.send(embed=embed)

@bot.command(aliases=["credit"])
async def クレジット(ctx):
    embed = discord.Embed(title="クレジット(Credit)", description="クレジットとは、ゲーム内通貨の一つ。\nマシンのアップグレードやアイテムの購入で使う。",color=0xfcc403)
    embed.add_field(name="入手方法:", value="・レース報酬で入手\n・トークンで購入\n・イベント報酬で入手\n・カードパックから入手\n・特別オファー(課金パック)から入手",inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/719041194872799264/719043421578199071/667999131049918464.png")
    await ctx.send(embed=embed)

@bot.command(aliases=["token"])
async def トークン(ctx):
    embed = discord.Embed(title="トークン(Token)", description="トークンとは、ゲーム内通貨の一つ。\nクレジットより価値が高く、\nカードパック購入やレジェンドストア、\nマシンの給油時間スキップや\nイベントチケットの回復で使用する。",color=0x0090ff)
    embed.add_field(name="入手方法:", value="・イベント報酬で入手\n・デイリー目標で入手\n・課金して入手\n・カードパックから入手\n・特別オファー(課金パック)から入手\n・(その他)ゲームロフトからのお詫びなどで入手",inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/719041194872799264/719042930823659611/664809947149631509.png")
    await ctx.send(embed=embed)

@bot.command(aliases=["tradecoin"])
async def トレードコイン(ctx):
    embed = discord.Embed(title="トレードコイン(Trade Coin)", description="トレードコインとは、レジェンドストアで使用できる通貨の一つ。",color=0x0090ff)
    embed.add_field(name="入手方法:", value="・所持設計図MAXのマシンの設計図をゲットして変換で入手\n・カンストしているアイテムをゲットして変換で入手\n・インポートパーツなどを売却して入手",inline=False)
    embed.set_image(url="https://media.discordapp.net/attachments/719041194872799264/719044194102018168/668063046043959296.png")
    await ctx.send(embed=embed)

@bot.command(aliases=["car","machine"])
async def マシン(ctx):
    embed = discord.Embed(title="アスファルト9のマシン", description="アスファルト9のマシンについて、様々な情報を知ることができます。\n(実行は全て`a9:マシン名`というように行ってください。)\n※現在開発中の為、マシンの情報がかなり少ないですが、ご了承ください。",color=0xce0042)
    embed.add_field(name="**Dクラス**:", value="Lancer Evolution\nZ4 LCI E89\nCamaro LT\nNismo Leaf RC(データ無し)\n370Z Nismo(データ無し)",inline=False)
    embed.add_field(name="**Cクラス**:", value="Challenger SRT8(データ無し)",inline=False)
    embed.add_field(name="**Bクラス**:", value="Asterion(データ無し)",inline=False)
    embed.add_field(name="**Aクラス**:", value="Vulcan(データ無し)",inline=False)
    embed.add_field(name="**Sクラス**:", value="Jesko(データ無し)",inline=False)
    embed.set_footer(text="ヒント: コピー&ペーストでマシン名の入力を省略できます。\n(全て小文字でも実行できます。)")
    await ctx.send(embed=embed)

@bot.command()
async def about(ctx):
    embed = discord.Embed(title="このbotについて...", description="アスファルト 9：Database",color=0xce0042)
    embed.add_field(name="製作者", value="うぇあChannel#6928",inline=True)
    embed.add_field(name="バージョン", value="Ver.0.6.3b\nコマンドフレームワーク移行版",inline=False)
    embed.add_field(name="招待リンク",value="開発中のため、現在非公開です。\n一般公開までお待ちください。",inline=True)
    embed.add_field(name="提携", value="辞書 bot#2369 と提携しています。\n導入はこちら。https://discordapp.com/api/oauth2/authorize?client_id=702390058896064512&permissions=8&scope=bot",inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    starttime = time.time()
    msg = await ctx.send("Pingを測定しています。\nしばらくお待ちください...")
    ping = time.time() - starttime
    await msg.edit(content=f"測定結果:{round(ping * 1000)}ms")
    #float(ping * 1000)

@bot.event
async def on_message(message):
    """
    if message.author == bot.user:
        return
    """#Bot判定は下のif文で十分。ちなみにこれは複数行コメントアウト
    if message.author.bot:
        return

    if bot.user in message.mentions:
        print(f"{message.author.name}にメンションされました")
        await message.channel.send(f"{message.author.mention} ヘルプが必要ですか？\n`a9:help` でヘルプを表示します。")

    elif message.content in ["a9:Lancer Evolution","a9:lancer evolution"]:
        embed = discord.Embed(title="マシンの情報",description="Mitsubishi Lancer Evolution",color=0x065ec9)
        embed.add_field(name="マシンクラス:", value="Dクラス")
        embed.add_field(name="レア度:", value="アンコモン")
        embed.add_field(name="給油時間:", value="05m00s(<:switch:726284432234774600>02m00s)")
        embed.add_field(name="初期状態:", value="マシンランク:467\n最高速度:250.0\n加速:42.40\nハンドリング:46.30\nニトロ:54.80",inline=False)
        embed.add_field(name="☆1 MAX:", value="マシンランク:791\n最高速度:257.2\n加速:46.89\nハンドリング:48.96\nニトロ:59.59")
        embed.add_field(name="☆2 MAX:", value="マシンランク:1,094\n最高速度:263.9\n加速:51.08\nハンドリング:51.44\nニトロ:64.03")
        embed.add_field(name="☆3 MAX:", value="マシンランク:1,381\n最高速度:270.1\n加速:55.03\nハンドリング:53.79\nニトロ:68.19")
        embed.set_image(url="https://media.discordapp.net/attachments/719041194872799264/720183961677987860/Mitsubishi_Lancer_Evolution.png?width=884&height=497")
        embed.set_footer(text="最終更新:2020 07/05")
        await message.channel.send(embed=embed)

    elif message.content in ["a9:Z4 LCI E89","a9:z4 lci e89"]:
        embed = discord.Embed(title="マシンの情報",description="BMW Z4 LCI E89",color=0xbe2e3d)
        embed.add_field(name="マシンクラス:", value="Dクラス")
        embed.add_field(name="レア度:", value="アンコモン")
        embed.add_field(name="給油時間:", value="05m00s(<:switch:726284432234774600>02m00s)")
        embed.add_field(name="初期状態:", value="マシンランク:518\n最高速度:250.0\n加速:58.60\nハンドリング:39.02\nニトロ:45.09",inline=False)
        embed.add_field(name="☆1 MAX:", value="マシンランク:859\n最高速度:256.0\n加速:62.24\nハンドリング:42.00\nニトロ:49.49")
        embed.add_field(name="☆2 MAX:", value="マシンランク:1,172\n最高速度:261.5\n加速:65.64\nハンドリング:44.79\nニトロ:53.91")
        embed.add_field(name="☆3 MAX:", value="マシンランク:1,476\n最高速度:266.8\n加速:68.86\nハンドリング:47.43\nニトロ:57.49")
        embed.set_image(url="https://cdn.discordapp.com/attachments/719041194872799264/720573470500716605/BMW_Z4_LCI_E89.png")
        embed.set_footer(text="最終更新:2020 07/05")
        await message.channel.send(embed=embed)

    elif message.content in ["a9:Camaro LT","a9:camaro lt"]:
        embed = discord.Embed(title="マシンの情報",description="Chevrolet Camaro LT",color=0xd0bf25)
        embed.add_field(name="マシンクラス:", value="Dクラス")
        embed.add_field(name="レア度:", value="アンコモン")
        embed.add_field(name="給油時間:", value="05m00s(<:switch:726284432234774600>02m00s)")
        embed.add_field(name="初期状態:", value="マシンランク:556\n最高速度:265.0\n加速:51.40\nハンドリング:41.17\nニトロ:48.53",inline=False)
        embed.add_field(name="☆1 MAX:", value="マシンランク:910\n最高速度:271.8\n加速:56.19\nハンドリング:43.75\nニトロ:53.78")
        embed.add_field(name="☆2 MAX:", value="マシンランク:1,232\n最高速度:278.9\n加速:60.63\nハンドリング:46.13\nニトロ:58.68")
        embed.add_field(name="☆3 MAX:", value="マシンランク:1,546\n最高速度:284.1\n加速:64.81\nハンドリング:48.39\nニトロ:63.29")
        embed.set_footer(text="最終更新:2020 07/05")
        await message.channel.send(embed=embed)
        
    elif message.content in ["a9:Challenger SRT8","a9:Challenger Srt8","a9:challenger srt8"]:
        embed = discord.Embed(title="マシンの情報", description="Dodge Challenger SRT8",color=0xe65420)
        embed.add_field(name="マシンクラス:", value="Cクラス")
        embed.add_field(name="レア度:", value="アンコモン")
        embed.add_field(name="給油時間:", value="30m00s(<:switch:726284432234774600>13m00s)")
        embed.add_field(name="初期状態:", value="マシンランク:799\n最高速度:292.0\n加速:64.00\nハンドリング:26.47\nニトロ:23.08",inline=False)
        embed.add_field(name="☆1 MAX:", value="マシンランク:1,077\n最高速度:297.5\n加速:66.40\nハンドリング:29.96\nニトロ:30.34")
        embed.add_field(name="☆2 MAX:", value="マシンランク:1,425\n最高速度:No Data\n加速:No Data\nハンドリング:No Data\nニトロ:No Data")
        embed.add_field(name="☆3 MAX:", value="マシンランク:1,687\n最高速度:308.6\n加速:71.92\nハンドリング:37.98\nニトロ:45.41")
        embed.set_footer(text="最終更新:2020 07/10")
        await message.channel.send(embed=embed)
        
    elif message.content in ["a9:Vulcan","a9:vulcan"]:
        embed = discord.Embed(title="マシンの情報", description="Aston Martin Vulcan",color=0x455d4c)
        embed.add_field(name="マシンクラス:", value="Aクラス")
        embed.add_field(name="レア度:", value="レア")
        embed.add_field(name="給油時間:", value="3h00m(<:switch:726284432234774600>54m00s)")
        embed.add_field(name="初期状態:", value="マシンランク:1,970\n最高速度:328.0\n加速:73.00\nハンドリング:39.63\nニトロ:50.33")
        embed.add_field(name="☆1 MAX:", value="マシンランク:2,205\n最高速度:331.5\n加速:74.30\nハンドリング:41.49\nニトロ:53.61")
        embed.add_field(name="☆2 MAX:", value="マシンランク:2,452\n最高速度:335.1\n加速:75.67\nハンドリング:43.44\nニトロ:57.07")
        embed.add_field(name="☆3 MAX:", value="マシンランク:2,736\n最高速度:339.2\n加速:77.29\nハンドリング:45.75\nニトロ:60.85")
        embed.add_field(name="☆4 MAX:", value="マシンランク:3,012\n最高速度:343.5\n加速:78.70\nハンドリング:47.80\nニトロ:64.79")
        embed.set_footer(text="最終更新:2020 07/10")
        await message.channel.send(embed=embed)

    await bot.process_commands(message)


bot.run(token)
