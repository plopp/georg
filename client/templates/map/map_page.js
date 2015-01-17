Template.mapPage.rendered = function(){

	  google.maps.Polygon.prototype.Contains = function(point) { var crossings = 0, path = this.getPath();
			  	// for each edge
		for (var i=0; i < path.getLength(); i++) {
		    var a = path.getAt(i),
		        j = i + 1;
		    if (j >= path.getLength()) {
		        j = 0;
		    }
		    var b = path.getAt(j);
		    if (rayCrossesSegment(point, a, b)) {
		        crossings++;
		    }
		}

		// odd number of crossings?
		return (crossings % 2 == 1);

		function rayCrossesSegment(point, a, b) {
		    var px = point.lng(),
		        py = point.lat(),
		        ax = a.lng(),
		        ay = a.lat(),
		        bx = b.lng(),
		        by = b.lat();
		    if (ay > by) {
		        ax = b.lng();
		        ay = b.lat();
		        bx = a.lng();
		        by = a.lat();
		    }
		    // alter longitude to cater for 180 degree crossings
		    if (px < 0) { px += 360 };
		    if (ax < 0) { ax += 360 };
		    if (bx < 0) { bx += 360 };

		    if (py == ay || py == by) py += 0.00000001;
		    if ((py > by || py < ay) || (px > Math.max(ax, bx))) return false;
		    if (px < Math.min(ax, bx)) return true;

		    var red = (ax != bx) ? ((by - ay) / (bx - ax)) : Infinity;
		    var blue = (ax != px) ? ((py - ay) / (px - ax)) : Infinity;
		    return (blue >= red);

		}
	  }; 

	  var mapOptions = {
	    zoom: 13,
	    center: new google.maps.LatLng(57.13,11.87)
	  };
	  map = new google.maps.Map(document.getElementById('map'),mapOptions);

	  /*google.maps.event.addListener(map, 'click', function(e) {
	    placeMarker(e.latLng, map);
	  }); */
	  //console.log(this.data[0]);
	  var polygons = this.data[0];


	  var polygonCoords = [];
	  polygonArr = [];
	  for(var i = 0;i<polygons.length;i++){
		  for(var j = 0;j<polygons[i].coordinates.length;j++){
		    var position = new google.maps.LatLng(polygons[i].coordinates[j].lat,polygons[i].coordinates[j].lon);
		    polygonCoords.push(position);
			/*var marker = new google.maps.Marker({
				position: position,
				map:map
			});*/
			map.panTo(position);
		  }
		  var curPolygon = new google.maps.Polygon({
		    paths: polygonCoords,
		    strokeColor: '#FF0000',
		    strokeOpacity: 0.8,
		    strokeWeight: 3,
		    fillColor: '#FF0000',
		    fillOpacity: 0.35
		  });
		  polygonArr.push(curPolygon);
		  curPolygon.setMap(map);
	  }

	  var events = this.data[1];
	  console.log(events);
	  markers = [];
	  for(var i = 0;i<events.length;i++){
		    var position = new google.maps.LatLng(events[i].lat,events[i].lon);
			var marker = new google.maps.Marker({
				position: position,
				map:map
			});
			marker.eventId = events[i]._id;
			markers.push(marker);
			google.maps.event.addListener(marker, 'click', panToMarker);
	  }

	  function panToMarker(data){
	  	//console.log(data);
	  	map.panTo(data.latLng);
	  }

	  /*google.maps.event.addListener(curpolygon, 'click', isInsidePolygon);
	  google.maps.event.addListener(map, 'click', isInsideMap);

	  function isInsidePolygon(data){
	  	var lat = data.latLng.D;
	  	var lon = data.latLng.k;
	  	var point = new google.maps.LatLng(lon,lat);

	  	
	  }

	  function isInsideMap(data){
	  	var lat = data.latLng.D;
	  	var lon = data.latLng.k;
	  	var point = new google.maps.LatLng(lon,lat);

	  	console.log(data.latLng);
	  }*/


	  //var point = new google.maps.LatLng(52.05249047600099, -0.6097412109375); 
	  
	/*function placeMarker(position, map) {
	  var marker = new google.maps.Marker({
	    position: position,
	    map: map
	  });
	  map.panTo(position);
	}	*/
}

Template.mapPage.helpers({
	events: function(){
		return Events.find({});
	},
	visible: function(){
		return Events.findOne(this._id).visible;
	},
	scope: function(){
		return Session.get("scope");
	}
});

Template.mapPage.events({
	'click #withinPolygon':function(){
		for (var i = markers.length - 1; i >= 0; i--) {
			for (var i = polygonArr.length - 1; i >= 0; i--) {
				var lat = markers[i].position.D;
			  	var lon = markers[i].position.k;
			  	var point = new google.maps.LatLng(lon,lat);
				if (polygonArr[i].Contains(point)) { // point is inside polygon 
				  	;
				}
				else{
				  	markers[i].setMap(null);
				  	Events.update(markers[i].eventId, {$set: {visible: false}});
				}
			};
		};
		Session.set("scope","within");
	},
	'click #nearby':function(){
		if(navigator.geolocation) {
			console.log(navigator.geolocation);
		    navigator.geolocation.getCurrentPosition(function(position) {
		      var pos = new google.maps.LatLng(position.coords.latitude,
		                                       position.coords.longitude);

		      /*var infowindow = new google.maps.InfoWindow({
		        map: map,
		        position: pos,
		        content: 'Du är här!'
		      });*/

		      for (var i = markers.length - 1; i >= 0; i--) {
		      	var lat = markers[i].position.D;
			  	var lon = markers[i].position.k;
			  	var point = new google.maps.LatLng(lon,lat);
		      	if((google.maps.geometry.spherical.computeDistanceBetween(pos, point) / 1000) > 0.5){
		      		markers[i].setMap(null);
		        }
		      };
		      //calculates distance between two points in km's

		      map.setCenter(pos);
		    }, function() {
		      handleNoGeolocation(true);
		    });
		} else {
		    // Browser doesn't support Geolocation
		    handleNoGeolocation(false);
		}
		for (var i = markers.length - 1; i >= 0; i--) {
			markers[i].setMap(map);
			Events.update(markers[i].eventId, {$set: {visible: true}});
		};
		Session.set("scope","nearby");
	},
	'click #all':function(){
		for (var i = markers.length - 1; i >= 0; i--) {
			markers[i].setMap(map);
			Events.update(markers[i].eventId, {$set: {visible: true}});
		};
		Session.set("scope","all");
	}
});