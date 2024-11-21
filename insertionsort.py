import random
import timeit

def generate_random():

    input_size=[20,100,2000,6000]
    Input_Filename =["arr20.txt","arr100.txt","arr2000.txt","arr6000.txt"]
    Output_Filename=["arrIS_O_20.txt","arrIS_O_100.txt","arrIS_O_2000.txt","arrIS_O_6000.txt"]
    for inputs in range(4):
        Final_list=[]

        #Generating random integer values for different size inputs of range (0,99) 
        for values in range(input_size[inputs]):

            random_list=[]
            value1,value2,value3=random.randint(0,99),random.randint(0,99),random.randint(0,99)
            random_list.append(value1)
            random_list.append(value2)
            random_list.append(value3)
            Final_list.append(random_list)

        # open file name from Input_Filename list in write mode
        Input_file = open(Input_Filename[inputs],"w")

        # writing the random values generated in the list into the input files
        for i in range(len(Final_list)):
            for j in range(3):
                Input_file.write(str(Final_list[i][j])+' ')
            Input_file.write('\n')

def insertion_sort():
    
    generate_random()
    input_size=[20,100,2000,6000]
    Input_Filename =["arr20.txt","arr100.txt","arr2000.txt","arr6000.txt"]
    Output_Filename=["arrIS_O_20.txt","arrIS_O_100.txt","arrIS_O_2000.txt","arrIS_O_6000.txt"]
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
            sum=value1+value2+value3
            random.append(value1)
            random.append(value2)
            random.append(value3)
            random.append(sum)
            Final_list.append(random)

        
        #start time of the algorithm
        Start_Time=timeit.default_timer()

        #insertion_sort algorithm
        for i in range(1,len(Final_list)):
            key=Final_list[i]
            j=i-1
            while j>=0 and Final_list[j][3]>key[3]:
                Final_list[j+1]=Final_list[j]
                j-=1
            Final_list[j+1] = key

        
        #End time of the algorithm    
        End_Time=timeit.default_timer()

        # open file name from Output_Filename list in write mode
        Output_file = open(Output_Filename[inputs],"w")
        # writing the sorted list into the output files 
        for i in range(len(Final_list)):
            for j in range(4):
                Output_file.write(str(Final_list[i][j])+' ')    
            Output_file.write('\n')

        execution_time =(End_Time-Start_Time)*1000
        
        #Total execution time of the algorithm at different input sizes
        print(f"Total Run Time for {input_size[inputs]} inputs is : {execution_time} ms")

        Output_file.write(str(execution_time)+" "+"ms")

insertion_sort()     # calling the function