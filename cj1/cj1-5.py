import numpy as np
import math 

def gen_sine_table(start, end, num_entries):
    x = np.linspace(start, end, num_entries)
    sin_x = np.sin(x)
    table = np.column_stack((x, sin_x))
    return table

def main():
    start = 0
    end = math.pi
    num_entries = 1000
    sine_table = gen_sine_table(start, end, num_entries)
    
    print("x\t\t  sin(x)")
    for row in sine_table:
        x, sin_x = row
        print(f"{x:.3f}\t  {sin_x:.3f}")

if __name__ == "__main__":
    main()