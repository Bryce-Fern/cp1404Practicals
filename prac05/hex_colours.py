
hex_codes = {"aquamarine1": "#7fffd4", "blueviolet": "#8a2be2", "coral": "#ff7f50",
               "darkgreen": "#006400", "DarkOrchid": "#9932cc", "MediumBlue": "#0000cd", "NavyBlue": "#000080",
               "orchid": "#da70d6", "purple": "#a020f0", "turquoise": "#40e0d0"}

colour_name = input("Colour name:")
while colour_name != "":
    print("The colour code for {} is {}".format(colour_name, hex_codes.get(colour_name)))
    colour_name = input("Colour name:")
