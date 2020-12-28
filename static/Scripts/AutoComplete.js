let startCitiesUl = document.getElementById('startCities');
$(document).ready(function(){
    $("#sourceCountry").on("input",function(e){                      
        $("#startCities").empty();
        if ($("#sourceCountry").val() !== "") {
          $.ajax({
            method:"post",
            url:"/livesearch",
            data:{text:$("#sourceCountry").val()},
            success:function(res){  
                $.each(res,function(index,value){
                  let listElement = document.createElement('li')
                  listElement.innerText = value.city + ', ' + value.state ;
                  listElement.addEventListener('click', () => {
                      chooseStartCity(value.city);
                  }, false);
                  startCitiesUl.appendChild(listElement)
                });                                                                                                     
            }
          });
        }                         
    });
});

$(document).ready(function() {
    $("#sourceCountry").on("input",function(e){
      if ($("#sourceCountry").val() == "") {
        $("#startCities").empty();
      }
    });
});

function chooseStartCity(city) {
  $("#sourceCountry").val(city)
  $("#startCities").empty();
}



let destCitiesUl = document.getElementById('destinationCities');
$(document).ready(function(){
    $("#destinationCountry").on("input",function(e){                      
        $("#destinationCities").empty();
        if ($("#destinationCountry").val() !== "") {
            $.ajax({
            method:"post",
            url:"/livesearch",
            data:{text:$("#destinationCountry").val()},
            success:function(res){  
                $.each(res,function(index,value){
                    let listElement = document.createElement('li')
                    listElement.innerText = value.city + ', ' + value.state;
                    listElement.addEventListener('click', () => {
                        chooseDestinationCity(value.city);
                    }, false);
                    destCitiesUl.appendChild(listElement)
                });                                                                                                     
            }
            });
        }                         
    });
});

$(document).ready(function() {
    $("#destinationCountry").on("input",function(e) {
        if ($("#destinationCountry").val() == "") {
        $("#destinationCities").empty();
        }
    });
});

function chooseDestinationCity(city) {
    $("#destinationCountry").val(city)
    $("#destinationCities").empty();
}


function processCities(result) {
    if ($.isEmptyObject(result)) {
        return
    }
    let startCity = result[0][0]
    let destCity = result[1][0]
    return [startCity, destCity]               
    }

function sendFilters() {
    parks = document.getElementById("parksCheckbox");
    campsites = document.getElementById("campsCheckbox");
    airbnb = document.getElementById("airbnbCheckbox");
    const list = []
    if (parks.checked) 
        list.push("parks")

    if (campsites.checked) 
        list.push("campsites")

    if (airbnb.checked) 
        list.push("airbnb")
    
    $.ajax({
        type: "POST",
        contentType: 'application/json;charset=UTF-8',
        url: "http://127.0.0.1:5000/locations",
        data: JSON.stringify({filterList: list}),
        success: function(result) {
            addLocationToMap(result[0])                    
            addLocationToMap(result[9400])    
        },
        error: function(result) {
            alert('error at filters');
        },
        dataType: "json",
    });                              
}
    

$("#plantrip").click(function(e) {
e.preventDefault();
const sourceCity = $("#sourceCountry").val()
const destCity = $("#destinationCountry").val()
$.ajax({
    type: "POST",
    contentType: 'application/json;charset=UTF-8',
    url: "http://127.0.0.1:5000/cities/start_cities",
    data: JSON.stringify({cities: [sourceCity, destCity]}),
    success: function(result) {
        const cities = processCities(result)
        addCityToMap(cities[0])
        addCityToMap(cities[1])
        sendFilters()
    },
    error: function(result) {
        alert('error: unable to submit');
    },
    dataType: "json",
});
});



function hideSearch() {
const searchDiv = document.getElementById("trip-locations")
searchDiv.style.display = "none"
    const locationsDiv =  document.getElementById("locations")
    locationsDiv.style.display = "block"
}

