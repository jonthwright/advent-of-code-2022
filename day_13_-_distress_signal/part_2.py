#!/usr/bin/env python3

import os


def compare_distress_signals(packets_one: list | int, packets_two: list | int) -> int:
	if isinstance(packets_one, int) and isinstance(packets_two, int):
		return (packets_one < packets_two) - (packets_one > packets_two)

	if isinstance(packets_one, int):
		packets_one = [packets_one]

	if isinstance(packets_two, int):
		packets_two = [packets_two]

	for i in range(min(len(packets_one), len(packets_two))):
		if worked_out_signal := compare_distress_signals(packets_one[i], packets_two[i]):
			return worked_out_signal

	return (len(packets_one) < len(packets_two)) - (len(packets_one) > len(packets_two))


def solution(elements: list) -> int:
	divider_one, divider_two = [[2]], [[6]]
	lesser_than_divider_one = len([signal for signal in elements if compare_distress_signals(signal, divider_one) > 0])
	greater_than_divider_two = len([signal for signal in elements if compare_distress_signals(divider_two, signal) > 0])

	divider_one_index = lesser_than_divider_one + 1
	divider_two_index = len(elements) - greater_than_divider_two + 2
	decoder_key = divider_one_index * divider_two_index

	return decoder_key


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		raw_data_chunks = [line.strip().split('\n') for line in file.read().split('\n\n')]
		inputs = [eval(partial_data_chunk) for data_chucks in raw_data_chunks for partial_data_chunk in data_chucks]

	print('Day 13 : Distress Signal - part 2')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
