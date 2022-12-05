#!/usr/bin/env python3

import os
import re
from collections import defaultdict, deque


def solution(sets: dict[int, list[str]], elements: list[tuple[str, str, str]]) -> int:
	for amount, source, destination in elements:
		moving_deque = deque()

		for _ in range(amount):
			moving_deque.append(sets[source].pop())
		for _ in range(amount):
			sets[destination].append(moving_deque.pop())

	return ''.join(sets[i].pop() for i in range(1, max(sets) + 1))


def parse_inputs(inputs: str) -> tuple[dict[int, list[str]], list[tuple[str, str, str]]]:
	input_data_sets, input_elements = inputs.split('\n\n')
	*inputs_sets, input_row = input_data_sets.split('\n')

	data_sets = defaultdict(deque)
	max_sets_size = max(int(size) for size in re.split(r'\s+', input_row) if size.isnumeric())
	inputs_line_regex = ' '.join(['.(.).'] * max_sets_size)

	for input_line in inputs_sets:
		line_regex = re.search(inputs_line_regex, input_line)

		assert line_regex, 'Could not find line inputs for stacks to parse!'

		for i, character in enumerate(line_regex.groups(), 1):
			if character.isalpha():
				data_sets[i].appendleft(character)

	data_elements = []
	for element in input_elements.strip().split('\n'):
		instruction_regex = re.findall(r'(\d+)', element)

		assert instruction_regex, 'Could not parse of inputs!'
		assert len(instruction_regex) == 3, 'Could not parse for the right number of inputs!'

		data_elements.append(tuple(int(elem) for elem in instruction_regex))

	return data_sets, data_elements


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		sets, elements = parse_inputs(file.read())

	print('Day 05 : Supply Stacks - part 2')
	print(f'>>> Answer : {solution(sets, elements)}')


if __name__ == '__main__':
	main()
