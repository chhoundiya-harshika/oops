list = [1,2,3,4,5]
# print(list[3], end=" ")
# def cal_len(list):
#     print(len(list))
#     return list
# cal_len(list)

# def print_list(list):
#     for i in list:
#         print(i, end= " ")
#     return list
# print_list(list)

# n=5
# def fac(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
# fac(9)

# def converter(usd_val):
#     inr_val = usd_val*97
#     print(usd_val, "USD=", inr_val, "INR")
# converter(45)

#num= int(input("enter a num:"))
# def to_check(num):
#     if num%2==1:
#         print("ODD")
#     else:
#         print("EVEN")
# to_check(num)

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)

# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(6))

def nat_sum(n):
    if(n==0):
        return 0
    return nat_sum(n-1)+n
sum=nat_sum(5)
print(sum)