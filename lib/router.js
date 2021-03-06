Router.configure({
  layoutTemplate: 'layout',
  loadingTemplate: 'loading',
  waitOn: function() { return [Meteor.subscribe('events'),Meteor.subscribe('polygons')]; }
});

Router.route('/', function(){
	var polygons = Polygons.find({}).fetch();
	var events = Events.find({}).fetch();
    this.render('mapPage', {data: [polygons,events]});
});

//Router.route('/',{name:"mapPage"});

/*Router.route('/posts/:_id', {
  name: 'postPage',
  data: function() { return Posts.findOne(this.params._id); }
});*/