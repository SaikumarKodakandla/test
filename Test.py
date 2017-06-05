# -*- coding: utf-8 -*-
"""
Created on Mon May 29 19:32:51 2017

@author: Srinivas.Mullangi
"""

###Web scrapping LIB's
from lxml import html
import requests

page = requests.get('https://www.tripadvisor.in/Hotel_Review-g186487-d193947-Reviews-Macdonald_Hotels-Aberdeen_Aberdeenshire_Scotland.html')

tree = html.fromstring(page.content)

#This will create a list of buyers:
datec = tree.xpath('//span[@class="ratingDate relativeDate"]/text()')
nameuser = tree.xpath('//span[@class="expand_inline scrname"]/text()')
cmntuser = tree.xpath('//p[@class="partial_entry"]/text()')
quoteuser = tree.xpath('//span[@class="noQuotes"]/text()')


print ('datec: ', datec)
print ('nameuser: ', nameuser)
print ('cmntuser: ', cmntuser)
print ('quoteuser: ', quoteuser)

print i for i in datec
##Not Getting data for below
rateuser = [i for i in tree.xpath('//span[@class="ui_bubble_rating"]/text()')]
print ('rateuser: ', rateuser)

##Not Getting data for below
comprev = tree.xpath('//p[@property="reviewBody"]/text()')
print ('comprev: ', comprev)

