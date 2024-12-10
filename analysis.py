import matplotlib.pyplot as plt

# Extracting genre sales and visualizing trends
def genre_sales_analysis(df_sales):

    # Making dataframes based off every genre
    sportsDf = df_sales[df_sales['genre'] == 'Sports']
    platformDf = df_sales[df_sales['genre'] == 'Platform']
    racingDf = df_sales[df_sales['genre'] == 'Racing']
    rpgDf = df_sales[df_sales['genre'] == 'Role-Playing']
    puzzleDf = df_sales[df_sales['genre'] == 'Puzzle']

    # Minecraft is in miscDf
    miscDf = df_sales[df_sales['genre'] == 'Misc']
    shooterDf = df_sales[df_sales['genre'] == 'Shooter']
    simDf = df_sales[df_sales['genre'] == 'Simulation']
    actionDf = df_sales[df_sales['genre'] == 'Action']
    fightingDf = df_sales[df_sales['genre'] == 'Fighting']
    adventureDf = df_sales[df_sales['genre'] == 'Adventure']
    strategyDf = df_sales[df_sales['genre'] == 'Strategy']

    # This is the code I used to find the genre that had sold the highest amount of copies
    # I needed to do this because I need to edit the df for this genre to make the plots scale better, otherwise one point ruins it all
    # For reference, the game is Minecraft, and it is in the Misc genre

    # maximum_sales = df_sales['global_sales'].max()
    # max_df = df_sales[df_sales['global_sales'] == maximum_sales]
    # max_game = max_df['title']
    # max_genre = max_df['genre']
    # print('the highest selling game is', max_game, 'and its genre is', max_genre)

    # This is a df that doesn't have minecraft in it, NM stands for No Minecraft lol
    miscDfNM = miscDf[miscDf['title']!='Minecraft']

    # Making a list of the dataframes to automate future plt functions
    dfList = [sportsDf, platformDf, racingDf, rpgDf, puzzleDf, miscDfNM, shooterDf, simDf, actionDf, fightingDf, adventureDf, strategyDf]
    dfNames = ['sportsDf', 'platformDf', 'racingDf', 'rpgDf', 'puzzleDf', 'miscDfNM', 'shooterDf', 'simDf', 'actionDf', 'fightingDf', 'adventureDf', 'strategyDf']

    print('')

    # Used this to see which genres have the most games and tend to sell the best
    for i in range(len(dfList)):
        print(dfNames[i], 'has an average global_sales of', dfList[i]['global_sales'].mean())
        print(dfNames[i], 'has a length of', len(dfList[i]))

    # This is a new df that is the year and the amount sold for the highest selling game from that year
    ts_df = df_sales.groupby('year')['global_sales'].max().reset_index()

    plt.plot(ts_df['year'], ts_df['global_sales'], marker = 'o', color = 'blue')
    plt.title('How many copies the highest selling game of each year has sold')
    plt.xlabel('year')
    plt.ylabel('global_sales (millions)')

    plt.show()

    # The plot above is adjusted to give maximum sales because this way the values are independent of how many values are in that year
    # For example, if one year has only a few popular games and another year has many games, the many games year will have a lower average
    # Using max lets us focus on blockbuster games, because those are the types of games that have major releases
    # The one major dot in 2009 is Minecraft

    # I did the below code because I wanted 2 handy graphs, that way it's less info to look at
    # But 6 trend lines that are this similar make it difficult to spot trends unless u focus
    # I want it to look nice and in depth, which is why I have to manaully decide
    # Which genres I'd like to focus on
    # And also loop through dfList to make trend graphs for all the genres

    maxDfList = []
    meanDfList = []
    colList = ['b', 'r', 'g', 'orange', 'tab:purple', 'tab:brown']
    for i in range(int(len(dfList)/2)):
        maxDfList.append(dfList[i].groupby('year')['global_sales'].max().reset_index())
        meanDfList.append(dfList[i].groupby('year')['global_sales'].mean().reset_index())
        plt.plot(maxDfList[i]['year'], maxDfList[i]['global_sales'], marker = 'o', color = colList[i], label = dfNames[i])

    plt.legend()
    plt.show()

    maxDfList = []
    meanDfList = []
    for i in range(len(dfList) - int(len(dfList)/2)):
        maxDfList.append(dfList[int(len(dfList)/2) + i].groupby('year')['global_sales'].max().reset_index())
        meanDfList.append(dfList[int(len(dfList)/2) + i].groupby('year')['global_sales'].mean().reset_index())
        plt.plot(maxDfList[i]['year'], maxDfList[i]['global_sales'], marker = 'o', color = colList[i], label = dfNames[int(len(dfList)/2) + i])

    plt.legend()
    plt.show()

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



