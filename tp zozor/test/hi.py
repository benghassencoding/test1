from pytube import YouTube
folder = 'C:\Users\ASUS\Desktop\photo'
url="https://youtu.be/ovEJc47qJ5Y"
video = YouTube(url)
stream = video.strams.get_heighest_resolutions()
stream.download(folder)