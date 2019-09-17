import sys

branches = [
    'master',
    '1-vulnerable-components/code',
    '1-vulnerable-components/test',
    '1-vulnerable-components/fix',
    '2.1-sql-injection/code',
    '2.1-sql-injection/test',
    '2.1-sql-injection/fix',
    '2.2-sql-injection/test',
    '2.2-sql-injection/fix',
    '2.3-sql-injection/fix',
    '3.1-weak-password-storage/code',
    '3.1-weak-password-storage/fix',
    '3.2-weak-password-storage/test',
    '3.2-weak-password-storage/fix',
    '4-broken-authentication/code',
    '4-broken-authentication/fix',
    '5.1-broken-deauthentication/code',
    '5.1-broken-deauthentication/test',
    '5.1-broken-deauthentication/fix',
    '5.2-broken-deauthentication/code',
    '5.2-broken-deauthentication/test',
    '5.2-broken-deauthentication/fix',
    '6-csrf/code',
    '6-csrf/test',
    '6-csrf/fix',
    '7-xss/code',
    '7-xss/test',
    '7-xss/fix',
    '8-broken-access-control/code',
    '8-broken-access-control/test',
    '8-broken-access-control/fix',
    '9-sensitive-data-exposure/code',
    '9-sensitive-data-exposure/fix',
]

_, command, branch = sys.argv
i = branches.index(branch)
if command == 'next':
    next = branches[i + 1] if i + 1 < len(branches) else ""
    print(next)
elif command == 'prev':
    prev = branches[i-1] if i > 0 else ""
    print(prev)
