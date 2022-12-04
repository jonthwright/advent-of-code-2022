#!/usr/bin/env python3

import os


def rucksack_priority(rucksack: str) -> int:
	half_rucksack_point = len(rucksack) // 2
	priority_set = set(rucksack[: half_rucksack_point]) & set(rucksack[half_rucksack_point:])

	assert priority_set, 'No priority letters found!'
	assert len(priority_set) == 1, 'More than one priority letters found!'

	priority_letter = priority_set.pop()
	lower_priority_score = priority_letter.islower() * (ord(priority_letter) - ord('a') + 1)
	upper_priority_score = priority_letter.isupper() * (ord(priority_letter) - ord('A') + 27)

	return lower_priority_score + upper_priority_score


def solution(elements: list[str]) -> int:
	return sum(rucksack_priority(rucksack) for rucksack in elements)


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		inputs = [line.strip() for line in file.readlines()]

	print('Day 03 : Rucksack Reorganization - part 1')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
