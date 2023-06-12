from pytube import YouTube
from sys import argv

# To run this program in terminal
# type:
# python YTdownloader.py "youTubeVideoLink"
# Ex:
# python YTdownloader.py "https://www.youtube.com/watch?v=vEQ8CXFWLZU&ab_channel=InternetMadeCoder"

# link=argv[1]
link = input("Enter the link of the video from YT: ")
yt=YouTube(link)
yd = yt.streams.get_highest_resolution()
yd.download("C:/Users/User/Videos/YT dowloader")
print("You've downloaded the video successfully!")
print("check directory: C:/Users/User/Videos/YT dowloader")