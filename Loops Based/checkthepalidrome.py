from reversestr import reverse

def checkpalidrome(name):
    name_in_reverse = reverse(name)
    if name == name_in_reverse:
        print("Palidrome")
    else:
        print("Not a palidrome")

checkpalidrome("naman")
checkpalidrome("bhanu")
