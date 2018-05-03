import pandas
from sklearn.cluster import KMeans
import numpy
import sklearn
from sklearn.naive_bayes import BernoulliNB as bNB
from sklearn.naive_bayes import GaussianNB as gNB
from sklearn.naive_bayes import MultinomialNB as mNB
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

from numpy import array


matches = pandas.read_csv('Match.csv')
teams = pandas.read_csv('Team.csv').set_index("Team_Id",drop=False)


#print(teams.loc[1,'Team_Name'])
# for index, team in teams.iterrows():
# 	test[team['Team_Id']] = {'Team_Id':team['Team_Id'],'Team_Name':team['Team_Name'],'Team_Short_Code':team['Team_Short_Code']}

# #print(test[1]['Team_Name'])
dataset = []

for index, match in matches.iterrows():
 	# print(teams.loc[match['Team_Name_Id'],'Team_Name'])

 								#------------------for simple 2d array----------------------------#
 	# dataset[index] = { 
 	# 				  'Team1': teams.loc[match['Team_Name_Id'],'Team_Name'], 
 	# 				  'Team2': teams.loc[match['Opponent_Team_Id'],'Team_Name'], 
 	# 				  'Venue_Name': match['Venue_Name'],
 	# 				  'Toss_Winner': teams.loc[match['Toss_Winner_Id'],'Team_Name'], 
 	# 				  'Toss_Decision': match['Toss_Decision'], 
 	# 				  'Match_Winner':'No winner' if match.isnull().values.any() else 'Win' if match['Match_Winner_Id']==match['Team_Name_Id'] else 'Lose'
 	# 				 } 
 	
 							#------------------for dataframe----------------------------#
 	# dataset.append ((
 	# 				   teams.loc[match['Team_Name_Id'],'Team_Name'], 
 	# 				   teams.loc[match['Opponent_Team_Id'],'Team_Name'], 
 	# 				   match['Venue_Name'],
 	# 				   teams.loc[match['Toss_Winner_Id'],'Team_Name'], 
 	# 				   match['Toss_Decision'], 
 	# 				  'No winner' if match.isnull().values.any() else 'Win' if match['Match_Winner_Id']==match['Team_Name_Id'] else 'Lose'
 	# 				))

 							#------------------for intValues----------------------------#
 								#	  1->win, 0->lose, 2->nodecision
 								#     1->bat , 0->field
 								#     venue not added
 	dataset.append ((
 					   match['Team_Name_Id'], 
 					   match['Opponent_Team_Id'], 
 					   #match['Venue_Name'],
 					   match['Toss_Winner_Id'], 
 					   '1' if match['Toss_Decision']=='bat' else '0', 
 					   '2' if match.isnull().values.any() else '1' if match['Match_Winner_Id']==match['Team_Name_Id'] else '0'
 					))

#keys = ['Team1','Team2','Venue_Name','Toss_Winner','Toss_Decision','Match_Winner']
keys = ['Team1','Team2','Toss_Winner','Toss_Decision','Match_Winner'] 					 

data = pandas.DataFrame(data=dataset, columns=keys)	
used_features =['Team1','Team2','Toss_Winner','Toss_Decision']

#print(data['Match_Winner'].values)

X_train, X_test = train_test_split(data, test_size=0.8, random_state=24)

gnb = mNB()
used_features =['Team1','Team2','Toss_Winner','Toss_Decision']
gnb.fit(
    X_train[used_features].values,
    X_train['Match_Winner']
)


#y_pred = gnb.predict(X_test[used_features])

joblib.dump(gnb, 'naive_bayes.pkl')

test = []
test.append(( '7',
			  '3',
			  '7',
			  '0'	
	       ))

Test = pandas.DataFrame(data=test, columns=used_features)	
y_pred = gnb.predict(Test[used_features])
print(y_pred)
# print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
#       .format(
#           X_test.shape[0],
#           (X_test['Match_Winner'] != y_pred).sum(),
#           100*(1-(X_test['Match_Winner'] != y_pred).sum()/X_test.shape[0])
# ))