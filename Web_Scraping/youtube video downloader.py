import pytube

yt=pytube.YouTube("https://youtu.be/0MW0mDZysxc")
print(yt.title)
print(yt.views)
print(yt.streams.first())
print(yt.streams.last())
print(yt.streams.filter(progressive=True).all())
print(yt.streams.filter(adaptive=True).all())

