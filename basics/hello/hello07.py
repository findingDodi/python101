
def canLogin(username):
    if username.lower() == "dorina":
        return True
    
    return False

name = input("Enter Username ")

if canLogin(name):
    print("Welcome", name)
else:
    print("Access denied", name)