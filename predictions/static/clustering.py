import pandas
from sklearn.cluster import KMeans
from numpy import array
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import codecs, json

players = pandas.read_csv('Player.csv')
ball_by_ball = pandas.read_csv('Ball_by_Ball.csv')

player_details = [None] * 600
actual_details = []

for index, player in players.iterrows():
	player_details[player['Player_Id']] = {'runs': 0, 'wickets': 0, 'name': player['Player_Name']};
	actual_details.append([0, 0, 0])

for index, ball in ball_by_ball.iterrows():
	player_details[ball['Striker_Id']]['runs'] += int(ball['Batsman_Scored'])
	actual_details[ball['Striker_Id']][0] += int(ball['Batsman_Scored'])
	actual_details[ball['Striker_Id']][2] = actual_details[ball['Striker_Id']][1] * actual_details[ball['Striker_Id']][0]
	if ball['Dissimal_Type'] != " " and ball['Dissimal_Type'] != "runout":
		player_details[ball['Bowler_Id']]['wickets'] += 1
		actual_details[ball['Bowler_Id']][1] += 1
		actual_details[ball['Bowler_Id']][2] = actual_details[ball['Bowler_Id']][1] * actual_details[ball['Bowler_Id']][0]

X = array(actual_details)
kmeans = KMeans(n_clusters = 4)
kmeans.fit(X)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

colors = ["g","r","c","y"]
ax = plt.axes(projection='3d')

for i in range(len(X)):
	if player_details[i + 1] is None:
		print(i)
	player_details[i + 1]['grade'] = str(labels[i])
	ax.scatter3D(X[i][0], X[i][1], X[i][2], c = colors[labels[i]])

plt.show()
file_path = "clustering.json"
json.dump(player_details[1:523], codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)
