# with open ("SAMPLE.TXT", "w") as f:
#     f.write("Hello everyone!\nI want to explore file handling in python")


with open("SAMPLE.TXT", "r") as f1:
    data=f1.read()
    print(len(data))
    