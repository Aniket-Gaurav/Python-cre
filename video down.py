from pytube import YouTube
link = input("Enter url of video: ")
video = YouTube(link)
stream = video.streams.get_lowest_resolution()
stream.download()