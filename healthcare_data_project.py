# Head and Neck Cancer Cell Line Inventory Analysis by Minifdi76
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class HeadAndNeckCancerCellLineInventory:
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        self.cell_line_data = self.load_cell_line_data()

    def load_cell_line_data(self):
        """Load head and neck cancer cell line data from a CSV file."""
        data = pd.read_csv(self.data_file_path)
        return data

    def analyze_growth_rate(self):
        """Analyze and visualize the growth rate of head and neck cancer cell lines."""
        plt.figure(figsize=(12, 6))
        sns.barplot(data=self.cell_line_data, x='CellLine', y='GrowthRate', ci=None)
        plt.title('Growth Rate of Head and Neck Cancer Cell Lines')
        plt.xlabel('Cell Line')
        plt.ylabel('Growth Rate')
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    def analyze_cell_viabilities(self):
        """Analyze and visualize cell viabilities for different cell lines."""
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=self.cell_line_data, x='CellLine', y='Viability')
        plt.title('Cell Viabilities of Head and Neck Cancer Cell Lines')
        plt.xlabel('Cell Line')
        plt.ylabel('Viability')
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    def generate_correlation_matrix(self):
        """Generate and display a correlation matrix for the data."""
        correlation_matrix = self.cell_line_data.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Matrix of Head and Neck Cancer Cell Line Data')
        plt.tight_layout()
        plt.show()

    def summarize_inventory(self):
        """Summarize the head and neck cancer cell line inventory."""
        summary = self.cell_line_data.describe()
        return summary

if __name__ == "__main__":
    data_file_path = 'head_and_neck_cancer_cell_line_data.csv'

    # Initialize the HeadAndNeckCancerCellLineInventory
    inventory = HeadAndNeckCancerCellLineInventory(data_file_path)

    # Analyze and visualize the growth rate of head and neck cancer cell lines
    inventory.analyze_growth_rate()

    # Analyze and visualize cell viabilities
    inventory.analyze_cell_viabilities()

    # Generate and display the correlation matrix
    inventory.generate_correlation_matrix()

    # Summarize the inventory
    summary = inventory.summarize_inventory()
    print("Summary of the Head and Neck Cancer Cell Line Inventory:")
    print(summary)
