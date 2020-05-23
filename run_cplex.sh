#!/bin/bash
for y in 3 4 5 6 7
do
   python3 file_generator.py 7 $y 7
   ./cplex -c "read files/7${y}7.lp" "optimize" "display solution variables -" > "logs/7${y}7.log"
done

rm c*.log