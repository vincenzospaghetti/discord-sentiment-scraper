import discord
from textblob import TextBlob

client = discord.Client()

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Use TextBlob to calculate the sentiment of the message
    blob = TextBlob(message.content)
    sentiment = blob.sentiment.polarity

    # Print the sentiment of the message
    print(f"{message.author}: {sentiment}")

client.run("YOUR_DISCORD_BOT_TOKEN_HERE")
