"""
CP1404/CP5632 Practical
Name: Hein Htet
Make a program to look up hexadecimals of colors
"""
COLOR_TO_HEX = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                "alizarin crimson": "#e32636", "blue green": "#0d98ba", "bright lavender": "#bf94e4",
                "coral pink": "#f88379", "daffodil": "#ffff31",
                "dark brown": "#654321", "dark orange": "#ff8c00"}

print([color for color in COLOR_TO_HEX])

color_name = input("Input the color: ").lower()
while color_name != "":
    if color_name in COLOR_TO_HEX:
        print(color_name, "is", COLOR_TO_HEX[color_name])
    else:
        print("Invalid color.")
    color_name = input("Input the color: ").lower()

color_width = int((max(len(color_name) for color_name in COLOR_TO_HEX)))
hex_width = (max(len(COLOR_TO_HEX[color_name]) for color_name in COLOR_TO_HEX))
for color_name in COLOR_TO_HEX:
    print(f"{color_name:<{color_width}} is {COLOR_TO_HEX[color_name]}")