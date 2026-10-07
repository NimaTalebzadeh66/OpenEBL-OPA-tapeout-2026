import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def array_factor(theta, wavelength, pitch, phases, amplitudes):
    """
    Calculate the complex array factor of a 1D optical phased array.
    """
    k0 = 2 * np.pi / wavelength

    af = 0

    for n in range(len(phases)):
        x_n = n * pitch

        af += amplitudes[n] * np.exp(
            1j * (phases[n] - k0 * x_n * np.sin(theta))
        )

    return af

wavelength = 1.55
pitch = wavelength / 2

phases = [0, 0, 0, 0]
amplitudes = [1, 1, 1, 1]

theta_deg = np.linspace(-90, 90, 1001)
theta = np.deg2rad(theta_deg)

af = array_factor(
    theta,
    wavelength,
    pitch,
    phases,
    amplitudes,
)

power = np.abs(af) ** 2
power_normalized = power / np.max(power)

plt.plot(theta_deg, power_normalized)
plt.xlabel("Angle θ (degrees)")
plt.ylabel("Normalized power |AF|²")
plt.title("Uniform 4-Element OPA Array Factor")
plt.grid(True)
project_root = Path(__file__).resolve().parents[2]
figure_path = project_root / "figures" / "day1_uniform_4element_array_factor.png"

plt.savefig(
    figure_path,
    dpi=300,
    bbox_inches="tight",

)
plt.show()