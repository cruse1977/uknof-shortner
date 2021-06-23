#!/usr/bin/env python

from shortlib import Database as db
from shortlib import User
import random
import ipaddr
import string


def main():

    if db.exists() is True:
        p = db.path()
        print ("\nDatabase already exists: %s\n" % (p))
        exit(1)

    print("\nCreating database...")
    db.create()
    username = "admin"
    password = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    newuser = User.create(username, password)
    print("New user '%s' created with password '%s'" % (username, password))

    return


if __name__ == '__main__':
    main()
