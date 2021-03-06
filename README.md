# Installations

## Environment

* python 2.7.6
* module-opencv 
* module-numpy
* module-scipy
* module-PIL

## Bootstrap Steps

1. python rank_clut.py source_img
2. python main.py source_img
3. python decode.py

# Algorithms
 
## CLUT generator

In CLUT generator, We unique all pixel from input img and calculate each of unique pixel's count. After these step, sort the list and extrac top 256 colours.
  
## Find similar color

How we find similar color, we use a low-cost approximation method, The proposed algorithm (used by our products EGI, AniSprite and PaletteMaker) is a combination both weighted Euclidean distance functions, where the weight factors depend on how big the "red" component of the colour is. First one calculates the mean level of "red" and then weights the ΔR′ and ΔB′ signals as a function of the mean red level. The distance between colours C1 and C2 (where each of the red, green and blue channels has a range of 0-255) is:


[Formula](https://4406arthur.pancakeapps.com/lowcost_formula.png)

# Members

* 1001543
* 1001521
* 1001503
