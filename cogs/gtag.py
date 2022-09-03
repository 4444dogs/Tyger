import voltage
from voltage.ext import commands
import requests

def setup(client) -> commands.Cog:
    gtag =commands.Cog(
        "Gorilla Tag",
        "Different utilities related to Gorilla Tag!",
    )

    @gtag.command(description="Get how many people are playing Gorilla Tag!")
    async def gtusersonline(ctx:commands.CommandContext):
        usersonline = requests.get("http://ntsfranz.crabdance.com/how_many_monke")
        await ctx.reply(str(usersonline.text))

    return gtag
