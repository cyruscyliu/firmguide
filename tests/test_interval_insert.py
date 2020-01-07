from unittest import TestCase


def interval_insert(targets, mmio_base, end):
    # no overlapping this time
    left, right = [], []
    for target in targets:
        if mmio_base >= target[1]:
            left.append(target)
        elif end <= target[0]:
            right.append(target)
        else:
            # must be overlapped
            if target[0] <= mmio_base < target[1] < end:
                return -1
            elif mmio_base < target[0] < end <= target[1]:
                return -2
            elif (mmio_base, end) == target:
                return -3
            elif target[0] <= mmio_base < end <= target[1]:
                return -4
    return left + [(mmio_base, end)] + right


class TestIntervalInsert(TestCase):
    def test_interval_insert(self):
        # target must be in order
        targets = [(0, 1), (3, 4), (8, 12)]
        self.assertEqual(-1, interval_insert(targets, 0, 3))
        self.assertEqual(-2, interval_insert(targets, 2, 4))
        self.assertEqual(-3, interval_insert(targets, 3, 4))
        self.assertEqual(-4, interval_insert(targets, 8, 9))
        self.assertEqual(-4, interval_insert(targets, 9, 10))
        self.assertEqual(-4, interval_insert(targets, 11, 12))
        print(interval_insert(targets, 1, 2))
        print(interval_insert(targets, 7, 8))
