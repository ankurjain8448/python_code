t = int(raw_input())
while t:
    t-=1
    n = int(raw_input())
    a = raw_input()
    b = raw_input()
    w = [ int(i) for i in raw_input().split() ]
    index = 0
    for i in xrange(n):
        if a[i] == b[i] :
            index+=1
    arr = w[:index+1]
    print max(arr)