from n_queens import NQueens
import time
import pandas as pd
import pathlib
import bruteforce
SIZE = 8
ITERATIONS = 10
def main():
    print('.: N-Queens Problem :.')
    if not SIZE:
        size = int(input('Please enter the size of board: '))
    else: size = SIZE
    pd.set_option('precision',4)
    dfs,bfs,bf,dfs_solutions,bfs_solutions,bf_solutions = [],[],[],[],[],[]
    rows = {'dfs':dfs,'bfs':bfs,'bf':bf}

    for i in range(ITERATIONS):
        n_queens = NQueens(size)

        t_dfs = time.time()
        dfs_solutions = n_queens.solve_dfs()
        t_dfs = time.time() - t_dfs
        dfs.append(t_dfs)

        t_bfs = time.time()
        bfs_solutions = n_queens.solve_bfs()
        t_bfs = time.time()-t_bfs
        bfs.append(t_bfs)


        t_bf = time.time()
        bf_solutions = bruteforce.solvebf()
        t_bf = time.time()-t_bf
        bf.append(t_bf)
    rows_solutions = {'dfs_solutions':dfs_solutions,'bfs_solutions':bfs_solutions,'bf_solutions':bf_solutions}
    df = pd.DataFrame(rows)
    df.to_csv('mydata.csv',index=0)
    pd.DataFrame(rows_solutions).to_csv('mysolutionsdatas.csv',index=1)
    print(df)
    print(df.mean())


if __name__ == '__main__':
    main()
