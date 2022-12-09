#!/usr/bin/env python3

import os


def validate_tree_location(new_tree: complex, map_height: int, map_width: int) -> bool:
	return 0 < new_tree.real < map_height - 1 and 0 < new_tree.imag < map_width - 1


def interior_scenic_score(trees_map: list[list[int]], tree_row: int, tree_col: int) -> int:
	tree_height = trees_map[tree_row][tree_col]
	map_height, map_width = len(trees_map), len(trees_map[tree_row])
	original_tree_location = complex(tree_row, tree_col)

	neighbouring_trees = [1j, 1, -1, -1j]

	scenic_score = 1

	for offset in neighbouring_trees:
		tree_loc = original_tree_location
		distance_until_blocked = 0

		while 0 < tree_loc.real < map_height - 1 and 0 < tree_loc.imag < map_width - 1:
			tree_loc += offset
			distance_until_blocked += 1

			is_valid_location = validate_tree_location(tree_loc, map_height, map_width)
			if is_valid_location and trees_map[int(tree_loc.real)][int(tree_loc.imag)] >= tree_height:
				break

		scenic_score *= distance_until_blocked

	return scenic_score


def solution(elements: list[list[int]]) -> int:
	return max(interior_scenic_score(elements, i, j) for i in range(len(elements)) for j in range(len(elements[i])))


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		inputs = [[int(elem) for elem in line.strip()] for line in file.readlines()]

	print('Day 08 : Treetop Tree House - part 2')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
