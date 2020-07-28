import csv
def read_electric():
    with open('ctest2.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            print(row)
def write_electric():
    with open('ctest2.csv', mode='w') as File:
        writer = csv.writer(File, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        rows_add_num = int(input('How many row you want to add ---> \t'))
        writer.writerow(['production','month','Year'])
        for i in range(0,rows_add_num):
            writer.writerow([input('production -->\t'),input('month -->\t'),input('year -->\t')])
def append_electric():
        with open('ctest2.csv', mode='a') as File:
            writer = csv.writer(File, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            rows_add_num = int(input('How many row you want to add ---> \t'))
            for i in range(0,rows_add_num):
                writer.writerow([input('production -->\t'),input('month -->\t'),input('year -->\t')])
def read_water():
    with open('waterfile.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            print(row)
def write_water():
    with open('waterfilenew.csv', mode='w') as File:
        writer = csv.writer(File, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        rows_add_num = int(input('How many row you want to add ---> \t'))
        writer.writerow(['production','month','Year'])
        for i in range(0,rows_add_num):
            writer.writerow([input('production -->\t'),input('month -->\t'),input('year -->\t')])
def append_water ():
        with open('waterfile.csv', mode='a') as File:
            writer = csv.writer(File, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            rows_add_num = int(input('How many row you want to add ---> \t'))
            for i in range(0,rows_add_num):
                writer.writerow([input('production -->\t'),input('month -->\t'),input('year -->\t')])



def choice():
    print('1_ Add or show electricity production \n2_ Add or show water production \n3_ The expected production of electricity \n4_ The expected production of water \n ')
    cho = input('Enter the selection number please --->\t')
    check_cho = cho.isdigit()
    if cho == '1' :
        ele_cho = input('1_ New file \n2_ Show data file\n3_ Add data to an existing file\n')
        if ele_cho == '1':
            write_electric()
        elif ele_cho == '2':
            read_electric()
        elif ele_cho == '3':
            append_electric()
        else :
            print('Check your input please\n')
    elif cho == '2' :
        water_cho = input('1_ New file \n2_ Show data file\n3_ Add data to an existing file\n')
        if water_cho == '1':
            write_water()
        elif water_cho == '2':
            read_water()
        elif water_cho == '3':
            append_water()
        else :
            print('Check your input please\n')
    elif cho == '3' :
        print('calculate the expected production of electricity\n')
    elif cho == '4' :
        print('calculate the expected production of water\n')
    elif check_cho == False :
        print('please enter number\n')
    else :
        print('this number not found\n')
def repeat_op():
    while True :
        try :
            QUESTION = input('If you want another operation please enter : [Yes] \nIf you want to stop please enter [No]\n')
            line()
            if QUESTION == 'Yes':
                choice()
                line()
            elif QUESTION == 'No':
                print ('We are happy to serve you')
                line()
                break
            else :
                print ('Check your input please')
                line()
        except:
            continue
def line():
    print('------------------------------------------------------')
def main():
    choice()
    line()
    repeat_op()
main()
