from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class NameListApp(App):
    def build(self):
        # Character names
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

        root = Builder.load_file('dynamic_labels.kv')

        for name in self.names:
            label = Label(text=name, font_size=24)
            root.ids.name_box.add_widget(label)

        return root


NameListApp().run()
