alphabet  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction =  input('Type "encode" to encrypt,Type "decode to decrpyt"\n').lower()
text = input("Type your message\n").lower()
shift = int(input("type the shift Number \n"))

# todo create a function called encrypt 
# def encrypt(orginal_text,shift_amount):
#     cipher_text = ""
#     for letter in orginal_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text +=alphabet[shift_amount]
#     print(f"here is the encoded result:{cipher_text}")    

# encrypt(orginal_text=text, shift_amount=shift)
    
   
    
# # end encrypt

# def decrypt(orginal_text,shift_amount):
#     output_text = ""
#     for letter in orginal_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         output_text_text +=alphabet[shift_amount]
#     print(f"here is the encoded result:{output_text}")
#combining result    
def ceaser(orginal_text,shift_amount,encode_or_decode): 
    output_text = ""
    for letter in orginal_text:
        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text +=alphabet[shift_amount]
    print(f"here is the encoded result:{encode_or_decode}d result:{output_text}")   


ceaser(orginal_text=text, shift_amount=shift,encode_or_decode=direction)