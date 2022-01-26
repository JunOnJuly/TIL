import random


class ClassHelper:

    def __init__(self, students):
        self.students = students

    def pick(self, n):
        return random.sample(self.students, n)

    def match_pair(self):
        pair = []
        pair_lst = []
        while len(self.students) > 3:
            pair.append(random.sample(self.students, 2))

            pair_lst.append(pair[:2])
            pair = pair[2:]

            # break

        if len(self.students) <= 3:
            last_pair = pair.append(self.students)
            pair_lst.append(last_pair)

            return pair_lst