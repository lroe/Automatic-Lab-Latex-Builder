from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def code_to_images(input_directory, output_directory):
    # Iterate through all files in the input directory and its subdirectories
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            # Check if the file is a text file
            if file.endswith(".txt"):
                # Create the file path
                file_path = os.path.join(root, file)

                # Generate output file path
                output_prefix = os.path.splitext(file)[0]
                output_path = os.path.join(output_directory, f"{output_prefix}_part")

                # Process the code and create images
                process_code(file_path, output_path)

def process_code(code_file, output_prefix):
    # Open the code file and read its contents
    with open(code_file, 'r') as file:
        code = file.read()

    # Set fixed image width, padding, max height, and light background color
    image_width = 800
    max_image_height = 300
    font_size = 24  # Adjust font size to your preference
    line_height = 30  # Adjust line height for better spacing
    padding_left = 10
    padding_right = 10
    padding_top = 10
    padding_bottom = 10
    background_color = "#f0f0f0"  # Replace with your desired light background color code
    text_color = "black"

    # Use Arial font
    font_path = "arial.ttf"  # Replace with the path to your Arial font file
    font = ImageFont.truetype(font_path, font_size)

    # Split code into lines and wrap long lines
    lines = []
    for line in code.split('\n'):
        wrapped_lines = textwrap.wrap(line, width=int((image_width - padding_left - padding_right) / font_size*1.85))
        lines.extend(wrapped_lines)

    # Create images with a maximum height of max_image_height
    image_count = 1
    current_lines = []
    for wrapped_line in lines:
        # Check if adding the current line exceeds the max height
        current_height = len(current_lines) * line_height + padding_top + padding_bottom
        if current_height + line_height > max_image_height and current_lines:
            create_image(current_lines, output_prefix, image_count, image_width, max_image_height, padding_left, padding_top, padding_bottom, font, text_color, line_height, background_color)
            image_count += 1
            current_lines = [wrapped_line]
        else:
            current_lines.append(wrapped_line)

    # Create the last image if there are remaining lines
    if current_lines:
        create_image(current_lines, output_prefix, image_count, image_width, max_image_height, padding_left, padding_top, padding_bottom, font, text_color, line_height, background_color)

def create_image(lines, output_prefix, image_count, image_width, max_image_height, padding_left, padding_top, padding_bottom, font, text_color, line_height, background_color):
    # Calculate the image height based on the lines
    image_height = len(lines) * line_height + padding_top + padding_bottom

    # Create a new image with the specified width and height, and a light background color
    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    # Draw each line on the image
    y_position = padding_top
    for wrapped_line in lines:
        draw.text((padding_left, y_position), wrapped_line, font=font, fill=text_color)
        y_position += line_height

    # Save the image
    image.save(f"{output_prefix}_{image_count}.png")

# Example usage
code_to_images(".", "output_images")

