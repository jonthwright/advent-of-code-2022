#!/usr/bin/env python3

import operator
import os
import re
from collections import deque
from heapq import heapify, heappop
from math import prod


class Monkey:
	def __init__(self, raw_monkey_input: str):
		raw_monkey = raw_monkey_input.split('\n')
		self.item_worry_levels = deque(int(item) for item in raw_monkey[1].replace('  Starting items: ', '').split(', '))

		operation_regex = re.match(r'^\s*Operation: new = old (.) .+$', raw_monkey[2])
		operation = operator.mul if operation_regex.groups(1)[0] == '*' else operator.add
		operand_regex = re.match(r'^\s*Operation: new = old . (\d+)$', raw_monkey[2])
		self.worry_level_test = lambda old: operation(old, int(operand_regex.groups(1)[0]) if operand_regex else old)

		self.monkey_divisor = int(raw_monkey[3].replace('  Test: divisible by ', ''))
		self.target_worry_passed = int(raw_monkey[4].replace('    If true: throw to monkey ', ''))
		self.target_worry_failed = int(raw_monkey[5].replace('    If false: throw to monkey ', ''))
		self.inspections_made = 0

	def make_inspection(self) -> tuple[int, int]:
		self.inspections_made += 1

		item_worry_level = self.worry_level_test(self.item_worry_levels.popleft())
		item_bored_worry_level = self.boredom_level(item_worry_level)

		passed_test = item_bored_worry_level % self.monkey_divisor == 0
		monkey_dest = passed_test * self.target_worry_passed + (not passed_test) * self.target_worry_failed

		return monkey_dest, item_bored_worry_level

	@staticmethod
	def boredom_level(worry_level: int) -> int:
		return worry_level // 3

	@staticmethod
	def monkey_business_level(monkeys: list['Monkey'], number_of_monkeys: int = 2) -> int:
		monkeys_copy = monkeys.copy()
		heapify(monkeys_copy)

		return prod(heappop(monkeys_copy).inspections_made for _ in range(number_of_monkeys))

	def __lt__(self, other: 'Monkey') -> bool:
		return self.inspections_made > other.inspections_made

	def __eq__(self, other: 'Monkey') -> bool:
		return self.inspections_made == other.inspections_made

	def __gt__(self, other: 'Monkey') -> bool:
		return self.inspections_made < other.inspections_made


def solution(elements: list[Monkey]) -> int:
	monkeys, stuff_slinging_simian_shenanigans_rounds = elements, 20

	for _ in range(stuff_slinging_simian_shenanigans_rounds):
		for current_monkey in range(len(monkeys)):
			while monkeys[current_monkey].item_worry_levels:
				destination_monkey, monkey_item = monkeys[current_monkey].make_inspection()
				monkeys[destination_monkey].item_worry_levels.append(monkey_item)

	return Monkey.monkey_business_level(monkeys)


def main():
	aoc_day_loc = os.path.dirname(__file__)

	with open(os.path.join(aoc_day_loc, 'inputs.txt'), 'r') as file:
		inputs = [Monkey(monkey) for monkey in file.read().strip().split('\n\n')]

	print('Day 11 : Monkey in the Middle - part 1')
	print(f'>>> Answer : {solution(inputs)}')


if __name__ == '__main__':
	main()
