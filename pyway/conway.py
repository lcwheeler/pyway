import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.signal
from numba import jit

class Game(object): 

    """Object class that simulates Conway's Game of Life and produces an animation."""

    def __init__(self):
        """Instantiate an instance of the cluster_set class"""

        self.grid = None
        #self.new_grid = None
        self.options = 2


    def initial_conditions(self, size1, size2):
        """Generate a random arrangement of the game grid."""

        #the number of possible states. For Conway's game of life this is two (0 and 1). 
        if self.options != 2:
            raise Exception('The game only has two states!')

        #generate the grid using np.random.randint with the sizes equal to desired dimensions of array. 
        grid = np.random.randint(self.options, high=None, size=(size1,size2))
        self.grid = grid

    @jit
    def conway(self):
        """Function that applies the rules of Conway's game of life on an initialized 2D array"""


        # Create an identical copy of the grid, which will become the grid of the next generation. 
        new_grid = np.copy(self.grid)
        
        donut_kernel = np.ones((3,3),dtype=int)
        donut_kernel[1,1] = 0
        
        # Find the number of living neighbours by convolving a donut shaped kernel with the current grid
        # This num_neighbours variable is a 2D array of the same size as the grid variable, where each of
        # the entries contains the sum of neighbours for the applicable entry in grid
        num_neighbours = scipy.signal.convolve2d(self.grid, donut_kernel, mode="same", boundary="wrap")
        
        #Iterate over the grid array elements and apply the rules of life using conditional statements. 
        for i, j in np.ndenumerate(self.grid):

            if self.grid[i[0], i[1]] == 1:
                if num_neighbours[i[0], i[1]] < 2 or num_neighbours[i[0], i[1]] > 3:
                    new_grid[i[0], i[1]] = 0

            elif self.grid[i[0], i[1]] == 0:

                if num_neighbours[i[0], i[1]] == 3:
                    new_grid[i[0], i[1]] = 1
        
        #replace the original grid with the new grid that represents the next generation
        self.grid = np.copy(new_grid)
        
    @jit
    def make_animation(self, generations=100, Cmap='BuGn', interval=700, repeat_delay=1000, 
                        blit=True, name="Conway_animation", export=True):
    
        """This function will iterate over generations and build and animation from a series of snapshots."""
        

        #intialize a plot object to show the grids as images
        fig = plt.figure()
        plt.axis('off')
        shots = []

        #Loop over the number of generations (i) and play the game
        for i in range(generations):
            # Make a list of image snapshots of the grid at each generation
            shots.append((plt.imshow(self.grid, cmap='BuGn'),))
            self.conway()
            
        # Create an animation using the matplolib animation 
        movie = animation.ArtistAnimation(fig, shots, interval=100, repeat_delay=1000, blit=True)
        self.movie = movie

        # Save the animation if the user requests 
        if export==True:
            movie.save(name+'.mp4', writer=animation.FFMpegWriter())

        else:
            pass


