import hashlib
import os
import sys
import time
import colorama
from colorama import Fore, Style
import readline

colorama.init()

colors = [Fore.MAGENTA, Fore.BLUE, Fore.GREEN, Fore.RED, Fore.CYAN, Fore.YELLOW + Style.BRIGHT, Fore.YELLOW + Style.BRIGHT]

print(" ➖➖➖🟥➖🟪🟪🟪  ")
print(" ➖➖➖➖🟥🟪🔳🟪🟪")
print(" ➖➖➖🟥➖➖🟪🟪🟪")
print(" ➖➖➖➖➖➖➖🟪🟪")
print(" ➖➖➖➖➖➖➖🟪🟪")
print(" ➖🟪🟪➖🟪🟪➖🟪🟪")
print(" 🟪🟪➖🟪🟪🟪🟪🟪🟪")
print(" 🟪🟪🟪🟪➖🟪🟪🟪🟪")
print(" ➖🟪🟪➖➖➖🟪🟪  ")
print("Python Hash-Cracker ")
print("| SICARIO | 2023 |  ")


def checkOS():
    if os.name == "nt":
        operatingSystem = "Windows"
    elif os.name == "posix":
        operatingSystem = "posix"
    else:
        operatingSystem = "Unknown"
    return operatingSystem


class HashCracking:
    def __init__(self):
        self.lineCount = 0

    def hashCrackWordlist(self, userHash, hashType, wordlist, verbose, bruteForce=False):
        start = time.time()
        solved = False
        if "md5" in hashType:
            h = hashlib.md5
        elif "sha1" in hashType:
            h = hashlib.sha1
        elif "sha224" in hashType:
            h = hashlib.sha224
        elif "sha256" in hashType:
            h = hashlib.sha256
        elif "sha384" in hashType:
            h = hashlib.sha384
        elif "sha512" in hashType:
            h = hashlib.sha512
        else:
            print("[-] Is \'%s\' a supported hash type?" % hashType)
            exit()
        if bruteForce is True:
            while True:
                line = "%s" % self.lineCount
                line.strip()
                numberHash = h(line.encode()).hexdigest().strip()
                if verbose is True:
                    sys.stdout.write('\r' + colors[0] + str(line) + ' ' * 20 + Style.RESET_ALL)
                    sys.stdout.flush()
                if numberHash.strip() == userHash.strip().lower():
                    end = time.time()
                    print("\n" + Fore.GREEN + "[+] Hash is: %s" % self.lineCount)
                    print("[*] Time: %s seconds" % round((end - start), 2))
                    savedHashFile = open('SavedHashes.txt', 'a+')
                    for solvedHash in savedHashFile:
                        if numberHash in solvedHash.split(":")[1].strip():
                            solved = True
                    if solved is False:
                        print("[*] Hash to SavedHashes.txt")
                        savedHashFile.write('%s:{}'.format(numberHash) % line)
                        savedHashFile.write('\n')
                    savedHashFile.close()
                    exit()
                else:
                    self.lineCount = self.lineCount + 1
        else:
            with open(wordlist, "r", encoding="latin-1") as infile:
                for line in infile:
                    line = line.strip()
                    lineHash = h(line.encode()).hexdigest()
                    if verbose is True:
                        sys.stdout.write('\r' + colors[0] + str(line) + ' ' * 20 + Style.RESET_ALL)
                        sys.stdout.flush()

                    if str(lineHash) == str(userHash.lower()):
                        end = time.time()
                        print("\n" + Fore.GREEN + "[+] Hash is: %s" % line)
                        print("[*] Words tried: %s" % self.lineCount)
                        print("[*] Time: %s seconds" % round((end - start), 2))
                        savedHashFile = open('SavedHashes.txt', 'a+')
                        for solvedHash in savedHashFile:
                            if lineHash in solvedHash.split(":")[1].strip():
                                solved = True
                        if solved is False:
                            print("[*] Hash to SavedHashes.txt")
                            savedHashFile.write('%s:{}'.format(lineHash) % line)
                            savedHashFile.write('\n')
                        savedHashFile.close()
                        exit()
                    else:
                        self.lineCount = self.lineCount + 1

            end = time.time()
            print("\n" + Fore.RED + "[-] Cracking Failed")
            print("[*] Reached end of wordlist")
            print("[*] Words tried: %s" % self.lineCount)
            print("[*] Time: %s seconds" % round((end - start), 2))
            exit()


def main():
    hashType = None
    userHash = None
    wordlist = None
    verbose = None
    numbersBruteForce = False
    print("[Running on %s]\n" % checkOS())
    try:
        print("[*] Options:")
        hashType = input(colors[1] + "[*] Enter the type of hash [See supported hashes]: " + Style.RESET_ALL).strip().lower()
        userHash = input(colors[2] + "[*] Hash: " + Style.RESET_ALL).strip().lower()
        readline.set_completer_delims('\t')
        readline.parse_and_bind("tab: complete")
        wordlist = input(colors[3] + "[*] Wordlist path? " + Style.RESET_ALL).strip()
        verbose = input(colors[4] + "[*] Verbose? [y/n]: " + Style.RESET_ALL).lower() == 'y'
        numbersBruteForce = input(colors[5] + "[*] Numbers of attempts? [y/n]: " + Style.RESET_ALL).lower() == 'y'
    except KeyboardInterrupt:
        print("\n[Exiting...]")
        sys.exit()

    if not (hashType and userHash and wordlist):
        print('[*] Please provide all the required options.')
        sys.exit()

    # looks through saved hash file instead of hashing all Wordlist entries
    with open('SavedHashes.txt', 'a+') as savedHashFile:
        for solvedHash in savedHashFile:
            solvedHash = solvedHash.split(":")
            if userHash.lower() == solvedHash[1].strip():
                print("[*] Saved Hash is: %s" % solvedHash[0])
                exit()
        else:
            print("[*] Hash: %s" % userHash)
            print("[*] Hash type: %s" % hashType)
            print("[*] Wordlist: %s" % wordlist)
            print("[+] Cracking...")
            try:
                h = HashCracking()
                h.hashCrackWordlist(userHash, hashType, wordlist, verbose, bruteForce=numbersBruteForce)

            except IndexError:
                print("\n[-] Hash not cracked:")
                print("[*] Reached end of wordlist")
                print("[*] Try another wordlist")
                print("[*] Words tried: %s" % h.lineCount)

            except KeyboardInterrupt:
                print("\n[Exiting...]")
                print("Words tried: %s" % h.lineCount)

            except IOError as e:
                print("\n[-] Couldn't find wordlist")
                print("[*] Is this right?")
                print("[>] %s" % wordlist)


if __name__ == "__main__":
    main()
