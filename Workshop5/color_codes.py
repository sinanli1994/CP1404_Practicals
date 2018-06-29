color_codes = {"Aliceblue": "#f0f8ff", "Antiquewhite": "#faebd7", "Antiquewhite1": "#ffefdb",
               "Antiquewhite2": "#eedfcc", "Antiquewhite3": "#cdc0b0", "Antiquewhite4": "#8b8378",
               "Aquamarine1": "#7fffd4", "Aquamarine2": "#76eec6", "Azure1": "#f0ffff", "Azure2": "#e0eeee"}

color = input("Enter color name: ").title()
while color != "":
    if color in color_codes:
        print(color, "is", color_codes[color])
    else:
        print("Invalid short state")
    color = input("Enter color name: ").title()

for color in color_codes:
    print("{:4} is {}".format(color, color_codes[color]))