import pandas as pd
import matplotlib.pyplot as plt

# Return a scatter plot comparing a publisher's game count to their total sales
def publisher_scatter_plot(publisher_stats):

    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(
        publisher_stats['game_count'], 
        publisher_stats['total_sales'], 
        alpha=0.7, 
        s=60, 
        label="Publisher"
    )

    x_offset = (publisher_stats['game_count'].max() - publisher_stats['game_count'].min()) * 0.02
    y_offset = (publisher_stats['total_sales'].max() - publisher_stats['total_sales'].min()) * 0.02

    # Add labels
    for i, row in publisher_stats.iterrows():
        plt.text(
            row['game_count'] + x_offset, 
            row['total_sales'] + y_offset,
            row['publisher'], 
            fontsize=7, 
            ha='right'
        )

    # Chart aesthetics
    plt.title('Game Release Count vs Total Sales by Publisher')
    plt.xlabel('Games Released')
    plt.ylabel('Total Sales')
    plt.grid(alpha=0.3)
    plt.show()
