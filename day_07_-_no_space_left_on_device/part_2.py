#!/usr/bin/env python3

import os
import re
from collections import defaultdict


def find_directory_sizes(commands: list[str]) -> defaultdict[str, int]:
	directory_sizes, directory_stack = defaultdict(int), []

	for command in commands:
		if command == '$ cd /':
			directory_stack.append('/')
		elif command == '$ cd ..':
			directory_stack.pop()
		elif change_directory := re.match(r'^\$ cd (\w+)$', command):
			directory_stack.append(change_directory.group(1))
		# elif command == '$ ls':
		# 	continue
		elif directory_size_regex := re.match(r'^(\d+) .+$', command):
			current_directory = ''
			for directory in directory_stack:
				current_directory = os.path.join('/', current_directory, directory).replace('\\', '/')
				directory_sizes[current_directory] += int(directory_size_regex.group(1))

	return directory_sizes


def solution(elements: list[str]) -> int:
	total_disk_space = 70000000
	minimum_unused_space = 30000000

	directory_sizes = find_directory_sizes(elements)
	root_directory_size = directory_sizes.get('/', 0)
	required_space = minimum_unused_space - (total_disk_space - root_directory_size)

	return min(size for size in directory_sizes.values() if size >= required_space)


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		inputs = [line.strip() for line in file.readlines()]

	print('Day 07 : No Space Left On Device - part 2')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
