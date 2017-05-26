import csv
import datetime
from collections import OrderedDict
import os
from smtp import send


def write(input):
	w = open('transactions.csv', 'ab')
	w = csv.DictWriter(w, fieldnames=input.keys(),delimiter=',')
	w.writerow(input)
	send(input)
	return "Transaction Complete"



while True:
	try:
		input = OrderedDict()
		input["name"] = False
		input["model"] = False
		input["serial number"] = False
		input["in-out"] = False
		now = datetime.datetime.now()
		for item in input.keys():
			input[item] = raw_input("Scan %s: "%item).upper()
			if input[item] == "RESET":
				raise NameError('User reset')
		input["time"] = "%d:%d" % (now.hour, now.minute)
		input["day"] = now.day
		input["month"] = now.month
		input["year"] = now.year
		fins = raw_input("Please confirm the information is correct? Y/N:")
		if fins != "TRUE":
			raise NameError('User reset')
		else:
			write(input)
		
	except:
		print "Transaction has been reset"
		os.system('clear')
		continue
