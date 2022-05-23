def introduction():
    print("Welcome")
    print("To your new role")
    print("You are a software development Intern")
introduction() 

# #function allowing inputs
def introduce_person(name):
    print(f"Welcome {name}")
    print(f"{name} you have a new role")
    print(f"You are now a software development Intern {name}!!")
introduce_person("Lona")
# #every time you call a new name it can be modified

# #function with several arguements
def introduce_name_career(name,career):
    print(f"Hello {name}")
    print(f"Welcome to {career}")
introduce_name_career("software development","Ruth")
# #above is positional arguements takes and prints arguements as they are ordered sometimes not making sense

# #keyword arguements though pass parameters exactly as ordered and assigned
def introduce_name_career(name="Lona",career="Software Development"):
    print(f"Hello {name}")
    print(f"Welcome to {career}")
introduce_name_career()
# #or
def introduce_name_career(name,career):
    print(f"Hello {name}")
    print(f"Welcome to {career}")
introduce_name_career(name="Atieno",career="User research")

##challenge
import math
def paintcans_calculations(height,width,coverage):
    cans_used = (width*height) / coverage
    exact_cans=math.ceil(cans_used)
    print(f"You will need {exact_cans} can to paint your wall")
def average_ages(*ages,no_of_students):
    average_age=(sum(ages))/no_of_students
    print(f"Your students average age is {average_age}")
# #checking for prime numbers
def prime_check(number):
    if number%2==1:
        print("This is a prime number")
    else:
        print("this is not a prime number") 
#method 2
# def prime_checker(number):
#     is_prime=True
#     for i in range(2,number-1):
#         if number%1==0:
#           is_prime=False  
#     if is_prime:
#         print("This is prime")  
#     else:
#         print("This is not a prime number")

        #CEASER CIPHER=ENCRYPT
        #encrypt
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c',
 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your word:\n").lower()
shift = int(input("Type the shift number of your word:\n"))

#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(word,shift_by):
    cipher_text=""
    for i in word:
        letter_position=alphabet.index(i)
        new_position =letter_position+shift_by
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")
         
encrypt(word=text,shift_by=shift )

         #CEASER CIPHER #DECRYPT

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_by):
    plain_word =""
    for i in  cipher_text:
        position=alphabet.index(i)
        new_position=position -shift_by
        plain_word+=alphabet[new_position]
    print(f"The text decoded is {plain_word}")    
        
# Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
if direction == "encode":
  encrypt (word=text, shift_by=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_by=shift)

#a shorter code that does everything
def decrypt_encrypt(first_text,shift_bywhat,text_direction):
    last_text=""
    for a in first_text:
        position=alphabet.index(a)
        if text_direction=="decode":
          shift_bywhat*= -1
        new_position =position +shift_bywhat  
        last_text +=alphabet[new_position]
    print(f"The {text_direction}d text is {last_text}")  

    decrypt_encrypt(first_text=text,shift_bywhat=shift,text_direction=direction)  


# import logo
from logo import logo
print(logo)
        


