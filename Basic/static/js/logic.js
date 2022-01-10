function createMap(FastFoodStations) {

  // Create the tile layer that will be the background of our map.
  var streetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  });


  // Create a baseMaps object to hold the streetmap layer.
  var baseMaps = {
    "Street Map": streetmap
  };

  // Create an overlayMaps object to hold the bikeStations layer.
  var overlayMaps = {
    "Fast Food Locations": FastFoodStations
  };

  // Create the map object with options.
  var map = L.map("map-id", {
    center: [33.7490, -84.3880],
    zoom: 12,
    layers: [streetmap, FastFoodStations]
  });

  // Create a layer control, and pass it baseMaps and overlayMaps. Add the layer control to the map.
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(map);
}

function createMarkersFF(response) {

  // Pull the "stations" property from response.data.
  var stations = response //.data.stations;
    // console.log(stations)
  // Initialize an array to hold bike markers.
  var FastFoodMarkers = [];

  // Loop through the stations array.
  for (var index = 0; index < stations.length; index++) {
    var station = stations[index];
    // console.log(station)
    // For each station, create a marker, and bind a popup with the station's name.
    var FastFoodMarker = L.marker([station.Store_Lat, station.Store_Long])
      .bindPopup("<h3>" + station.name + "<h3><h3>Capacity: " + station.capacity + "</h3>");

    // Add the marker to the bikeMarkers array.
    FastFoodMarkers.push(FastFoodMarker);
  }

  // Create a layer group that's made from the bike markers array, and pass it to the createMap function.
  createMap(L.layerGroup(FastFoodMarkers));
}

// Perform an API call to the Citi Bike API to get the station information. Call createMarkers when it completes.
d3.json("resources/county_fast_food_final.json").then(createMarkersFF);

