import os
from time import sleep

from functions import create, organize, remove

if __name__ == '__main__':
    print('Welcome to DeClutter')
    src_path = input('Enter Source Path: ')
    dest_path = os.path.join(src_path,'DeClutter')
    print('Destination: ',dest_path)
    print('Enter your desired choice')
    print('1. Run DeClutter')
    print('2. Remove DeClutter')
    while True:
        choice = int(input('Choice: '))
        if choice == 1:
            create(dest_path)
            organize(src_path,dest_path)
            print('Running...')
        elif choice == 2:
            print("Removing Files...")
            remove(src_path,dest_path)
        else:
            print('Stopped')
            break