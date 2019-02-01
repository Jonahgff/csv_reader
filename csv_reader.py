import csv
import pandas as pd

with open("my_csv.csv","r") as read_file:
	my_reader = csv.reader(read_file)
	read = []
	for row in my_reader:
		if len(row) != 0:
			read = read + [row]

read_file.close()
data_file = pd.DataFrame(read)
print data_file