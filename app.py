import sys
import shutil
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, 
                             QLineEdit, QProgressBar, QFileDialog, QSpinBox, QMessageBox)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from datetime import datetime
from image_fetcher import ImageDownloaderThread
from pdf_converter import convert_images_to_pdf

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Window settings
        self.setWindowTitle("Images to pdf Convertor")
        self.setGeometry(300, 300, 400, 200)
        
        # Layout setup
        layout = QVBoxLayout()
        
        # Widgets
        self.keyword_label = QLabel("Enter Keyword:")
        self.keyword_input = QLineEdit(self)
        
        self.num_images_label = QLabel("Enter Number of Images:")
        self.num_images_input = QSpinBox(self)
        self.num_images_input.setRange(1, 50)
        
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        
        self.download_button = QPushButton("Export to PDF", self)
        self.download_button.clicked.connect(self.download_images)
        
        # Adding widgets to layout
        layout.addWidget(self.keyword_label)
        layout.addWidget(self.keyword_input)
        layout.addWidget(self.num_images_label)
        layout.addWidget(self.num_images_input)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.download_button)
        
        # Set layout to the window
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def download_images(self):
        # Get user input
        keyword = self.keyword_input.text()
        num_images = self.num_images_input.value()
        
        # Create a folder with timestamp as its name
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        folder_name = os.path.join(os.getcwd(), timestamp)
        os.makedirs(folder_name, exist_ok=True)
        
        # Start downloading images in a separate thread
        self.thread = ImageDownloaderThread(keyword, num_images, folder_name)
        self.thread.progress.connect(self.update_progress_bar)
        self.thread.finished.connect(lambda: self.convert_to_pdf(folder_name, keyword))
        self.progress_bar.setMaximum(num_images)
        self.thread.start()

    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)
    
    def convert_to_pdf(self, folder_name, keyword):
        # Convert images to PDF
        image_files = [f for f in os.listdir(folder_name) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        if not image_files:
            QMessageBox.warning(self, "No Images Downloaded", "No images were downloaded for the keyword: " + keyword)
            try:
                shutil.rmtree(folder_name)
                print(f"{folder_name} folder deleted: ")
            except FileNotFoundError:
                print(f"Folder not found: {folder_name}")
            except OSError:
                print(f"Folder is not empty or cannot be removed: {folder_name}")
            return

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        pdf_filename = keyword + "_" + timestamp + ".pdf"
        if pdf_filename:
            convert_images_to_pdf(folder_name, pdf_filename)
            print(f"PDF saved as: {pdf_filename}")
            try:
                shutil.rmtree(folder_name)
                print(f"{folder_name} folder deleted: ")
            except FileNotFoundError:
                print(f"Folder not found: {folder_name}")
            except OSError:
                print(f"Folder is not empty or cannot be removed: {folder_name}")
            if os.path.exists(pdf_filename):
                self.show_message("Success", f"pdf of {keyword} images are ready!")
            else:
                self.show_message(f"No {keyword} images are found.")

        else:
            print("PDF saving canceled.")
    
    def show_message(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
