import os
from typing import List
import numpy as np

def get_input(file_name: str) -> List:
    with open(file_name, 'r') as f:
        return f.readlines()

def solution(list_of_dirs: List, part)->int:
    horizontal = 0
    vertical=0
    aim = 0
    for line in list_of_dirs:
        
        dir, val = line.split(" ")
        val = int(val)
        if dir =='forward':
            horizontal+=val
            if part ==2 : 
                vertical+=aim*val
        elif dir == 'down':
            if part ==1:
                vertical+=val
            aim +=val
        elif dir =='up':
            if part==1:
                vertical-=val
            aim-=val
            
    return horizontal*vertical
        
def main():
    file_name=f'{os.getcwd()}/day2/input.txt'
    lines = get_input(file_name)
    
    print(solution(lines,1))
    print(solution(lines,2))
        
    

if __name__ == '__main__':
    main()
