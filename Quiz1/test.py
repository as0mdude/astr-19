import numpy as np

def main():

  #define a filename

  fname = 'numpy_data_hw3.txt'

  #read the file using loadtxt

  a = np.loadtxt(fname)

  #print some information

  print(a[0,1]/a[1,1])

#run the program

if __name__=="__main__":

  main()