# Cesear_cracker
This program takes a English language string encrypted by a Cesearian cipher ([Wikipedia link about Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher)) and attempts to decrypt it using freqeuncy analysis. The shift is calculated by finding the highest frequency letter and performing a shift based on the differnce between the highest frequency letter and the letter "e". This has shown to be effective aganist most normal text, but could be defeated if the plaintext string has a letter that has a higher frequency than "e".

### Planned Improvements:
- validate the shift based on multiple letter frequencies 
- check for digraphs and trigraphs 
- crack for additional ciphers
