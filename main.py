def filter_custom(l, f):
    '''Filter a list using a function

    Return a new list that contains all the elements e of l
    for which f(e) is True

    :param l: a list
    :param f: a function that takes one argument and returns either
        True or False
    '''
    filtered_list = [e for e in l if f(e)]
    return filtered_list

def map_custom(l, f):
    '''Map a list using a function

    Return a new list that applies f(e) for every element e in l

    :param l: a list
    :param f: a function that takes one argument and returns a value'''

#    new_list = []
#    for e in l:
#        new_list.append(f(e))
    new_list = [f(e) for e in l]
    return new_list

def reduce_custom(l, f, starting_value):
    '''Reduce a list using a reducer function and a starting value

    Return a single value that applies f(v, e) for every
    e in l from left to right.  The initial value for v
    should be starting_value, and subsequent values should be the previously
    calculated value from f(v, e)

    :param l: a list
    :param f: a function that takes one argument and returns a value
    :param starting_value: the beginning value for the reducer function
        computation
    '''

    reduced_list = [e for e in l if f(v, e)]
    return reduced_list

if __name__ == '__main__':
    l = [7,8,9]
    f = lambda x: x * 10
    print(map_custom(l,f))

    def f(e):
        if e + 1 > 8:
            return True
        else:
            return False
    print(filter_custom(l, f))



