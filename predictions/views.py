from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
import json
from sklearn.externals import joblib
import numpy as np

def get_algos(request):
	f=os.path.join( settings.BASE_DIR, 'predictions/static/clustering.json' )
	json_data = open(f)
	player_details = json.load(json_data)
	json_data.close()
	return render(request, 'app.html', {'data': player_details})

def predictScore(request):
	x = request.GET['x']
	y = request.GET['y']
	reg = joblib.load(os.path.join( settings.BASE_DIR, 'algorithms/linear_regression.pkl' ))
	prediction = float(reg.predict(np.array([[int(x), int(y)]]))[0])
	return HttpResponse(str(prediction))