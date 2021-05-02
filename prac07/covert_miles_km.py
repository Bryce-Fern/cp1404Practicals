
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

    def handle_addsubtract(self, increment):



ConvertMtoKM().run()