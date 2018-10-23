import os

str1 = 'a-p-4-8-h-g-1-7-5-2'
str2 = ' '
i=0

#pr1
print "car number plate being temporarily stored"
fo = open("msg.txt","w")
fo.write(str1)
fo.close()

#pr2
print "Algorithm initiation"
fo = open("msg.txt","w")
str2 = str1
fo.write(str1)
fo.close()

print "Algorithm starts"
#pr3 --->  cipher algorithm starts
 
l = str2.split('-')
l1 = str2.split('-')
l2 = str2.split('-')
#print l1

for i in range(0,10):
	if l[i] == 'a':
		l1[i] = '!'
	elif l[i] == 'b':
		l1[i] = '@'
	elif l[i] == 'c':
		l1[i] = '#'
	elif l[i] == 'd':
		l1[i] = '$'
	elif l[i] == 'e':
		l1[i] = '%'
	elif l[i] == 'f':
		l1[i] = '^'
	elif l[i] == 'g':
		l1[i] = '&'
	elif l[i] == 'h':
		l1[i] = '*'
	elif l[i] == 'i':
		l1[i] = '('
	elif l[i] == 'j':
		l1[i] = ')'
	elif l[i] == 'k':
		l1[i] = '{'
	elif l[i] == 'l':
		l1[i] = '}'
	elif l[i] == 'm':
		l1[i] = '['
	elif l[i] == 'n':
		l1[i] = ']'
	elif l[i] == 'o':
		l1[i] = '?'
	elif l[i] == 'p':
		l1[i] = '/'
	elif l[i] == 'q':
		l1[i] = '+'
	elif l[i] == 'r':
		l1[i] = '='
	elif l[i] == 's':
		l1[i] = '***'
	elif l[i] == 't':
		l1[i] = ';'
	elif l[i] == 'u':
		l1[i] = ':'
	elif l[i] == 'v':
		l1[i] = '##'
	elif l[i] == 'w':
		l1[i] = '$$'
	elif l[i] == 'x':
		l1[i] = '**'
	elif l[i] == 'y':
		l1[i] = '++'
	elif l[i] == 'z':
		l1[i] = '--'
	elif l[i] == '1':
		l1[i] = '(('
	elif l[i] == '2':
		l1[i] = '))'
	elif l[i] == '3':
		l1[i] = '[['
	elif l[i] == '4':
		l1[i] = ']]'
	elif l[i] == '5':
		l1[i] = '^^'
	elif l[i] == '6':
		l1[i] = '%%'
	elif l[i] == '7':
		l1[i] = '??'
	elif l[i] == '8':
		l1[i] = '::'
	elif l[i] == '9':
		l1[i] = ';;'
	else:
		l1[i] = '//'

		
for i in range(0,10):
	l2[i] = '0'

print "50% completed"
for i in range(0,10):
	if i == 0:
		l2[7] = l1[0]
	elif i == 1:
		l2[3] = l1[1]
	elif i == 2:
		l2[8] = l1[2]
	elif i == 3:
		l2[1] = l1[3]
	elif i == 4:
		l2[6] = l1[4]
	elif i == 5:
		l2[9] = l1[5]
	elif i == 6:
		l2[2] = l1[6]
	elif i == 7:
		l2[0] = l1[7]
	elif i == 8:
		l2[4] = l1[8]
	else:
		l2[5] = l1[9]

str2 = '-'.join(l2)
#print str1
print " Completion of algorithm"
fo = open("cipher.txt","w")
fo.write(str2)
fo.close()

os.rename("/home/ironman/Desktop/cipher.txt", "/home/ironman/Pictures/project/project/project/project/project/project/cipher.txt")
#os.remove("msg.txt")
