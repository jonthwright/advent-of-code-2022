#!/usr/bin/env python3

import os
from heapq import heapify, heappop


def solution(elements: list[int]) -> int:
	elves_calories = [sum(elf_calories) * -1 for elf_calories in elements]
	heapify(elves_calories)

	three_largest_elves_sum = 0
	for _ in range(3):
		three_largest_elves_sum += heappop(elves_calories)
	
	return three_largest_elves_sum * -1


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [[int(line.strip()) for line in block.split()] for block in f.read().split('\n\n')]

	print('Day 01 : Calorie Counting - part 2')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
