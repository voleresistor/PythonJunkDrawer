'''
Some grid things
'''
import sys

def print_horiz(box_width, grid_width):
    '''
    Prints horizontals in our boxes
    '''
    print('+ ', end='')
    print(('- '*box_width + '+ ') * grid_width)

def print_vert(box_width, grid_width):
    '''
    Prints the verticals in our boxes
    '''
    print('| ', end='')
    print(('  '*box_width + '| ') * grid_width)

def print_box(box_width, grid_width):
    '''
    Uses print_vert and print_horiz to generate a single box
    '''
    print_horiz(box_width, grid_width)
    for i in range(0, box_width):
        print_vert(box_width, grid_width)
    print_horiz(box_width, grid_width)

def print_grid(box_width, grid_height, grid_width):
    '''
    Uses print_horiz and print_vert to generate a grid of boxes
    '''
    for i in range(0, grid_width):
        print_horiz(box_width, grid_width)
        for j in range(0, box_width):
            print_vert(box_width, grid_height)
    print_horiz(box_width, grid_width)

def main(dim, num_box):
    '''
    Take command line args to generate the grid
    '''
    from math import floor
    box_scale = floor(dim/num_box)
    print_grid(box_scale, dim, dim)

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
