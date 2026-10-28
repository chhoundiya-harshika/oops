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

num= int(input("enter a num:"))
def to_check(num):
    if num%2==1:
        print("ODD")
    else:
        print("EVEN")
to_check(num)