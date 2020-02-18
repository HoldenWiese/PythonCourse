
def getInfo():
    var1 = input('Please provide the first numeric value: ')
    var2 = input('Please provide the second numeric value: ')
    return var1, var2

def compute():
    go = True
    while go:
        var1, var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False
        except ValueError as e:
            print('{}: \n\nYou didn\'t provide a numeric value. Try again please.'.format(e))
        except:
            print("\n\nOops, you provided invalid input, program will now close!")
    print('{} + {} = {}'.format(var1,var2,var3))
        

if __name__ == '__main__':
    compute()
