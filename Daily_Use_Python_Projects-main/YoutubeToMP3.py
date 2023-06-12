from pytube import YouTube
import os

# url input from user
yt = YouTube(input("Enter the url of the video you to download: \n>>"))

# extract only audio
video = yt.streams.filter(only_audio=True).first()

# replace destination with the path you want to save the downloaded audio file
destination = "C:/Users/User/Music"

# download the file
out_file = video.download(output_path=destination)

# saving the file
base, ext = os.path.splitext(out_file)
new_file = base + ".mp3"
os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded to your music folder!")