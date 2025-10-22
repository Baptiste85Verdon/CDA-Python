import arcade

from views.game_view import GameView

class MenuView(arcade.View):

    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

    def on_draw(self):
        self.clear()
        arcade.draw_text("MENU PRINCIPAL", self.window.width/2, self.window.height/2 + 50, arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("Appuyez sur ESPACE pour commencer", self.window.width/2, self.window.height/2, arcade.color.LIGHT_GRAY, 20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            game_view = GameView()
            self.window.show_view(game_view)
