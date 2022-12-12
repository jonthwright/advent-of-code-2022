#!/usr/bin/env python3

import os
from collections import deque


def valid_hill_position(position: complex, width: int, height: int) -> bool:
	return 0 <= int(position.real) < width and 0 <= int(position.imag) < height


def find_start_and_end_positions(hill_elevations: list[list[str]]) -> tuple[complex, complex]:
	starting_position = ending_position = None

	for row in range(len(hill_elevations)):
		for col in range(len(hill_elevations[row])):
			if hill_elevations[row][col] == 'S':
				starting_position = complex(row, col)
				hill_elevations[row][col] = 'a'
			if hill_elevations[row][col] == 'E':
				ending_position = complex(row, col)
				hill_elevations[row][col] = 'z'

	if starting_position is None:
		raise Exception('Cannot find the starting position S in the elevation hills map')

	if ending_position is None:
		raise Exception('Cannot find the ending position E in the elevation hills map')

	return starting_position, ending_position


def solution(elements: list[list[str]]) -> int | None:
	hill_elevations = elements
	width, height = len(hill_elevations), len(hill_elevations[0])

	starting_position, ending_position = find_start_and_end_positions(hill_elevations)
	hills_frontier, seen_hill_elevations = deque([(starting_position, 0)]), {starting_position}

	elevation_neighbour_offsets = (-1, 1, -1j, 1j)

	while hills_frontier:
		current_hill, current_step_cost = hills_frontier.popleft()

		if current_hill == ending_position:
			return current_step_cost

		current_hill_elevation = ord(hill_elevations[int(current_hill.real)][int(current_hill.imag)])

		for hill_position_offset in elevation_neighbour_offsets:
			neighbour_hill = current_hill + hill_position_offset
			valid_neighbour_hill = valid_hill_position(neighbour_hill, width, height)

			if neighbour_hill not in seen_hill_elevations and valid_neighbour_hill:
				neighbour_hill_elevation = ord(hill_elevations[int(neighbour_hill.real)][int(neighbour_hill.imag)])
				if neighbour_hill_elevation - current_hill_elevation <= 1:
					hills_frontier.append((neighbour_hill, current_step_cost + 1))
					seen_hill_elevations.add(neighbour_hill)

	return None


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		inputs = [list(line.strip()) for line in file.readlines()]

	print('Day 12 : Hill Climbing Algorithm - part 1')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
