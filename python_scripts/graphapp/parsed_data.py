#Pandas was the easiest for me, and math for our ceil method. 
import pandas as pd
import math

#open our dataframe
df = pd.read_csv('graphapp/89-19_total_pops.csv')
#I just do this for memory purposes
listed_data = df.values.tolist()

# def our function for evaluating our years, this can be improved as it is hardcoded.
def render_years():
    years = []
    for index in range(10,41):

        current_year = listed_data[index][0]

        years.append(current_year)

    return years

# def our function for evaluating our total lives affected, this can be improved as it is hardcoded.
def render_total():
    totals = []
    for jndex in range(10,41):
        current_year_pop = listed_data[jndex][5]

        current_year_pop = math.ceil(int(float(current_year_pop)))
        
        totals.append(current_year_pop)

    return totals