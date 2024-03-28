import json
from Case import Case
from Sudoku import Sudoku

if __name__ == '__main__':
    sudoku = Sudoku('[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]')
    print(sudoku)
    sudoku.print_board()

    cases = sudoku.extract_cases_info()

    prob_cases = Case.calculate_probabilities(cases)
    for case in prob_cases:
        print(case)

    sudoku_solution = Sudoku.convert_to_sudoku(cases)
    print(sudoku_solution)