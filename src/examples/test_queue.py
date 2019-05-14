from string import ascii_letters
from hypothesis._strategies import text
from hypothesis.stateful import RuleBasedStateMachine, rule, precondition
from itertools import count
from collections import namedtuple


Entry = namedtuple('Entry', 'order, item')


class Q:

    def __init__(self):
        self._q = []

    def push(self, item):
        self._q.append(item)

    def pop(self):
        return self._q.pop()

    def __len__(self):
        return len(self._q)


class QMachine(RuleBasedStateMachine):

    def __init__(self):
        super().__init__()
        self._q = Q()
        self._elements = set()
        self._count = count()

    @property
    def N(self):
        return next(self._count)

    @rule(item=text(alphabet=ascii_letters))
    def push(self, item):
        self._q.push(item)
        self._elements.add(Entry(self.N, item))

    @rule()
    @precondition(lambda self: self._elements)
    def pop(self):
        popped = self._q.pop()
        expected = min(self._elements)
        assert popped == expected.item
        self._elements.remove(expected)
        # did the expected thing get popped?

    @rule()
    def len(self):
        assert len(self._q) == len(self._elements)


TestQ = QMachine.TestCase


def test_one():
    q = Q()
    assert len(q) == 0
    q.push(1)
    q.push(2)
    q.push(3)
    assert len(q) == 3
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3
