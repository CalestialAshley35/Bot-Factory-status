# Bot Factory Status

Welcome to the **Bot Factory Status** project! This repository provides a simple example of how to set a custom status for your Discord bot using Python and the `discord.py` library. 

## Overview

**Bot Factory Status** is designed to help you set a custom status for your Discord bot. The status can be set to any message you choose, and it will be updated whenever your bot starts up.

## Features

- Customizable bot status
- Easy to integrate into your existing bot project
- Built with Python and `discord.py`

## Getting Started

To use this project, follow these steps:

1. **Open Your Replit Project:**
   Go to your Bot Factory Status project on Replit: [Bot Factory Status on Replit](https://replit.com/@calestialashley/Bot-Factory-Status?s=app).

2. **Add the Code:**
   Insert the provided code into your main Python file (typically `main.py`).

3. **Configure the Bot Token:**
   Replace `'YOUR_BOT_TOKEN'` in the code with your actual Discord bot token.

4. **Run the Bot:**
   Start your bot on Replit. Your bot's status should now display as the custom message you specified.

## Code Example

Here's a basic code snippet to set your bot's status:

```python
import discord
from discord.ext import commands

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Event to set the bot's status
@bot.event
async def on_ready():
    # Custom status
    activity = discord.Game(name="Building Bots at Bot Factory!")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'Logged in as {bot.user}')

# Your bot's token
bot.run('YOUR_BOT_TOKEN')
```

## Customization

You can customize the status message by changing the text inside `discord.Game(name="Your Custom Status")` to whatever you like.

## Contributing

Feel free to fork this repository and submit pull requests if you have improvements or new features to add.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, contact me at calestialashley@gmail.com
