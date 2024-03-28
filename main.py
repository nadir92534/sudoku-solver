import copy
import random

from Case import Case
from Sudoku import Sudoku

def try_solve(cases):
    filled = 0
    while True:
        undefined_cases = len(Case.get_undefined_cases(cases))
        if undefined_cases != 0:
            print(str(undefined_cases) + " wait to go")
        else:
            return True, filled, cases

        cases = Case.calculate_probabilities(cases)
        try:
            cases = Case.solve_one(cases)
            filled += 1
        except Exception as e:
            return False, filled, cases

if __name__ == '__main__':
    sudoku = Sudoku('[[".","7","4","2",".","8","5","6","1"],[".",".","2",".",".","5","3",".","8"],["1",".",".",".","7",".","4",".","."],[".",".","1",".","6","2",".",".","."],[".","4",".","3",".","1",".","5","7"],[".",".",".","4",".",".",".",".","."],[".","9",".","5",".","7","8",".","."],["2","1","8",".","3",".","7",".","5"],[".",".","3","8","2",".","1",".","6"]]')
    print(sudoku)
    sudoku.print_board()

    initial_cases = sudoku.extract_cases_info()

    while True:
        cases = copy.deepcopy(initial_cases)
        random.shuffle(cases)
        is_success, filled, cases = try_solve(cases)

        sudoku_state = Sudoku.convert_to_sudoku(cases)
        sudoku_state.print_board()

        if is_success == True:
            break
        else:
            print(f"Failed with {str(filled)} filled cases")

    print("SUCCESS")