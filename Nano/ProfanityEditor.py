# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:18:50 2017

@author: fang2
"""

import urllib

def read():
    file = open(r"C:\Users\fang2\Desktop\Udacity\Nano\movie_quotes.txt")
    content = file.read();
    file.close();
    res = check_content("pengcheng")
    print(res)
#    if(res is True):
#        print("No problem everything is good")
#    elif(res is False):
#        print("I need to call Police")
#    else:
#        print("I can't make sure this text is good.")
    
    
    
def check_content(content):
    query = urllib.request.quote(content)
    connection = urllib.request.urlopen("https://www.google.com/?q="+query)
    output = connection.read()
    connection.close()
    return output

    
read()
    
    
