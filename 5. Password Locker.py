#! python3

passwords = {'email':'12345', 'site':'abcde', 'bank':'1a2b3'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('You forgot to enter something')
    sys.exit

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password ' + passwords[account] + ' added to your clipboard')
else:
    print('There no account like that here')
