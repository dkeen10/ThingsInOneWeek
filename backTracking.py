"""
Pseudocode for backracking:
void FIND_SOLUTIONS( parameters):
    if (valid solution):
        store the solution
        Return
    for (all choice):
        if (valid choice):
            APPLY (choice)
            FIND_SOLUTIONS (parameters)
            BACKTRACK (remove choice)
    Return

Time Complexity of backtracking is typically either Exponential (O(K^N)) 
or Factorial (O(N!))

Historical Backtracking Problems:
- N-Queens
- Sudoku
- Maze
- Knight's Tour
- Hamiltonian Path
- Graph Coloring
- Subset Sum
- Knapsack
- Crossword
- Map Coloring

"""

