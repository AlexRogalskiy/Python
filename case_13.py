import time
import os
import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy
from datetime import datetime
from datetime import date
from datetime import timedelta
import random
import shelve

historyFile = "./record"
plotFile = "./history.png"

def measureNewDatapoint():
	return random.randint(0, 1000)


def main():
	db = shelve.open(historyFile)
	db['language'] = ['ru', 'rn', 'ua']
	db['colors'] = ['red', 'blue', 'green']
	db.close()

	history = shelve.open(historyFile)
	if "x" not in history.keys():
		history["x"] = [];
		history["y"] = []

	for x in range(1, 100):
		history["x"] += [datetime.now()]
		history["y"] += [measureNewDatapoint()]

	now = datetime.now()
	#sampleCount = int(24 * 60 * 60 * 1000 / 5)
	history['x'] = history["x"][-50:]
	history['y'] = history["y"][-50:]

	plot = plt.figure()
	plt.title("Test plot")
	plt.ylabel("Random data")
	plt.xlabel("Time")
	plt.setp(plt.gca().get_xticklabels(), rotation=35)
	plt.plot(history["x"], history["y"], color="#4884ff")
	plt.savefig(plotFile)
	history.close()

if __name__ == "__main__":
	main()