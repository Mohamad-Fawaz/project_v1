import csv
def write_electric():
    with open('ctest2.csv', mode='w') as ctest2:
        writer = csv.writer(ctest2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['production','month','Year'])
        writer.writerow([input('production'),input('month'),input('year')])
        writer.writerow([input('production'),input('month'),input('year')])
write_electric()

def read2_electric():
    with open('ctest2.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            print(row)
read2_electric()

def read2_electric():
    with open('ctest.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            print(row)
read2_electric()
