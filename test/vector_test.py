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
	print("add: x:{} y:{}".format(myvec.x,myvec.y))

	# for sub
	myvec = Vec2(2,3);
	secvec = Vec2(4,5);
	myvec = myvec - secvec
	print("sub: x:{} y:{}".format(myvec.x,myvec.y))

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
	print("scale: x:{} y:{}".format(myvec.x,myvec.y))

	# for vec_len
	myvec = Vec2(2,3);
	length = myvec.vec_len()
	print("length: {}".format(length))

	# for normal
	myvec = Vec2(2,3);
	nor = myvec.normal()
	print("normal: {} {}".format(myvec.x,myvec.y))

	# for angle
	myvec = Vec2(2, 2);
	secvec = Vec2(3, 4)
	ang = myvec.angle(secvec)
	print("angle: {}".format(ang))

	myvec = Vec2(0, 1);
	secvec = Vec2(1, 0)
	ang = myvec.angle(secvec)
	print("angle: {}".format(ang))

if __name__ == '__main__':
	main()