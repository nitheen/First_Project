import webbrowser
import time

count = 0

while count < 3:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=CGyEd0aKWZE")
    count = count + 1
else:
    print("Loop exhausted!!")