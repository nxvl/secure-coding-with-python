from hashlib import sha256
from sys import argv


def generate_rainbow_table(wordlist, outfile):
    with open(outfile, 'w+') as o:
        with open(wordlist, 'rb') as f:
            for line in f:
                password = line.strip()
                calc_hash = sha256(password).hexdigest()
                o.write("%s %s\n" % (calc_hash, password))


if __name__ == '__main__':
    generate_rainbow_table(argv[1], argv[2])
