#!/usr/bin/env python3

import os


def elf_assignments_overlaps(elf_assignment_one: tuple[int, int], elf_assignment_two: tuple[int, int]) -> bool:
	return min(elf_assignment_two) <= max(elf_assignment_one) and min(elf_assignment_one) <= max(elf_assignment_two)


def solution(elements: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
	return sum(elf_assignments_overlaps(*elf_assignments) for elf_assignments in elements)


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		inputs = [tuple(tuple(int(elem) for elem in row.split('-')) for row in line.split(',')) for line in file.readlines()]

	print('Day 04 : Camp Cleanup - part 2')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
