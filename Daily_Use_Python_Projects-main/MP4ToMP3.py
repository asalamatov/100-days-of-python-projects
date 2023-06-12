# import moviepy.editor to convert
from moviepy import editor

# import tkinter to open PC directory
from tkinter.filedialog import *

# chose video file from your PC
video = askopenfilename()

# start by getting video into editor
video = editor.VideoFileClip(video)

# change video to audio
audio = video.audio

# name the audio
audio.write_audiofile("sample.mp3")

# result of success
print("completed!")

