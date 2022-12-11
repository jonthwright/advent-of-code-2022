#!/usr/bin/env python3

import math
import operator
import os
import re
from heapq import heapify, heappop


class Monkey:
	def __init__(self, raw_monkey_input: str):
		raw_monkey = raw_monkey_input.split('\n')
		self.items = [int(item) for item in raw_monkey[1].replace('  Starting items: ', '').split(', ')]

		operation_regex = re.search(r'^\s*Operation: new = old (.) .+$', raw_monkey[2])
		operation = operator.mul if operation_regex.groups(1)[0] == '*' else operator.add
		operand_regex = re.search(r'^\s*Operation: new = old . (\d+)$', raw_monkey[2])
		self.monkey_worry_level = lambda old: operation(old, int(operand_regex.groups(1)[0]) if operand_regex else old)

		self.monkey_divisor = int(raw_monkey[3].replace('  Test: divisible by ', ''))
		self.monkey_throw_true = int(raw_monkey[4].replace('    If true: throw to monkey ', ''))
		self.monkey_throw_false = int(raw_monkey[5].replace('    If false: throw to monkey ', ''))
		self.inspections = 0

	def make_inspection(self, lowest_common_divisor: int) -> tuple[int, int]:
		self.inspections += 1
		self.items[0] = self.boredom_level(self.monkey_worry_level(self.items[0]), lowest_common_divisor)
		monkey_dest = self.monkey_throw_true if self.items[0] % self.monkey_divisor == 0 else self.monkey_throw_false
		return monkey_dest, self.items.pop(0)

	@staticmethod
	def boredom_level(worry_level: int, lowest_common_divisor: int) -> int:
		return worry_level % lowest_common_divisor

	@staticmethod
	def monkey_business(monkeys: list['Monkey']) -> int:
		monkeys_copy = monkeys.copy()
		heapify(monkeys_copy)
		return heappop(monkeys_copy).inspections * heappop(monkeys_copy).inspections

	def __lt__(self, other: 'Monkey') -> bool:
		return self.inspections > other.inspections

	def __eq__(self, other: 'Monkey') -> bool:
		return self.inspections == other.inspections

	def __gt__(self, other: 'Monkey') -> bool:
		return self.inspections < other.inspections


def solution(elements: list[Monkey]) -> int:
	monkeys = elements
	number_of_turns = 10000

	lowest_common_divisor = math.lcm(*(monkey.monkey_divisor for monkey in monkeys))

	for _ in range(number_of_turns):
		for current_monkey in range(len(monkeys)):
			while monkeys[current_monkey].items:
				destination_monkey, monkey_item = monkeys[current_monkey].make_inspection(lowest_common_divisor)
				monkeys[destination_monkey].items.append(monkey_item)

	return Monkey.monkey_business(monkeys)


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		inputs = [Monkey(monkey) for monkey in file.read().strip().split('\n\n')]

	print('Day 11 : Monkey in the Middle - part 2')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
