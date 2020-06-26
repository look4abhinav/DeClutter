import os,shutil,logging,re

#Creating a Logger for logs
log_format = '%(levelname)s: %(asctime)s - %(message)s'
logging.basicConfig(filename = 'D:/Python/TestFolder/logs_declutter.log',level = logging.DEBUG,format = log_format)
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


def rename(file,path):
	while os.path.exists(os.path.join(path,file)):			
		i=0
		temp = file
		while True and i<10:
			filename = os.path.splitext(temp)
			number = re.findall('([0-9]+)$',filename[0])
			newfilename = filename[0]
			if not number:
				i+=1
			else:
				i=int(number[0])+1
				newfilename = re.sub('([0-9]+)$','',filename[0])
			newfilename = newfilename + str(i) + filename[1]
			#print(newfilename,os.path.exists(os.path.join(os.path.dirname(file),newfilename)))
			if os.path.exists(os.path.join(os.path.dirname(file),newfilename)):
				i+=1
				temp = newfilename
			else:
				os.rename(file,newfilename)
				break
		file = newfilename
	logger.warning('File exists in {}. Renaming file to {}'.format(os.path.abspath(path),newfilename))
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
						path = rename(os.path.basename(path),os.path.join(dest,types))
					shutil.move(path,os.path.join(dest,types))
					

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
