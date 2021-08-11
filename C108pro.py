import random
import plotly.figure_factory as ff
import pandas
 
file1 = pandas.read_csv('108.csv')
#count =[]
#diceResult =[]
#for i in range(0,100):
    #dice1 = random.randint(1,6)
    #dice2 = random.randint(1,6)
    #diceResult.append(dice1+dice2)
    #count.append(i)

#fig=ff.create_distplot([diceResult],['result'],show_hist=False)
#fig.show()
fig = ff.create_distplot([file1['Avg Rating'].tolist()],['Rating Chart'],show_hist=False)
fig.show()