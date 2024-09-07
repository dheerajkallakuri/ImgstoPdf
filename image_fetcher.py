import os
import requests
import shutil
from PyQt5.QtCore import QThread, pyqtSignal

UNSPLASH_ACCESS_KEY = "ACCESS KEY"

class ImageDownloaderThread(QThread):
    progress = pyqtSignal(int)
    
    def __init__(self, keyword, num_images, folder_name):
        super().__init__()
        self.keyword = keyword
        self.num_images = num_images
        self.folder_name = folder_name

    def run(self):
        image_urls = self.get_image_urls(self.keyword, self.num_images)
        for i, url in enumerate(image_urls):
            self.download_image(url, i)
            self.progress.emit(i + 1)
    
    def get_image_urls(self, keyword, num_images):
        image_urls = []
        # Unsplash API URL
        api_url = f"https://api.unsplash.com/search/photos"
        headers = {
            'Authorization': f'Client-ID {UNSPLASH_ACCESS_KEY}'
        }
        params = {
            'query': keyword,
            'per_page': num_images,
            'page': 1
        }
        
        try:
            response = requests.get(api_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            for result in data.get('results', []):
                image_urls.append(result['urls']['regular'])
        except Exception as e:
            print(f"Error fetching image URLs: {e}")
        
        return image_urls

    def download_image(self, url, index):
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                img_name = os.path.join(self.folder_name, f'img{index+1}.JPEG')
                with open(img_name, 'wb') as file:
                    shutil.copyfileobj(response.raw, file)
        except Exception as e:
            print(f"Error downloading {url}: {e}")
