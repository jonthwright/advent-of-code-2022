#!/usr/bin/env python3

import os


def solution(elements: list[list[int]]) -> int:
	return max(sum(elf_calories) for elf_calories in elements)


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [[int(line.strip()) for line in block.split()] for block in f.read().split('\n\n')]

	print('Day 01 : Calorie Counting - part 1')
	print(f'>>> Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()
