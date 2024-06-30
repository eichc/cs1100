# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 13:58:18 2022

@author: Cam Eich

Ask a user to select a grid, and if they want the grid printed. Give the user
a few potential starting points, and the neighbors of those points. Determine
whether a chosen path through the grid is possible, and if so tell the user
the change in elevation.
"""

import hw5_util

def get_nbrs(location, num_rows, num_cols):
    '''
    Return a list containing all of the possible neighbors of a given location.
    A neighbor is not included if it occurs outside the given grid.
    '''
    r, c = location
    neighbors = []
    if r > 0:
        neighbors.append((r-1,c))
    if c > 0:
        neighbors.append((r,c-1))
    if c < num_cols - 1:
        neighbors.append((r,c+1))
    if r < num_rows - 1:
        neighbors.append((r+1,c))
    return neighbors

def is_neighbor(first, second):
    '''
    Determine if two locations are neighbors of each other. Return a boolean.
    '''
    r1, c1 = first
    r2, c2 = second
    flag = False
    if c1 == c2 and abs(r1-r2) <= 1:
        flag = True
    elif r1 == r2 and abs(c1-c2) <= 1:
        flag = True
    return flag

def is_valid(path):
    '''
    Determine if a given path is valid or not. If the path is invalid, print
    the two points that make the path invalid. Return a boolean.
    '''
    for i in range(len(path)-1):
        if not is_neighbor(path[i], path[i+1]):
            print("Path: invalid step from {} to {}".format(path[i], path[i+1]))
            return False
    return True


if __name__ == "__main__":
    #force the user to input a grid number 1-3, or 0 to stop the program
    n = 4
    while n > 3 or n < 0:
        n = input("Enter a grid index less than or equal to 3 (0 to end): ").strip()
        print(n)
        n = int(n)
    
    #program stops if user entered 0
    if n != 0:
        grid = hw5_util.get_grid(n)
        
        #print the grid if the user wants to
        print_grid = input("Should the grid be printed (Y or N): ").strip()
        print(print_grid)
        if print_grid == 'y' or print_grid == 'Y':
            print("Grid {}".format(n))
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    print("{:4d}".format(grid[i][j]), end='')
                print("")
        #print the number of columns and rows
        print("Grid has {} rows and {} columns".format(len(grid), len(grid[0])))
        
        #get the starting locations and print each one's set of neighbors
        starts = hw5_util.get_start_locations(n)
        for i in range(len(starts)):
            neighbors = get_nbrs(starts[i], len(grid), len(grid[0]))
            print("Neighbors of {}:".format(starts[i]), end='')
            for j in range(len(neighbors)):
                print(' {}'.format(neighbors[j]), end='')
            print('')
        
        #get the suggested path and determine if it is valid or not
        path = hw5_util.get_path(n)
        if is_valid(path):
            print("Valid path")
            #determine the change in elevation
            total_up = 0
            total_down = 0
            for i in range(len(path)-1):
                change = grid[path[i+1][0]][path[i+1][1]] - grid[path[i][0]][path[i][1]]
                if change > 0:
                    total_up += change
                else:
                    total_down -= change
            print("Downward {}".format(total_down))
            print("Upward {}".format(total_up))

        
        
        
        
        
        