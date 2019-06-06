# Jigsaw Cryptography

Jigsaw Cryptography takes its inspiration from jigsaw puzzles. Most cryptography methods is a 1-to-1 file method - during encryption, a single unencrypted file (commonly known as plain text) is encrypted into one encrypted file (commonly known as cipher text) using a key. Decryption does the reverse. Mathematically,

encrypt(plaintext, key) --> ciphertext

decrypt(ciphertext, key) --> plaintext

If encryption and decryption are seen as transformation and de-transformation functions, respectively, between plain text and cipher text; the weakest link is in the 1-to-1 file mapping. Brute force attack is possible because all the plain text information exist in the cipher text, though transformed.

Jigsaw Cryptography addresses the 1-to-1 file weakness by using 1-to-N file mapping. This is likened to taking a picture and make a jigsaw puzzle out of it. The complexity of brute force attack increases exponentially with the number of jigsaw pieces. By producing many files, it also makes it possible to transport the encrypted file safely via multiple routes, and this prevents reduces the chances of man-in-the-middle attack. This is like making a 1000-piece jigsaw puzzle, shuffle the pieces, load the pieces into 5 containers and the assembly instruction in the 6th container. If one container is hijacked, all the information is not compromised. 

## Comparison with AES-256

Given that the key size of AES-256 is 32 characters long (32 characters of 8 bytes each = 256 bytes) and given that there are 94 characters in the set of mixed alphanumeric with symbols, the total number of keys is 1.38e63 (94 to the power of 32).

How does this number of permutations compare with Jigsaw Cryptography?

Assuming that Jigsaw Cryptography is used to encrypt a 1 MB (1048576 bytes) file and split into 16 64-KB Jigsaw files, there are 2e13 permutations to assemble 16 64-KB files into the original 1 MB file using Jigsaw version 1. By varying the size of the Jigsaw File (using blocksize parameter), one can easily achieve a much larger number of permutations; for example, the 1 MB file can be split into 256 4-KB Jigsaw files, which will then yield 8.5e506 permutations.

## Encryption

```
python jsc.py encrypt \
  --slicer=even \
  --blocksize=262144 \
  --filenamelength=30 \
  --hashlength=16 \
  --version=1 \
  --verbose=2 \
  --filename=test_data/DataA.xlsx \
  --output_dir=./test_data
```

## Decryption

```
python jsc.py decrypt \
  --keyfilename=test_data/DataA.xlsx.jgk \
  --outputfile=test_data/DataA_1.xlsx \
  --encrypt_dir=./test_data
```
