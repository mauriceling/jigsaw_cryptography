'''
Command-line processor for Jigsaw Cryptography

Date created: 5th June 2019

Copyright (c) 2018, Jigsaw Cryptography Team.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import math
import os
import sys
from pprint import pprint

# Ensure fire is installed
try: 
    import fire
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 
                           'install', 'fire'])
    import fire

import jigsaw


def sufficientBlockSize(filename):
    """
    Function to calculate the block size needed to reach AES-256 
    key permutation of 94**32.
    
    Example usage:

        python jsc.py obs --filename=test_data/DataA.xlsx

    @param filename String: Relative or absolute path to the file to 
    estimate block size.
    """
    filename = os.path.abspath(filename)
    size = os.path.getsize(filename)
    print('')
    aes_block = size // 50
    print('Size of %s is %s bytes' % (filename, str(size)))
    print('Minimum block size to reach AES-256 is ' + str(aes_block))


def encrypt(filename, 
            slicer='even', 
            blocksize=32768,
            filenamelength=30,
            hashlength=16,
            version=1,
            verbose=2,
            output_dir=''):
    """
    Function to encrypt a file.

    Example usage:

        python jsc.py encrypt --slicer=even --blocksize=262144 --filenamelength=30 --hashlength=16 --version=1 --verbose=2 --filename=test_data/DataA.xlsx --output_dir=./test_data

    @param filename String: Relative or absolute path to the file to 
    be encrypted.
    @param slicer String: Set the file slicing method. Allowable values 
    are 'even' (even Jigsaw file size) or 'uneven' (uneven Jigsaw file 
    size). Default = even.
    @param blocksize Integer: Set the size of a Jigsaw file. Allowable 
    values are any positive integer. In the case of uneven slicer, size 
    of Jisgaw files will be between 1 to 2  block sizes. Default = 32768.
    @param filenamelength Integer: Set the length of file name of a 
    Jigsaw file. Longer file name determines the number of allowable
    Jigsaw files in a directory, up to file system limits. Allowable 
    values are any positive integer. Default = 30.
    @param hashlength Integer: Set the file has length of each Jigsaw 
    file. This is used to check for fidelity of the files. Allowable 
    values are any positive integer. Default = 16.
    @param version Integer: Set the Jigsaw version. Allowable values 
    are 1 (version 1). Default = 1.
    @param verbose Interger: Set the verbosity from 1 (most information) 
    onwards. Default = 1.
    """
    j = jigsaw.JigsawFile()
    j.setting('slicer', str(slicer))
    j.setting('blocksize', int(blocksize))
    j.setting('filenamelength', int(filenamelength))
    j.setting('hashlength', int(hashlength))
    j.setting('version', int(version))
    j.setting('verbose', int(verbose))
    filename = os.path.abspath(filename)
    output_dir = os.path.abspath(output_dir)
    keyFileName = j.encrypt(filename, output_dir)


def decrypt(keyfilename, outputfile, encrypt_dir=''):
    """
    Function to decrypt a file.

    Example usage:

        python jsc.py decrypt --keyfilename=test_data/DataA.xlsx.jgk --outputfile=test_data/DataA_1.xlsx --encrypt_dir=./test_data

    @param keyfilename String: Relative or absolute path to the key 
    file (produced during encryption process).
    @param outputfile String: Relative or absolute path to the file 
    after decryption.
    @param encrypt_dir String: Relative or absolute path to the directory 
    containing the jigsaw files.
    """
    j = jigsaw.JigsawFile()
    keyfilename = os.path.abspath(keyfilename)
    outputfile = os.path.abspath(outputfile)
    encrypt_dir = os.path.abspath(encrypt_dir)
    j.decrypt(keyfilename, outputfile, encrypt_dir)


if __name__ == '__main__':
    exposed_functions = {'decrypt': decrypt,
                         'encrypt': encrypt,
                         'obs': sufficientBlockSize}
    fire.Fire(exposed_functions)
