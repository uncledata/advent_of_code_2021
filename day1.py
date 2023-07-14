import os
from typing import List
import numpy as np
from utils.advent_of_code_utils import get_list_input

def solution(list_of_ints:List, length:int)-> int:
    cnt = 0
    zipped = np.lib.stride_tricks.sliding_window_view(np.array(list_of_ints), window_shape=length)[::1]
    for i in range(zipped.shape[0]-1):
        if sum(zipped[i])<sum(zipped[i+1]):
            cnt+=1
    return cnt

def main():
    file_name=f'{os.getcwd()}/inputs/input_d1.txt'
    lines = get_list_input(file_name)
    
    list_of_ints = [int(a) for a in lines]
    
    print(solution(list_of_ints,1))
    print(solution(list_of_ints,3))

if __name__ == '__main__':
    main()
