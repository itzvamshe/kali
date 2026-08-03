def recursive_sum(n):

   # base case
   if n==1:
       return 1


   return n + recursive_sum(n - 1)

if __name__=="__main__":
    n = 5
    print(recursive_sum(n))
