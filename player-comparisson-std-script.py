import pandas as pd
import csv

# Extract 2019 NBA data and place into dataframe and spreadsheet
dfs = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2019_per_game.html', header=0)
df = dfs[0]
cols = ['Age', 'G', 'GS', 'MP', 'FG','FGA','FG%','3P','3PA','3P%','2P','2PA','2P%','eFG%','FT','FTA','FT%','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS']
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce', axis=1)
dfs[0].to_excel('NBA_2019_per_game.xlsx')


# Extract 2019 WNBA data and place into dataframe and spreadsheet
dfs = pd.read_html('https://www.basketball-reference.com/wnba/years/2019_per_game.html', header=0)
df = dfs[0]
cols = ['G', 'GS', 'MP', 'FG','FGA','FG%','3P','3PA','3P%','2P','2PA','2P%','eFG%','FT','FTA','FT%','ORB','TRB','AST','STL','BLK','TOV','PF','PTS']
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce', axis=1)
dfs[0].to_excel('WNBA_2019_per_game.xlsx')


# Loop through all player comparisons
nba_df = pd.read_excel('NBA_2019_per_game.xlsx', sheet_name='STANDARDIZED')
wnba_df = pd.read_excel('WNBA_2019_per_game.xlsx', sheet_name='STANDARDIZED')

diffs = pd.DataFrame(columns = nba_df.columns[0:28])

n = 0
while n <= 278:
    w = 0

    while w <= 113:
        nba_row = nba_df.loc[n]
        wnba_row = wnba_df.loc[w]
        players = nba_row[0], wnba_row[0]      
        i = 0
        vals = []
        
        while i <= 27:
            if i <= 2:
                vals.append(nba_row[i] + ', ' + wnba_row[i])
            else:
                val = abs(nba_row[i] - wnba_row[i])
                vals.append(val)
            i = i + 1

        absvals = pd.DataFrame([vals], columns = nba_df.columns[0:28])
#         rows.append(absvals)
        diffs = diffs.append(absvals, ignore_index=True)
        w = w + 1
        
    n = n + 1

diffs[cols] = diffs[cols].apply(pd.to_numeric, errors='coerce', axis=1)
diffs.to_excel("spreadsheet.xlsx", sheet_name='sheet')  
    