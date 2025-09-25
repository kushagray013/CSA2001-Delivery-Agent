# CSA2001 - Project Report

## 1. Introduction
This project implements an autonomous delivery agent in a 2D grid.

## 2. Environment Model
- Grid world with terrain costs ≥ 1
- Static obstacles as -1
- Dynamic obstacles with schedule

## 3. Algorithms
- BFS
- UCS
- A* with Manhattan heuristic
- Local search (hill climbing)

## 4. Experimental Setup
Maps: small, medium, large, dynamic.
Metrics: path cost, nodes expanded, time.

## 5. Results
(Insert tables + plots here)

## 6. Analysis
- BFS: exhaustive, ignores cost
- UCS: optimal but slower
- A*: best trade-off
- Replanning: works under dynamic obstacles

## 7. Conclusion
A* with replanning is most efficient.
