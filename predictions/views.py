from django.shortcuts import render
from django.conf import settings
import os
import json

def get_algos(request):
	f=os.path.join( settings.BASE_DIR, 'predictions/static/clustering.json' )
	json_data = open(f)
	player_details = json.load(json_data)
	json_data.close()
	return render(request, 'app.html', {'data': player_details}) 