import sys
import random
from time import perf_counter 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from algorithms import *

try:
	n=int(input("--- Enter no. of elements to be added for sorted:"))
except IndexError:
	print ("-----> Number of Elements to added should be provided for the program to run **")
	sys.exit(1)
except ValueError:
	print("-----> Value cannot be anything else otherthan integer value **")
	sys.exit(1)

bubList,qList,qMedList,inList,merLis,heLsit,selList,mainList= ([],)*8 #using * operator to initialize multiple lists
Display("mainList",mainList) #Display Function to print the Unsorted list

for i in range(0,n):mainList.append(random.randint(0,1000))
execTime =[]
totalSpace=[]
merLis = mainList[:]
heLsit = mainList[:]
inList = mainList[:]
bubList = mainList[:]
qList = mainList[:]
qMedList = mainList[:]
selList = mainList[:]
####################### MERGE SORT funciton ####################
start_time = perf_counter()
sortedMerg = merge(merLis)
end_time = perf_counter()
run_time = end_time - start_time
space = n+6
least_time = (1000*run_time) 
dispList = displayList(sortedMerg,run_time,space)
Display("merge",dispList)
totalSpace.append(space)
execTime.append(1000*run_time) # in millisecond
####################### MERGE SORT funciton END ####################
####################### HEAP SORT funciton ####################
Display("mainList",heLsit)
start_time = perf_counter()
sortedHeap = heap(heLsit)
end_time = perf_counter()
run_time = end_time - start_time
space = n+5
dispList = displayList(sortedHeap,run_time,space)
Display("heap",dispList)
totalSpace.append(space)
execTime.append(1000*run_time)
if((1000*run_time) < least_time):least_time = (1000*run_time)
####################### HEAP SORT funciton END ####################
####################### QUICK SORT funciton ####################
Display("mainList",qList)
start_time = perf_counter()
soretedQuick= quick(qList,0,len(qList)-1,len(qList)-1)
end_time = perf_counter()
run_time = end_time - start_time
space = n+5
dispList = displayList(soretedQuick,run_time,space)
Display("quick",dispList)
totalSpace.append(space)
execTime.append(1000*run_time)
if((1000*run_time) < least_time):least_time = (1000*run_time)
####################### QUICK SORT funciton END ####################
####################### QUICK-MEDIAN SORT funciton ####################
Display("mainList",qMedList)
start_time = perf_counter()
soretedQuickMed= quickMedian(qMedList,0,len(qMedList))
end_time = perf_counter()
run_time = end_time - start_time
space = (2*n)+7
dispList = displayList(soretedQuickMed,run_time,space)
Display("quickMed",dispList)
totalSpace.append(space)
execTime.append(1000*run_time)
if((1000*run_time) < least_time):least_time = (1000*run_time)
####################### QUICK-MEDIAN SORT funciton END ####################
####################### INSERTION SORT funciton ####################
Display("mainList",inList)
start_time = perf_counter()
sortedInst = insertion(inList)
end_time = perf_counter()
run_time = end_time - start_time
space = n+3
dispList = displayList(sortedInst,run_time,space)
Display("insert",dispList)
totalSpace.append(space)
execTime.append(1000*run_time)
if((1000*run_time) < least_time):least_time = (1000*run_time)
####################### INSERTION SORT funciton END ####################
# ####################### SELECTION SORT funciton ####################
Display("mainList",selList)
start_time = perf_counter()
sortedSel = selection(selList)
end_time = perf_counter()
run_time = end_time - start_time
space = n+3
dispList = displayList(sortedSel,run_time,space)
Display("select",dispList)
totalSpace.append(space)
execTime.append(1000*run_time)
if((1000*run_time) < least_time):least_time = (1000*run_time)
# ####################### SELECTION SORT funciton END ####################
####################### BUBBLE SORT funciton ####################
Display("mainList",bubList)
start_time = perf_counter()  
sortBub = bubble(bubList)
end_time = perf_counter()
run_time = end_time - start_time
space = n+2
dispList = displayList(sortBub,run_time,space)
Display("bubble",dispList)
totalSpace.append(space)
execTime.append(1000*run_time)
if((1000*run_time) < least_time):least_time = (1000*run_time)
####################### BUBBLE SORT funciton END####################
####################### VISUALIZATION ####################
sort=["Merge","Heap","Quick","QuickMedian","Insertion","Selection","Bubble"]
for i in range(0,len(execTime)):
	if(execTime[i] == least_time):
		message =" Best Sorting Algorithm for the given no. of Elements is: "+sort[i]+" and the time taken is "+str(execTime[i])
		boxmessage(message)

plt.scatter(totalSpace,execTime, marker='o', color=['blue','red','green','orange','yellow','pink','purple'], s=12)
Merge = mpatches.Patch(color='blue', label='Merge')
Heap = mpatches.Patch(color='red', label='Heap')
Quick = mpatches.Patch(color='green', label='Quick')
QuickMed = mpatches.Patch(color='orange', label='QuickMedian')
Insertion = mpatches.Patch(color='yellow', label='Insertion')
Selection = mpatches.Patch(color='pink', label='Selection')
Bubble = mpatches.Patch(color='purple', label='Bubble')
plt.legend(handles=[Merge,Heap,Quick,QuickMed,Insertion,Selection,Bubble])
plt.xlabel('Space with respect to variables')
plt.ylabel('Runtime in millisecs')
plt.title('Comparison of Different Sorting Algorithm')
plt.show()
