import arcade
from pyexpat.errors import messages
from pyglet.resource import texture

from managers.input_manager import InputManager
from core.money import Money
from core.augment import Augment
from arcade.gui import UIFlatButton, UIManager, UIOnClickEvent, UIMessageBox, UITextureButton

totalMoney = Money()
listAugment = (
    Augment('Augmente vos clics de 2', 20, 1, False, totalMoney, 0, 550),
    Augment('Augmente vos clics de 10', 40, 10, False, totalMoney, 0, 500),
    Augment('Augmente vos clics de 20', 40, 20, False, totalMoney, 0, 450),
    Augment('Augmente vos clics de 150', 400, 150, False, totalMoney, 0, 400)
)


class GameView(arcade.View):
    """Vue principale du jeu."""

    def __init__(self):
        super().__init__()
        self.manager = UIManager()

    def setup_augments_buttons(self):
        for index, augment in enumerate(listAugment):
            bouton = UIFlatButton(
                text=augment.title + ' pour ' + str(augment.price) + ' Or',
                width=350,
                height=50,
                x=augment.pos_x,
                y=augment.pos_y,
            )
            self.manager.add(bouton)
            @bouton.event
            def on_click(event: UIOnClickEvent, a=augment):
                message = UIMessageBox(
                    width=350,
                    height=150,
                    message_text=a.buy_bonus(),
                )
                self.manager.add(message)
    def setup_click_button(self):
        texture_btn=arcade.load_texture("assets/gold_ore.webp")
        bouton_click = UITextureButton(
            width=350,
            height=350,
            x=680,
            y=100,
            texture=texture_btn
        )
        self.manager.add(bouton_click)
        @bouton_click.event
        def on_click(event: UIOnClickEvent):
            totalMoney.add_money_click()

    def on_show_view(self):
        self.setup_augments_buttons()
        self.setup_click_button()
        self.manager.enable()
        arcade.set_background_color(arcade.color.AMETHYST)

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        self.clear()
        self.manager.draw()
        arcade.draw_text("Or : "+str(totalMoney.get_total()), self.window.width / 2 + 200, self.window.height / 2 + 200,arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("Par clic : "+str(totalMoney.get_per_click())+" + "+str(totalMoney.get_bonus())+" = "+ str(totalMoney.get_per_click()+totalMoney.get_bonus()), self.window.width / 2 + 200, self.window.height / 2 + 250 ,arcade.color.WHITE, 20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            totalMoney.add_money_click()
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_RIGHT:
            totalMoney.add_money_click()


