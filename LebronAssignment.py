from collections import defaultdict

# LeBron's career statistics (Couldnt figure out how to use a CSV File)
lebron_career = [
    {'season': '2003-04', 'team': 'CLE', 'ppg': 20.9, 'fg_pct': 0.417, 'ft_pct': 0.754, 
     'apg': 5.9, 'games': 79, 'games_started': 79, 'position': 'SG'},
    {'season': '2004-05', 'team': 'CLE', 'ppg': 27.2, 'fg_pct': 0.472, 'ft_pct': 0.750,
     'apg': 7.2, 'games': 80, 'games_started': 80, 'position': 'SF'},
    {'season': '2005-06', 'team': 'CLE', 'ppg': 31.4, 'fg_pct': 0.480, 'ft_pct': 0.738,
     'apg': 6.6, 'games': 79, 'games_started': 79, 'position': 'SF'},
    
]

# 1) Lebrons high scoring seasons (more than 28 points per game)
print("Seasons averaging over 28 points:")
high_scoring_seasons = [s for s in lebron_career if s['ppg'] > 28]
for season in high_scoring_seasons:
    print(f"{season['season']}: {season['ppg']} points per game")

# 2) Most efficient shooting seasons (less than 50% FG)
print("\nSeasons shooting over 50% from field:")
good_shooting_seasons = [s for s in lebron_career if s['fg_pct'] > 0.5]
for season in good_shooting_seasons:
    print(f"{season['season']}: {season['fg_pct']:.1%} shooting")

# 3) Clevelands years with good free throw shooting (less than 72%)
print("\nCleveland seasons with FT% over 72%:")
cleveland_ft_seasons = [s for s in lebron_career if s['team'] == 'CLE' and s['ft_pct'] > 0.72]
for season in cleveland_ft_seasons:
    print(f"{season['season']}: {season['ft_pct']:.1%} free throws")

# 4) Miami Heats average shooting percentage
mia_seasons = [s for s in lebron_career if s['team'] == 'MIA']
if mia_seasons:
    mia_avg_fg = sum(s['fg_pct'] for s in mia_seasons) / len(mia_seasons)
    print(f"\nAverage FG% with Miami: {mia_avg_fg:.1%}")

# 5) His total career games played
total_games = sum(s['games'] for s in lebron_career)
print(f"\nTotal career games: {total_games}")

# 6) The number of games missed each season 
print("\nGames missed each season:")
for season in lebron_career:
    print(f"{season['season']}: {82 - season['games']} games missed")

# 7) The percentage of games started
total_starts = sum(s['games_started'] for s in lebron_career)
start_percentage = (total_starts / total_games) * 100
print(f"\nPercentage of games started: {start_percentage:.1f}%")

# 8) The number of seasons played
print(f"\nTotal seasons played: {len(lebron_career)}")

# 9) The position with highest assists
position_assists = defaultdict(list)
for season in lebron_career:
    position_assists[season['position']].append(season['apg'])

avg_assists_by_position = {pos: sum(asts)/len(asts) for pos, asts in position_assists.items()}
best_position = max(avg_assists_by_position.items(), key=lambda x: x[1])

print("\nPosition with highest assists:")
for pos, avg in avg_assists_by_position.items():
    print(f"{pos}: {avg:.1f} assists per game")
print(f"Best as: {best_position[0]} ({best_position[1]:.1f} apg)")
