import disnake
from disnake.ext import commands
import os
import jishaku
from dotenv import load_dotenv

load_dotenv()

intents: disnake.Intents = disnake.Intents.all()


class EconomyBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned_or("-"),
            case_insensitive=True,
            strip_after_prefix=True,
            intents=intents
        )

    async def on_connect(self):
        print("Connected to discord")
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')
        bot.load_extension("jishaku")
        print("Loaded all cogs")
        

    async def on_ready(self) -> None:
        print(f"{self.user.name} is now ready to use")
        print(f"Disnake version: {disnake.__version__}")

    async def on_command_error(self, context: commands.Context, exception: commands.CommandError) -> None:
        if isinstance(exception, commands.CommandNotFound):
            return


bot = EconomyBot()

os.environ["JISHAKU_NO_UNDERSCORE"] = "True"


token: str | None = os.getenv(key="TOKEN")

bot.run(token)
