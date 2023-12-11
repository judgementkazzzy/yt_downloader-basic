import yt_dlp
import methodMadness as mad
import time

mad.textCrawlNoWait("PROVIDE ME WITH A LINK HUMAN_\n")
url = input()
mad.textCrawlNoWait("NOW WHERE DO I PUT THIS VIDEO?!ಠ_ಠ\n")
download_directory = input()

ydl_opts = {
    'outtmpl': f'{download_directory}/%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
mad.textCrawlNoWait('DOWNLOADED MALWARE.EXE .... \n')
time.sleep(3)
mad.textCrawlNoWait("JUST KIDDIN....(￣y▽￣)╭ Ohohoho.....")