import os
from PIL import Image
import io

def compress_and_convert_to_webp(input_folder, output_folder, max_size_kb=30):
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input directory
    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    # Process each file
    for file in files:
        file_path = os.path.join(input_folder, file)

        # Open the image using Pillow
        try:
            image = Image.open(file_path)

            # Convert and compress the image to WebP format with a quality setting
            buffer = io.BytesIO()
            quality = 90
            image.save(buffer, format="WEBP", quality=quality)
            buffer.seek(0)

            # Check the size of the image and adjust quality if it exceeds the specified limit
            while len(buffer.getvalue()) > max_size_kb * 1024 and quality > 10:
                quality -= 5
                buffer = io.BytesIO()
                image.save(buffer, format="WEBP", quality=quality)
                buffer.seek(0)

            # Save the compressed image to the output directory
            output_path = os.path.join(output_folder, os.path.splitext(file)[0] + "_compressed.webp")
            with open(output_path, "wb") as f:
                f.write(buffer.getvalue())

            print(f"Compressed {file} to {quality} quality and saved to {output_path}")

        except Exception as e:
            print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    input_directory = input("Enter the path to the input directory: ")
    output_directory = input("Enter the path to the output directory: ")
    max_kb = int(input("Enter the maximum size in KB (default is 30KB): ") or "30")

    compress_and_convert_to_webp(input_directory, output_directory, max_kb)
