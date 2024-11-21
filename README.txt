#Running a python script for sorting Insertion, merge and quick sort algorithms through Visual Studio Code.

This code generates a set of 3 random integers between 0 to 99 of input sizes 20,100,2000 and 6000 and saves it in input files arr20.txt, arr100.txt, arr2000.txt, and arr6000 through a function called generate random() in Insertion.py.
We read the same file and compute the sum of each row and sort by the sum in the last column by displaying it in the ascending order and store it in Output files.(Same goes in Merge_sort.py and quick_sort.py)

#prerequisites
Make sure these are installed on your system

Visual Studio Code : Download and Install VS code from [https://code.visualstudio.com/]
Python             : Download and Install Python from [https://www.python.org/downloads/]
System properties > Advanced > Environment Variables > add the path of python file
Python Extension   :  Install the python extension code by Microsoft(Eligible for vesions python >=3.7)

#Open the project in vs code
File > Open Folder > /path/to/yourproject

(Optional)
#To isolate dependencies create a Virtual Environment using the terminal
python -m venv venv
venv\Scripts\activate

On mac and linux to activate  source venv/bin/activate

Environment dependencies:

Python      : Version 3.8 and above
Interpreter : 3.8.10 64 bit(Microsoft) 
System Requirements: This can run on any operating system but it should follow the above steps mentioned.
random and timeit libraries are inbuilt in python 3.8 version, no need to install or upgrade it.
To install External dependencies use pip install in integrated terminal.

# To run the python script
Open the integrated terminal in the vs code  
view > terminal
python Insertion_Sort.py
python Merge_sort.py
python quick_sort.py