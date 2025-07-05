a=8
b=2
c=20

def get_larger(x,y):
    if x > y:
        return x
    else:
        return y

def get_larger_of_3(x,y,z):
    return get_larger(get_larger(x,y), z)

def get_smaller(x,y):
    if x < y:
        return x
    else:
        return y
    
def get_smaller_of_3(x,y,z):
    return get_smaller(get_smaller(x,y),z)
    
if a%2 != 0 and b%2 != 0 and c%2 != 0:
    print('all are odd',get_larger_of_3(a,b,c))

if a%2 != 0 and b%2 != 0 and c%2 == 0:
    print('a,b are odd',get_larger(a,b))

if a%2 == 0 and b%2 != 0 and c%2 != 0:
    print('b,c are odd',get_larger(b,c))

if a%2 != 0 and b%2 == 0 and c%2 != 0:
    print('a,c are odd',get_larger(a,c))

if a%2 != 0 and b%2 == 0 and c%2 == 0:
    print('a is odd',a)

if a%2 == 0 and b%2 != 0 and c%2 == 0:
    print('b is odd',b)

if a%2 == 0 and b%2 == 0 and c%2 != 0:
    print('c is odd',c)

if a%2 == 0 and b%2 == 0 and c%2 == 0:
    print('all are not odd',get_smaller_of_3(a,b,c))
