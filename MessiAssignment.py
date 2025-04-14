# The data from each season 
messi_stats = [
    {"Season": "2004-2005", "Goals": 1, "Assists": 0},
    {"Season": "2005-2006", "Goals": 6, "Assists": 3},
    {"Season": "2006-2007", "Goals": 14, "Assists": 3},
    {"Season": "2007-2008", "Goals": 10, "Assists": 12},
    {"Season": "2008-2009", "Goals": 23, "Assists": 11},
    {"Season": "2009-2010", "Goals": 34, "Assists": 9},
    {"Season": "2010-2011", "Goals": 31, "Assists": 19},
    {"Season": "2011-2012", "Goals": 50, "Assists": 16},
    {"Season": "2012-2013", "Goals": 46, "Assists": 11},
    {"Season": "2013-2014", "Goals": 28, "Assists": 11},
    {"Season": "2014-2015", "Goals": 43, "Assists": 18},
    {"Season": "2015-2016", "Goals": 26, "Assists": 16},
    {"Season": "2016-2017", "Goals": 37, "Assists": 9},
    {"Season": "2017-2018", "Goals": 34, "Assists": 12},
    {"Season": "2018-2019", "Goals": 36, "Assists": 13},
    {"Season": "2019-2020", "Goals": 25, "Assists": 21},
    {"Season": "2020-2021", "Goals": 30, "Assists": 9},
    {"Season": "2021-2022", "Goals": 2, "Assists": 10},
]

# The years Messi scored over 35 goals
over_35_goals = tuple(stat["Season"] for stat in messi_stats if stat["Goals"] > 35)

# The years Messi had over 11 assists
over_11_assists = tuple(stat["Season"] for stat in messi_stats if stat["Assists"] > 11)

# The total number of goals
total_goals = sum(stat["Goals"] for stat in messi_stats)

# The total number of points (goals + assists)
total_points = sum(stat["Goals"] + stat["Assists"] for stat in messi_stats)

# The tuple for more than 50 points and count how many times
over_50_points_flags = tuple((stat["Goals"] + stat["Assists"]) > 50 for stat in messi_stats)
over_50_count = sum(over_50_points_flags)

over_30_goal_years = [stat for stat in messi_stats if stat["Goals"] > 30]
num_years_over_30 = len(over_30_goal_years)
goals_in_over_30_years = sum(stat["Goals"] for stat in over_30_goal_years)

print("1. Years with over 35 goals:", over_35_goals)
print("2. Years with over 11 assists:", over_11_assists)
print("3. Total career goals:", total_goals)
print("4. Total career points (goals + assists):", total_points)
print("5. Over 50 points each year (T/F):", over_50_points_flags)
print("Number of seasons with over 50 points:", over_50_count)
print("6. Years over 30 goals:", num_years_over_30)
print("Total goals in those years:", goals_in_over_30_years)
