import random,time

def qsort(array):
    def smaller(num, array):
        return qsort([x for x in array if x < num])

    def bigger(num, array):
        return qsort([x for x in array if x >= num])

    if len(array) <  2:
        return array
    else:
        return smaller(array[0], array[1:]) + [array[0]] +  bigger(array[0], array[1:])
def main():
    t_start = time.time()
    a = random.sample(range(0, 9999999), 9999999)
    t_end = time.time()
    print "spent " ,  (t_end - t_start), " seconds to sort "
    t_start = time.time()
    a.sort()
    t_end = time.time()
    print "spent " ,  (t_end - t_start), " seconds to sort "
    #print "before: ", a, "\nafter: ", qsort(a)
main()
