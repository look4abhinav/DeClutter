from functions import *

src_path = os.getcwd()
dest_path = os.path.join(src_path,'DeClutter')
log_folder = os.path.join(src_path,'logs_declutter.log')
print(src_path,dest_path,log_folder,sep = '\n')

remove(src_path,dest_path)