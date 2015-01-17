
if (Meteor.isClient) {
	Meteor.subscribe('polygons', 'bob-smith');
	Meteor.subscribe('events', 'bob-smith');
}

if (Meteor.isServer) {
  	Meteor.publish('polygons', function() {
	  return Polygons.find({}); 
	});
	Meteor.publish('events', function() {
	  return Events.find({}); 
	});
}


Meteor.startup(function(){
	//if(Posts.) Kolla om posts är empty
	//Posts.remove({});
	console.log("Startup");
	console.log(Polygons.find().count());
});