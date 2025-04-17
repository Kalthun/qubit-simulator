# qubit-simulator
TODO

## Overview

### Fundamentals
A qubit can be described as a ... using a two-dimentional vector space over the complex numbers, with basis vectors $\lvert0\rangle$ and $\lvert1\rangle$.

General form: $\lvert\psi\rangle = \alpha\lvert0\rangle + \beta\lvert1\rangle$

- $\lvert\psi\rangle:$ current state vector
- $\\;\alpha\\;:$ the complex probability amplitude of $0$
- $\lvert0\rangle:\left[ 1 \atop 0 \right]:\text{ket 0}$
- $\\;\beta\\;:$ the complex probability amplitude of $1$
- $\lvert1\rangle:\left[ 0 \atop 1 \right]:\text{ket 1}$

With the **nomilization constraint**: $\lvert\langle\psi\vert\psi\rangle\rvert = \lvert\alpha\rvert^{2} + \lvert\beta\rvert^{2} = 1$

### Bloch Sphere
```math
\begin{align}

    \lvert\psi\rangle &= \alpha\lvert0\rangle + \beta\lvert1\rangle \\

    &= \Bigl[ a_{\alpha}+b_{\alpha}j \Bigr] \lvert0\rangle
     + \Bigl[ a_{\beta}+b_{\beta}j \Bigr] \lvert1\rangle \\

    &= \Bigl[r_{\alpha}\Bigl(\text{cos}(\phi_{\alpha})+\text{sin}(\phi_{\alpha})j\Bigr)\Bigr] \lvert0\rangle
     + \Bigl[r_{\beta}\Bigl(\text{cos}(\phi_{\beta})+\text{sin}(\phi_{\beta})j\Bigr)\Bigr] \lvert1\rangle \\

    &= \Bigl[r_{\alpha}e^{j\phi_{\alpha}}\Bigr] \lvert0\rangle
     + \Bigl[r_{\beta}e^{j\phi_{\beta}}\Bigr] \lvert1\rangle \\

    \lvert\psi\rangle &\equiv \lvert\psi'\rangle \\

    \lvert\psi'\rangle &= \Bigl( e^{-j\phi_{\alpha}} \Bigr)
       \Biggl[ \Bigl[r_{\alpha}e^{j\phi_{\alpha}}\Bigr] \lvert0\rangle
     + \Bigl[r_{\beta}e^{j\phi_{\beta}}\Bigr] \lvert1\rangle \Biggr] \\

    &= r_{\alpha} \lvert0\rangle
     + r_{\beta}e^{j(\phi_{\beta}-\phi_{\alpha})} \lvert1\rangle \\

    &= r_{\alpha}\lvert0\rangle
     + r_{\beta}e^{j\phi} \lvert1\rangle

\end{align}
```
