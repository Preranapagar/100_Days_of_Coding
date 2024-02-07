import pandas as pd
import numpy as np

def create_matrics(nums):
    
    result = np.array(nums).reshape(3,3)
    print(result)

def main():
    
    list1 = [1,2,3,4,5,6,7,8,9]

    create_matrics(list1)


if __name__=='__main__':
    main()