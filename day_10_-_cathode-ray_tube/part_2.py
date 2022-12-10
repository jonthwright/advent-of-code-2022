#!/usr/bin/env python3

import os
import re


def create_crt_pixel(cycle: int, register_x: int) -> str:
	return '#' if abs(cycle - register_x) <= 1 else '.'


def solution(elements: list[str]) -> str:
	circuit_ticks = 40
	register_x, instructions = 1, elements
	crt_display_cycle, crt_display, crt_rows = 0, '', 6

	register_cycles = [register_x]

	for instruction in instructions:
		crt_display += create_crt_pixel(crt_display_cycle, register_x)
		crt_display_cycle = (crt_display_cycle + 1) % circuit_ticks

		if value := re.search(r'^addx (-?\d+)$', instruction):
			crt_display += create_crt_pixel(crt_display_cycle, register_x)
			crt_display_cycle = (crt_display_cycle + 1) % circuit_ticks

			register_cycles.append(register_x)
			register_x += int(value.group(1))

		register_cycles.append(register_x)

	return '\n'.join(crt_display[row * circuit_ticks: (row + 1) * circuit_ticks] for row in range(crt_rows))


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		inputs = [line.strip() for line in file.readlines()]

	print('Day 10 : Cathode-Ray Tube - part 2')
	print(f'>>> Answer :')
	print(solution(inputs))


if __name__ == '__main__':
	main()
