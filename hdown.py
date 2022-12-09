from pytube import YouTube
import progressbar as progress



def progress(streams, chunk: bytes, bytes_remainig: int):
    csize = yd.filesize
    size = csize - bytes_remainig

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/csize), ' '*(20-int(size*20/csize)),
    float(size/csize*100)), end='')

caminho = 'c:\Ytv'
link = input()
yt = YouTube(link, on_progress_callback=progress)
yd = yt.streams.get_highest_resolution()
yd.download(caminho)







