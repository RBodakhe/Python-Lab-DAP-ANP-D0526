"""
Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.
"""
sum = 0
print("Enter numbers to calculate sum\nEnter 0 to end loop\n")
i = 0
while True:
    i += 1
    no = float(input(f"Enter {i}th number: "))
    if no == 0:
        break
    else:
        sum += no
print(f"\nSum of {i - 1} numbers is {sum}")
