import sys
sys.path.append("..")
import zurg

from math import inf
from os import remove, system
from plotly.graph_objects import Figure, Scatter
from time import time


def haskell_interpreted():
    seconds_taken = {}

    inputs = {2: "A,B", 3: "A,B,C", 4: "A,B,C,D", 5: "A,B,C,D,E", 6: "A,B,C,D,E,F"}

    for key, value in inputs.items():
        toys = ["module Toys where",
                "data Toy = A | B | C | D | E | F  deriving (Eq,Ord,Show)",
                "toys :: [Toy]",
                f"toys = [{value}]"]

        with open("Toys.hs", 'w') as f:
            f.write("\n".join(toys))

        start = time()
        system("runhaskell Zurg.hs")
        end = time()

        seconds_taken[key] = end - start

    remove("Toys.hs")

    return seconds_taken


def python_interpreted():
    num_solutions = {}
    seconds_taken = {}

    for i in range(2, 7):
        start = time()
        solutions = zurg.two_cross(range(1, i+1), [], inf, [])
        end = time()

        num_solutions[i] = len(solutions)
        seconds_taken[i] = end - start

    return seconds_taken


if __name__ == "__main__":
    hs = haskell_interpreted()
    py = python_interpreted()
    #TODO: An interesting future project would be to add profiling for compiled Haskell and Python

    fig = Figure()
    fig.add_trace(Scatter(x=list(hs.keys()), y=list(hs.values()), mode='markers', name='haskell'))
    fig.add_trace(Scatter(x=list(py.keys()), y=list(py.values()), mode='markers', name='python'))
    fig.update_yaxes(title='Runtime (seconds)', type='log')
    fig.update_xaxes(title='Number of toys that need to cross the bridge')
    fig.update_layout(title='Runtime to find all possible solutions')
    fig.write_image("../docs/runtime.png")
