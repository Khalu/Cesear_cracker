from Cesear import caesar_crypto_encode
import string





count=0
enc_dict={}

alpha_index = dict(zip(string.ascii_lowercase, range(1, 27)))
eng_letter_freq_dict={'a':'8.167','b':'1.492','c':'2.782','d':'4.253','e':'12.702','f':'2.228','g':'2.015','h':'6.094','i':'6.966','j':'0.153','k':'0.772','l':'4.025','m':'2.406','n':'6.749','o':'7.507','p':'1.929','q':'.095','r':'5.987','s':'6.327','t':'9.056','u':'0.978','v':'.978','w':'2.360','x':'.15','y':'1.974','z':'.074'}

encoded_string=input("cipher text here \n")

#reads the encoded string into a dictionary with the letter as the key and number of occurences as the value, incrementing
for i in encoded_string:
    i = i.lower()
    if i.isalpha():
        count+=1
        if i in enc_dict.keys():
            enc_dict[i]+=1
        elif i not in enc_dict.keys():
            enc_dict[i]=1




#initializes the variables used for getting top 3 letters and their frequencies

for key, value in enc_dict.items():
    #converts the number of occurences to a percentage of occurences
    enc_dict[key] = round((value / count) * 100, 3)

max_freq = [0, '']
for key,values in enc_dict.items():
    #checks for the highest freqeuencies in the encoded string dictionary
    if values > max_freq[0]:
        max_freq[0] = values
        max_freq[1] = key

suspect_shift=0
#trys to find the shift



for key, value in eng_letter_freq_dict.items():

   if float(value) < (float(max_freq[0])*1.10) and float(value) > (float(max_freq[0])*.90):
        suspect_shift = int(alpha_index[max_freq[1]]) - int(alpha_index['e'])

        #elif suspect_shift == int(alpha_index[max_freq_2[1]]) - int(alpha_index['o']):
        #    print("Another one this one O though")


print("The suspected shift is  "+str(suspect_shift))

caesar_crypto_encode(encoded_string, -(suspect_shift))
