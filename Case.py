import json


class Probabilities:
    def __init__(self, number, times_shown):
        self.number = number
        self.times_shown = times_shown

    def __str__(self):
        return f"Number {self.number} | Times shown {self.times_shown}"


class Case:
    def __init__(self, value, row_id, col_id, square_id):
        self.value = value
        self.row_id = row_id
        self.col_id = col_id
        self.square_id = square_id

        self.probabilities = None

    @staticmethod
    def get_undefined_cases(cases):
        return [x for x in cases if x.value is None]

    @staticmethod
    def calculate_probabilities(cases):
        for case in cases:
            if not case.value is None:
                continue

            same_row = [x for x in cases if x.row_id == case.row_id]
            same_col = [x for x in cases if x.col_id == case.col_id]
            same_square = [x for x in cases if x.square_id == case.square_id]

            same = same_row + same_col + same_square

            probabilities = []

            for i in range(9):
                number = i + 1
                times_shown = len([x for x in same if x.value == str(number)])

                prob = Probabilities(number, times_shown)
                probabilities.append(prob)

            case.probabilities = probabilities

        return cases

    @staticmethod
    def solve_one(cases):
        number = -1
        undefined_cases = Case.get_undefined_cases(cases)
        case = undefined_cases[0]

        for prob in case.probabilities:
            if prob.times_shown == 0:
                number = prob.number
                break
        if number == -1:
            raise Exception("Unsolvable :(")

        case.value = str(number)

        return cases

    def __str__(self):
        return f"Case {self.value if self.value else '?'} | Row: {self.row_id} | Column: {self.col_id} | Square: {self.square_id} | Probabilities: {self.probabilities}"