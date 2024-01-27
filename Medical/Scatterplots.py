import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

average_work_exp = np.array([3.418181818, 3.472727273, 3.531818182, 3.768181818, 4.040909091, 4.113636364])
disengagement = np.array([9.8, 9.8, 10, 10, 10.4, 10.2])
exhaustion = np.array([11.8, 11.9, 12, 11.8, 12.5, 12.5])


#slope, intercept, _, _, _ = linregress(average_work_exp, disengagement)
slope, intercept, _, _, _ = linregress(average_work_exp, exhaustion)

plt.scatter(average_work_exp, exhaustion, label='Data')

x_values = np.linspace(min(average_work_exp), max(average_work_exp), 100)
y_values = slope * x_values + intercept
plt.plot(x_values, y_values, color='red', label='LSRL')

slope, intercept, r_value, p_value, std_err = linregress(average_work_exp, exhaustion)
slope, intercept, _, _, _ = linregress(average_work_exp, exhaustion)


print(f"LSRL Equation: y = {slope:.2f}x + {intercept:.2f}")

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value**2)
print("P-value:", p_value)
print("Standard error:", std_err)

# Labels and legend
plt.xlabel('Average Work Experience')
plt.ylabel('Exhaustion')
plt.title('Scatter Plot with LSRL')
plt.legend()

# Show plot
plt.grid(True)
plt.show()