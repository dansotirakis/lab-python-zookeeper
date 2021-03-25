# Save the input in this variable
ticket = str(input())
numbers = list(ticket)
# Add up the digits for each half
half1 = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
half2 = int(numbers[-1]) + int(numbers[-2]) + int(numbers[-3])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
