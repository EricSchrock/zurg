module Zurg where

import Search
import Data.List( (\\), delete, sort)
import Toys

data Pos = L | R                  deriving (Eq,Show)
type Group = [Toy]
type BridgePos = (Pos,Group)
type Move = Either Toy Group

time :: Toy -> Int
time A = 1
time B = 2
time C = 3
time D = 4
time E = 5
time F = 6

duration :: [Move] -> Int
duration = sum . map (either time (maximum . map time))

backw :: Group -> [(Move,BridgePos)]
backw xs = [(Left x,(L,sort (x:(toys \\ xs)))) | x <- xs]

forw :: Group -> [(Move,BridgePos)]
forw xs = [(Right [x,y],(R,delete y ys)) |
              x <- xs,let ys=delete x xs, y <- ys, x<y]

instance SearchProblem BridgePos Move where
  trans (L,l)  = forw l
  trans (R,l)  = backw (toys \\ l)
  isSolution (ms,s) = s == (R,[]) && duration ms <= 60

solution :: [Move]
(solution,_):_ = solutions (L,toys)

allSolutions :: [([Move], (Pos, [Toy]))] -> [[Move]]
allSolutions ss = [s | (s,_) <- ss]

main :: IO ()
main = do
  let ss = allSolutions $ solutions (L,toys)
   in print $ length ss
