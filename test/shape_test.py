import sys,pygame
sys.path.append("../")
from shape import *

def main():
	first = Rect(0,0,300,300)
	second = Rect(301,301,400,400)

	print("inside:{}".format(first.check_point(300,300)))

	circle1 = Circle(3,3,2)
	circle2 = Circle(8,8,1)
	print("inside:{}".format(circle1.check_circle(circle2)))



if __name__ == '__main__':
	main()
