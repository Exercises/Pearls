import random,time,guppy
from bitarray import bitarray
from guppy import hpy
n = 1000000
#@profile
def bitsort(list):
    #hp = hpy()
    #print "heap before : ", hp.heap()
    t = time.time()
    array = bitarray(n)
    t1 = time.time()
    print "init time : ", str(t1- t), " seconds"
    resultlist = []
    for i in range(0,n):
        array[i] = False
    t2 = time.time()
    print "all 0 time : ", str(t2 - t1), " seconds"
    for item in list:
        array[item] = True
    t3 = time.time()
    print "sort time", str(t3 - t2), " seconds"
    for i in range(0, n):
        if array[i] == True:
           resultlist.append(i)
    t4 = time.time()
    print "append-time", str(t4- t3), " seconds"
    #print "heap after: ", hp.heap()
#@profile
def qsort(array):
    def smaller(num, array):
        return qsort([x for x in array if x < num])

    def bigger(num, array):
        return qsort([x for x in array if x >= num])

    if len(array) <  2:
        return array
    else:
        return smaller(array[0], array[1:]) + [array[0]] +  bigger(array[0], array[1:])

#@profile
def systemsort(list):
    list.sort()

def main():
    list = random.sample(range(0,n),n-1)
    t_start = time.time()
    #bitsort(list)
    #systemsort(list)
    qsort(list)
    t_end = time.time()
    print "bitsort spent : ",str(t_end - t_start)," secondes"
main()
