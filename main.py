import color_palette_functions

def main():
    print("Hello! Welcome to Color Palette Maker! ")
    user_color = input("Please enter what color you're using! ")

    color_wheel = color_palette_functions.get_colors()
    recommended_color = color_palette_functions.get_complimentary(user_color, color_wheel)

    print(f"Here is your recommended_color: {recommended_color}")

if __name__ == "__main__":
    main()
