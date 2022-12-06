#!/usr/bin/env python3

import os


def solution(element: str) -> int:
	pass


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		inputs = file.read().strip()

	print('Day 07 : *** - part 1')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
