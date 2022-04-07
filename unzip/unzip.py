#!/usr/bin/python3

import zipfile
import optparse
import os
from threading import Thread


def extract_file(zip_file, pwd):
    try:
        zip_file.extractall(pwd=pwd.encode())
        print("[+] Password is: {}".format(pwd))
    except:
        pass


def main():
    parser = optparse.OptionParser(
        "usage: {} -f <zipfile> -d <dictionary>".format(os.path.basename(__file__)))

    parser.add_option('-f', dest='zname', type='string',
                      help='specify zip file')
    parser.add_option('-d', dest='dname', type='string',
                      help='specify dictionary file')

    (options, _) = parser.parse_args()

    if (options.zname == None) or (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zip_file = zipfile.ZipFile(zname)
    pass_file = open(dname, 'r')

    for password in pass_file.readlines():
        stripped_pass = password.strip()
        t = Thread(target=extract_file, args=(zip_file, stripped_pass))
        t.start()


if __name__ == "__main__":
    main()
