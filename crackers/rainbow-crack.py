from sys import argv


class RainbowCracker():
    def __init__(self, dbfile):
        self.db = dict()
        with open(dbfile, 'rb') as f:
            for line in f:
                k, v = line.strip().split(b' ', 1)
                self.db[k] = v

    def crack_hashes(self, hashfile):
        with open(hashfile, 'rb') as f:
            for line in f:
                pw = line.strip()
                print("password for %s is %s" % (pw, self.db[pw]))


if __name__ == '__main__':
    rc = RainbowCracker(argv[1])
    rc.crack_hashes(argv[2])
