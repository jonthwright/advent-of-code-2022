#!/usr/bin/env python3

import os


def elf_section_assignments_fully_contain(elf_id_one: tuple[int, int], elf_id_two: tuple[int, int]) -> bool:
	def fully_contain(section_id_one: tuple[int, int], section_id_two: tuple[int, int]) -> bool:
		return min(section_id_one) <= min(section_id_two) and max(section_id_two) <= max(section_id_one)

	return fully_contain(elf_id_one, elf_id_two) or fully_contain(elf_id_two, elf_id_one)


def solution(elements: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
	return sum(elf_section_assignments_fully_contain(*elf_section_pair) for elf_section_pair in elements)


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'rb') as file:
		print(file.readlines())
		inputs = []

	print('Day 04 : Camp Cleanup - part 1')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
