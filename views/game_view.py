import time
import arcade

from core.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from core.money import Money
from core.augment import Augment
from arcade.gui import UIManager, UIOnClickEvent, UIMessageBox, UITextureButton, UIAnchorLayout, Property, UISpace, bind
from arcade.types import Color

totalMoney = Money()
listAugment = (
    Augment(1,'Augmente vos clics de 1', 20,1, 1, False,0,100,'',0,0, 0,totalMoney, 0, 550),
    Augment(2,'Augmente vos clics de 10', 40,1, 10, False,0,30,'Test de message',5,1, 1,totalMoney, 0, 495),
    Augment(3,'Réduit le temps de vos clics auto de 8s',40, 3, 8, False,0,1,'',0,0, 2,totalMoney, 0, 440),
    Augment(4,'Augmente vos clics auto de 800',10, 2, 800, False,0,10,'',0,0, 2,totalMoney, 0, 385),
    Augment(5,'Augmente vos clics de 150', 400, 1, 150, False,0,10,'Test',123456789,0,2, totalMoney, 0, 330)
)
print(listAugment)
class ProgressbarAutomation(UIAnchorLayout):
    """A custom progress bar widget using UISpace for fill animation."""

    value = Property(0.0)  # Va de 0.0 à 1.0

    def __init__(
        self,
        value: float = 0.0,
        width=400,
        height=20,
        color: Color = arcade.color.GREEN,
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            size_hint=None,
        )
        self.with_background(color=arcade.uicolor.GRAY_CONCRETE)
        self.with_border(color=arcade.uicolor.BLACK)

        self._bar = UISpace(
            color=color,
            size_hint=(value, 1),
        )
        self.add(self._bar, anchor_x="left", anchor_y="top")
        self.value = value
        # Met à jour la barre
        bind(self, "value", self._update_bar)

    def _update_bar(self):
        # Rempli proportionnellement de gauche à droite
        self._bar.size_hint = (self.value, 1)
        self._bar.visible = self.value > 0

class GameView(arcade.View):
    """Vue principale du jeu."""

    def __init__(self):
        super().__init__()
        self.manager = UIManager()
        self.background = arcade.load_texture('assets/minecraft_background2.png')

        self.progress_bar = ProgressbarAutomation()
        self.progress_bar.center_x = 950
        self.progress_bar.center_y = 100
        self.manager.add(self.progress_bar)

        self.interval = totalMoney.get_initial_interval()
        self.last_interval = self.interval
        self.cycle_start_time = time.time()
        arcade.schedule(self.auto_click_tick, totalMoney.get_initial_interval())

    def setup_augments_buttons(self):
        texture_btn_augments=arcade.load_texture("assets/trade_background.png")
        for index, augment in enumerate(listAugment):
            bouton = UITextureButton(
                text=augment.title + ' pour ' + str(augment.price) + ' Or',
                width=425,
                height=50,
                x=augment.pos_x,
                y=augment.pos_y,
                texture=texture_btn_augments,
                style={"normal": UITextureButton.UIStyle(font_color=arcade.color.BLACK),
                        "hover":  UITextureButton.UIStyle(font_color=arcade.color.BLACK),
                        "press":  UITextureButton.UIStyle(font_color=arcade.color.BLACK),
                       },
            )
            self.manager.add(bouton)
            @bouton.event
            def on_click(event: UITextureButton, a=augment):
                message = UIMessageBox(
                    width=450,
                    height=175,
                    # message_text=a.buy_bonus(),
                    message_text=a.check_condition(),
                    # message_text=a.get_all_instances(),
                )
                self.manager.add(message)

    def setup_click_button(self):
        texture_btn_click=arcade.load_texture("assets/gold_ore.webp")
        bouton_click = UITextureButton(
            width=350,
            height=350,
            x=780,
            y=175,
            texture=texture_btn_click
        )
        self.manager.add(bouton_click)
        @bouton_click.event
        def on_click(event: UIOnClickEvent):
            totalMoney.add_money_click()

    def auto_click_tick(self, dt: float):
        totalMoney.add_money_automation()
        # Reset du cycle de la progress_bar
        self.cycle_start_time = time.time()

        # Si changement d'interval on relance le schedule
        new_interval = totalMoney.get_initial_interval()
        if new_interval != self.interval:
            self.interval = new_interval
            arcade.unschedule(self.auto_click_tick)
            arcade.schedule(self.auto_click_tick, self.interval)

    def on_update(self, delta_time: float):
        now = time.time()
        elapsed = now - self.cycle_start_time

        # Remplissage de la progress_bar de manière proportionnelle par rapport à l'interval et au temps écoulé
        progress = min(elapsed / self.interval, 1.0)
        self.progress_bar.value = progress


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
        arcade.draw_text("Or : "+str(totalMoney.get_total()), 950, 565,arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("Par clic : "+ str(totalMoney.get_per_click()+totalMoney.get_bonus_per_click()), 950, 615 ,arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("temps entre chaque clic automatique : "+str(totalMoney.get_initial_interval()-totalMoney.get_bonus_interval())+"s", 950, 60 ,arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Par clic automatique : "+ str(totalMoney.get_per_automation()+totalMoney.get_bonus_per_automation()), 950, 25 ,arcade.color.WHITE, 20, anchor_x="center")

    #TODO ENLEVER
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            totalMoney.add_money_click()
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_RIGHT:
            totalMoney.add_money_click()





