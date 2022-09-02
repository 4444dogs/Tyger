import voltage
from voltage.ext import commands
from datetime import datetime

def setup(client) -> commands.Cog:
    info = commands.Cog(
        "Users",
        "Commands for getting info about Revolt users, channels, and categories!",
    )

    @info.command(description="Get the join date of a user.")
    async def joindate(ctx: commands.CommandContext, member: voltage.Member):
        await ctx.reply(datetime.fromtimestamp(member.created_at / 1000))
    @info.command(description="Get the link to a user's profile picture.")
    async def profilepic(ctx: commands.CommandContext, member: voltage.Member):
        await ctx.reply(member.avatar.url)
    @info.command(description="Get the creation date of a channel.")
    async def channelcreationdate(ctx: commands.CommandContext, channel: voltage.Channel):
        await ctx.reply(datetime.fromtimestamp(channel.created_at / 1000))

    return info
