#1-2
try:
    a = 1/0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
#3
# is the code is legal it always print "finally"
#4
#it will caoght all exeption
#5
# you will not be able to catch different types of errors and handle the code different for each error
#6
# IOError is handles input/output errors
# ZeroDivisionError - is handles with number that divided by zero

#7 -10

my_file = open("words.txt", "a")
my_file.write("Amit")
my_file.close()

my_file = open("words.txt", encoding="utf-8")
for line in my_file.readlines():
    print(line)

#11
from PIL import Image, ImageDraw

def create_png_image(width, height, background_color, output_path):
    # Create a new image with the specified size and background color
    image = Image.new("RGB", (width, height), background_color)

    # Create a drawing object to draw on the image
    draw = ImageDraw.Draw(image)

    # Optional: Draw something on the image (e.g., a red rectangle)
    draw.rectangle([(50, 50), (150, 150)], fill="red")

    # Save the image to the specified file path
    image.save(output_path)

# Example usage
create_png_image(300, 200, "white", "output.png")
