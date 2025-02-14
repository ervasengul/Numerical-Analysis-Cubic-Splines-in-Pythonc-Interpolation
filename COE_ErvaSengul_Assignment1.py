import numpy as np
from scipy.interpolate import CubicSpline

#Data table where x is km y is elevation
x = np.array([0, 5, 10, 15, 20])
y = np.array([100, 150, 120, 170, 130])

#this was suggested to be used in the assignment :
# Create cubic spline
cs = CubicSpline(x, y, bc_type='natural')

# Interpolated elevation at 7.5 km
interp_value = cs(7.5)
print(f"Interpolated elevation at 7.5 km: {interp_value:.2f} meters")

#Generate points for the elevation curve, did it for 250 points:
x_curve = np.linspace(0, 20, 250)
y_curve = cs(x_curve)
# Plot the elevation curve
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Original Data Points')
plt.plot(x_curve, y_curve, '-', label='Cubic Spline Interpolation')
plt.title("Elevation Curve")
plt.xlabel("Distance (km)")
plt.ylabel("Elevation (m)")
plt.legend()
plt.grid()
plt.show()

