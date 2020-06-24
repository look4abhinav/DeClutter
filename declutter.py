import os,shutil,logging,re

#Creating a Logger for logs
log_format = '%(levelname)s: %(asctime)s - %(message)s'
logging.basicConfig(filename = 'D:/Python/Logs/logs_declutter.log',level = logging.DEBUG,format = log_format,filemode='w')
logger = logging.getLogger()

formats = {
	'Image' : ['jpg','jpeg','png','gif','raw'],
	'Audio' : ['mp3','wav','aac'],
	'Video' : ['mp4','mkv','avi','flv','wmv','mov','m4a'],
	'Document' : ['txt','csv','pdf','rtf','doc','docx','ppt','xls','xlsx'],
	'Compressed' : ['zip','rar','7z'],
	'Executable' : ['exe','msi','wsf']
}


def getFileType(path):
	#path = os.path.splitext(path)[-1]
	return path.split('.')[-1]

def rename(file):
	filename = os.path.splitext(file)
	number = re.findall('([0-9]+)$',filename[0])
	newfilename = filename[0]
	if not number:
		i=1
	else:
		i=int(number[0])+1
		newfilename = re.sub('([0-9]+)$','',filename[0])
	return newfilename + str(i) + filename[1]
		

def checkDuplicate(file,path):
	while os.path.exists(os.path.join(path,file)):			
		newfilename = rename(file)
		while True:
			try:
				os.rename(file,newfilename)
			except FileExistsError:
				os.rename(file,rename(newfilename))
		file = newfilename
	logger.info('File exists in {}. Rename file to {}'.format(os.path.abspath(path),newfilename))
	return os.path.abspath(newfilename)
		

def organize(src,dest):
	paths = [os.path.abspath(_) for _ in os.listdir(src) if not os.path.isdir(_)]
	for path in paths:
		if path != __file__:
			fileType = getFileType(path)
			for types in formats.keys():
				if fileType in formats[types]:
					logger.info('Moving {} to {} directory'.format(os.path.basename(path),types))
					if os.path.exists(os.path.join(os.path.join(dest,types),os.path.basename(path))):
						path = checkDuplicate(os.path.basename(path),os.path.join(dest,types))
						print('Duplicate found',os.path.basename(path))
					try:
						shutil.move(path,os.path.join(dest,types))
						pass
					except:
						print('Stopped')
					

def remove(src,dest):
	logger.info('Moving all files to {}'.format(src))
	paths = [folders[0] for folders in os.walk(dest)]
	for path in paths[::-1]:
			for file in os.listdir(path):
				logger.info('Moving {}'.format(os.path.basename(file)))
				shutil.move(os.path.join(path,file), src)
			os.rmdir(path)
	logger.info('Removing DeClutter')

src_path = os.getcwd()
dest_path = os.path.join(src_path,'DeClutter')

try:
	os.mkdir('DeClutter')
	logger.info('Creating DeClutter directory')
	for extn in formats.keys():
		logger.info('Creating {} directory'.format(extn))
		os.mkdir('./DeClutter/'+extn)
	logger.info('Getting file paths')
	organize(src_path,dest_path)

except FileExistsError:
	#remove(src_path,dest_path)
	organize(src_path,dest_path)
