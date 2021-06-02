import sys

def main():
    v = sys.version_info
    print('python version {}.{}.{}'.format(*v))

    a = sys.platform
    print(a)
if __name__ == '__main__': main()


import os

def main():
    v1 = os.name
    print(v1)

if __name__ == '__main__': main()