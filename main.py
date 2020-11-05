import json
import os
import hashlib

blockchain_dir = os.curdir + "/blockchain/"

def get_files():
    files = os.listdir(blockchain_dir)
    files = sorted([int(i) for i in files])

def get_hash(filename):
    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()

def check_integrity():
    files = get_files()

    for file in files:
        h = json.load(open(blockchain_dir+ str(file)))['hash']

        actual_hash = get_hash(str(file - 1))

        if h == actual_hash:
            res = "OK"
        else:
            res = "Corrupted"

def write_block(name, amount, to_whom, prev_hash=''):
    files = get_files()

    last_file = files[-1]

    filename = str(last_file + 1)

    prev_hash = get_hash(str(last_file))

    data = {"name": name,
            "amount": amount,
            "to_whom": to_whom,
            "hash": prev_hash
            }
    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    write_block(name='oleg', amount=5, to_whom='ksenia')


if __name__ == '__main__':
    main()