


name = ""

while name != "stop":
    name = input("Enter your name (type 'stop' to end): ")
    print("Hello", name)
    


while True:
    user_input = input("Enter a number (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    if user_input.isdigit():
        num = int(user_input)
        print("You entered the number:", num)
    else:
        print("Invalid input. Enter a number or 'q' to exit.")
        

secret = 5
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))
    
    if guess == secret:
        print("Correct!")
    else:
        print("Try again")
        
num = 2
t = 1

while t <= 10:
    print(num, "x", t, "=", num * t)
    t += 1
    
password = ""

while password != "admin123":
    password = input("Enter password: ")

print("Access granted")

word = "Python"
o = 0

while o < len(word):
    print(word[o])
    o += 1