import json
from Case import Case

class Sudoku:
    def __init__(self, seed:str):
        """
        :param seed: sudoku input
        """
        self.dimension = 9
        self.seed = seed

        try:
            self.rows = json.loads(seed)
        except json.decoder.JSONDecodeError:
            raise Exception('Json Error decoding the soduku')

        valid, reason = self.verify()
        if not valid:
            raise Exception('Invalid sudoku. '+reason)

    def extract_cases_info(self):
        cases = []

        for row_id, row in enumerate(self.rows):
            for col_id, item in enumerate(row):

                square_id = -1
                if col_id < 3:
                    square_id = 1
                elif col_id < 6:
                    square_id = 2
                else:
                    square_id = 3

                if row_id > 2:
                    square_id += 3

                if row_id > 5:
                    square_id += 3

                case = Case(item if not item == "." else None, row_id, col_id, square_id)
                cases.append(case)
                # print(case)

        return cases

    def print_board(self):
        print("+" + "--" * self.dimension + "-+")  # delimiter

        for i, line in enumerate(self.rows):
            output_line = ""

            for j, item in enumerate(line):
                output_line += item + " "

                if j in [2, 5]:
                    output_line += "  "

            if i in [2, 5]:
                output_line += "\n"

            print(output_line.replace(".", "_"))

        print(f"\nSudoku {self.dimension}x{self.dimension}")

    def verify(self):
        if not isinstance(self.rows, list):
            return False, 'Provided is not a list'

        if len(self.rows) != 9:
            return False, 'Sudoku doesn\'t match 9 length requirement'

        for _, row in enumerate(self.rows):
            if not isinstance(row, list):
                return False, f'Row number {_+1} is not a list'

            for item in row:
                if not isinstance(item, str):
                    return False, f'Not all items are string on Row number {_+1}'

            if len(row) != 9:
                return False, f'Row number {_+1} is not 10 item length'

        return True, 'Successful'

    @staticmethod
    def convert_to_sudoku(cases):
        rows = []
        for i_row in range(9):
            row = []
            for j_col in range(9):
                case = [x for x in cases if x.row_id == i_row and x.col_id == j_col][0]
                row.append(case.value or ".")
            rows.append(row)

        sudoku_str = str(json.dumps(rows)).replace(" ", "")

        return Sudoku(sudoku_str)

    def __str__(self):
        return self.seed