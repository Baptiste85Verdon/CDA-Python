import arcade

class InputManager:
    def __init__(self):
        self.keys_pressed = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
        }

    def on_key_press(self, symbol):
        if symbol == arcade.key.Z:
            self.keys_pressed["up"] = True
        elif symbol == arcade.key.S:
            self.keys_pressed["down"] = True
        elif symbol == arcade.key.Q:
            self.keys_pressed["left"] = True
        elif symbol == arcade.key.D:
            self.keys_pressed["right"] = True

    def on_key_release(self, symbol):
        for key in self.keys_pressed:
            self.keys_pressed[key] = False
