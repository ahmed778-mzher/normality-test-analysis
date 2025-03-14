import pandas as pd
from scipy.stats import shapiro, norm
import matplotlib.pyplot as plt
import numpy as np

def load_data(file_path):
    """
    Load data from an Excel file.
    :param file_path: The path to the file
    :return: A DataFrame containing the data if successfully loaded, or None if an error occurred.
    """
    try:
        data = pd.read_excel(file_path)
        return pd.DataFrame(data)
    except FileNotFoundError:
        print("File not found")
        return None
    except ValueError as e:
        print(f"Error reading the file: {e}")
        return None

def check_column(df, column_name):
    """
    Check if the required column exists in the dataset.
    :param df: The DataFrame containing the data
    :param column_name: The name of the column to check for
    :return: The data from the column after dropping missing values, or None if the column doesn't exist.
    """
    if column_name in df.columns:
        return df[column_name].dropna()
    else:
        print("Column not found")
        return None

def perform_shapiro_test(data):
    """
    Perform the Shapiro-Wilk test to check for normality.
    :param data: The data to be tested
    :return: The p-value of the test
    """
    stat, p = shapiro(data)
    print(f"stat = {stat:.4f}, p = {p:.4f}")
    if p > 0.05:
        print("The data follows a normal distribution")
    else:
        print("The data does not follow a normal distribution")
    return p

def plot_histogram(data):
    """
    :param data: The data to plot
    """
    # Plot the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=15, color='skyblue', edgecolor='black', alpha=0.7, density=True)

    # Add a normal distribution curve
    mu, std = norm.fit(data)  # Fit a normal distribution to the data
    xmin, xmax = plt.xlim()  # Get the range of the x-axis
    x = np.linspace(xmin, xmax, 100)  # Create a range of values for x
    p = norm.pdf(x, mu, std)  # Get the probability density function for the normal distribution
    plt.plot(x, p, 'k', linewidth=2)  # Plot the normal distribution curve
    plt.title('Histogram of Data with Normal Distribution', fontsize=16)
    plt.xlabel('Values', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

def main():
    """
    Main function to execute the program.
    """
    file_path = "path_to_your_file"  # Ensure you update the path
    column_name = "target_column"  # Ensure you update the column name
    
    df = load_data(file_path)
    if df is not None:
        data = check_column(df, column_name)
        if data is not None:
            p = perform_shapiro_test(data)
            plot_histogram(data)

if __name__ == "__main__":
    main()

# Author: Ahmed S.Jabbar
# Date: 2025-03-01
