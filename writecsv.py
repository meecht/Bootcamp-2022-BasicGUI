# writecsv.py
import csv

def writecsv(data):
	# data = ['Time','10', 500]
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)


# d = ['2021-05-11 10:15:10',50,5000]
# writecsv(d)


def readercsv():
	with open('data.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file)
		# print(list(fr))
		data = list(fr)
	return data

def sumdata():
	result = readercsv()
	sumlist_quan = []
	sumlist_total = []
	for d in result:
		sumlist_quan.append(float(d[1]))
		sumlist_total.append(float(d[1]))

		

result = readercsv()	
print(result)

sumlist_quan = []
for d in result:
	sumlist_quan.append(float(d[1])) 
print(sumlist_quan, sum(sumlist_quan))

sumlist_quan2 = [ float(d[1]) for d in result]
print(sumquan)






