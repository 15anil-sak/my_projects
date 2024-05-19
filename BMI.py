import math
height=float(input("enter your height:"))
weight=float(input("Enter your weight:"))
bmi=weight/pow(height,2)
round_bmi=round(bmi,4)
print("your bmi value is:",round_bmi)
if round_bmi<0.0018:
    print("your are underweight")
    print("the diet should follow:")
if round_bmi>=0.0018 and round_bmi<=0.0024:
        print("your are health person")
        print("the diet should follow:")
elif round_bmi>=0.0024 and round_bmi<=0.0029:
        print("your are overweight")
        print("the diet should follow:")
elif round_bmi>=0.0029 and round_bmi<=0.0039:
        print("your are obsee")
        print("the diet should follow:")
else:
    print("given values are not be correct")
    

    
    
