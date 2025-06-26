from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

class ExerciseScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.exercise_label = Label(text="Welcome to Fitness Corner!", font_size=32)
        self.timer_label = Label(text="Seconds: 0", font_size=24)
        self.message_label = Label(text="Press Start to begin.", font_size=20)
        self.start_button = Button(text="Start", size_hint=(1, 0.2), font_size=24)
        self.start_button.bind(on_press=self.start_exercise)

        self.add_widget(self.exercise_label)
        self.add_widget(self.timer_label)
        self.add_widget(self.message_label)
        self.add_widget(self.start_button)

        self.seconds = 0
        self.exercise_index = 0
        self.exercises = [
            "Knee Exercise",
            "Pillow Exercise",
            "Strengthening",
            "Folding",
            "Bending",
            "Hip Up",
            "Hip Side",
            "Hip Down"
        ]
        self.exercise_durations = [20, 8, 15, 30, 30, 8, 8, 8]  # seconds for each exercise
        self.running = False

    def start_exercise(self, instance):
        self.exercise_index = 0
        self.seconds = 0
        self.running = True
        self.exercise_label.text = f"Exercise: {self.exercises[self.exercise_index]}"
        self.message_label.text = "Let's start!"
        self.start_button.disabled = True
        Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        if not self.running:
            return False
        self.seconds += 1
        self.timer_label.text = f"Seconds: {self.seconds}"
        if self.seconds >= self.exercise_durations[self.exercise_index]:
            self.exercise_index += 1
            if self.exercise_index >= len(self.exercises):
                self.exercise_label.text = "All exercises completed!"
                self.message_label.text = "Congratulations!"
                self.start_button.disabled = False
                self.running = False
                return False
            else:
                self.exercise_label.text = f"Exercise: {self.exercises[self.exercise_index]}"
                self.message_label.text = "Next exercise!"
                self.seconds = 0
        return True

class FitnessApp(App):
    def build(self):
        return ExerciseScreen()

if __name__ == '__main__':
    FitnessApp().run()

