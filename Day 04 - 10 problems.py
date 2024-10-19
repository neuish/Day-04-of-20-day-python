# 1. Write a function that takes a list of numbers and returns their sum.
def list_sum():
    sumlist = list(map(int, input("enter the list of numbers you wish to sum upto saperated by a space:").split()))

    if len(sumlist) == 0:
        print('the list is empty')
    else:
        total = 0
        for num in sumlist:
            total += num
        print('the sum of numbers in tne list is: ', total)

#2. Write a function that reverses a string.
def string_rev():
    stringr = input('enter the string to reverse:')
    #print(f'the reverse of the string is {string[::-1]}')
    #print('the reversed string is').join(reversed(stringr))

    reversestr = ''
    for char in stringr:
        reversestr += char
        print('the reversed string is: ', reversestr)

#3. Write a function that accepts a list of strings and returns a new list with each string's length.
def list_string():
    stringr = input('enter the string to add to the list:').split()

    if len(stringr) == 0:
        print('the string is empty')
    else:
        lengthstr = [len(x) for x in stringr]
        print('the lenght of character strings are', lengthstr)
            

#4. Write a function that checks if a string is a palindrome (reads the same forwards and backwards).
def palindrome():
    palindromestring = input('enter the string to check if it is a palindrome:').split()

    if palindromestring == palindromestring[::-1]:
        print('the string/character is a palindrome')
    
    else:
        print("not a palindrome")

#5. Implement a function that takes a list of integers and returns a new list with only the even numbers.
def evenist():
    evennum = list(map(int, input('enter the list of numbers you wish to use:').split()))

    if len(evennum) == 0:
        print('the list is empty')
    
    else:
        for x in evennum:
            if x%2 == 0:
                print(x)
        
def main_menu():
    while True:
        print('\n...main menu...')
        print('1. sum of numbers in a list')
        print('2. string reverse')
        print('3. length of a character in a string')
        print('4. palindrome string')
        print('5. print even from list of int')
        print('0. Exit')

        choice = input('Choose an option: ').strip()

        if choice == '1':
            list_sum()
        
        elif choice == '2':
            string_rev()
        
        elif choice == '3':
            list_string()
        
        elif choice == '4':
            palindrome()
        
        elif choice == '5':
            evenist()

        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

# Start the program
main_menu()
