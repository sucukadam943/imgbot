import discord
from discord.ext import commands
import Dcbot


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def selam(ctx):
    await ctx.send(f"Selam {ctx.author}. Ben {bot.user}")

@bot.command() 
async def Photograph(ctx):
    if ctx.message.attachments:
        for dosya in ctx.message.attachments:
            await dosya.save(f"resimler/{dosya.filename}")
            await ctx.send("Geldi")
        x,y = Dcbot.dcaktar(f"resimler/{dosya.filename}")
        y=round(y*100,1)
        if x == "Karga\n":
            await ctx.send(f"Bu bir Karga. %{y}, oranıyla eminim.")
            await ctx.send(f"Kargalar doğada bulunan her şeyi yiyebilir. Çöp, böcek, sinek gibi birçok canlıyı yiyerek beslenebilir. Kargaların çeşidi olan leş kargaları sadece leşleri yer.")
        elif x == "Guvercin\n":
            await ctx.send(f"Bu bir Güvercin. %{y}, oranıyla eminim.")
            await ctx.send(f"Bulgur ve pirinci bolca tüketen güvercinler oldukça sıcakkanlı canlılardır. Güvercinler aynı zamanda çeşitli sebzeleri de beraberinde tüketmektedir. Lahana, bezelye, karnabahar ve marul gibi yiyecekleri dilimleyerek güvercine verebilirsiniz. Dilerseniz petshoplarda yer alan güvercin yemlerini de tercih edebilirsiniz.")
        elif x == "Serce\n":
            await ctx.send(f"Bu bir Serçe. %{y}, oranıyla eminim.")
            await ctx.send(f"Genellikle meyve, tohum, böcek ve larva gibi besinler tüketirler. Göçmen değildirler. Çekirdek ve ekmek artıkları da yerler.")
        elif x == "Diger\n":
            await ctx.send(f"Bunun ne olduğu hakkında hiçbir fikrim olamdığına. %{y}, oranıyla eminim.")
    else:
        await ctx.send("Gelmedi")

bot.run("Your-bot-key")
