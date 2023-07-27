import psutil
import re
import sys
sys.path.append("..")
import zurg

from glob import glob
from math import inf
from os import getpid, remove, system
from plotly.graph_objects import Figure, Scatter
from time import time


def haskell_profiling():
    inputs = {2: "A,B", 3: "A,B,C", 4: "A,B,C,D", 5: "A,B,C,D,E", 6: "A,B,C,D,E,F"}
    seconds_interpreted = {}
    seconds_compiled = {}
    memory_used = {}

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
        seconds_interpreted[key] = end - start

        system("ghc -main-is Zurg Zurg.hs -o Zurg")
        start = time()
        system("./Zurg")
        end = time()
        seconds_compiled[key] = end - start

        system("ghc -prof -fprof-auto -rtsopts -main-is Zurg Zurg.hs -o Zurg")
        system("./Zurg +RTS -p")
        with open("Zurg.prof", 'r') as f:
            lines = f.readlines()
        for line in lines:
            if "total alloc" in line:
                memory_used[key] = int(re.sub('[^0-9]','', line))
                break

    files = glob("*.hi") + glob("*.o") + ["Toys.hs"] + ["Zurg"] + ["Zurg.prof"]
    for file in files:
        remove(file)

    return seconds_interpreted, seconds_compiled, memory_used


def python_profiling():
    seconds_interpreted = {}
    memory_used = {}

    for i in range(2, 7):
        process = psutil.Process(getpid())
        initial = process.memory_info().vms
        start = time()
        solutions = zurg.two_cross(range(1, i+1), [], inf, [])
        end = time()
        final = process.memory_info().vms

        seconds_interpreted[i] = end - start
        memory_used[i] = (final - initial)

    return seconds_interpreted, memory_used


if __name__ == "__main__":
    hs_int, hs_comp, hs_mem = haskell_profiling()
    py_int, py_mem = python_profiling()

    fig = Figure()
    fig.add_trace(Scatter(x=list(hs_int.keys()), y=list(hs_int.values()), mode='markers', name='Haskell (interpreted)'))
    fig.add_trace(Scatter(x=list(hs_comp.keys()), y=list(hs_comp.values()), mode='markers', name='Haskell (compiled)'))
    fig.add_trace(Scatter(x=list(py_int.keys()), y=list(py_int.values()), mode='markers', name='Python (interpreted)'))
    fig.update_yaxes(title='Runtime (seconds)', type='log')
    fig.update_xaxes(title='Number of inputs')
    fig.update_layout(title='Runtime vs number of inputs')
    fig.write_image("../docs/runtime.png")

    fig = Figure()
    fig.add_trace(Scatter(x=list(hs_mem.keys()), y=list(hs_mem.values()), mode='markers', name='Haskell (compiled)'))
    fig.add_trace(Scatter(x=list(py_mem.keys()), y=list(py_mem.values()), mode='markers', name='Python (interpreted)'))
    fig.update_yaxes(title='Memory allocated (bytes)', type='log')
    fig.update_xaxes(title='Number of inputs')
    fig.update_layout(title='Memory allocated vs number of inputs')
    fig.write_image("../docs/ram.png")
