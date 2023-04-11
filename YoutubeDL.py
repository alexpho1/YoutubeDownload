from pytube import YouTube

link = input("Paste the link to youtube video here: ")
yt = YouTube(link)

print('Title: ', yt.title)
print('Views: ', yt.views)

dl = yt.streams.get_highest_resolution()
dl.download('/Users/alex.phommachanh/Downloads')
