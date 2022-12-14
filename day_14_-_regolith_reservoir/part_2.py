#!/usr/bin/env python3

import os
from typing import Generator


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


def quicksand(cave_system: set[complex], sand_position: complex = 500 + 0j) -> Generator[complex, None, None]:
	cave_system.add(sand_position)

	down, left, right = 1j, -1, 1
	if (new_sand_position := sand_position + down) not in cave_system:
		yield from quicksand(cave_system, new_sand_position)
	if (new_sand_position := sand_position + left + down) not in cave_system:
		yield from quicksand(cave_system, new_sand_position)
	if (new_sand_position := sand_position + right + down) not in cave_system:
		yield from quicksand(cave_system, new_sand_position)

	yield sand_position


def solution(elements: list[list[complex]]) -> int:
	cave_system, cave_max_depth = create_cave_system(elements), cave_system_max_depth(elements)
	offset = 4

	for horizontal_position in range(500 - cave_max_depth - offset, 500 + cave_max_depth + offset):
		cave_system.add(horizontal_position + (cave_max_depth + offset // 2) * 1j)

	return len(list(quicksand(cave_system)))


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		inputs = [[complex(*[int(e) for e in elem.split(',')]) for elem in line.split(' -> ')] for line in file.readlines()]

	print('Day 14 : Regolith Reservoir - part 2')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
