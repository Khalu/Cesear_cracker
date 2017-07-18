import string


def caesar_crypto_encode(text, shift):
    output = ''
    mover = ''
    # returns empty if string is null or just space
    if not text:
        return ''
    elif text.isspace():
        return ''
    # creates a dictorary with lowercase letters
    letter_dict = dict(zip(string.ascii_lowercase, range(1, 27)))


    # if the shift is greater than 26 the shift is just repeated this finds the shift
    if shift >= 26 or shift <= -26:
        shift = shift % 26
    # if the shift is betwen 0 and -26 we add positive 26 to have it shift correclty
    if shift > -26 and shift < 0:
        shift = shift + 26

    for i in text:

        if i.isalpha():
            if i.isupper():
                iscap=True
            elif i.islower():
                iscap=False
            i = i.lower()
            for key, value in letter_dict.items():
                if i == key:
                    mover = value + shift
                    # checks to see if the shift if out of range and if so we inverse it
                    if mover > 26 or mover < -26:
                        mover += (26 * (-shift / shift))
            # Picks the letters out of the dictonary based on the shift
            for key, value in letter_dict.items():
                if mover == value:
                    if iscap:
                        output = output + key.upper()
                    elif not iscap:
                        output=output+key
        else:
            output = output + i

    print(output)

#text = input("input text to be encoded ")
#shift = input("input amount to shift ")
#caesar_crypto_encode(text, int(shift))