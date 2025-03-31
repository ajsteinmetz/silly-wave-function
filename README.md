# silly-wave-function
## Time Evolution of a Quantum Wave Function in a 1 Å Box

This repository contains a Python script that computes and animates the time evolution of a quantum wave function inside a one-dimensional infinite potential well (box) with a length of 1 Å. The code uses a Fourier expansion method to express the time-dependent wave function in terms of the eigenstates of the infinite well.

## Overview

The initial wave function is defined as:
```math
\psi(x,0) =
\begin{cases}
  \sqrt{\frac{4}{a}} \sin\frac{2\pi x}{a}, & 0 \le x < a/2, \\
  0, & a/2 \le x \le a,
\end{cases}
```
where $a = 1 \times 10^{-10}$ m is the length of the box.

The eigenfunctions of the infinite well are:
```math
\phi_n(x)=\sqrt{\frac{2}{a}}\sin\frac{n\pi x}{a}.
```
The Fourier coefficients $c_n$ for the expansion of the initial state are computed using:
```math
c_n = \frac{\sqrt{2}}{\pi}\left[\frac{\sin\frac{(2-n)\pi}{2}}{2-n}-\frac{\sin\frac{(2+n)\pi}{2}}{2+n}\right],
```
with the $n=2$ case evaluated via its limiting value:
```math
c_2 = \frac{\sqrt{2}}{2}.
```

The full time-dependent wave function is then given by:
```math
\Psi(x,t)=\sum_{n=1}^{N_{\max}} c_n\,\sqrt{\frac{2}{a}}\sin\frac{n\pi x}{a}\,\exp\Bigl(-i\frac{n^2\pi^2\hbar t}{2ma^2}\Bigr),
```
where $N_{\max}$ is the number of Fourier terms used (set to 50 in the script).

The probability density $|\Psi(x,t)|^2$ is computed and animated over a time interval from $t=0$ to $t=10\tau$, where the characteristic time $\tau$ is defined from the ground state ($n=1$):
```math
\tau = \frac{2ma^2}{\pi^2\hbar}.
```

The animation is saved as a GIF file named `wavefunction.gif`.

## Requirements

The following Python packages are required:
- **NumPy** for numerical computations.
- **Matplotlib** for plotting and animation.
- **Pillow** for saving the animation as a GIF.

## Code Overview

- **Fourier Coefficients Calculation:**  
  The function `c_n(n)` computes the Fourier coefficient for each eigenstate based on the given initial wave function. A special case is implemented for $n=2$ to handle the limit.

- **Time Evolution:**  
  The function `psi(x, t)` constructs the time-dependent wave function by summing the contributions from each eigenstate, each evolving with a phase factor $\exp\left(-i\frac{n^2\pi^2\hbar t}{2ma^2}\right)$.

- **Animation:**  
  The script uses Matplotlib's `FuncAnimation` to animate the probability density $|\Psi(x,t)|^2$.

- **Output:**  
  The animation is saved as a GIF file using `PillowWriter`.

## License

This project is provided under the [MIT License](LICENSE).
