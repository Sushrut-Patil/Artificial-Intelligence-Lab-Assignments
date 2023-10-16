import pandas as pd
import matplotlib.pyplot as plt

# Read data from the CSV file
data = pd.read_csv("Lab Assignment 4\Dataset.csv")

# Extract X0, X1, and Class columns
X0 = data['X0']
X1 = data['X1']
Class = data['Class']

# Create a scatter plot
plt.figure(figsize=(8, 6))  # Set the figure size (adjust as needed)
plt.scatter(X0, X1, c=Class, cmap='viridis', marker='o', s=100)
plt.xlabel('X0')
plt.ylabel('X1')
plt.title('Scatter Plot of X0 vs. X1')
plt.colorbar(label='Class')
plt.grid(True)
plt.show()
