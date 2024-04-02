import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()


class EconomyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("-"),
            case_insensitive=True,
            strip_after_prefix=True
        )

    async def on_ready(self):
        print(f"{self.user.name} is now ready to use")
        print(f"Disnake version: {disnake.__version__}")


bot = EconomyBot()


token = os.getenv("TOKEN")

bot.run(token)

# this comment is to test if the env is added to git or not