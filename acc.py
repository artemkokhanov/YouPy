import urllib.request, urllib.parse
import os
import re

#Get HTML file from URL
def getHTML(URL):
    hdr = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    response = urllib.request.Request(URL, headers = hdr)
    response = urllib.request.urlopen(response)      #store the response
    response = response.read()                  #Read the HTML
    return response.decode('unicode_escape')    #Decode escape chars
    

#Get Title of YouTube video from HTML content
def getTitle(html):
    title = html.split('</title>', 1)[0].split('<title>')[1]
    title = title.replace("&#39;","'")
    title = title.replace("&quot;",'"')
    title = title[:-10]
    return title

#Same functionality as before but now for a list of videos
def getTitles(URLList):
    titles = []
    count = 0
    for i in range(len(URLList)):
        titles.append(getTitle(getHTML(URLList[i])))
        selection = '[' + str(count) + ']: ' + titles[i]
        count = count + 1
        print(selection)
    return titles

#Returns the links of the video
def getStreamList(html):
    stream_list = []
    for video_stream in parseHTML(html)['url']:
        if "googlevideo" == video_stream.split('/')[2].split('.')[1]:
            stream_list.append(video_stream)
    return stream_list

#Parses HTML
def parseHTML(html):
    return urllib.parse.parse_qs(html)

#Specify directory to download video to
def selectDir():
    myDir = input("Enter desired save location: ")
    while not os.path.exists(myDir):
        print("Invalid Path! Try again.")
        myDir = input("Enter desired save location: ")
    return myDir

def getVideoURLS(htmlURL):
    html = getHTML(htmlURL)
    index = [i.start() for i in re.finditer('/watch?', html)]
    URLFinal = []
    for i in range(len(index)):
        endIndex = html.find('"', index[i])
        if "/watch?v=" in html[index[i]:endIndex] and (len(html[index[i]:endIndex]) == 20 or "list=" in html[index[i]:endIndex]):
            URLFinal.append("https://www.youtube.com" + html[index[i]:endIndex])
    URLFinal = list(set(URLFinal))
    selection = getTitles(URLFinal)
    return URLFinal
