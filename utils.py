import os

def SET_ROOT(name):
	global ROOT
	ROOT = name

ROOT = ''
PATH = { \
	'image': 'assets/img'
}

def GET_PATH(t, name):
	return os.path.join(ROOT, PATH[t], name)
