import voltage
from voltage.ext import commands
from random import randint

def setup(client) -> commands.Cog:
    numbers = commands.Cog(
        "Numbers",
        "MATH!!!",
    )

    @numbers.command(description="Run math equations with one operator! Current operations: `add, multiply, divide, modulus, exponent, floordivide`")
    async def math(ctx: commands.CommandContext, operation, num1, num2):
        if str(operation) == "add":
            if num1 == "9" and num2 == "10":
                await ctx.reply("21!!!!!!!!!!")
            else:
                await ctx.reply(str(float(num1) + float(num2)))
        elif str(operation) == "multiply":
            await ctx.reply(str(float(num1) * float(num2)))
        elif str(operation) == "subtract":
            await ctx.reply(str(float(num1) - float(num2)))
        elif str(operation) == "divide":
            await ctx.reply(str(float(num1) / float(num2)))
        elif str(operation) == "modulus":
            await ctx.reply(str(float(num1) % float(num2)))
        elif str(operation) == "exponent":
            await ctx.reply(str(float(num1) ** float(num2)))
        elif str(operation) == "floordivide":
            await ctx.reply(str(float(num1) // float(num2)))
    @numbers.command(description="Generate a random number!")
    async def randomnum(ctx: commands.CommandContext, num1, num2):
        await ctx.reply(str(randint(int(num1), int(num2))))

    return numbers
