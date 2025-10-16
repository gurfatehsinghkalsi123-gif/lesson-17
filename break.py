msg = input("Enter your message: ")
for i in msg :
    if i == "a" or i == "A":
        print("A is found")
        break
    else:
        print("|A not found . The character is", i)
        
