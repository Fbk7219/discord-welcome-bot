import discord
import os
from flask import Flask
import threading

YOUR_USER_ID = 1191415811773059137

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot ONLINE as {client.user}")

@client.event
async def on_member_join(member):
    try:
        you = await client.fetch_user(YOUR_USER_ID)
        await you.send(f"🔔 NEW JOIN: {member.name} joined {member.guild.name} - {member.guild.member_count} members")
    except: pass
    try:
        msg1 = f"Hello {member.mention}, Welcome to my discord trading community.\n\nAttend to the notice below,\n\nNOTICE‼️\nYou are advised to disable friend request on your account. It helps for the security of your discord account from spam messages. You can do so here👇\nYou can go to your settings, click on friend request and disable all three options"
        files = [discord.File("guide1.jpg"), discord.File("guide2.jpg")]
        await member.send(content=msg1, files=files)
        msg2 = f"Let me know when you attend to the notice 👇\n\n{member.mention} Reply Done once you have disabled the friend requests."
        await member.send(content=msg2)
    except Exception as e:
        print(f"DM error: {e}")

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot ONLINE"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

threading.Thread(target=run_web).start()
client.run(os.environ.get("BOT_TOKEN"))
