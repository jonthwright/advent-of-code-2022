#!/usr/bin/env python3

import os
import re


def solution(elements: list[str]) -> int:
	circuit_cycle, circuit_ticks, max_cycle = 20, 40, 220
	register_x, instructions = 1, elements
	register_cycles = [register_x]

	for instruction in instructions:
		if value := re.search(r'^addx (-?\d+)$', instruction):
			register_cycles.append(register_x)
			register_x += int(value.group(1))
		register_cycles.append(register_x)

	return sum(cycle * register_cycles[cycle - 1] for cycle in range(circuit_cycle, max_cycle + 1, circuit_ticks))


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		inputs = [line.strip() for line in file.readlines()]

	print('Day 10 : Cathode-Ray Tube - part 1')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
