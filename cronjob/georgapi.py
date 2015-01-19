#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import urllib
import urllib2
import re

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

def FindEvents(searchterm, useRegex):
	req = urllib2.Request(georgUrlEvents)
	response = urllib2.urlopen(req)
	georgJson = json.load(response)
	#print georgJson
	resultOut = []
	#Loop through items, add point for each matched searchterm
	#If all searchterms matrch add to out
	for jsonItem in georgJson:
		#print "For jsonItem: "+str(jsonItem)
		matchPoints = 0
		#Loop through searchterms
		for searchtermKey, searchtermValue in searchterm.iteritems():
			#print "For searchterm: "+str(searchtermKey)+" "+str(searchtermValue)
			if useRegex:
				s = jsonItem[searchtermKey].encode('utf-8')
				m = re.match(searchtermValue, s)
				if m:
					#print "regex-match"
					matchPoints += 1
			else:
				if searchtermValue == jsonItem[searchtermKey]:
					#print "ordinary-match"
					matchPoints += 1
		#If the number of searchterms are equal to matchpoints, all searchterms are matched
		if len(searchterm) == matchPoints :
			resultOut.append(jsonItem)
		#print ""
	#print ""
	#print "Search-result:"
	#print ""
	if len(resultOut) > 0:
		return resultOut
	else:
		return None


def FindPositions(searchterm, useRegex):
	req = urllib2.Request(georgUrlPositions)
	response = urllib2.urlopen(req)
	georgJson = json.load(response)
	#print georgJson
	resultOut = []
	#Loop through items, add point for each matched searchterm
	#If all searchterms matrch add to out
	for jsonItem in georgJson:
		#print "For jsonItem: "+str(jsonItem)
		matchPoints = 0
		#Loop through searchterms
		for searchtermKey, searchtermValue in searchterm.iteritems():
			#print "For searchterm: "+str(searchtermKey)+" "+str(searchtermValue)
			if useRegex:
				s = jsonItem[searchtermKey].encode('utf-8')
				m = re.match(searchtermValue, s)
				if m:
					#print "regex-match"
					matchPoints += 1
			else:
				if searchtermValue == jsonItem[searchtermKey]:
					#print "ordinary-match"
					matchPoints += 1
		#If the number of searchterms are equal to matchpoints, all searchterms are matched
		if len(searchterm) == matchPoints :
			resultOut.append(jsonItem)
		#print ""
	#print ""
	#print "Search-result:"
	#print ""
	if len(resultOut) > 0:
		return resultOut
	else:
		return None


def EventCreate(dict):
	req = urllib2.Request(georgUrlEvents)
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(dict))
	return True

def PositionCreate(dict):
	req = urllib2.Request(georgUrlPositions)
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(dict))
	return True

def UpdateEvent(id, dict):
	url = georgUrlEvents+"/"+urllib.quote(id)
	opener = urllib2.build_opener(urllib2.HTTPHandler)
	request = urllib2.Request(url, data=json.dumps(dict))
	request.add_header('Content-Type', 'your/contenttype')
	request.get_method = lambda: 'PUT'
	url = opener.open(request)
	return True

def UpdatePosition(id, dict):
	url = georgUrlPositions+"/"+urllib.quote(id)
	opener = urllib2.build_opener(urllib2.HTTPHandler)
	request = urllib2.Request(url, data=json.dumps(dict))
	request.add_header('Content-Type', 'your/contenttype')
	request.get_method = lambda: 'PUT'
	url = opener.open(request)
	return True

def addressToLatLong(address):
	req = urllib2.Request(
		"http://nominatim.openstreetmap.org/search/" +
		urllib.quote(address) +
		"?format=json&limit=1")
	response = urllib2.urlopen(req)
	jsonResponse = json.load(response)
	print jsonResponse

def DeleteEvent(id):
	url = georgUrlEvents+"/"+urllib.quote(id)
	opener = urllib2.build_opener(urllib2.HTTPHandler)
	request = urllib2.Request(url)
	request.add_header('Content-Type', 'your/contenttype')
	request.get_method = lambda: 'DELETE'
	url = opener.open(request)
	return True


def DeletePosition(id):
	url = georgUrlPositions+"/"+urllib.quote(id)
	opener = urllib2.build_opener(urllib2.HTTPHandler)
	request = urllib2.Request(url)
	request.add_header('Content-Type', 'your/contenttype')
	request.get_method = lambda: 'DELETE'
	url = opener.open(request)
	return True

