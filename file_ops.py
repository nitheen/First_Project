import urllib.request

def open_file():
    quotes = open("C:/Users/Nitheen/Desktop/Udacity/sample.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check_prof(contents)

def check_prof(text):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text)
    response = connection.read()
    print(response)
    connection.close()

open_file()