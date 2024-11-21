import timeit

def quick_sort():
    def partition(a,low,high):
         
        idx=low-1         # index variable to create spaces for smallest elements than pivot
        for i in range(low,high):
            if(a[i][-1]<a[high][-1]):   #compare each element with pivot and sort
                idx+=1
                temp=a[idx]
                a[idx]=a[i]
                a[i]=temp
        idx+=1                       # pivot to it's correct index and return
        temp2=a[idx]
        a[idx]=a[high] 
        a[high]=temp2
        return idx

    def qsort(a,low,high):
        if low<high:
            pivot_idx = partition(a,low,high)   # returns  partition index 
            qsort(a,low,pivot_idx-1)     # divide on pivot and recursive call to left
            qsort(a,pivot_idx+1,high)    # divide on pivot and recursive call to right

    input_size=[20,100,2000,6000]
    Input_Filename =["arr20.txt","arr100.txt","arr2000.txt","arr6000.txt"]
    Output_Filename=["arrQK_O_20.txt","arrQK_O_100.txt","arrQK_O_2000.txt","arrQK_O_6000.txt"]
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

        low=0
        high=len(Final_list)-1

        #start time of the algorithm
        Start_Time=timeit.default_timer()

        qsort(Final_list,low,high)   #calling the function

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

quick_sort()  #calling the function
