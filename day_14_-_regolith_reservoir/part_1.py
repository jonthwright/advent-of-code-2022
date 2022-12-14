#!/usr/bin/env python3

import os


def create_cave_system(cave_paths: list[list[complex]]) -> set[complex]:
	cave_system_with_rocks = set()

	for cave_path in cave_paths:
		for position in range(len(cave_path) - 1):
			if cave_path[position].real == cave_path[position + 1].real:
				min_depth = int(min(cave_path[position].imag, cave_path[position + 1].imag))
				max_depth = int(max(cave_path[position].imag, cave_path[position + 1].imag))
				for vertical_position in range(min_depth, max_depth + 1):
					cave_system_with_rocks.add(cave_path[position].real + vertical_position * 1j)
			else:
				max_left = int(min(cave_path[position].real, cave_path[position + 1].real))
				max_right = int(max(cave_path[position].real, cave_path[position + 1].real))
				for horizontal_position in range(max_left, max_right + 1):
					cave_system_with_rocks.add(horizontal_position + cave_path[position].imag * 1j)

	return cave_system_with_rocks


def cave_system_max_depth(cave_paths: list[list[complex]]) -> int:
	max_depth = 0

	for cave_path in cave_paths:
		for cave_position in cave_path:
			max_depth = max(max_depth, int(cave_position.imag))

	return max_depth


def sand_resting_inside_cave_system(cave_system: set[complex], cave_max_depth: int) -> bool:
	sand_position = 500
	abyss_position = 500 + 0j
	down, left, right = 1j, -1 + 1j, 1 + 1j

	while sand_position.imag < cave_max_depth and abyss_position not in cave_system:
		if sand_position + down not in cave_system:
			sand_position += down
		elif sand_position + left not in cave_system:
			sand_position += left
		elif sand_position + right not in cave_system:
			sand_position += right
		else:
			cave_system.add(sand_position)
			return True

	return False


def solution(elements: list[list[complex]]) -> int:
	cave_system, cave_max_depth = create_cave_system(elements), cave_system_max_depth(elements)

	sand_rested_unit = 0
	while sand_resting_inside_cave_system(cave_system, cave_max_depth):
		sand_rested_unit += 1

	return sand_rested_unit


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		inputs = [[complex(*[int(e) for e in elem.split(',')]) for elem in line.split(' -> ')] for line in file.readlines()]

	print('Day 14 : Regolith Reservoir - part 1')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
