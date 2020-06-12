from itertools import accumulate
nums = list(accumulate(range(10)))
print(nums)
name = "chidex"


print("""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| Guess any number to check      |
| If it is in the range          |
| If not in the range you get    |
| Stuck in my loop!              |    
|                                |
|                                |
+================================+
""")
userinput = int(input("Guess the number game,Enter any number(0-50):"))
print ("Answer this question before leaving")
use = str(input("who wrote this program :"))

while userinput != 0:
    if userinput in nums:
     
        
        print("Well done, muggle! You are free now you are smart!!!!")

    if use in name:
        print("weldone!!!")
        
           

        userinput = int(input("Enter 0 to stop or guess another number:"))
    else:
        print("Ha ha! You're stuck in my loop")
