import json

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

        # self.square_structs = self.get_square_structs()
        # print(self.square_structs)

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

    # def get_square_structs(self):
    #     structs = []
    #     struct_start = 0
    #
    #     for i in range(9):
    #         structs.append([])
    #
    #     for row_i, row in enumerate(self.rows):
    #         if row_i > 2:
    #             struct_start = 3
    #         if row_i > 5:
    #             struct_start = 6
    #
    #         for item_i, item in enumerate(row):
    #             if item_i < 3:
    #                 structs[struct_start].append()
    #
    #     return structs

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
