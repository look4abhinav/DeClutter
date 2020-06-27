import os
from time import sleep

from watchdog.observers import Observer

from functions import EventHandler, create, organize, remove

if __name__ == '__main__':
    print('Welcome to DeClutter')
    src_path = input('Enter Source Path: ')
    dest_path = os.path.join(src_path,'DeClutter')
    print('Destination: ',dest_path)
    print('Enter your desired choice')
    print('1. Run DeClutter in background')
    print('2. Run DeClutter once')
    print('3. Remove DeClutter')
    while True:
        choice = input('Choice: ')
        if choice == 1 or choice == 2:
            create(dest_path)
            organize(src_path,dest_path)
            if choice == 1:
                print('Running in Background...')
                event_handler = EventHandler(src=src_path, dest=dest_path)
                observer = Observer()
                observer.schedule(event_handler, src_path, recursive=True)
                observer.start()
            else:
                print('Running once...')
                try:
                    while True:
                        sleep(60)
                except KeyboardInterrupt:
                    observer.stop()
                observer.join()
        elif choice == 3:
            print("Removing Files...")
            remove(src_path,dest_path)
        else:
            print('Stopped')
            break