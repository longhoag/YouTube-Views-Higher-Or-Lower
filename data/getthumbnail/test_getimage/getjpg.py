import urllib.request

def download_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

url = 'https://img.youtube.com/vi/nIl_gX9W5qQ/maxresdefault.jpg'
file_name = 'max2'

download_jpg(url, '/Users/Leo/Library/Mobile Documents/com~apple~CloudDocs/Developer 🔨/YouTube-View-Rank', file_name)