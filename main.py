import json

class Sudoku:
    def __init__(self, seed):
        """
        :param seed: sudoku input
        """
        try:
            self.seed_json = json.loads(seed)
        except json.decoder.JSONDecodeError:
            raise Exception('Json Error decoding the soduku')

        valid, reason = self.verify()
        if not valid:
            raise Exception('Invalid sudoku. '+reason)

        self.square_structs = self.get_square_structs()
        print(self.square_structs)

    def get_square_structs(self):
        structs = []
        struct_start = 0

        for i in range(9):
            structs.append([])

        for row_i, row in enumerate(self.rows):
            if row_i > 2:
                struct_start = 3
            if row_i > 5:
                struct_start = 6

            for item_i, item in enumerate(row):
                if item_i < 3:
                    structs[struct_start].append()

    def verify(self):
        if not isinstance(self.seed_json, list):
            return False, 'Provided is not a list'

        self.rows = self.seed_json

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
    sudo = Sudoku('[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]')
