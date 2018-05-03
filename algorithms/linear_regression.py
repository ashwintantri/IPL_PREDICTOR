from sklearn.linear_model import LinearRegression
import pandas
import numpy as np

ball_by_ball = pandas.read_csv('Ball_by_Ball.csv').T.to_dict().values()
matches = pandas.read_csv('Match.csv')

myData = []
myLabel = []

for index, match in matches.iterrows():
	first_innings_balls = []
	second_innings_balls = []
	for balls in ball_by_ball:
		if (balls['Match_Id'] == match['Match_Id']) and (balls['Innings_Id'] == 1):
			first_innings_balls.append(balls)
		elif (balls['Match_Id'] == match['Match_Id']) and (balls['Innings_Id'] == 2):
			second_innings_balls.append(balls)
	count = 0
	wicket = 0
	balls_left = 120
	for balls in first_innings_balls:
		if balls == 0:
			print(count)
		count += balls['Batsman_Scored']
		if balls['Extra_Runs'] != " ":
			count += int(balls['Extra_Runs'])
		if balls['Player_dissimal_Id'] != " ":
			wicket += 1
		balls_left -= 1
		if balls['Extra_Type'] != " ":
			balls_left += 1
		myData.append([count, balls_left, wicket])
	for i in range(len(first_innings_balls)):
		myLabel.append(count)
	print(count)
	count = 0
	wicket = 0
	balls_left = 120
	for balls in second_innings_balls:
		if balls == 0:
			print(count)
		count += balls['Batsman_Scored']
		if balls['Extra_Runs'] != " ":
			count += int(balls['Extra_Runs'])
		if balls['Player_dissimal_Id'] != " ":
			wicket += 1
		balls_left -= 1
		if balls['Extra_Type'] != " ":
			balls_left += 1
		myData.append([count, balls_left, wicket])
	for i in range(len(second_innings_balls)):
		myLabel.append(count)
	print(count)

reg = linear_model.LinearRegression()
reg.fit(np.array(myData), np.array(myLabel))
print(reg.coef_)