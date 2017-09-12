import sys
import struct

for i in range(1, 778):
	fname1 = "./Broken_PNG/"+str(i)+"/1"
	fname2 = "./Broken_PNG/"+str(i)+"/2"
	fname3 = "./Broken_PNG/"+str(i)+"/3"

	FH1 = open(fname1, 'rb')
	FH2 = open(fname2, 'rb')
	FH3 = open(fname3, 'rb')

	test = open('./Broken_PNG/result/'+str(i)+'.png', 'wb')

	qq = FH1.read(1)
	ww = FH2.read(1)
	ee = FH3.read(1)

	print int(ord(qq))

	if int(ord(qq)) == 137:
		first = open(fname1, 'rb')
		second = open(fname2, 'rb')
		third = open(fname3, 'rb')

	elif int(ord(ww)) == 137:
		first = open(fname2, 'rb')
		second = open(fname3, 'rb')
		third = open(fname1, 'rb')

	else:
		first = open(fname3, 'rb')
		second = open(fname2, 'rb')
		third = open(fname1, 'rb')

	while True:
		s1 = first.read(1)
		if s1 == '': break
		test.write(s1)

	while True:
		s2 = second.read(1)
		if s2 == '': break
		test.write(s2)

	while True:
		s3 = third.read(1)
		if s3 == '': break
		test.write(s3)	


	FH1.close()
	FH2.close()
	FH3.close()
	test.close()
