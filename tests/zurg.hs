module Zurg where

import Data.List (nub, (\\))

type Time = Int
type Toy  = Time
type Toys = [Toy]

type Crossing = (Toys,Toy,Toys,Toy,Toys)

toys :: Toys
toys = [5,10,20,25]

fwd :: Toys -> [(Time,Toys,Toys)]
fwd g = [ (max x y,[x,y],g'\\[y]) | x <- g, let g'=g\\[x], y <- g', x<y]

bwd :: Toys -> [(Time,Toys)]
bwd g = [ (x,g++[x]) | x <- toys\\g]

cross :: Toys -> [(Time,Crossing)]
cross g = [ (t1+t2+t3+t4+max x y,(ts1,t2,ts3,t4,g4)) |
            (t1,ts1,g1)   <- fwd g,
            (t2,g2)       <- bwd g1,
            (t3,ts3,g3)   <- fwd g2,
            (t4,g4@[x,y]) <- bwd g3
          ]

solution :: [Crossing]
solution = [ c | (t,c) <- cross toys, t<=60]

