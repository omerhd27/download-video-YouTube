from importlib.resources import path
import pytube
print('Download video py python')
url = input('Enter the video url: ')
pytube.YouTube(url).streams.get_highest_resolution().download('Desktop')