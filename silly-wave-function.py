import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Physical constants and parameters
a = 1e-10                   # Box length in meters (1 Å)
m = 9.10938356e-31          # Electron mass in kg
hbar = 1.054571817e-34      # Reduced Planck's constant in J*s

# Characteristic time from the ground state (n=1)
tau = 2 * m * a**2 / (np.pi**2 * hbar)
t_max = 10 * tau            # Animate over 10τ

# Spatial grid: x from 0 to a
x = np.linspace(0, a, 1000)

# Maximum number of Fourier terms to include in the expansion
Nmax = 50

def c_n(n):
    """
    Compute the Fourier coefficient c_n for the initial wave function:
      psi(x,0) = sqrt(4/a)*sin(2*pi*x/a) for 0 <= x < a/2,
                 0 otherwise.
    The eigenfunctions are phi_n(x)=sqrt(2/a)*sin(n*pi*x/a).
    Analytical expression:
      c_n = (sqrt(2)/pi)*[ sin((2-n)*pi/2)/(2-n) - sin((2+n)*pi/2)/(2+n) ]
    with the n=2 case handled by taking the limit.
    """
    if n == 2:
        return np.sqrt(2) / 2  # Evaluated limit for n=2
    else:
        return (np.sqrt(2)/np.pi) * ( np.sin((2 - n)*np.pi/2)/(2 - n) - np.sin((2 + n)*np.pi/2)/(2 + n) )

def psi(x, t):
    """
    Compute the time-dependent wave function Psi(x,t) using its Fourier expansion:
      Psi(x,t) = sum_{n=1}^{Nmax} c_n * sqrt(2/a)*sin(n*pi*x/a)*exp(-i*E_n*t/ħ)
    where E_n = n^2*pi^2*hbar/(2*m*a^2).
    """
    psi_val = np.zeros_like(x, dtype=complex)
    for n in range(1, Nmax+1):
        # Time evolution phase: exp(-i*E_n*t/ħ) where E_n = n^2*pi^2*hbar/(2*m*a^2)
        phase = np.exp(-1j * n**2 * np.pi**2 * hbar * t / (2 * m * a**2))
        psi_val += c_n(n) * np.sqrt(2/a) * np.sin(n * np.pi * x / a) * phase
    return psi_val

# Set up the plot for animation
fig, ax = plt.subplots()
y0 = np.abs(psi(x, 0))**2
line, = ax.plot(x, y0, lw=2)
ax.set_xlim(0, a)
ax.set_ylim(0, y0.max() * 1.4)  # y-axis limit increased to 1.4 times the max initial value
ax.set_xlabel('x (m)')
ax.set_ylabel(r'$|\Psi(x,t)|^2$')
ax.set_title('Time Evolution of the Probability Density (With 2x Box)')

# Text object for time annotation
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    """Initialization function for the animation."""
    line.set_ydata(np.abs(psi(x, 0))**2)
    time_text.set_text('t = 0 s')
    return line, time_text

def update(t):
    """Update function for each animation frame."""
    y = np.abs(psi(x, t))**2
    line.set_ydata(y)
    time_text.set_text(f't = {t:.2e} s')
    return line, time_text

# Create time frames from 0 to t_max
frames = np.linspace(0, t_max, 200)

# Set up the animation using FuncAnimation
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=50)

# Save the animation as a GIF using PillowWriter (ensure Pillow is installed: pip install pillow)
writer = PillowWriter(fps=20)
ani.save("wavefunction2.gif", writer=writer)

plt.show()
