from redbot.core.bot import Red

from .banmessage import BanMessage


async def setup(bot: Red) -> None:
    cog = BanMessage(bot)
    bot.add_cog(cog)
