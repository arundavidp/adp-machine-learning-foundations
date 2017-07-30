import webbrowser
import time

a = 3
for a in range(3):
	time.sleep(2)
	webbrowser.open("https://www.youtube.com/watch?v=H4f2A4LlgX8")
	print "hello again" + str(a)