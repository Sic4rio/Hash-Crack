# Python Hash Cracker
[![Python](https://img.shields.io/badge/Python-%E2%89%A5%203.x-yellow.svg)](https://www.python.org/) 
<img src="https://img.shields.io/badge/Developed%20on-kali%20linux-blueviolet">
[![License](https://img.shields.io/badge/License-MIT-red.svg)]
<img src="https://img.shields.io/badge/Maintained%3F-Yes-96c40f">

<img src="https://user-images.githubusercontent.com/75425513/228818247-c7a68838-2324-4879-aa99-f6668d2a837a.gif" alt="GIF" width="300" />

A command-line tool for cracking hashed passwords using a wordlist.

## Introduction

This is a script written in Python that allows you to crack hashed passwords using a specified hash type and a wordlist. It supports various hash algorithms, including MD5, SHA1, SHA224, SHA256, SHA384, and SHA512.

## Usage

To use the tool, follow the steps below:

1. Clone this repository or download the script.
2. Open a terminal and navigate to the script's directory.
3. Make sure you have Python 3.x installed on your system.
4. Install the required dependencies by running the following command:
```pip install colorama```
5. Run the script using the following command:
```python hash_cracker.py```

6. Follow the on-screen instructions to provide the necessary options, including the hash type, the hash value to crack, the path to the wordlist file, and other preferences.

## Options

The Python Hash Cracker provides the following command-line options:
```
- `--help`: Display the help message with detailed instructions and available options.
- `--Accepted-hash-type`: Specify the type of hash to crack (e.g., md5, sha1, sha256).
- `--hash`: The hash value to crack. Provide the hashed password you want to crack.
- `--wordlist`: Path to the wordlist file to use for cracking. The default is set to `/usr/share/wordlists/rockyou.txt`.
- `--verbose`: Enable verbose mode, which displays additional information during the cracking process.
- `--brute-force`: Enable brute-force mode, allowing the script to attempt all possible combinations of numbers.
```
## Examples

Here are some examples of how to use the Python Hash Cracker:

```$ python hash_cracker.py --Accepted-hash-type sha256 --hash 0a52730597fb4ffa01fc117d9e71e3a9 --wordlist /path/to/wordlist.txt --verbose y```

Copy code
```$ python hash_cracker.py --Accepted-hash-type md5 --hash 5f4dcc3b5aa765d61d8327deb882cf99 --brute-force y```


## Dependencies

The Python Hash Cracker depends on the `colorama` package. You can install it using the following command:
```pip install colorama```

### Contributors
If you like to contribute to the development of the project, in that case, pull requests are open for you.
Also, you can suggest an ideas and create a task in my track list

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0) [![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/stanislav-web)  
