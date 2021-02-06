import unittest
import dataclasses as dc
import typing as t
from pathlib import Path
import itertools as iter

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

def mangle_items(items: t.List[t.Tuple[str, str]]) -> t.List[t.Tuple[str, str]]:
    if len(items) == 0:
        return []
    cyclic_iter = iter.cycle(items)
    next(cyclic_iter)
    result: t.List[t.Tuple[str, str]] = []
    for item in items:
        result.append((item[0], next(cyclic_iter)[1]))
    return result



class TestMangleItems(unittest.TestCase):
    def test_three_items(self):
        result: t.List[t.Tuple[str, str]] = mangle_items([("a", "b"),
                                                          ("c", "d"),
                                                          ("e", "f")])
        self.assertEqual(result, [('a', 'd'), ('c', 'f'), ('e', 'b')])

    def test_zero_items(self):
        result: t.List[t.Tuple[str, str]] = mangle_items([])
        self.assertEqual(result, [])

    def test_one_item(self):
        result: t.List[t.Tuple[str, str]] = mangle_items([("a", "b")])
        self.assertEqual(result, [("a", "b")])


def mangle_groups(groups: t.List[Group]) -> t.List[Group]:
    if len(groups) == 0:
        return []
    cyclic_iter = iter.islice(iter.cycle(groups), len(groups) - 1, None)
    result: t.List[Group] = []
    for group in groups:
        result.append(Group(header=group.header, items=next(cyclic_iter).items))
    return result

class TestMangleGroups(unittest.TestCase):
    def test_two_groups(self):
        result: t.List[Group] = mangle_groups([Group(header="h1", items=[("a", "b"), ("1", "2")]),
                                               Group(header="h2", items=[("c", "d"), ("3", "4")])])
        self.assertEqual(result, [Group(header="h1", items=[("c", "d"), ("3", "4")]),
                                  Group(header="h2", items=[("a", "b"), ("1", "2")])])

    def test_zero_groups(self):
        result: t.List[Group] = mangle_groups([])
        self.assertEqual(result, [])

def mangle(groups: t.List[Group]) -> t.List[Group]:
    for group in groups:
        group.items = mangle_items(group.items)
    return mangle_groups(groups)

class TestMangleG(unittest.TestCase):
    def test_two_groups(self):
        result: t.List[Group] = mangle([Group(header="h1", items=[("a", "b"),
                                                                  ("1", "2")]),
                                        Group(header="h2", items=[("c", "d"),
                                                                  ("3", "4")])])
        self.assertEqual(result, [Group(header="h1", items=[("c", "4"), ("3", "d")]),
                                  Group(header="h2", items=[("a", "2"), ("1", "b")])])


def main():
    unittest.main()

main()
