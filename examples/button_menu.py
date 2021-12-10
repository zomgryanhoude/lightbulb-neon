import os

import dotenv
import lightbulb
from hikari import ButtonStyle

import neon

dotenv.load_dotenv()

bot = lightbulb.BotApp(
    os.environ["DISCORD_TOKEN"],
    prefix="n.",
)


class ButtonMenu(neon.ComponentMenu):
    @neon.button("Dog", "dog", ButtonStyle.PRIMARY, emoji="\N{DOG FACE}")
    async def dog_button(self) -> None:
        await self.edit_msg("Dog are so cute!")

    @neon.button("Cat", "cat", ButtonStyle.DANGER, emoji="\N{CAT FACE}")
    async def cat_button(self) -> None:
        await self.edit_msg("Cats are adorable!")

    @neon.button("Fish", "fish", ButtonStyle.SUCCESS, emoji="\N{FISH}")
    async def fish_button(self) -> None:
        await self.edit_msg("Fish are so cool!")

    @neon.button("Bird", "bird", ButtonStyle.SECONDARY, emoji="\N{BIRD}")
    async def bird_button(self) -> None:
        await self.edit_msg("Birds are so small and cute!")


@bot.command()
@lightbulb.command("pet", "Choose a pet!")
@lightbulb.implements(lightbulb.PrefixCommand)
async def pet_cmd(ctx: lightbulb.Context) -> None:
    menu = ButtonMenu(ctx, timeout=30)
    resp = await ctx.respond("Choose a pet!", components=menu.build())
    await menu.run(resp)


if __name__ == "__main__":
    bot.run()
