import os,shutil

formats = {
	'image' : ['jpg','jpeg','png','gif','raw'],
	'audio' : ['mp3','wav','aac'],
	'video' : ['mp4','mkv','avi','flv','wmv','mov','m4a'],
	'document' : ['txt','csv','pdf','rtf','doc','docx','ppt','xls','xlsx'],
	'compressed' : ['zip','rar','7z'],
	'executable' : ['exe','msi','wsf']
}
def getFileType(path):
	return path.split('.')[-1]

src_path = os.getcwd()
dest_path = os.path.join(src_path,'DeClutter')
try:
	os.mkdir('DeClutter')
	print('Creating DeClutter directory')
	for ext in formats.keys():
		print('Creating',ext.capitalize(),'directory')
		os.mkdir('./DeClutter/'+ext.capitalize())
	print('Getting file paths')
	path = [os.path.abspath(_) for _ in os.listdir(src_path) if not os.path.isdir(_)]
	for file in path:
		if file != __file__:
			fileType = getFileType(file)
			for types in formats.keys():
				if fileType in formats[types]:
					print('Moving {} to {} directory'.format(os.path.basename(file),types.capitalize()))
					shutil.move(file,os.path.join(dest_path,types.capitalize()))

except FileExistsError:
	print('Moving all files to',src_path)
	paths = [folders[0] for folders in os.walk(dest_path)]
	for path in paths[::-1]:
			for file in os.listdir(path):
				print('Moving',os.path.basename(file))
				shutil.move(os.path.join(path,file), src_path)
			os.rmdir(path)
	print('Removing DeClutter')
	
