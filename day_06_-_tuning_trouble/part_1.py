#!/usr/bin/env python3

import os


def solution(element: str) -> int:
	packet_size = packet_index = 4

	for i in range(len(element) - packet_size):
		if len(set(element[i: i + packet_size])) == packet_size:
			return packet_index
		packet_index += 1

	return -1


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		inputs = file.read().strip()

	print('Day 06 : Tuning Trouble - part 1')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
