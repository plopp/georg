Gerog API cronjobs
==================

This is a collection of scripts to collect data from various sources,
and send it into the collection api of meteor. The objects created are
described below in pretend-JSON ([] is an array, {} a hash, : delimits
key and value...).

Position objects
----------------

    [
      {
        id : unique position ID,
        name : Marker name,
        description : Description,
        category : E.g. "concert", "popupstore", ...,
        source : e.g. data.göteborg.se, ...
        creationTime : When the marker was created,
        location : {
          lon : Longitude,
          lat : Latitude
        },
        radius : Relevant radius for the marker,
        events : [
          event id,
          another event id,
          ...
        ]
      },
      {
        ...
      },
      ...
    ]

Event objects
-------------

    [
      {
        id : unique event ID,
        description : Describing the event (at the position),
        startTime : When the event starts,
        endTime : When the party is over
      },
      {
        ...
      },
      ...
    ]
