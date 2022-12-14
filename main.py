import voltage
from voltage.ext import commands
import dotenv
import os
import ast
from voltage.internals import HTTPHandler


class CustomHelpCommand(commands.HelpCommand):
    async def send_help(self, ctx: commands.CommandContext):
        embed = voltage.SendableEmbed(
            title="Help",
            description=f"Use `{ctx.prefix}help <command>` to get help for a command.",
            colour="#EA7618",
            icon_url=ctx.author.display_avatar.url
        )
        text = "\n### **No Category**\n"
        for command in self.client.commands.values():
            if command.cog is None:
                text += f"> {command.name}\n"
        for i in self.client.cogs.values():
            text += f"\n### **{i.name}**\n{i.description}\n"
            for j in i.commands:
                text += f"\n> {j.name}"
        if embed.description:
            embed.description += text
        return await ctx.reply(f"[]({ctx.author.id})", embed=embed)
    async def send_command_help(self, ctx: commands.CommandContext, command: commands.Command):
        embed = voltage.SendableEmbed(
            title=f"Help for {command.name}",
            colour="#EA7618",
            icon_url=ctx.author.display_avatar.url
        )
        text = str()
        text += f"\n### **Usage**\n> `{ctx.prefix}{command.usage}`"
        if command.aliases:
            text += f"\n\n### **Aliases**\n> {ctx.prefix}{', '.join(command.aliases)}"
        embed.description = command.description + text if command.description else text
        return await ctx.reply(f"[]({ctx.author.id})", embed=embed)
    async def send_cog_help(self, ctx: commands.CommandContext, cog: commands.Cog):
        embed = voltage.SendableEmbed(
            title=f"Help for {cog.name}",
            colour="#EA7618",
            icon_url=ctx.author.display_avatar.url,
        )
        text = str()
        text += f"\n### **Description**\n{cog.description}"
        text += f"\n\n### **Commands**\n"
        for command in cog.commands:
            text += f"> {ctx.prefix}{command.name}\n"
        embed.description = text
        return await ctx.reply(f"[]({ctx.author.id})", embed=embed)

client = commands.CommandsClient("~", help_command=CustomHelpCommand)

config = dotenv.dotenv_values(".env")

dotenv.load_dotenv()

@client.listen("ready")
async def ready():
    client.add_extension("cogs.numbers")
    client.add_extension("cogs.info")
    client.add_extension("cogs.mod")
    client.add_extension("cogs.minecraft")
    client.add_extension("cogs.gtag")
    for i in range(len(client.servers)):
        approved = False
        for q in range(len(ast.literal_eval(os.getenv("APPROVED_SERVERS")))):
            if ast.literal_eval(os.getenv("APPROVED_SERVERS"))[q] == client.servers[i].id:
                approved = True
        if approved == False:
            await client.servers[i].leave()
@client.listen("server_create")
async def server_create(server: voltage.Server):
    approved = False
    for q in range(len(ast.literal_eval(os.getenv("APPROVED_SERVERS")))):
            if ast.literal_eval(os.getenv("APPROVED_SERVERS"))[q] == server.id:
                approved = True
            if approved == False:
                await server.leave()
@commands.command(description="Get info about the instance of Tyger you are using.")
async def instance(ctx: commands.CommandContext):
    if os.getenv("INSTANCE_NAME") != "": instance_name = os.getenv("INSTANCE_NAME")
    else: instance_name = "Unnamed Instance"
    if os.getenv("INSTANCE_DESCRIPTION") != "": instance_description = os.getenv("INSTANCE_DESCRIPTION")
    else: instance_description = "No Description"
    if os.getenv("INSTANCE_OWNER") != "": instance_owner = client.get_user(os.getenv("INSTANCE_OWNER")).name
    else: instance_owner = "No Owner"
    await ctx.reply(f"""Instance Name: `{instance_name}`
    Instance Description: `{instance_description}`
    Instance Owner: `{instance_owner}`""")

if os.getenv("API_URL") != "": api_url = os.getenv("API_URL")
else: api_url = "https://api.revolt.chat/"

original__init__ = HTTPHandler.__init__
def new__init__(self, *args, **kwargs):
    original__init__(self, *args, **kwargs)
    self.api_url = api_url
HTTPHandler.__init__ = new__init__

client.run(os.getenv("TOKEN"))
