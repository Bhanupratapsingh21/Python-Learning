def checkgrades():
   total_marks = int(input("Total Marks Of Exam"))
   gotten_marks = int(input("Total Marks You Got"))
   percentage  = (gotten_marks / total_marks) * 100 
   if percentage >= 90:
        grade = "A"
   elif percentage >= 80:  # No need for `or percentage < 89`, already handled by previous condition
        grade = "B"
   elif percentage >= 70:  # No need for `or percentage < 79`, same reason as above
        grade = "C"
   else:
        grade = "F"
   print (f"percentage is {percentage} And Grade Is {grade}")
   