
function createMarkers(response,style) {

  // Pull the "stations" property from response.data.
  var stations = response //.data.stations;
    // Initialize an array to hold bike markers.
  var StoreMarkers = [];
  
  // Loop through the stations array.
  for (var index = 0; index < stations.length; index++) {
    var station = stations[index];
    // console.log(style)
    // For each station, create a marker, and bind a popup with the station's name.
    var StoreMarker = L.marker([station.Store_Lat, station.Store_Long], style)
      .bindPopup("<h3>" + station.Store_Name + "<h3><h3>County: " + station.County_Name + "</h3>");

    // Add the marker to the bikeMarkers array.
    StoreMarkers.push(StoreMarker);
  }
  console.log(StoreMarkers)
  // Create a layer group that's made from the bike markers array, and pass it to the createMap function.
  // createMap(L.layerGroup(FastFoodMarkers));
  return L.layerGroup(StoreMarkers)
}

// function createMarkersFF(response) {

// Perform an API call to the Citi Bike API to get the station information. Call createMarkers when it completes.
// d3.json("resources/county_fast_food_final.json").then(createMarkersFF);
d3.json("http://127.0.0.1:5001/data1").then(function (ffdata) {
  d3.json("http://127.0.0.1:5001/data2").then(function (dsdata) {
   d3.json("http://127.0.0.1:5001/data3").then(function (grocerydata) {
    // Create the tile layer that will be the background of our map.
    var streetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });
    // console.log(ffdata,grocerydata)
    let FFLayer = createMarkers(ffdata,{color:'red'})
    let DSLayer = createMarkers(dsdata,{color:'blue'})
    let GroceryLayer = createMarkers(grocerydata,{color:'green'})
    // Create a baseMaps object to hold the streetmap layer.
    var baseMaps = {
      "Street Map": streetmap
    };
    
    
    // Create an overlayMaps object to hold the bikeStations layer.
    var overlayMaps = {
      "Fast Food Locations": FFLayer,
      "Grocery Store Locations": GroceryLayer,
      "Dollar Store Locations": DSLayer
    };
    
    // Create the map object with options.
    var map = L.map("map-id", {
      center: [33.7490, -84.3880],
      zoom: 12,
      layers: [streetmap, FFLayer]
    });
    
    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(map);
  });
});
});