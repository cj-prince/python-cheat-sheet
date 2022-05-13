from pytube import YouTube

url = 'https://www.youtube.com/watch?v=8124kv-632k'
my_video = YouTube(url)

print(my_video.title)

print(my_video.thumbnail_url)

for stream in my_video.streams:
    print(stream)

my_video = my_video.streams.get_highest_resolution()

my_video.download()
