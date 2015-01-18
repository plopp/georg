#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib
import urllib2

georgUrlEvents = "http://localhost:3000/collectionapi/events"
georgUrlPositions = "http://localhost:3000/collectionapi/positions"

def GetAllEvents():
	try:
		req = urllib2.Request(georgUrlEvents)
		response = urllib2.urlopen(req)
		georgJson = json.load(response)
		return georgJson
	except:
		return None


def GetAllPositions():
	try:
		req = urllib2.Request(georgUrlPositions)
		response = urllib2.urlopen(req)
		georgJson = json.load(response)
		return georgJson
	except:
		return None

def GetEvent(id):
	try:
		url = georgUrlEvents+"/"+urllib.quote(id)
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		georgJson = json.load(response)
		return georgJson
	except:
		return None

def GetPosition(id):
	try:
		url = georgUrlPositions+"/"+urllib.quote(id)
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		georgJson = json.load(response)
		return georgJson
	except:
		return None

def EventCreate(dict):
	try:
		req = urllib2.Request(georgUrlEvents)
		req.add_header('Content-Type', 'application/json')
		response = urllib2.urlopen(req, json.dumps(dict))
		return True
	except:
		return None

def PositionCreate(dict):
	try:
		req = urllib2.Request(georgUrlPositions)
		req.add_header('Content-Type', 'application/json')
		response = urllib2.urlopen(req, json.dumps(dict))
		return True
	except:
		return None

def UpdateEvent(id, dict):
	try:
		url = georgUrlEvents+"/"+urllib.quote(id)
		opener = urllib2.build_opener(urllib2.HTTPHandler)
		request = urllib2.Request(url, data=json.dumps(dict))
		request.add_header('Content-Type', 'your/contenttype')
		request.get_method = lambda: 'PUT'
		url = opener.open(request)
		return True
	except:
		return None

def UpdatePosition(id, dict):
	try:
		url = georgUrlPositions+"/"+urllib.quote(id)
		opener = urllib2.build_opener(urllib2.HTTPHandler)
		request = urllib2.Request(url, data=json.dumps(dict))
		request.add_header('Content-Type', 'your/contenttype')
		request.get_method = lambda: 'PUT'
		url = opener.open(request)
		return True
	except:
		return None

def addressToLatLong(address):
	req = urllib2.Request(
		"http://nominatim.openstreetmap.org/search/" +
		urllib.quote(address) +
		"?format=json&limit=1")
	response = urllib2.urlopen(req)
	jsonResponse = json.load(response)
	print jsonResponse

#	data = {
#		"description": description,
#		"lat": lat,
#		"lon": lon,
#		"visible": True
#	}

