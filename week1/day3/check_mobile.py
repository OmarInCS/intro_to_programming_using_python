
mobile = input("add mobile number: ")

if len(mobile) == 10 and mobile.isdigit() and mobile.startswith("05"):
    print ("ok")
else:
    print("Not Ok")