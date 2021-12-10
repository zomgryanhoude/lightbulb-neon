# Neon

Neon is an add-on for [Lightbulb](https://github.com/tandemdude/hikari-lightbulb/) making it easier to handle component interactions.

## Installation

```bash
pip install git+https://github.com/neonjonn/lightbulb-neon.git
```

## Documentation

[ReadTheDocs](https://lightbulb-neon.readthedocs.io/en/latest/)

## Usage

```python
class Menu(neon.ComponentMenu):
    @neon.button("earth", "earth_button", hikari.ButtonStyle.SUCCESS, emoji="\N{DECIDUOUS TREE}")
    async def earth(self, button: neon.Button) -> None:
        await self.edit_msg(f"{button.emoji} - {button.custom_id}")

    @neon.option("Water", "water", emoji="\N{DROPLET}")
    @neon.option("Fire", "fire", emoji="\N{FIRE}")
    @neon.select_menu("sample_select_menu", "Pick fire or water!")
    async def select_menu_test(self, values: list) -> None:
        await self.edit_msg(f"You chose: {values[0]}!")

    @neon.button("Wind", "wind_button", hikari.ButtonStyle.PRIMARY, emoji="\N{WIND BLOWING FACE}\N{VARIATION SELECTOR-16}")
    @neon.button("Rock", "rock_button", hikari.ButtonStyle.SECONDARY, emoji="\N{MOYAI}")
    @neon.button_group()
    async def wind_rock(self, button: neon.Button) -> None:
        await self.edit_msg(f"You pressed: {button.custom_id}")

    @neon.on_timeout(disable_components=True)
    async def on_timeout(self) -> None:
        await self.edit_msg("\N{ALARM CLOCK} Timed out!")

@bot.command
@lightbulb.command("neon", "Check out Neon's component builder!")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def neon_command(ctx: lightbulb.Context) -> None:
    menu = Menu(ctx, timeout=30)
    resp = await ctx.respond("Bar", components=menu.build())
    await menu.run(resp)
```

## Contributing

If you wish to contribute to this project, please [open an issue](https://github.com/neonjonn/lightbulb-neon/issues/new) first to describe your issue or feature request. 

As soon as you've done that you may make a pull request, and I'll review your changes.

## Contributors

* [thomm.o](https://github.com/tandemdude) - [Refactor, improve code, mypy compliance](https://github.com/neonjonn/lightbulb-neon/pull/1)
