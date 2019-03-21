import sys,pygame

sys.path.append("../")
from vector import *
from utils import *

SET_ROOT('..')

def main():

	# for add
	myvec = Vec2(2,3);
	secvec = Vec2(4,5);
	myvec = myvec + secvec
	print("add: {}".format(myvec))

	# for sub
	myvec = Vec2(2,3);
	secvec = Vec2(4,5);
	myvec = myvec - secvec
	print("sub: {}".format(myvec))

	# for dot
	myvec = Vec2(2,3);
	secvec = Vec2(4,5);
	val = myvec * secvec
	print("dot: {}".format(val))

	# for equal
	myvec = Vec2(2,3);
	secvec = Vec2(4,5);
	if myvec == secvec:
		print("Equal")
	else:
		print("Not Equal")

	# for scale
	myvec = Vec2(2,3);
	myvec.scale(3);
	print("scale: {}".format(myvec))

	# for vec_len
	myvec = Vec2(3,4);
	length = myvec.vec_len()
	print("length: {}".format(length))

	# for normal
	myvec = Vec2(1, 1);
	nor = myvec.normal()
	print("normal: {}".format(nor))

	# for angle
	myvec = Vec2(2, 2);
	secvec = Vec2(3, 4)
	ang = myvec.angle(secvec)
	print("angle: {}".format(ang))

	# rotate
	myvec = Vec2(1, 0);
	# print("rotate: {} {}".format(myvec.x,myvec.y))
	myvec.rotate(90)
	print("rotate: {}".format(myvec))
if __name__ == '__main__':
	main()