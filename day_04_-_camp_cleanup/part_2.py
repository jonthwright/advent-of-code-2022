#!/usr/bin/env python3

import os


def elf_section_assignments_overlaps(elf_section_id_one: tuple[int, int], elf_section_id_two: tuple[int, int]) -> bool:
	return min(elf_section_id_two) <= max(elf_section_id_one) and min(elf_section_id_one) <= max(elf_section_id_two)


def solution(elements: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
	return sum(elf_section_assignments_overlaps(*elf_sections_pair) for elf_sections_pair in elements)


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		inputs = [tuple(tuple(int(elem) for elem in row.split('-')) for row in line.strip().split(',')) for line in file.readlines()]

	print('Day 04 : Camp Cleanup - part 2')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
