import json

class Case:
    def __init__(self, row_id, column_id, square_id):
        self.row_id = row_id
        self.column_id = column_id
        self.square_id = square_id

    def __str__(self):
        return f"Case | Row: {self.row_id} | Column: {self.column_id} | Square: {self.square_id}"

class Sudoku:
    def __init__(self, seed):
        """
        :param seed: sudoku input
        """
        self.dimension = 9

        try:
            self.rows = json.loads(seed)
        except json.decoder.JSONDecodeError:
            raise Exception('Json Error decoding the soduku')

        valid, reason = self.verify()
        if not valid:
            raise Exception('Invalid sudoku. '+reason)

        self.cases = self.extract_cases_info()

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

                case = Case(row_id, col_id, square_id)
                cases.append(case)

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

if __name__ == '__main__':
    sudostr = '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'

    sudoku = Sudoku(sudostr)
    sudoku.print_board()
