Polygons.remove({});
Events.remove({});
if(Polygons.find().count() == 0){
	Polygons.insert({
		coordinates:[
			{lat:57.709344,lon:11.925856},
			{lat:57.711567,lon:11.934783},
			{lat:57.711888,lon:11.944782},
			{lat:57.711888,lon:11.944782},
			{lat:57.707899,lon:11.952550},
			{lat:57.705675,lon:11.944353},
			{lat:57.702993,lon:11.932895},
			{lat:57.703061,lon:11.928002}
		]
	});
}

if(Events.find().count() == 0){
	Events.insert({
		lat:57,
		lon:12,
		description:"Beskrivning"
	});
}