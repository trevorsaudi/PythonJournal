#!/usr/bin/env python3

PASSWORDS = {
    'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'
}

import sys
import pyperclip
if len(sys.argv) < 2:
    print("Usage: passwordlocker.py [account] = copy account password")
    sys.exit()

account = sys.argv[1] #first command line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+ account + 'copied to the clipboard')
else:
    print('There is no account named ' + account)