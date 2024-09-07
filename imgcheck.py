import os
from PIL import Image
def get_image_details(folder_path):
    image_details = []

    # List all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    details = {
                        'File Name': file_name,
                        'Format': img.format,
                        'Mode': img.mode,
                        'Size': img.size  # (width, height)
                    }
                    image_details.append(details)
            except IOError:
                print(f"Cannot open file: {file_path}")
    
    return image_details

folder_path = "PATH OF THE FOLDER"
details = get_image_details(folder_path)
for detail in details:
    print(detail)