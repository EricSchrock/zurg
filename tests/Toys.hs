module Toys where

data Toy = Buzz | Hamm | Rex | Woody  deriving (Eq,Ord,Show)

toys :: [Toy]
toys = [Buzz,Hamm,Rex,Woody]

time :: Toy -> Int
time Buzz  = 5
time Woody = 10
time Rex   = 20
time Hamm  = 25
