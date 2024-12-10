from typing import Iterable, List
from dataclasses import dataclass
from time import time
from pathlib import Path
from tqdm import tqdm
import re

ROOT = Path(__file__).parent

@dataclass
class Node:
    source_start: int
    source_end: int
    destination_start: int
    destination_end: int

class Mapping:
    def __init__(self, starter_list: List) -> None:
        self.name = starter_list[0]
        self.nodes = [self.process_node_string(x) for x in starter_list[1:]]

    def process_node_string(self, node_string: str) -> Iterable:
        destination_start, source_start, range = [int(x.strip()) for x in node_string.split(" ")]
        source_end = source_start + range - 1
        destination_end = destination_start + range - 1
        return Node(source_start, source_end, destination_start, destination_end)        

    def find_mapping(self, source_num: int) -> int:
        for node in self.nodes:
            if source_num >= node.source_start and source_num <= node.source_end:
                diff = source_num - node.source_start
                return node.destination_start + diff
        return source_num

    def sort_mapping(self, key) -> None:
        pass

    def __repr__(self) -> str:
        return f'{self.name}: {self.nodes}'

# def seeds_p2(num_list: str) -> List:
#     seeds_contenders = [int(x) for x in num_list.split(':')[1].strip().split(' ')]
#     seeds = list()
#     for i in range(0, len(seeds_contenders), 2):
#         start = seeds_contenders[i]
#         num_range = seeds_contenders[i+1]
#         temp_list = [i for i in range(start, start+num_range)]
#         seeds.extend(temp_list)
#     # print(seeds)
#     return seeds

def seeds_p2(num_list: str) -> List:
    seeds_contenders = [int(x) for x in num_list.split(':')[1].strip().split(' ')]
    seeds = []
    for start, num_range in tqdm(zip(seeds_contenders[::2], seeds_contenders[1::2])):
        seeds.extend(range(start, start + num_range))
    return seeds


def read_file(file_path: str):
    with open(file_path, 'r') as f:
        data = f.readlines()
    data = [x.strip() for x in data]

    mapping_objects = list()
    new_seeds = seeds_p2(data[0])
    seeds = [int(x) for x in data[0].split(':')[1].strip().split(' ')]
    other = data[2:]
    start = 0
    for i, item in enumerate(other):
        if item == '':
            mapping_objects.append(Mapping(other[start: i]))
            start=i+1
    mapping_objects.append(Mapping(other[start:]))
    
    return new_seeds, seeds, mapping_objects        

def play_game(seed_number, mapping_list):
    for mapping_object in mapping_list:
        # print(f'Checking mapping {mapping_object.name}')
        # print(f'Before: {seed_number}')
        seed_number = mapping_object.find_mapping(seed_number)
        # print(f'After: {seed_number}')
    return seed_number


if __name__ == '__main__':

    print('Making seeds')
    # start=time.time()
    new_seeds, seeds, mapping_list = read_file(ROOT / 'd5.txt')

    print('Trying to solve part 1:')
    locations = list()
    for seed_number in tqdm(seeds):
        location = play_game(seed_number, mapping_list)
        # print(f'Location for {seed_number} is {location}')
        locations.append(location)
    print(f'Final answer part 1: {min(locations)}')

    print('Now trying to solve part 2:')
    locations = list()
    for seed_number in tqdm(new_seeds):
        location = play_game(seed_number, mapping_list)
        # print(f'Location for {seed_number} is {location}')
        locations.append(location)
    print(f'Final answer part 2: {min(locations)}')