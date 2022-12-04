#!/usr/bin/env python3

import os
from heapq import heapify, heappop


class Elf:
	def __init__(self, calories: list[int]):
		self.calories_consumed = sum(calories)

	def __lt__(self, other: 'Elf') -> bool:
		return self.calories_consumed > other.calories_consumed

	def __eq__(self, other: 'Elf') -> bool:
		return self.calories_consumed == other.calories_consumed

	def __gt__(self, other: 'Elf') -> bool:
		return self.calories_consumed < other.calories_consumed


def solution(elements: list[list[int]]) -> int:
	elves_calories = [Elf(elf_calories) for elf_calories in elements]
	heapify(elves_calories)

	return sum(heappop(elves_calories).calories_consumed for _ in range(3))


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as file:
		inputs = [[int(line.strip()) for line in block.split()] for block in file.read().split('\n\n')]

	print('Day 01 : Calorie Counting - part 2')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
