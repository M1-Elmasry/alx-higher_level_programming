#!/usr/bin/python3

def weight_average(my_list=[]):
    if list is None:
        return None
    if len(my_list) > 0:
        return sum([(i[0]*i[1]) for i in my_list])/sum([i[1]for i in my_list])
    else:
        return 0
