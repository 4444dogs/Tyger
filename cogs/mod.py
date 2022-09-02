import voltage
from voltage.ext import commands

def setup(client) -> commands.Cog:
    mod = commands.Cog(
        "Moderation",
        "All of the basic moderation actions!"
    )

    @mod.command(description="Purge / mass delete a certain amount of messages.", aliases=["clear"])
    async def purge(ctx: commands.CommandContext, amount: int):
        if ctx.author.permissions.manage_messages == True or ctx.author.id == ctx.server.owner.id:
            await ctx.channel.purge(amount + 1)
            await ctx.send(f"Purged {str(amount)} messages!")
        else:
            await ctx.reply("Sorry, you must have the `Manage Messages` permission to use this command.")

    @mod.command(description="Ban a member.")
    async def ban(ctx: commands.CommandContext, member: voltage.Member, reason: str = "No Reason"):
        if ctx.author.permissions.ban_members == True or ctx.author.id == ctx.server.owner.id:
            if ctx.author.id == member.id:
                await ctx.send("Bro, why would you want to ban yourself?")
            elif member.id == "01GBWFPMTGMWMH89HZQB1PRWYG":
                await ctx.send("Trying to beat me at my own game? Nice try.")
            elif member.permissions.ban_members == True or member.id == ctx.server.owner.id:
                await ctx.send("Sorry, you cannnot ban a member that can also ban members.")
            else:
                try:
                    await ctx.reply(f"Banned `{member.name}` \n Reason: `{reason}`")
                    await client.cache.http.open_dm(member.id)
                    dm_channel = await client.http.open_dm(member.id)
                    dm_channel = voltage.DMChannel(dm_channel, client.cache)
                    await dm_channel.send(f"You have been banned from `{ctx.server.name}` \n Reason: `{reason}`")
                    await member.ban(reason)
                except voltage.BotNotEnoughPerms:
                    await ctx.send("The member could not be banned because Tyger does not have the `Ban Members` permission.")
        else:
            await ctx.reply("Sorry, you must have the `Ban Members` permission to use this command.")
    @mod.command(description="Kick a member.")
    async def kick(ctx: commands.CommandContext, member: voltage.Member, reason:str = "No Reason"):
        if ctx.author.permissions.kick_members == True or ctx.author.id == ctx.server.owner.id:
            if ctx.author.id == member.id:
                await ctx.send("Bro, why would you want to kick yourself?")
            elif member.id == "01GBWFPMTGMWMH89HZQB1PRWYG":
                await ctx.send("Trying to beat me at my own game? Nice try.")
            elif member.permissions.kick_members == True or member.id == ctx.server.owner.id:
                await ctx.send("Sorry, you cannnot kick a member that can also kick members.")
            else:
                try:
                    await ctx.reply(f"Kicked `{member.name}` \n Reason: `{reason}`")
                    await client.cache.http.open_dm(member.id)
                    dm_channel = await client.http.open_dm(member.id)
                    dm_channel = voltage.DMChannel(dm_channel, client.cache)
                    await dm_channel.send(f"You have been kicked from `{ctx.server.name}` \n Reason: `{reason}`")
                    await member.kick()
                except voltage.BotNotEnoughPerms:
                    await ctx.send("The member could not be kicked because Tyger does not have the `Kick Members` permission.")

    return mod

