# Conway's Game of Life in Python ![Tests](https://github.com/domoritz/gameoflife-python/workflows/Tests/badge.svg)

# User Domoritz implementation
Implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life) in an infinite space in Python. Alive cells are stored in a set. To calculate the next iteration, we compute the number of neighbors for each cell that has neighbors.

Peter Norvig has a fantastic explanation in a [Jupyter Notebook](https://nbviewer.jupyter.org/url/norvig.com/ipython/Life.ipynb).

My goal was to write a pythonic program that is easy to understand (limit the use of comprehensions).

I am implementing the Game of Life in different programming languages to learn about them. You can find [all of my implementations on GitHub](https://github.com/domoritz?tab=repositories&q=gameoflife).


## What I liked/disliked about python

* Python syntax is easy to read and write.
* Named tuples, iterators, defaultdict, and list comprehensions are awesome.
* Writing tests is really easy.


## Run an example

```sh
python game_of_life.py
```


## Running the tests

Run `python test.py`.

## More

Check out this sonification of the output of this program: https://github.com/Mystified131/GameOfMusic.


# Game of life, with CUDA

## Objective

The objective of this fork is to add NVIDIA CUDA implementaion and parallelization capabilities to this implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life).

Some references :
* https://developer.nvidia.com/how-to-cuda-python
* https://developer.nvidia.com/blog/numba-python-cuda-acceleration/


## Install

1. Download Cuda (tested with CUDA 11.0)
2. Download Anaconda Navigator (tested with Anaconda3, v1.9.12)
3. Create a (conda) virtual environnement in the navigator, with a 3.6 python version
4. Open a terminal in the virtual environnement
5. `conda install -c numba pyculib`
6. `conda install numba cudatoolkit pyculib`
