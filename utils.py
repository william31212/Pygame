import os

PATH = { \
	'image': 'assets/img'
}

def GET_PATH(t, name):
	return os.path.join(PATH[t], name)
