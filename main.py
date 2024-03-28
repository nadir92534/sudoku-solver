import copy
import random

from Case import Case
from Sudoku import Sudoku

best_filled = 0
best_cases = None

def try_solve(cases):
    global best_filled
    global best_filled
    global best_cases

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
            if filled > best_filled:
                best_cases = cases
                best_filled = filled

            return False, filled, cases

def run():
    # currently works on [[".","7","4","2",".","8","5","6","1"],[".",".","2",".",".","5","3",".","8"],["1",".",".",".","7",".","4",".","."],[".",".","1",".","6","2",".",".","."],[".","4",".","3",".","1",".","5","7"],[".",".",".","4",".",".",".",".","."],[".","9",".","5",".","7","8",".","."],["2","1","8",".","3",".","7",".","5"],[".",".","3","8","2",".","1",".","6"]]
    sudoku = Sudoku('[[".","7","4","2",".","8","5","6","1"],[".",".","2",".",".","5","3",".","8"],["1",".",".",".","7",".","4",".","."],[".",".","1",".","6","2",".",".","."],[".","4",".","3",".","1",".","5","7"],[".",".",".","4",".",".",".",".","."],[".","9",".","5",".","7","8",".","."],["2","1","8",".","3",".","7",".","5"],[".",".","3","8","2",".","1",".","6"]]')
    sudoku.print_board()

    initial_cases = sudoku.extract_cases_info()

    while True:
        cases = copy.deepcopy(initial_cases)
        is_success, filled, cases = try_solve(cases)

        sudoku_state = Sudoku.convert_to_sudoku(cases)
        sudoku_state.print_board()

        if is_success == True:
            break
        else:
            print(f"Failed with {str(filled)} filled cases")

    print("SUCCESS")

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print("Best filled: "+str(best_filled))
        sudoku_state = Sudoku.convert_to_sudoku(best_cases)
        sudoku_state.print_board()

        raise KeyboardInterrupt("Keyboard interruption detected.")
