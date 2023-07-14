from typing import List

def get_list_input(file_name: str) -> List[str]:
    with open(file_name, 'r') as f:
        return f.readlines()

def get_list_int_input(file_name: str) -> List[str]:
    with open(file_name, 'r') as f:
        return [int(a) for a in f.readlines()]

def get_grid_int_input(file_name: str) -> List[List[int]]:
    with open(file_name, 'r') as f:
        lst = f.readlines()
        clean_lst = [chr.replace("\n","") for chr in lst]
        return [[int(chr) for chr in arr_elem] for arr_elem in clean_lst]