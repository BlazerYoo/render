#!/usr/bin/env python

import re, sys


def main():
    extern_url = input('Enter external database url: ')
    split = re.split(r'//|:|@|/', extern_url)
    try:
        server = split[4]
        database = split[-1]
        port = 5432
        username = split[2]
        password = split[3]
        print(f'Server: {server}\nDatabase: {database}\nPort: {port}\nUsername: {username}\nPassword: {password}')
    except Exception as ex:
        print(ex, file=sys.stderr)


if __name__ == '__main__':
    main()
    sys.exit(0)