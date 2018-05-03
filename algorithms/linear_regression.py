from sklearn.linear_model import LinearRegression
import pandas
import numpy as np
from sklearn.externals import joblib

ball_by_ball = pandas.read_csv('Ball_by_Ball.csv').T.to_dict().values()
matches = pandas.read_csv('Match.csv')

myData = []
myLabel = []
dict = {}

for balls in ball_by_ball:
	if dict.get(balls['Match_Id'], None) is None:
		dict[balls['Match_Id']] = [[], []]
	if balls['Innings_Id'] == 1:
		dict[balls['Match_Id']][0].append(balls)
	else:
		dict[balls['Match_Id']][1].append(balls)

for index, match in matches.iterrows():
	first_innings_balls = dict[match['Match_Id']][0]
	second_innings_balls = dict[match['Match_Id']][1]
	count = 0
	wicket = 0
	balls_left = 120
	for balls in first_innings_balls:
		count += balls['Batsman_Scored']
		if balls['Extra_Runs'] != " ":
			count += int(balls['Extra_Runs'])
		if balls['Player_dissimal_Id'] != " ":
			wicket += 1
		balls_left -= 1
		if balls['Extra_Type'] != " ":
			balls_left += 1
		myData.append([count, balls_left])
	for i in range(len(first_innings_balls)):
		myLabel.append(count)
	count = 0
	wicket = 0
	balls_left = 120
	for balls in second_innings_balls:
		count += balls['Batsman_Scored']
		if balls['Extra_Runs'] != " ":
			count += int(balls['Extra_Runs'])
		if balls['Player_dissimal_Id'] != " ":
			wicket += 1
		balls_left -= 1
		if balls['Extra_Type'] != " ":
			balls_left += 1
		myData.append([count, balls_left])
	for i in range(len(second_innings_balls)):
		myLabel.append(count)

reg = LinearRegression()
reg.fit(np.array(myData), np.array(myLabel))
print(reg.coef_)
print(reg.predict(np.array([[125, 12]])))
joblib.dump(reg, 'linear_regression.pkl')
