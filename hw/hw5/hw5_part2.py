# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:34:07 2022

@author: Cam Eich

Ask the user to select a grid and a maximum step height. Output the steepest
and least gradual paths for each starting point for the chosen grid, and
whether a global or local maximum is encountered in the path. Finally, if the
user wishes, output a grid displaying how many times each point in the grid
was encountered on a path.
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

def find_steep_path(grid, start, max_steps):
    '''
    Given a starting location and a maximum change in height between steps, 
    find and return the steepest possible path.
    '''
    path = [start]
    flag = True
    curr_loc = start
    #runs while there are still more possible locations to move to
    while flag:
        neighbors = get_nbrs(curr_loc, len(grid), len(grid[0]))
        steep_nbr = curr_loc
        #loop through the neighbors to find the greatest one, making sure to
        #not exceed the max step
        for i in range(len(neighbors)):
            r_new, c_new = neighbors[i]
            r_old, c_old = steep_nbr
            difference = grid[r_new][c_new] - grid[curr_loc[0]][curr_loc[1]]
            if grid[r_new][c_new] > grid[r_old][c_old] and difference <= max_steps:
                steep_nbr = neighbors[i]
        #runs if the current location wasn't updated
        if steep_nbr == curr_loc:
            flag = False
        else:
            path.append(steep_nbr)
            curr_loc = steep_nbr
    return path

def find_gradual_path(grid, start, max_steps):
    '''
    Given a starting location and a maximum change in height between steps, 
    find and return the most gradual path.
    '''
    path = [start]
    flag = True
    curr_loc = start
    #runs while there are still more possible locations to move to
    while flag:
        neighbors = get_nbrs(curr_loc, len(grid), len(grid[0]))
        short_nbr = neighbors[0]
        #loop through the neighbors to find the smallest one that is still 
        #greater than the current location, making sure to not exceed the max step
        for i in range(len(neighbors)):
            r_new, c_new = neighbors[i]
            r_old, c_old = short_nbr
            difference = grid[r_new][c_new] - grid[curr_loc[0]][curr_loc[1]]
            if grid[r_new][c_new] < grid[r_old][c_old] and 0 < difference <= max_steps:
                short_nbr = neighbors[i]
            #if the value being considered is less than the current height, skip it
            elif difference < 0 and not grid[r_old][c_old] > grid[r_new][c_new]:
                short_nbr = neighbors[(i+1)%len(neighbors)]
        #runs if the current location wasn't updated, ending the loop
        if grid[short_nbr[0]][short_nbr[1]] < grid[curr_loc[0]][curr_loc[1]]:
            flag = False
        elif grid[short_nbr[0]][short_nbr[1]] - grid[curr_loc[0]][curr_loc[1]] > max_steps:
            flag = False
        else:
            path.append(short_nbr)
            curr_loc = short_nbr
    return path

def is_local_max(grid, loc):
    '''
    Determine if a given location is a local maximum.
    '''
    r, c = loc
    for i in range(len(grid)):
        if grid[i][c] > grid[r][c]:
            return False
    for j in range(len(grid[0])):
        if grid[r][j] > grid[r][c]:
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
            starts = hw5_util.get_start_locations(n)
            
            #input max step height
            max_step = input("Enter the maximum step height: ").strip()
            print(max_step)
            max_step = int(max_step)
            
            #ask if the user wants the path grid printed
            print_grid = input("Should the path grid be printed (Y or N): ").strip()
            print(print_grid)
            
            #create the initial path grid
            path_grid = []
            for i in range(len(grid)):
                row = []
                for j in range(len(grid[0])):
                    row.append(0)
                path_grid.append(row)
            
            #print the number of columns and rows
            print("Grid has {} rows and {} columns".format(len(grid), len(grid[0])))
            
            #find the global maximum height
            global_max = 0
            max_loc = (0,0)
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] > global_max:
                        global_max = grid[i][j]
                        max_loc = (i, j)
            print("global max: {} {}".format(max_loc, global_max))
            
            #for each starting point, determine the steepest and most gradual paths
            for i in range(len(starts)):
                steep_path = find_steep_path(grid, starts[i], max_step)
                gradual_path = find_gradual_path(grid, starts[i], max_step)
                
                #print the steepest path
                print("===")
                print("steepest path")
                for i in range(len(steep_path)):
                    print(steep_path[i], end='')
                    path_grid[steep_path[i][0]][steep_path[i][1]] += 1
                    if i % 5 == 4:
                        print(" ")
                    else:
                        print(" ", end='')
                if len(steep_path) % 5 != 0:
                    print("")
                #determine if local or global maximum is encountered
                if steep_path[-1] == max_loc:
                    print("global maximum")
                elif is_local_max(grid, steep_path[-1]):
                    print("local maximum")
                else:
                    print("no maximum")
                
                #print the most gradual path
                print("...")
                print("most gradual path")
                for i in range(len(gradual_path)):
                    print(gradual_path[i], end='')
                    path_grid[gradual_path[i][0]][gradual_path[i][1]] += 1
                    if i % 5 == 4:
                        print(" ")
                    else:
                        print(" ", end='')
                if len(gradual_path) % 5 != 0:
                    print("")
                #determine if local or global maximum is encountered
                if gradual_path[-1] == max_loc:
                    print("global maximum")
                elif is_local_max(grid, gradual_path[-1]):
                    print("local maximum")
                else:
                    print("no maximum")
            print("===")
            
            #print the path grid if requested
            if print_grid == 'y' or print_grid == 'Y':
                print("Path grid")
                for i in range(len(path_grid)):
                    for j in range(len(path_grid[0])):
                        if path_grid[i][j] == 0:
                            print("  .", end='')
                        else:
                            print("{:3d}".format(path_grid[i][j]), end='')
                    print("")
            
            
            