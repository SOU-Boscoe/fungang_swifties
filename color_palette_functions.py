def get_colors(): 
    """Returns a set of primary, secondary, and tertiary colors that will be used in other functions
    """
    return [
        "red", 
        "red-orange", 
        "orange", 
        "yellow-orange", 
        "yellow", 
        "yellow-green", 
        "green", 
        "blue-green", 
        "blue", 
        "blue-violet", 
        "violet", 
        "red-violet"
    ]

def get_complimentary(color, color_wheel):
    if color in color_wheel:
        compliment_index = color_wheel.index(color) + 6
        if compliment_index > 11:
            compliment_index -= 12
        compliment = color_wheel[compliment_index]
        return compliment
    else:
        return "blank"

color_wheel = get_colors()    
print(get_complimentary("green", color_wheel))