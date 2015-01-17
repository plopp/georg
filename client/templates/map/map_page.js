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
	    zoom: 15,
	    center: new google.maps.LatLng(57.13,11.87)
	  };
	  var map = new google.maps.Map(document.getElementById('map'),mapOptions);

	  /*google.maps.event.addListener(map, 'click', function(e) {
	    placeMarker(e.latLng, map);
	  }); */
	  //console.log(this.data[0]);
	  var polygonCoords = [];
	  for(var i = 0;i<this.data.length;i++){
		  for(var j = 0;j<this.data[i].coordinates.length;j++){
		    var position = new google.maps.LatLng(this.data[i].coordinates[j].lat,this.data[i].coordinates[j].lon);
		    polygonCoords.push(position);
			/*var marker = new google.maps.Marker({
				position: position,
				map:map
			});*/
			console.log(this.data[i].coordinates[j]);
		  }
	  }

	  curpolygon = new google.maps.Polygon({
	    paths: polygonCoords,
	    strokeColor: '#FF0000',
	    strokeOpacity: 0.8,
	    strokeWeight: 3,
	    fillColor: '#FF0000',
	    fillOpacity: 0.35
	  });
	  curpolygon.setMap(map);
	  map.panTo(position);

	  google.maps.event.addListener(curpolygon, 'click', isInsidePolygon);
	  google.maps.event.addListener(map, 'click', isInsideMap);

	  function isInsidePolygon(data){
	  	var lat = data.latLng.D;
	  	var lon = data.latLng.k;
	  	var point = new google.maps.LatLng(lon,lat);

	  	console.log(data.latLng);
	  	if (curpolygon.Contains(point)) { // point is inside polygon 
		  	console.log("Contains");
		}
		else{
		  	console.log("Does not contain");
		}
	  }

	  function isInsideMap(data){
	  	var lat = data.latLng.D;
	  	var lon = data.latLng.k;
	  	var point = new google.maps.LatLng(lon,lat);

	  	console.log(data.latLng);
	  	if (curpolygon.Contains(point)) { // point is inside polygon 
		  	//console.log("Contains");
		}
		else{
		  	//console.log("Does not contain");
		}
	  }


	  //var point = new google.maps.LatLng(52.05249047600099, -0.6097412109375); 
	  
	/*function placeMarker(position, map) {
	  var marker = new google.maps.Marker({
	    position: position,
	    map: map
	  });
	  map.panTo(position);
	}	*/
}