//Polygons.remove({});
//Events.remove({});
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
		lat:57.721836,
		lon:11.952035,
		description:"Brand i Backa",
		visible:true
	});
	Events.insert({
		lat:57.708839,
		lon:11.939031,
		description:"Buss försenad",
		visible:true
	});
	Events.insert({
		lat:57.705756,
		lon:11.935523,
		description:"Konsert på Backa teater",
		visible:true
	});
	Events.insert({
		lat:57.707750,
		lon:11.926747,
		description:"Tävling isfiske - Sannegården",
		visible:true
	});
}

if(Positions.find().count() == 0){
	Positions.insert({
		lat:57.721836,
		lon:11.952035,
		description:"Brand i Backa",
		visible:true
	});
}
