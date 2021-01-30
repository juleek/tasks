import dataclasses as dc
import typing as t
from pathlib import Path

def read_file(path: Path) -> t.Generator[str, None, None]:
    with open(path) as file:
        for line in file:
            yield line


@dc.dataclass
class Group:
    header: str = ""
    items: t.List[t.Tuple[str, str]] = dc.field(default_factory=list) # []

def parse(text: t.Iterable[str]) -> t.List[Group]:
    def is_header(line: str) -> bool:
        return ' ' not in line
    def is_item(line: str) -> bool:
        return ' ' in line
    group: Group = Group()
    result: t.List[Group] = []

    def add_if_not_empty(group: Group) -> None:
        if len(group.header) == 0:
            return
        result.append(group)

    for line in text:
        if is_header(line):
            add_if_not_empty(group)
            group = Group()
            group.header = line
        elif is_item(line):
            t: t.Tuple[str, str] = tuple(line.split())
            assert len(t) == 2
            group.items.append(t)
    add_if_not_empty(group)
    return result

import unittest
class TestParsing(unittest.TestCase):
    def test_empty(self):
        result: t.List[Group] = parse("")
        self.assertEqual(len(result), 0)

    def test_empty_group(self):
        result: t.List[Group] = parse("h1\n".split("\n"))
        self.assertEqual(len(result), 1)
        expected: Group = Group(header="h1", items=[])
        self.assertEqual(result[0], expected)

    def test_one_non_empty_group(self):
        result: t.List[Group] = parse("h1\n" \
                                      "a b\n" \
                                      "c d".split("\n"))
        self.assertEqual(len(result), 1)
        expected: Group = Group(header="h1", items=[("a", "b"), ("c", "d")])
        self.assertEqual(result[0], expected)

    def test_two_groups(self):
        result: t.List[Group] = parse("h1\n" \
                                      "a b\n" \
                                      "c d\n"
                                      "\n"
                                      "h2\n"
                                      "k g\n"
                                      "f r\n"
                                      "\n".split("\n"))
        self.assertEqual(len(result), 2)
        expected1: Group = Group(header="h1", items=[("a", "b"), ("c", "d")])
        expected2: Group = Group(header="h2", items=[("k", "g"), ("f", "r")])
        self.assertEqual(result[0], expected1)
        self.assertEqual(result[1], expected2)


def main():
    unittest.main()

main()
