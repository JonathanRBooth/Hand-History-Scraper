import requests
from bs4 import BeautifulSoup
import time
import os
import sys
import threading

#Multi-threaded Hand History Scraper V2.2

#Contact me if you encounter significant connection errors or large numbers of attribute errors being logged.

#Try to keep usage responsible as this script will pull data as quickly as possible and may cause the data host to be unhappy if overused.

#If the total time running is greater than 0.2 seconds per hand either the connection is poor or you have been throttled by the site and should cease use immediately.  

timestart = time.time()

def scrape(start,end,fileletter):
    filenumber = 1
    for i in range(start,end):

        try:

            url = "https://anyrandompokernetwork.com/flashclient/gamehistory.php?gnr=%s&key=&nick=&note=" %(i)

            page = requests.get(url).content

            soup = BeautifulSoup(page, "lxml")

       
            textblock = soup.find("div",{"id":"div_urlcodes"})

            textblock2 = textblock.find("textarea",{"id":"txt_handhistory"})
            textblock2 = str(textblock2)
            textblock2 = textblock2.replace("""<textarea id="txt_handhistory" name="txt_handhistory" style="width:233px;height:50px;">""","")
            textblock2 = textblock2.replace("&lt;br&gt;","<br>")
            textblock2 = textblock2.replace("</textarea>","")

        except AttributeError:
            print "Hand", i, "not processed due to error"
            File = open("Error Log.txt", 'a')
            File.write("Hand %s not processed due to error"%(str(i)))
            File.write("\n")
            File.close()
            pass

        except "ConnectionError":
            print "ConnectionError"
            time.sleep(30)
            pass

        File = open("HH - %s%s.txt"%(fileletter,filenumber), 'a')
        if os.path.getsize("C:\Users\Desktop\Python\Betuniq Soup Scraper\HH 1\HH - %s%s.txt" %(fileletter,filenumber)) > 10000000:
            filenumber = filenumber + 1
            File = open("HH - %s%s.txt" %(fileletter,filenumber), 'a')
            File.close()

        File = open("HH - %s%s.txt" %(fileletter,filenumber), 'a')
        File.write(textblock2)
        File.write("\n\n")
        File.close()

        print "Hand Number", i, "Processed"
        
    timeend = time.time()

    print "Total Time Running =", timeend - timestart, "Seconds."

#Enter start/end page numbers for each thread (Leave the 3rd arg alone).
    
#Feel free to add more threads if you feel you need to quickly expand the scope of data scraped.

#I would suggest each thread having a range of no more than 1000.  

t1 = threading.Thread(target=scrape, args=(1,1001,"A")) 
t2 = threading.Thread(target=scrape, args=(1001,2001,"B"))
t3 = threading.Thread(target=scrape, args=(2001,3001,"C"))
t4 = threading.Thread(target=scrape, args=(3001,4001,"D"))
t5 = threading.Thread(target=scrape, args=(4001,5001,"E"))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

raw_input()
