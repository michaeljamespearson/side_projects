import pyperclip
import subprocess
import sys

def sqlify_sheets():
	val = pyperclip.paste()
	mid = val.splitlines()
	out = ""
	count = 0
	while count < len(mid):	
		line = mid[count]
		line.replace('\n','')
		line = "'" + line + "'"
		if(count != len(mid) - 1):
			line = line + ",\n"
		out = out + line
		count = count + 1

	print(out)
	pyperclip.copy(out)

def set_f1():
	pyperclip.copy("set f1_instance '/f1/display-ads/prod';")

if (int(sys.argv[1]) == 0):
	sqlify_sheets()
	print("SQLify ran")

elif(int(sys.argv[1]) == 1):
	set_f1()
	print("F1 ran")

