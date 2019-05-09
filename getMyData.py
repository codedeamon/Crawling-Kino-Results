import requests
import re
import urllib.request
import sys
import csv

#http://mg-analysis.gr/membership/kino/klirosis_kino.php

# this function downloads the needed data
def downdata(num_pages):
    p = 1
    draws = re.compile(r'[<td>](\d{6})[</td>]')
    dates = re.compile(r'[<td>](\d{1,2}/\d{1,2}/\d{4})[</td>]')
    # numbers = re.compile(r'>([(\d{1,2}+,?\s?)+]+)</td>')
    numbers = re.compile(r'>(\S[\d{1,2},?\s?]+)</td></tr>')

    while p <= num_pages:
        print(p)
        url = 'http://www.tostoixima.gr/games.aspx?gid=1&pgid=4&pg=' + str(p)
        source_code = requests.get(url)
        plaintext = source_code.text
        plaintext = source_code.text

        for ite in re.findall(draws, plaintext):
            fwdr.write(ite)
            fwdr.write('\n')

        for num in re.findall(numbers, plaintext):
            fwn.write(num)
            fwn.write('\n')

        for ite in re.findall(dates, plaintext):
            fwd.write(ite)
            fwd.write('\n')

        p += 1


ans = input("press 1 to download data, 2 to analyze: ")
if ans == '1':
    fwn = open('numbers.txt', 'a')
    fwd = open('dates.txt', 'a')
    fwdr = open('draws.txt', 'a')

    pages = input("number of pages to download? \n")
    pages = int(pages)
    downdata(pages)

    fwd.close()
    fwdr.close()
    fwn.close()

elif ans == '2':
    
    print("under construction...")





