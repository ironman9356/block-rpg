import disnake
from disnake.ext import commands


class Account(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def register(self, ctx) -> None:
        embed = disnake.Embed(title="Block RPG")
        embed.description = "Oh hello there new friend\nPlease read these before starting\n- Follow the Discord [ToS](https://discordapp.com/terms) and [CG](https://discordapp.com/guidelines)\n- Dont share your passwords with anyone\n- The bot only stores your usename and user id"
        embed.color = disnake.Color.random()
        await ctx.send("hello", embed=embed)


def setup(bot):
    print("Loaded Account")
    bot.add_cog(Account(bot))
