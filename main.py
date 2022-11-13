import argparse
from itertools import count

import requests


def getArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument('code')

    return parser.parse_args()


if __name__ == '__main__':
    args = getArgs()

    with open(f'video/{args.code}.ts', 'wb') as file:
        for i in count():
            r = requests.get(f'https://la2.killcovid2021.com/m3u8/{args.code}/{args.code}{i}.ts')

            if r.status_code != 200:
                break

            file.write(r.content)

            print(f'write video piece {i}')

    print(f'finish code {args.code}')
