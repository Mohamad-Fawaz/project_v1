class electric():
    pass
class water():
    pass
def electric_fun(name):
    elect = electric() # we creat like an object to use it with the parameters function
    # for example :
    # elect.name = name
def water_fun():
    water_ob = water()
def choice():
    print('1_ Show electricity production \n2_ Show water production \n3_ The expected production of electricity \n4_ The expected production of water \n ')
    cho = input('Enter the selection number please >\n')
    check_cho = cho.isdigit()
    if cho == '1' :
        print('Exeal File data for electricity production')
    elif cho == '2' :
        print('Exeal File data for Water production')
    elif cho == '3' :
        print('calculate the expected production of electricity')
    elif cho == '4' :
        print('calculate the expected production of water')
    elif check_cho == False :
        print('please enter number')
    else :
        print('this number not found')
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
