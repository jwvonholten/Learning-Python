
def primer(y):
    if y <= 1:
        print(y, 'not prime')
    else:
        x = y // 2      #for some y > 1
        while x > 1:
            if y % x == 0:
                print(y, ' has factor: ', x)
                break
            x -= 1
        else:
            print(y, ' is prime')

        
