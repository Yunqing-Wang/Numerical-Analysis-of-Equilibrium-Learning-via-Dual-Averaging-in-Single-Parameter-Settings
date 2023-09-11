# Numerical Analysis of Equilibrium Learning via Dual Averaging in Single-Parameter Settings
This project contains the research and findings focused on the numerical analysis of equilibrium learning, specifically via the dual averaging method in single-parameter settings. Through extensive simulations and analyses, this project seeks to explore and understand the dynamics of equilibrium learning in various scenarios where the governing parameters vary (the number of bidders, the number of items etc.). Feel free to explore the repository to gain insights into the world of numerical analysis and equilibrium learning.

## Auction forms
This project simulates the following auction forms:
- Multiunit auction
- Sponsored Search auction

## Payment rules
This project accounts for the following payment rules:
- First-price sealed bid
- Second-price sealed bid
- Vickrey–Clarke–Groves (VCG)

## Prior distributions
This project involves three different prior distributions:
- Uniform distribution
- Power rule distribution
- Exponential distribution

## About simulations
In order to mirror real-world auction environments as closely as possible, this project employs the concept of combinatorial sets to account for every conceivable bid and value proposition. Furthermore, we assume all bidders adhere to a symmetric strategy, the calculation methods are identical for each bidder. Hence, within the coding structure, we utilize bidder 1 as a representative for bidder i to maintain this consistency.

## About code
### Multiunit auctions
- First-price sealed bid auction based on multiunit: [Link](https://github.com/Yunqing-Wang/Numerical-Analysis-of-Equilibrium-Learning-via-Dual-Averaging-in-Single-Parameter-Settings/blob/main/Multiunit/First%20price.py)
- First-price sealed bid auction with different priors based on multiunit: [Link](https://github.com/Yunqing-Wang/Numerical-Analysis-of-Equilibrium-Learning-via-Dual-Averaging-in-Single-Parameter-Settings/blob/main/Multiunit/First%20price%20with%20prior.py)
- Second-price sealed bid auction based on multiunit: [Link](https://github.com/Yunqing-Wang/Numerical-Analysis-of-Equilibrium-Learning-via-Dual-Averaging-in-Single-Parameter-Settings/blob/main/Multiunit/Second%20price.py)
- Second-price sealed bid auction with different priors based on multiunit: [Link](https://github.com/Yunqing-Wang/Numerical-Analysis-of-Equilibrium-Learning-via-Dual-Averaging-in-Single-Parameter-Settings/blob/main/Multiunit/Second%20price%20with%20prior.py)
### Sponsored search auctions
- First-price sealed bid auction based on sponsored search: [Link](https://github.com/Yunqing-Wang/Numerical-Analysis-of-Equilibrium-Learning-via-Dual-Averaging-in-Single-Parameter-Settings/blob/main/Sponsored_Search/First%20price.py)
- First-price sealed bid auction with different priors based on sponsored search: [Link](https://github.com/Yunqing-Wang/Numerical-Analysis-of-Equilibrium-Learning-via-Dual-Averaging-in-Single-Parameter-Settings/blob/main/Sponsored_Search/First%20price%20with%20prior.py)
- Second-price sealed bid auction based on sponsored search: [Link](https://github.com/Yunqing-Wang/Numerical-Analysis-of-Equilibrium-Learning-via-Dual-Averaging-in-Single-Parameter-Settings/blob/main/Sponsored_Search/Second%20price.py)
- Second-price sealed bid auction with different priors based on sponsored search: [Link](https://github.com/Yunqing-Wang/Numerical-Analysis-of-Equilibrium-Learning-via-Dual-Averaging-in-Single-Parameter-Settings/blob/main/Sponsored_Search/Second%20price%20with%20prior.py)
- VCG based on sponsored search: [Link](https://github.com/Yunqing-Wang/Numerical-Analysis-of-Equilibrium-Learning-via-Dual-Averaging-in-Single-Parameter-Settings/blob/main/Sponsored_Search/VCG.py)
- VCG with random dice based on sponsored search: [Link](https://github.com/Yunqing-Wang/Numerical-Analysis-of-Equilibrium-Learning-via-Dual-Averaging-in-Single-Parameter-Settings/blob/main/Sponsored_Search/VCG%20with%20random%20dice.py)
