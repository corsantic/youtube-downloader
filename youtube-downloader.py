from pytube import YouTube


youtubeUrl = input("Enter youtube url for download: ")


yt = YouTube(youtubeUrl)

print(yt.title)

videoToDownload = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first();

print(videoToDownload)
print("downloading...")

videoToDownload.download()


print("done...")