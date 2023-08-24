print("Student grade system")
print("Enter the student's marks in Maths, Accounts and Commerce:")
a,b,c=map(int,input().split())
percent = (a+b+c)/3
if percent >= 90:
    print("Excellent A grade ",percent)
elif percent >=70 and percent < 90:
    print("Good B grade ",percent)
elif percent >= 50 and percent < 70:
    print("Satisfactory C grade ",percent)
elif percent >= 35 and percent < 50:
    print("Pass D grade ",percent)
else:
    print("Fail E grade ",percent)
