# qubit-simulator
A simple program that simulates a measurement taken on a **quantum register**.

## Description

### Fundamentals
A qubit can be described as a ... using a two-dimentional vector space over the complex numbers, with basis vectors $\lvert0\rangle$ and $\lvert1\rangle$. 

General form: $\lvert\psi\rangle = \alpha\lvert0\rangle + \beta\lvert1\rangle$

- $\lvert\psi\rangle:$ current state vector
- $\\;\alpha\\;:$ the complex probability amplitude of $0$
- $\lvert0\rangle:\left[ 1 \atop 0 \right]:\text{ket 0}$
- $\\;\beta\\;:$ the complex probability amplitude of 1$
- $\lvert1\rangle:\left[ 0 \atop 1 \right]:\text{ket 1}$

With the **nomilization constraint**: $\lvert\alpha\rvert^{2} + \lvert\beta\rvert^{2} = 1$

## Getting Started

### Requirements
#### Language
- python
#### Packages
- numpy
- matplotlib

### Installation
- clone repository

### Running
```sh
$ cd .../qubit-simulator
```
```sh
$ python main.py 
```

## Usage

## Roadmap
- [ ] Finish README
- [ ] add simulation iterations (to show correct distribution)
- [ ] support multiple qubits
- [ ] support **bloch sphere** visualization for single qubit registers
