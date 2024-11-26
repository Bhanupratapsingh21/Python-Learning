def checkstrength (password):
    points = 0
    
    if len(password) >= 6:
         points += 2
         print("pass")
    elif len(password) >= 3:
          points += 1
          print("pass")
    else :
        points -= 1
    if any(char.isdigit() for char in password):
        points += 2
        print("pass")
    print(f"Your Strength Score Is {points}")