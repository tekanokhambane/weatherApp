var activeLocation = null;

function showPreloader() {
	document.getElementById("preloader").style.display = "flex";
}

function hidePreloader() {
	document.getElementById("preloader").style.display = "none";
}

// Display a success toast
function showSuccessToast(message) {
	Toastify({
		text: message,
		duration: 3000, // 3 seconds
		gravity: "top", // Position the toast at the top of the screen
		backgroundColor: "green",
		close: true,
	}).showToast();
}

// Display an error toast
function showErrorToast(message) {
	Toastify({
		text: message,
		duration: 3000, // 3 seconds
		gravity: "top", // Position the toast at the top of the screen
		backgroundColor: "red",
		close: true,
	}).showToast();
}

function openDrawer() {
    document.getElementsByTagName("body")[0].style.overflow = "hidden";
    document.getElementById("drawer").style.visibility = "visible";
    document.getElementById("drawer").style.opacity = "1";
    document.getElementById("drawer").style.transform = "translateX(0)";
}
  
function closeDrawer() {
    document.getElementsByTagName("body")[0].style.overflow = "auto";
      document.getElementById("drawer").style.transform = "translateX(-100%)";
      document.getElementById("drawer").style.opacity = "0";
      document.getElementById("drawer").style.visibility = "hidden";
  }

document.addEventListener("DOMContentLoaded", function () {
	var form = document.getElementById("weather-form");
	var messageDiv = document.getElementById("message");
	const outputContainer = document.getElementById("output");

	form.addEventListener("submit", function (e) {
		e.preventDefault(); // Prevent the default form submission
		showPreloader();
		var formData = new FormData(form);

		fetch("/weather-search/", {
			method: "POST",
			body: formData,
			headers: {
				"X-Requested-With": "XMLHttpRequest", // Add this header to identify AJAX requests
			},
		})
			.then((response) => response.json())
			.then((data) => {
				if (data.data) {
					setTimeout(() => {
						hidePreloader();
						document.getElementById("weather-data").style.display = "none";
						document.getElementById("weather-tips").style.display = "none";
                        showSuccessToast(data.data.confirmation);
                        getLocations()

						outputContainer.innerHTML = `
                <div class="output-weather">
                    <div class="city">${data.data.city}</div>
                    <div class="temperature">${
											data.data.temperature
										} &deg; ${data.data.unit}</div>
                    <div class="description">${data.data.description}</div>
                    <img src="http://openweathermap.org/img/w/${
											data.data.icon
										}.png" alt="${data.data.description}">
                </div>
                <div class="suggestions">
                ${data.data.weather_tips.map((tip) => {
									return `
                    <div class="suggestion">${tip}</div>
                    `;
								}).join("")}
                </div>
            `;
					}, 100);
				} else {
					hidePreloader();
					showErrorToast("An error occurred. Please try again.");
					const outputContainer = document.getElementById("output");
					document.getElementById("weather-data").style.display = "none";
					document.getElementById("weather-tips").style.display = "none";
					outputContainer.innerHTML = `
                <div class="error">
                    <div class="">Error fetching data</div>
                </div>
            `;
				}
			})
			.catch((error) => {
				hidePreloader();
				console.error("Error:", error);
				const outputContainer = document.getElementById("output");
				outputContainer.innerHTML = `
                <div class="">
                    <div class="">Error fetching data</div>
                </div>
            `;
			})
			.finally(() => {
				hidePreloader();
			});
	});
});

function getLocations() {
	$(document).ready(function () {
		$.ajax({
			url: "/locations/", // Replace with the correct URL for your API
			type: "GET",
			success: function (response) {
				var locations = response;
				
                var locationsList = locations.locations.map((location) => {
                    
                    return `<div data-city="${location.city}" onClick="openDrawer()" class="location">${location.city}</div>`;
                }).join(""); // Join the array elements without a comma
                $("#locations").html(locationsList);

                 // Add click event listener to location elements
                 $(".location").click(function() {
                    var city = $(this).data("city");
                    fetchLocationData(city);
                });
			},
		});
	});
}

function getTips(index) {
    document.getElementById("tips-popup").style.display = "block";
    document.getElementById("tips-backdrop").style.display = "block";
    const tips = document.getElementById("tips-content").innerHTML = activeLocation.data[ index ]
        .weather_tips.map((tip) => {
            return `<div class="tip">${tip}</div>`
        }).join("");
    console.log(activeLocation.data[index]);
}

function closeTips() {
    document.getElementById("tips-popup").style.display = "none";
    document.getElementById("tips-backdrop").style.display = "none";
}

function fetchLocationData(city) {
    $.ajax({
        url: "/api/location/",
        type: "GET",
        data: { city: city },
        success: function(response) {
            console.log(response);
            activeLocation = response.data[ 0 ];
            console.log(activeLocation);
            var title = document.getElementById("drawer-title");
            title.innerText = response.data[0].city;
        
            document.getElementById("locations-list").innerHTML = response.data[0].data.map((item, index) => {
                return `<div data-index="${index}"  class="location-card">
                <img src="http://openweathermap.org/img/w/${ item.icon }.png" alt="">
                <div class="search-date">${ Date(item.moment) }</div>
                <div class="description" style="font-weight: bold">${ item.description }</div>
                <div class="temperature">${ item.temperature} &deg; ${item.unit }</div>
                <button class="tip-btn" onClick="getTips(${ index })">View Tips</button>
            </div>`
            }).join("");
            
            // Handle the location data here
            // Example: Update the UI with the location data
            $('#location').text(response.location);
        },
        error: function(xhr, status, error) {
            console.error('Error fetching location data:', error);
        }
    });
}



window.onload = getLocations();
