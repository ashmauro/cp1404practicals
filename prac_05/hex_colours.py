"""
CP1404/CP5632 Practical
Hex colours in a dictionary
"""

COLOUR_CODES = {"AliceBlue": "#f0f8ff", "aquamarine2": "#76eec6", "blue1": "#0000ff", "brown": "#a52a2a",
                "burlywood1": "#ffd39b", "CadetBlue1": "#98f5ff", "chartreuse3": "	#66cd00", "chocolate2": "#ee7621",
                "CornflowerBlue": "#6495ed", "DarkOrchid3": "#9a32cd"}
print(COLOUR_CODES)

hexadecimal_code = input("Enter hexadecimal colour name: ")
while hexadecimal_code != '':
    if hexadecimal_code in COLOUR_CODES:
        print("{} hexadecimal code is {}".format(hexadecimal_code, COLOUR_CODES[hexadecimal_code]))
    else:
        print("Invalid hexadecimal colour name.")
    hexadecimal_code = input("Enter hexadecimal colour name: ")
