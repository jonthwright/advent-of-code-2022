#!/usr/bin/env python3

import os


def validate_tree_location(new_tree_row: int, new_tree_col: int, map_height: int, map_width: int) -> bool:
	return 0 <= new_tree_row < map_height and 0 <= new_tree_col < map_width


def count_visible_tree_houses(trees_map: list[list[int]], tree_row: int, tree_col: int) -> bool:
	tree_height = trees_map[tree_row][tree_col]
	map_height, map_width = len(trees_map), len(trees_map[0])
	original_tree_location = (tree_row, tree_col)

	neighbouring_trees = [(0, 1), (1, 0), (-1, 0), (0, -1)]
	visible_from_outside = False

	for y_offset, x_offset in neighbouring_trees:
		tree_row, tree_col = original_tree_location

		while 0 <= tree_row < map_height and 0 <= tree_col < map_width:
			tree_row, tree_col = tree_row + y_offset, tree_col + x_offset

			if not validate_tree_location(tree_row, tree_col, map_height, map_width):
				visible_from_outside = True
			elif trees_map[tree_row][tree_col] >= tree_height:
				break

	return visible_from_outside


def solution(elements: list[list[int]]) -> int:
	return sum(count_visible_tree_houses(elements, i, j) for i in range(len(elements)) for j in range(len(elements[i])))


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		inputs = [[int(elem) for elem in line.strip()] for line in file.readlines()]

	print('Day 08 : Treetop Tree House - part 1')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
