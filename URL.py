import os
import urllib.request, urllib.parse
import acc

#Notifies Youtube that we are not a bot by replicating a browser header signature
hdr = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}

#Get URL input from user
def getURL():
    URL = input("Input Video URL: ")
    downloadByURL(URL)
    
#Download YouTube video inputting its URL
def downloadByURL(URL):

    #How many good links (working audio and video) in the stream list
    goodLinks = 0

    #Attempts made to download (up to 10 tries)
    attempts = 1

    #Get the links of the video, get its title too
    html = acc.getHTML(URL)
    title = acc.getTitle(html)
    if attempts == 1:
        print("Video Name: " + title)
    stream_list = acc.getStreamList(html)

    #Filter out bad streams, exit at first good link
    for i in (stream_list): 
        try:
            if 'keepalive' not in i:
                stream_list=''.join(i)
                req = urllib.request.Request(stream_list, headers = hdr)
                goodLinks = goodLinks + 1
                response = urllib.request.urlopen(req)
                break
        except Exception as e:
            goodLinks = goodLinks - 1

    #Download if possible, retry if possible, else, video is copyrighted
    if goodLinks != 0:
        print("Downloading video please wait.")
        with open(title + ".mp4",'wb') as f:
            myDir = acc.selectDir()
            f = open(str(myDir) + "/" + str(title), 'wb')
            f.write(response.read())
            f.close()
        print("Download Complete!")
    elif attempts == 10:
        print("Copyrighted Video! Illegal to Download. Please Try a Different Video.")
    elif goodLinks == 0 and attempts != 10:
        attempts = attempts + 1
        downloadByURL(URL)

def downloadByPlaylist():
    URL = input("Input Playlist URL: ")
    videoURLS = acc.getVideoURLS(URL)
    playlistTitle = acc.getHTML(URL)
    print("Downloading playlist: " + acc.getTitle(playlistTitle))
    for i in range(len(videoURLS)):
        end = videoURLS[i].find('&')
        videoURLS[i] = videoURLS[i][0:end]
    videoURLS = list(set(videoURLS))
    for i in range(len(videoURLS)):
        downloadByURL(videoURLS[i])
    
