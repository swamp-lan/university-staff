import Notify

def send(sender, message, style=""):
	Notify.Notify(sender, message, style)
	open("c:\\bin\\video_mes.txt", "a+").write("\nFrom: %s\nMessage:\n\t%s\n===="%(sender, message))