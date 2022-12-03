#!/usr/bin/env python3

import os


def rucksack_group_priority(rucksack_group: list[set[str]]) -> int:
	priority_set = set.intersection(*rucksack_group)

	assert priority_set, 'No priority letters found!'
	assert len(priority_set) == 1, 'More than one priority letters found!'

	priority_letter = priority_set.pop()
	lower_priority_score = priority_letter.islower() * (ord(priority_letter) - ord('a') + 1)
	upper_priority_score = priority_letter.isupper() * (ord(priority_letter) - ord('A') + 27)

	return lower_priority_score + upper_priority_score


def solution(elements: list[set[str]]) -> int:
	group_size = 3
	return sum(
		rucksack_group_priority(elements[group * group_size: group * group_size + group_size])
		for group in range(len(elements) // group_size)
	)


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'input_file.txt'), 'r') as f:
		inputs = [set(line.strip()) for line in f.readlines()]

	print('Day 03 : Rucksack Reorganization - part 2')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
