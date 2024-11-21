import random
import sys
import timeit


def Merge_algo(Final_list,p,q,r):
    n1=q-p+1               # n1 size for left list
    n2=r-q                 # n2 size for right list
    L=[[0,0,0,0] for i in range(n1+1)]   # create Left list of n1+1 size to add a Sentinal value
    R=[[0,0,0,0] for i in range(n2+1)]   # create Right list of n1+1 size to add a Sentinal value

    for i in range(0,n1):
        L[i]=Final_list[p+i-1]       # store values from Final_list to left list
    for j in range(0,n2):               
        R[j]=Final_list[q+j]         # store values from Final_list to right list
    #Sentinal values to left and right lists
    L[-1].append(sys.maxsize)
    R[-1].append(sys.maxsize)
    s1=0
    s2=0

    #compare values from left and right lists and sort them in the Final_list
    for k in range(p-1,r):
        if L[s1][-1]<=R[s2][-1]:
            Final_list[k]=L[s1]
            s1+=1
        else:
            Final_list[k]=R[s2]
            s2+=1


def Merge_sort():
    def Merge(Final_list,p,r):
        if p<r:
            q=int((p+r)/2)
            Merge(Final_list,p,q)         #divide and recursive call
            Merge(Final_list,q+1,r)       #divide and recursive call   
            Merge_algo(Final_list,p,q,r)  #compare and conquer recursive call

    input_size=[20,100,2000,6000]
    Input_Filename =["arr20.txt","arr100.txt","arr2000.txt","arr6000.txt"]
    Output_Filename=["arrMR_O_20.txt","arrMR_O_100.txt","arrMR_O_2000.txt","arrMR_O_6000.txt"]
    for inputs in range(0,4):
        Final_list=[]

        # open file name from Input_Filename list in read mode
        Input_file=open(Input_Filename[inputs],"r")
        # Reading Input_Filename text file values generated through Insertion_sort
        li = Input_file.readlines()

        #Converting from strings to Integer values and appending in a list 
        for x in li:
            temp_li=[]
            random=[]
            temp_li = x.split(" ")
            value1,value2,value3=int(temp_li[0]),int(temp_li[1]),int(temp_li[2])
            random.append(value1)
            random.append(value2)
            random.append(value3)
            sum=value1+value2+value3
            random.append(sum)
            Final_list.append(random)
       
        p=1
        r=len(Final_list)
        
        #start time of the algorithm
        Start_Time=timeit.default_timer()

        Merge(Final_list,p,r)        #calling the function

        
        #End time of the algorithm    
        End_Time=timeit.default_timer()

        # open file name from Output_Filename list in write mode
        Output_File=open(Output_Filename[inputs],"w")

        # writing the sorted list into the output files
        for i in range(len(Final_list)):
            for j in range(4):
                Output_File.write(str(Final_list[i][j])+" ")
            Output_File.write("\n")
        
        execution_time =(End_Time-Start_Time)*1000
        
        #Total execution time of the algorithm at different input sizes
        print(f"Total Run Time for {input_size[inputs]} inputs is : {execution_time} ms")
        Output_File.write(str(execution_time)+" "+"ms")
  
Merge_sort()   #calling the function