import random
def find_big_small_o(number_list):
    if len(number_list) < 1:
        return
    mincount = 0
    max = number_list[0]
    min = number_list[0]
    print "first: ", max
    for x in number_list:
        #print "x : ", x , "max : " ,  max , "  min: " , min
        if x > max:
            max = x
            print "bigger", x
        elif lower(x ,min):
            min = x

def lower(a , b):
    global if_count
    if_count = if_count+ 1
    return a < b

def main():
    #number_list =  [random.randint(0, 1000) for i in range(0, 1000)]
    number_list =  random.sample(range(0,10),10)
    #number_list = range(0,1000)
    #number_list = range(1000, 0, -1)
    global if_count
    if_count = 0
    find_big_small_o(number_list)
    print "if_count: ", if_count

main()
