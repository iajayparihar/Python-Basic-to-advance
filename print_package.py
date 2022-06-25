import sys
fh=open("myfile.txt")
line1=fh.readline()
line2=fh.readline()
sys.stdout.write(line1)
sys.stdout.write(line2)
sys.stderr.write(" \n no error occurred")