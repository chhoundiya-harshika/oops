# with open ("sample.txt", "w") as f:
#     f.write("Hi everyone\n we are learning python\n")

# with open ("sample.txt", "r") as f:
#     data=f.read()
#     new=data.replace('python','java')
#     print(new)
    
# with open ("sample.txt","w") as f:
#     f.write(new)

word="learning"

with open ("sample.txt","r") as f:
    data= f.read()
    if(data.find (word)!= -1):
        print("found")
    else:
        print("Not found")        
    
    