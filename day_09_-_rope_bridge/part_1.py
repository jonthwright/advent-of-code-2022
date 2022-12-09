#!/usr/bin/env python3

import os


def tail_is_touching_heading(head_knot: complex, tail_knot: complex) -> bool:
	return abs(head_knot.real - tail_knot.real) <= 1 and abs(head_knot.imag - tail_knot.imag) <= 1


def tail_displacement(head_knot: complex, tail_knot: complex) -> complex:
	vertical_displacement = (head_knot.real - tail_knot.real > 0) - (head_knot.real - tail_knot.real < 0)
	horizontal_displacement = (head_knot.imag - tail_knot.imag > 0) - (head_knot.imag - tail_knot.imag < 0)

	return complex(vertical_displacement, horizontal_displacement)


def solution(elements: list[tuple[str, int]]) -> int:
	displacement_dict = {'U': 1j, 'D': -1j, 'L': -1, 'R': 1}
	head_knot_loc, tail_knot_loc = 0j, 0j

	tail_knot_locs_visited = set()

	for direction, steps in elements:
		for _ in range(steps):
			head_knot_loc += displacement_dict[direction]

			if not tail_is_touching_heading(head_knot_loc, tail_knot_loc):
				tail_knot_loc += tail_displacement(head_knot_loc, tail_knot_loc)
				tail_knot_locs_visited.add(tail_knot_loc)

	return len(tail_knot_locs_visited)


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		raw_data = [line.strip().split() for line in file.readlines()]
		inputs = [(elem1, int(elem2)) for elem1, elem2 in raw_data]

	print('Day 09 : Rope Bridge - part 1')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
