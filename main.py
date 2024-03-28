import json
from Case import Case
from Sudoku import Sudoku

if __name__ == '__main__':
    sudoku = Sudoku('[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]')
    print(sudoku)
    sudoku.print_board()

    cases = sudoku.extract_cases_info()

    while True:
        undefined_cases = len(Case.get_undefined_cases(cases))
        if undefined_cases != 0:
            print(str(undefined_cases) + " wait to go")
        else:
            break

        cases = Case.calculate_probabilities(cases)
        try:
            cases = Case.solve_one(cases)
        except Exception as e:
            failed_state = Sudoku.convert_to_sudoku(cases)
            print("State before error ")
            failed_state.print_board()
            raise Exception(f"Failed with error {str(e)}")

    sudoku_solution = Sudoku.convert_to_sudoku(cases)
    print(sudoku_solution)