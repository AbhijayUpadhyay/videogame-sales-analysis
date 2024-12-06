import pandas
import matplotlib.pyplot as plt

def sales_analysis(df_sales):
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
