"""start / stop led in raspbery PI"""
import time
import os

def writeFile(filename, content):
	with open(filename, "w") as f:
		f.write(content);

print "GPIO 27 started"
if not os.path.isfile("/sys/class/gpio/gpio27/direction"):
	writeFile("/sys/class/gpio/export", "27")

time.sleep(0.1)
writeFile("/sys/class/gpio/gpio27/direction", "out")

writeFile("/sys/class/gpio/gpio27/value", "1")
time.sleep(2)
writeFile("/sys/class/gpio/gpio27/value", "0")