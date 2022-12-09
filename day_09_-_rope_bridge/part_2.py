#!/usr/bin/env python3

import os


def tail_is_touching_heading(head_knot: complex, tail_knot: complex) -> bool:
	return abs(head_knot.real - tail_knot.real) <= 1 and abs(head_knot.imag - tail_knot.imag) <= 1


def tail_displacement(head_knot: complex, tail_knot: complex) -> complex:
	vertical_displacement = (head_knot.real > tail_knot.real) - (head_knot.real < tail_knot.real)
	horizontal_displacement = (head_knot.imag > tail_knot.imag) - (head_knot.imag < tail_knot.imag)

	return complex(vertical_displacement, horizontal_displacement)


def solution(elements: list[tuple[str, int]]) -> int:
	directional_displacement_dict = {'U': 1j, 'D': -1j, 'L': -1, 'R': 1}
	knot_locations = [0j for _ in range(10)]

	tail_knot_locations_visited = set()

	for direction, steps in elements:
		for _ in range(steps):
			knot_locations[0] += directional_displacement_dict[direction]

			for knot in range(len(knot_locations) - 1):
				if not tail_is_touching_heading(knot_locations[knot], knot_locations[knot + 1]):
					knot_locations[knot + 1] += tail_displacement(knot_locations[knot], knot_locations[knot + 1])

					if knot == len(knot_locations) - 2:
						tail_knot_locations_visited.add(knot_locations[knot + 1])

	return len(tail_knot_locations_visited)


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		raw_data = [line.strip().split() for line in file.readlines()]
		inputs = [(elem1, int(elem2)) for elem1, elem2 in raw_data]

	print('Day 09 : Rope Bridge - part 2')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
