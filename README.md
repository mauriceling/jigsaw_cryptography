# Jigsaw Cryptography

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
