alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(para_text, para_shift):    
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    new_alpha = []
    for i in range(0, len(para_text)):
        alpha_index = alphabet.index(para_text[i])         #alpahbet.index(letter) index의 장점: 함수가 찾는 요소의 첫번째의 인덱스만 반환함. 뒤에나오는 중복된 항목에 대해서는 인덱스를 반환하지 않음
        if (alpha_index+para_shift) < len(alphabet):
            new_alpha += alphabet[alpha_index+para_shift]
        else:
            new_alpha += alphabet[(alpha_index+para_shift) - len(alphabet)]
    
    cipher_text = ''.join(new_alpha)
    print(f"The encoded text is {cipher_text}.")
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(para_text = text, para_shift = shift)