from itertools import accumulate
nums = list(accumulate(range(300)))
print(nums)



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
userinput = int(input("Guess the number game,Enter any number:"))
while userinput != 0:
    if userinput in nums:
     
        
        print("Well done, muggle! You are free now you are smart!!!!")
        
        userinput = int(input("Enter 0 to stop or guess another number:"))
    else:
        print("Ha ha! You're stuck in my loop")
    
        