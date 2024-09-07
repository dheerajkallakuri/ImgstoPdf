# ImgstoPdf

`ImgstoPdf` is a Python application that provides a simple graphical interface for searching and downloading images from an open-source photo database using an API. After fetching the images based on a user-defined keyword, the application converts the images into a single PDF file. The GUI also includes a loading bar to display the progress of the image download.

<img width="425" alt="Screenshot 2024-09-06 at 9 35 05 PM" src="https://github.com/user-attachments/assets/c377ec42-da50-4220-8895-e729c3a7ff12">


## Project Overview

This repository contains the following components:

1. **`app.py`**: The main graphical user interface (GUI) of the application, created using PyQt5. Users can input the number of images and the keyword for which they want to fetch photos. Upon clicking "Export to PDF," an API call is made to Unsplash to download the specified number of images. Once the images are successfully downloaded, they are converted into a PDF. The GUI also features a loading bar that updates based on the progress of the image download.

<img width="434" alt="Screenshot 2024-09-06 at 9 35 19 PM" src="https://github.com/user-attachments/assets/33f74e0c-49bc-4f5f-b01c-de9d1b22dee0">


3. **`image_fetcher.py`**: This Python script handles API calls to Unsplash to fetch images based on the provided keyword. It saves the downloaded images into a specified folder.

4. **`pdf_converter.py`**: This script takes the images from the specified folder and combines them into a single PDF file.

5. **`image_checker.py`**: This utility script checks the types of images downloaded via API calls. It is useful for debugging and verifying the content of the downloaded images.

## Results
<table>
  <tr>
    <td><img width="442" alt="Screenshot 2024-09-06 at 9 35 32 PM" src="https://github.com/user-attachments/assets/912ab970-cba5-4432-addf-396912fb0c5d"></td>
    <td><img width="574" alt="Screenshot 2024-09-06 at 9 36 11 PM" src="https://github.com/user-attachments/assets/c2b75799-1ace-4e20-b7ea-396f37951d58">
</td>
  </tr>
</table>

## Getting Started

### Prerequisites

Make sure you have Python installed. You can install all required libraries using the `requirements.txt` file provided in the repository.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dheerajkallakuri/ImgstoPdf.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ImgstoPdf
   ```

3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To run the application, execute the `app.py` file:

```bash
python app.py
```

### How It Works

1. **GUI Interaction**:
   - Open `app.py` to launch the GUI.
   - Enter the number of images and the keyword for the image search.
   - Click "Export to PDF" to initiate the process.

2. **Image Fetching**:
   - `app.py` calls `image_fetcher.py` to download images from Unsplash based on the provided keyword.
   - Images are saved in a folder named with the current timestamp.

3. **PDF Conversion**:
   - After images are downloaded, `app.py` calls `pdf_converter.py` to convert these images into a PDF file.

4. **Progress Tracking**:
   - The loading bar in the GUI updates as images are downloaded.

5. **Debugging**:
   - Use `image_checker.py` to verify the types of images downloaded and ensure they meet your requirements.

## File Details

- **`app.py`**: Main application GUI.
- **`image_fetcher.py`**: Handles API calls and image saving.
- **`pdf_converter.py`**: Converts images to PDF.
- **`image_checker.py`**: Checks and debugs image types.
