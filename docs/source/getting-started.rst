===============
Getting Started
===============

Basic Button Menu
=================

This assumes ``bot`` is an instance of :obj:`lightbulb.BotApp`

.. code-block:: python

    import neon

    class Menu(neon.ComponentMenu):
        @neon.button("fire", "fire_button", hikari.ButtonStyle.DANGER, emoji="\N{FIRE}")
        async def fire(self) -> None:
            await self.edit_msg("\N{FIRE}")

    @bot.command
    @lightbulb.command("flames", "Make a cosy fire")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def fire_command(ctx: lightbulb.Context) -> None:
        menu = Menu(ctx)
        msg = await ctx.respond("Bar", components=menu.build())
        await menu.run(msg)

When the ``flames`` command is ran, it will produce a message with a red button, that says ``fire`` next to the 🔥 emoji.

Retreiving the button instance
------------------------------

If you want to access the :obj:`neon.Button` instance in the callback function, just simply pass the ``button`` argument to the function, like so:

.. code-block:: python

    @neon.button("fire", "fire_button", hikari.ButtonStyle.DANGER, emoji="\N{FIRE}")
    async def fire(self, button: neon.Button) -> None:
        await self.edit_msg(f"\N{FIRE} - {button.custom_id}")

Grouping buttons
================

.. code-block:: python

    @neon.button("wind", "wind_button", hikari.ButtonStyle.PRIMARY, emoji="\N{WIND BLOWING FACE}\N{VARIATION SELECTOR-16}")
    @neon.button("rock", "rock_button", hikari.ButtonStyle.SECONDARY, emoji="\N{MOYAI}")
    @neon.button_group()
    async def wind_rock(self, button: neon.Button) -> None:
        await self.edit_msg(f"You chose: {button.custom_id}")

Select Menus
============

.. code-block:: python

    @neon.option("Water", "water", emoji="\N{DROPLET}")
    @neon.option("Earth", "earth", emoji="\N{DECIDUOUS TREE}")
    @neon.select_menu("select_menu", "Pick earth or water!")
    async def select_menu_test(self, values: list) -> None:
        await self.edit_msg(values[0])

Timeouts
========

By default the menu will time out after 60 seconds, after which no interactions will work for that message.

You can modify the timeout length by passing the ``timeout`` argument to your ``Menu`` constructor.

.. code-block:: python

    menu = Menu(ctx, timeout=30)

You can also create your own custom timeout function in your ``Menu`` class.

.. code-block:: python

    @neon.on_timeout(disable_components=True)
    async def on_timeout(self) -> None:
        await self.edit_msg("⏰ Timed out!")
