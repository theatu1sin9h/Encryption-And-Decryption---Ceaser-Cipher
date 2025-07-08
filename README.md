# Encryption-And-Decryption---Ceaser-Cipher


Caesar Cipher - 
The Caesar Cipher is one of the simplest and oldest methods of encrypting messages, named after Julius Caesar, who reportedly used it to protect his military communications. This technique involves shifting the letters of the alphabet by a fixed number of places. For example, with a shift of three, the letter ‘A’ becomes ‘D’, ‘B’ becomes ‘E’, and so on

How It Works - 
The Caesar cipher works by shifting the letters in the plaintext message by a certain number of positions, known as the “shift” or “key”. It’s a type of substitution cipher, where each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on


Encryption and Decryption

The encryption can be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A = 0, B = 1,…, Z = 25. Encryption of a letter by a shift n can be described mathematically as:

 - Encryption: [ E_n(x) = (x + n) \mod 26 ]
 - Decryption: [ D_n(x) = (x - n) \mod 26 ]
