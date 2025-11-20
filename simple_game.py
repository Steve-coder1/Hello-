import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

class TapGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.score = 0
        self.time_left = 10
        self.is_playing = False

        self.score_label = Label(text=f"Score: {self.score}", font_size=40)
        self.time_label = Label(text=f"Time left: {self.time_left}", font_size=30)
        self.tap_button = Button(text="Tap Me!", font_size=50, on_press=self.increment_score)
        self.start_button = Button(text="Start Game", font_size=30, on_press=self.start_game)

        self.add_widget(self.score_label)
        self.add_widget(self.time_label)
        self.add_widget(self.tap_button)
        self.add_widget(self.start_button)

        self.tap_button.disabled = True

    def start_game(self, instance):
        self.score = 0
        self.time_left = 10
        self.score_label.text = f"Score: {self.score}"
        self.time_label.text = f"Time left: {self.time_left}"
        self.tap_button.disabled = False
        self.is_playing = True
        Clock.schedule_interval(self.update_clock, 1)
        self.start_button.disabled = True

    def update_clock(self, dt):
        if not self.is_playing:
            return False
        self.time_left -= 1
        self.time_label.text = f"Time left: {self.time_left}"
        if self.time_left <= 0:
            self.end_game()
            return False
        return True

    def increment_score(self, instance):
        if self.is_playing:
            self.score += 1
            self.score_label.text = f"Score: {self.score}"

    def end_game(self):
        self.is_playing = False
        self.tap_button.disabled = True
        self.start_button.disabled = False
        self.time_label.text = f"Game Over! Final Score: {self.score}"

class TapGameApp(App):
    def build(self):
        return TapGame()

if __name__ == "__main__":
    TapGameApp().run()