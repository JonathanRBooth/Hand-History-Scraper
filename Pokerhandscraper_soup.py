#Poker hand history scraper

import requests
from bs4 import BeautifulSoup
import time
import os
import sys

#Program run timer start
timestart = time.time() 

#File number x to first write to: "HH - x.txt"
filenumber = 1 

for i in range(1,5000000):

    #Input url of HH records with %s in place of hand number
    url = "https://randompokerwebsite/flashclient/gamehistory.php?handnumber=%s" %(i)

    page = requests.get(url).content

    soup = BeautifulSoup(page)

    try:
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

    #If saved file is > than ~10MB, create file n + 1 and write to that instead
    if os.path.getsize("C:\Users\Desktop\HH - %s.txt" %(filenumber)) > 10000000:
        filenumber = filenumber + 1

    File = open("HH - %s.txt"%(filenumber), 'a')
    File.write(textblock2)
    File.write("\n\n")
    File.close()

    print "Hand Number", i, "Processed"
    
timeend = time.time()

print "Total Time Running =", timeend - timestart, "Seconds."

raw_input()
