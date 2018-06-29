from kivy.app import App
from kivy.lang import Builder


class MilesConversionApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('conversion.kv')
        return self.root

    def handle_calculation(self):
        value = self.get_valid_value()
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.get_valid_value() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculation()

    def get_valid_value(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0


MilesConversionApp().run()
