import arcade

from core.settings import SCREEN_WIDTH, SCREEN_HEIGHT, INTERVAL
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
        self.background = arcade.load_texture('assets/minecraft_background.png')
        self.elapsed = 0.0
        arcade.schedule(self.auto_click_tick, INTERVAL)

    def setup_augments_buttons(self):
        texture_btn_augments=arcade.load_texture("assets/trade_background.png")
        for index, augment in enumerate(listAugment):
            bouton = UITextureButton(
                text=augment.title + ' pour ' + str(augment.price) + ' Or',
                width=350,
                height=50,
                x=augment.pos_x,
                y=augment.pos_y,
                texture=texture_btn_augments,
                style={"normal": UITextureButton.UIStyle(font_color=arcade.color.BLACK),
                        "hover":  UITextureButton.UIStyle(font_color=arcade.color.BLACK),
                        "press":  UITextureButton.UIStyle(font_color=arcade.color.BLACK),
                        "disabled": UITextureButton.UIStyle(font_color=arcade.color.BLACK),
                       },
            )
            self.manager.add(bouton)
            @bouton.event
            def on_click(event: UITextureButton, a=augment):
                message = UIMessageBox(
                    width=350,
                    height=150,
                    message_text=a.buy_bonus(),
                )
                self.manager.add(message)

    def setup_click_button(self):
        texture_btn_click=arcade.load_texture("assets/gold_ore.webp")
        bouton_click = UITextureButton(
            width=350,
            height=350,
            x=780,
            y=100,
            texture=texture_btn_click
        )
        self.manager.add(bouton_click)
        @bouton_click.event
        def on_click(event: UIOnClickEvent):
            totalMoney.add_money_click()

    def auto_click_tick(self, dt: float):
        totalMoney.add_money_click()
        self.elapsed = 0.0

    # TODO UTILE???
    #def on_update(self, delta_time: float):
        #self.elapsed = min(self.elapsed + delta_time, 10.0)

    def on_show_view(self):
        self.setup_augments_buttons()
        self.setup_click_button()
        self.manager.enable()
        arcade.set_background_color(arcade.color.AMETHYST)

    def on_hide_view(self):
        self.manager.disable()
        arcade.unschedule(self.auto_click_tick)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.manager.draw()
        arcade.draw_text("Or : "+str(totalMoney.get_total()), self.window.width / 2 + 300, self.window.height / 2 + 200,arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("Par clic : "+str(totalMoney.get_per_click())+" + "+str(totalMoney.get_bonus())+" = "+ str(totalMoney.get_per_click()+totalMoney.get_bonus()), self.window.width / 2 + 300, self.window.height / 2 + 250 ,arcade.color.WHITE, 20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            totalMoney.add_money_click()
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_RIGHT:
            totalMoney.add_money_click()





