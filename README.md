# Jigsaw Cryptography

Jigsaw Cryptography takes its inspiration from jigsaw puzzles. Most cryptography methods is a 1-to-1 file method - during encryption, a single unencrypted file (commonly known as plain text) is encrypted into one encrypted file (commonly known as cipher text) using a key. Decryption does the reverse. Mathematically,

encrypt(plaintext, key) --> ciphertext

decrypt(ciphertext, key) --> plaintext

If encryption and decryption are seen as transformation and de-transformation functions, respectively, between plain text and cipher text; the weakest link is in the 1-to-1 file mapping. Brute force attack is possible because all the plain text information exist in the cipher text, though transformed.

Jigsaw Cryptography addresses the 1-to-1 file weakness by using 1-to-N file mapping. This is likened to taking a picture and make a jigsaw puzzle out of it. The complexity of brute force attack increases exponentially with the number of jigsaw pieces. By producing many files, it also makes it possible to transport the encrypted file safely via multiple routes, and this prevents reduces the chances of man-in-the-middle attack. This is like making a 1000-piece jigsaw puzzle, shuffle the pieces, load the pieces into 5 containers and the assembly instruction in the 6th container. If one container is hijacked, all the information is not compromised. 

The command-line interface (CLI) for Jigsaw Cryptography is ```jsc.py```, using the following command structure

```python jsc.py [command] [options]```

## Comparison with AES-256

Given that the key size of AES-256 is 32 characters long (32 characters of 8 bytes each = 256 bytes) and given that there are 94 characters in the set of mixed alphanumeric with symbols, the total number of keys is 1.38e63 (94 to the power of 32).

How does this number of permutations compare with Jigsaw Cryptography?

Assuming that Jigsaw Cryptography is used to encrypt a 1 MB (1048576 bytes) file and split into 16 64-KB Jigsaw files, there are 2e13 permutations to assemble 16 64-KB files into the original 1 MB file using Jigsaw version 1. By varying the size of the Jigsaw File (using blocksize parameter), one can easily achieve a much larger number of permutations; for example, the 1 MB file can be split into 256 4-KB Jigsaw files, which will then yield 8.5e506 permutations.

Essentially, you will need at least split the original file into at least 50 Jigsaw files to achieve the permutation of AES-256 as [P(50, 50) = 50! = 3e64] > 1.38e63.

You can estimate the largest block size using optimal block size command; such as, ```python jsc.py obs --filename=test_data/DataA.xlsx``` which gives

```
(py37) C:\Users\Maurice Ling\Dropbox\MyProjects\jigsaw_cryptography>python jsc.py obs \
--filename=test_data/DataA.xlsx

Size of C:\Users\Maurice Ling\Dropbox\MyProjects\jigsaw_cryptography\test_data\DataA.xlsx is 79343738 bytes
Minimum block size to reach AES-256 is 1586874 bytes
```

stating that the minimum block size should be 1,586,874 bytes.

## Encryption

Encryption is performed using the ```encrypt``` command,

```
python jsc.py encrypt \
  --slicer=<slicer> \
  --blocksize=<blocksize> \
  --filenamelength=<filenamelength> \
  --hashlength=<hashlength> \
  --version=<version> \
  --verbose=<verbose> \
  --filename=<filename>\
  --output_dir=<output_dir>
```

where

* filename: Relative or absolute path to the file to be encrypted.
* slicer: Set the file slicing method. Allowable values are 'even' (even Jigsaw file size) or 'uneven' (uneven Jigsaw file size). Default = even.
* blocksize: Set the size of a Jigsaw file. Allowable values are any positive integer. In the case of uneven slicer, size of Jisgaw files will be between 1 to 2  block sizes. Default = 32768.
* filenamelength: Set the length of file name of a Jigsaw file. Longer file name determines the number of allowable Jigsaw files in a directory, up to file system limits. Allowable values are any positive integer. Default = 30.
* hashlength: Set the file has length of each Jigsaw file. This is used to check for fidelity of the files. Allowable values are any positive integer. Default = 16.
* version: Set the Jigsaw version. Allowable values are 1 (version 1). Default = 1.
* verbose Interger: Set the verbosity from 1 (most information) onwards. Default = 1.

For example, 
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

Decryption is performed using the ```decrypt``` command,

```
python jsc.py decrypt \
  --keyfilename=<keyfilename> \
  --outputfile=<outputfile> \
  --encrypt_dir=<encrypt_dir>
```

where

* keyfilename: Relative or absolute path to the key file (produced during encryption process).
* outputfile: Relative or absolute path to the file after decryption.
* encrypt_dir: Relative or absolute path to the directory containing the jigsaw files.

For example, 
```
python jsc.py decrypt \
  --keyfilename=test_data/DataA.xlsx.jgk \
  --outputfile=test_data/DataA_1.xlsx \
  --encrypt_dir=./test_data
```
