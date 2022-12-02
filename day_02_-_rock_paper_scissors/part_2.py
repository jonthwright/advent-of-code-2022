#!/usr/bin/env python3

import os


def solution(elements: list[tuple[str, str]]) -> int:
	return sum((ord(elf) + ord(me) - 1) % 3 + 1 + (ord(me) - 88) * 3 for elf, me in elements)


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [tuple(element for element in line.strip().split(' ')) for line in f.readlines()]

	print('Day 02 : Rock Paper Scissors - part 2')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
