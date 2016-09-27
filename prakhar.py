import msvcrt
import time

finish=10
count=0

print "press enter key to get started"

raw_input()
s_time=time.time()

while(1):
	     key=msvcrt.getch()
	     if key=='d':
	     	      count=count+1
	     	      print "-",
	     	      if count==finish:
	     	      	       break


count=finish
finish=20    	      	       
while(1):
	     key=msvcrt.getch()
	     if key=='s':
	     	      count=count+1
	     	                      
	     	      print"\n\t\t  -",
	     	      if count==finish:
	     	      	       break
	     	      	      
count=finish
finish=30	     	      	       
while(1):
	     key=msvcrt.getch()
	     if key=='d':
	     	      count=count+1
	     	      print"-",
	     	      if count==finish:
	     	      	       break	     	      	       
time_elapsed=time.time()-s_time
print "congrats you  have finished the game"
print "time taken is "+str(time_elapsed)
