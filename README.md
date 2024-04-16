# qubit-simulator
A simple program that simulates a measurement taken on a **quantum register**.

## Description

### Fundamentals
A qubit can be described as a ... using a two-dimentional vector space over the complex numbers, with basis vectors $\lvert0\rangle$ and $\lvert1\rangle$. 

General form: $\lvert\psi\rangle = \alpha\lvert0\rangle + \beta\lvert1\rangle$

$\lvert\psi\rangle:$
$\\;\\;\alpha:$ the complex probability amplitude of $0$
$\lvert0\rangle:$
$\\;\\;\beta:$ the complex probability amplitude of $1$
$\lvert1\rangle:$

With the **nomilization constraint**: $\lvert\alpha\rvert^{2} + \lvert\beta\rvert^{2} = 1$

## Getting Started

### Requirements
- python (language)
- python-numpy (package)

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
