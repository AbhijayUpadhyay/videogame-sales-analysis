import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create a bubble chart comparing each genre's total sales, average rating, and number of reviews 
def genre_bubble_chart(genre_comparisons):

    genres = genre_comparisons['Genre']
    total_sales = genre_comparisons['Total Sales']
    avg_rating = genre_comparisons['Average Rating']
    number_of_reviews = genre_comparisons['Number of Reviews']

    sizes = number_of_reviews / 100

    # Plot
    plt.figure(figsize=(12, 8))
    plt.scatter(total_sales, avg_rating, s=sizes, alpha=0.6, c='green', edgecolors="black")

    # Add labels
    for i, genre in enumerate(genres):
        plt.text(total_sales[i], avg_rating[i] + 0.02, genre, fontsize=9, ha='center')

    # Chart aesthetics
    plt.xlabel('Total Sales (in millions)')
    plt.ylabel('Average Rating')
    plt.title('Total Sales vs. Average Rating (Bubble Size = Number of Reviews)')
    plt.grid()
    plt.tight_layout()
    plt.show()

# Create a scatter plot comparing a publisher's game count to their total sales
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
