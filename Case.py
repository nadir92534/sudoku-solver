import json

class Case:
    def __init__(self, value, row_id, col_id, square_id):
        self.value = value
        self.row_id = row_id
        self.col_id = col_id
        self.square_id = square_id

        self.probabilities = []

    @staticmethod
    def calculate_probabilities(cases):
        undefined_cases = [x for x in cases if x.value is None]

        new_cases = []

        for case in undefined_cases:
            same_row = [x for x in cases if x.row_id == case.row_id]
            same_col = [x for x in cases if x.col_id == case.col_id]
            same_square = [x for x in cases if x.square_id == case.square_id]

            same = same_row + same_col + same_square

            probabilities = []

            for i in range(9):
                number = i + 1
                times_shown = len([x for x in same if x.value == str(number)])
                probabilities.append({"number": number, "times_shown": times_shown})

            case.probabilities = probabilities
            new_cases.append(case)

        return new_cases

    def __str__(self):
        return f"Case {self.value if self.value else '?'} | Row: {self.row_id} | Column: {self.col_id} | Square: {self.square_id} | Probabilities: {self.probabilities}"