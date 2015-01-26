import random,time
def sliceRotate(str, rotate):
    return str[rotate:] + str[:rotate]

def multirotate(list, rotate):
    for i in range(0, rotate):
        first = list[0]
        for j in range(0, len(list) -1):
            list[j] = list[j+1]
        list[-1] = first
    return list

def main():
    n = 9999
    list = [random.choice("abcdefg") for x in range(0,n)]
    r = n/2
    t1 = time.time()
    #print "before: ", list
    list = sliceRotate(list,r)
    #list = multirotate(list, r)
    #print "after: ", list
    t2= time.time()
    print "rotate time : ",str(t2 - t1), " seconds"
main()
