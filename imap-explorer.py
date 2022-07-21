#!/usr/bin/env python3

import getpass
from imaplib import IMAP4_SSL

hostname = input("Enter the server address: ")
username = input("Enter the user name: ")
password = getpass.getpass("Enter the password: ")

with IMAP4_SSL(hostname) as imap:
    imap.login(username, password)
    folders = imap.list()
    for folder in folders[1]:
        print("Folder: %s" % folder)
    imap.logout()
