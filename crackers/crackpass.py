from hashlib import sha256
from sys import argv


def crack_hash(pass_hash, wordlist):
    with open(wordlist, 'rb') as f:
        for line in f:
            password = line.strip()
            calc_hash = sha256(password).hexdigest()
            if calc_hash == pass_hash:
                print("Password is: %s" % password.decode())
                break


if __name__ == '__main__':
    crack_hash(argv[1], argv[2])
