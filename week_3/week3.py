#created by Jaccob on sept 12, 20253
'''
light_color=input("what is the color of the lights (red, yellow or red):")
if light_color== 'red':
    print('stop')
elif light_color== 'yellow':
    print('yield')
elif light_color== 'green':
    print('go')
    '''

         #Q4
'''
age = int(input("Enter your age: "))
goal = input("Enter your athleticism goal (Above Average / Below Average): ")

# Check the age group and athleticism goal
if age >= 20 and age <= 39:
    if goal == "Above Average":
        print("Your resting heart rate should be between 47–72")
    elif goal == "Below Average":
        print("Your resting heart rate should be between 73–93")

elif age >= 40 and age <= 59:
    if goal == "Above Average":
        print("Your resting heart rate should be between 46–71")
    elif goal == "Below Average":
        print("Your resting heart rate should be between 72–94")

elif age >= 60 and age <= 79:
    if goal == "Above Average":
        print("Your resting heart rate should be between 45–70")
    elif goal == "Below Average":
        print("Your resting heart rate should be between 71–97")

else:
    print("Sorry, no data for your age.")

'''
#Q5
n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
n3=int(input("enter a number:"))
if n1<n2 and n2<n3:
   print(n1,n2,n3)