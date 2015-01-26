import sys,re,time

def addword(worddict):
    def add(word):
        if len(word) == 0:
            return;
        if worddict.has_key(word):
            worddict[word] = worddict[word] + 1
        else:
            worddict[word] = 1
    return add

def main():
    if len(sys.argv) <  2:
        print "at least 2 arguments"
        return
    filename = sys.argv[1]
    time_before = time.time()
    f = open(filename, "r")
    time_start = time.time()
    print "spent time : " + str(time_start - time_before)
    i = 0
    wordset = set()
    worddict = dict()
    lines = f.readlines()
    for line in lines:
        map(addword(worddict), re.split("[^a-zA-Z]", line))
    time_map_end = time.time()
    print "map time : " + str(time_map_end - time_start)
    worddict = sorted(worddict.iteritems(), key=lambda d:d[1], reverse = True)
    time_end = time.time()
    print "sort time : " + str(time_end - time_map_end)
    print worddict[:20]
print "start", __name__
if __name__ == "__main__":
    main()
