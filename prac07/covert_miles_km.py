from kivy.app import App
from kivy.lang import Builder

miles_to_km = 1.60934


class ConvertMtoKM(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_validated_value()
        result = value * miles_to_km
        self.root.ids.output_label.text = str(result)

    def handle_add_subtract(self, increment):
        value = self.get_validated_value() + increment
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()

    def get_validated_value(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertMtoKM().run()
