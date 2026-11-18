
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Çevre Dostu Bot aktif!")
    print("Bot çalışmaya hazır!")

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == "!yardim":
        await message.channel.send("🌍 ÇEVRE DOSTU BOT KOMUTLARI")
        await message.channel.send("!geridonusum - Geri dönüşüm bilgisi")
        await message.channel.send("!atik - Atık bilgisi")
        await message.channel.send("!oneri - Çevre önerileri")
        await message.channel.send("!plastik - Plastik kirliliği")

    elif message.content == "!geridonusum":
        await message.channel.send("♻️ Kağıt, cam, metal ve plastik uygun şekilde geri dönüştürülebilir!")

    elif message.content == "!atik":
        await message.channel.send("🗑️ Plastik şişelerin doğada parçalanması yüzlerce yıl sürebilir!")

    elif message.content == "!oneri":
        await message.channel.send("🌳 Bez çanta kullan, suyu boşa harcama ve gereksiz yanan ışıkları kapat!")

    elif message.content == "!plastik":
        await message.channel.send("🌊 Tek kullanımlık plastikleri azaltarak doğayı koruyabilirsin!")

client.run("BOT_TOKENİNİ_BURAYA_YAZ")
