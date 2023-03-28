# to find the factorial of the number
def factorial(n):
 if n==0:
  return 1

 return n*factorial(n-1)


num =5;
print("The factorial of ", num ," is :" ,factorial(num))





# # Use defined Factorial function
# # n!= n x n-1...1

# def facto(n):
#     f=1
#     while(n>0):
#         f*=n
#         n-=1
#         return f

# # define Main 
# def Main():
#     n=int(input("Enter a no:"))
#     print(n,"Factorial :",facto(n))

# if __name__=="__main__":
#     Main()