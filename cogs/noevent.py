from discord.ext import commands
from helpers import checks


class NoEvent(commands.Cog):
    """Halloween event commands."""

    def __init__(self, bot):
        self.bot = bot

    @checks.has_started()
    @commands.command()
    async def event(self, ctx: commands.Context):
        """No event."""

        await ctx.send("There is no event currently active.")


def setup(bot):
    bot.add_cog(NoEvent(bot))
