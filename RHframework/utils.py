import os

def SET_ROOT(name):
	global ROOT
	ROOT = name

# Constants for resource path map
IMG_SPRITE = 0
FONT_MAIN = 50
SE_MAIN = 100
MUSIC_MAIN = 200

ROOT = ''

PATH = { \
	IMG_SPRITE: 'assets/sprite/',
	FONT_MAIN: 'assets/font/',
	SE_MAIN: 'assets/se/',
	MUSIC_MAIN: 'assets/music/'
}

'''
GET_PATH(type, name) -> str (path/name)
	Get the full path depending on the type
'''
def GET_PATH(t, name):
	return os.path.join(ROOT, PATH[t]) + name

'''
GET_DIR(t) -> str (path)
'''
def GET_DIR(t):
	return os.path.join(ROOT, PATH[t])