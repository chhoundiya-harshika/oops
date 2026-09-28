a = int(input("Enter any num"))
rev=0
while a!=0:
    r=a%10
    a=a//10
    rev = rev * 10 +r
    print(rev)

   