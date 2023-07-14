import os
from typing import List
from utils.advent_of_code_utils import get_grid_int_input
import numpy as np

def main():
    file_name=f'{os.getcwd()}/inputs/input_d3.txt'
    grid = get_grid_int_input(file_name)
    
    t_grid = transpose(grid)
    gamma_list = [most_frequent_in_list(row) for row in t_grid]
    gamma_str = "".join(map(str,gamma_list))
    epsilon_str = "".join([str((val+1)%2) for val in gamma_list])
    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str, 2)
    print("solution 1", gamma*epsilon)
    

def transpose(grid: List[List[int]]) -> int:
    return np.array(grid).T.tolist()

def most_frequent_in_list(lst: List[int]) -> int:
    return max(set(lst), key=lst.count)


if __name__ == '__main__':
    main()
