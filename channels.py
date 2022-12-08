# Get a list of all channels in the server
channels = client.get_all_channels()

# Loop through each channel and scrape the messages
for channel in channels:
    # Get a list of all messages in the channel
    messages = await channel.history(limit=None).flatten()

    # Loop through each message and analyze the sentiment
    for message in messages:
        sentiment = analyze_sentiment(message.content)
        print(f'Sentiment for message "{message.content}": {sentiment}')
