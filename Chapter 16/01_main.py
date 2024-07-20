import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

# Get the YouTube video URL from the user
url = input("Enter the YouTube video URL: ")

# Create a YouTube object using the URL
yt = YouTube(url)

# Choose the desired audio format (optional)
# Uncomment and modify the following line to select a specific format
# preferred_format = yt.streams.filter(only_audio=True).first()

# If no format is chosen, get the highest bitrate audio stream
preferred_format = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

# Download the audio stream
audio_filename = preferred_format.download()

# Extract the audio from the downloaded video
clip = VideoFileClip(audio_filename)
audio_clip = clip.audio

# Get the filename without extension
filename, _ = os.path.splitext(audio_filename)

# Save the extracted audio as an MP3 file (modify extension if needed)
audio_clip.write_audiofile(f"{filename}.mp3")

# Optionally, delete the downloaded video file
os.remove(audio_filename)

print("Audio extraction complete!")


#TODO: 02:51:55
