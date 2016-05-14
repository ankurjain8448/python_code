a = [ i for i  in raw_input("Enter a string to permute: ").strip()]
def permute(a,i,n) :
  j=0
  if (i == n):
    print "".join(a)
  else:
    j=i
    while(j<=n):
      a[i] , a[j] = a[j] , a[i] #swap(a,i,j)
      permute(a,i+1,n)
      a[i] , a[j] = a[j] , a[i] #swap(a,i,j)
      j+=1

permute(a,0,2)