# TODO
- Finish README
- add simulation count (to show correct distribution
- support multiple qbits
- support **bloch sphere** visualization for single qubit registers

# qubit-simulator
A simple program that simulates a measurement taken on a **quantum register**.

## Description

### Fundamentals
A qubit can be described as a ... using a two-dimentional vector space over the complex numbers, with basis vectors $\lvert0\rangle$ and $\lvert1\rangle$. 

General form: $\lvert\psi\rangle = \alpha\lvert0\rangle + \beta\lvert1\rangle$

- $\psi:$
- $\alpha:$ the complex probability amplitude of $0$
- $\beta:$ the complex probability amplitude of $1$

With the **nomilization constraint**: $\lvert\alpha\rvert^{2} + \lvert\beta\rvert^{2} = 1$

## How to use

### Dependencies
- python (language)
- python-numpy (package)
### Installing
- clone repository
### Running
```sh
$ python main.py 
```
