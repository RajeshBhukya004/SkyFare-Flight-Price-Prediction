
document.addEventListener("DOMContentLoaded", function () {
    const sourceCity = document.getElementById("source_city");
    const destinationCity = document.getElementById("destination_city");
    const swapButton = document.getElementById("swapCities");
    const flightForm = document.getElementById("flightForm");

    // Swap departure and destination cities
    if (swapButton && sourceCity && destinationCity) {
        swapButton.addEventListener("click", function () {
            const originalSource = sourceCity.value;

            sourceCity.value = destinationCity.value;
            destinationCity.value = originalSource;
        });
    }

    // Validate the form and show a loading state
    if (flightForm) {
        flightForm.addEventListener("submit", function (event) {
            if (
                sourceCity &&
                destinationCity &&
                sourceCity.value === destinationCity.value
            ) {
                event.preventDefault();

                alert("Please choose two different cities.");
                return;
            }

            // Let the browser validate required fields first
            if (!flightForm.checkValidity()) {
                event.preventDefault();
                flightForm.reportValidity();
                return;
            }

            const predictButton = flightForm.querySelector(
                ".predict-button"
            );

            if (predictButton) {
                predictButton.disabled = true;
                predictButton.textContent = "Comparing fares...";
            }
        });
    }

    // After Flask returns the page, bring the results into view
    const results = document.getElementById("prediction-result");
    const errorMessage = document.getElementById("prediction-error");

    if (results || errorMessage) {
        const target = results || errorMessage;

        // A short delay lets the browser finish laying out the page
        window.setTimeout(function () {
            target.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }, 100);
    }
});

/* Sort and filter flight cards */
document.addEventListener("DOMContentLoaded", function () {
    const sortSelect = document.getElementById("sortFlights");
    const filterSelect = document.getElementById("filterAirline");
    const resultsContainer = document.getElementById("prediction-result");

    if (!sortSelect || !filterSelect || !resultsContainer) {
        return;
    }

    function updateFlights() {
        const cards = Array.from(
            resultsContainer.querySelectorAll(".flight-option")
        );

        const sortBy = sortSelect.value;
        const selectedAirline = filterSelect.value;

        cards.sort(function (a, b) {
            if (sortBy === "price-low") {
                return Number(a.dataset.price) - Number(b.dataset.price);
            }

            if (sortBy === "price-high") {
                return Number(b.dataset.price) - Number(a.dataset.price);
            }

            return a.dataset.airline.localeCompare(b.dataset.airline);
        });

        cards.forEach(function (card) {
            const matches =
                selectedAirline === "all" ||
                card.dataset.airline === selectedAirline;

            card.hidden = !matches;
            resultsContainer.appendChild(card);
        });
    }
    
    const visibleCount = cards.filter(function (card) {
        return !card.hidden;
    }).length;

    const countElement = document.getElementById("resultsCount");

    if (countElement) {
        countElement.textContent =
            `Showing ${visibleCount} of ${cards.length} flight options`;
    }

    sortSelect.addEventListener("change", updateFlights);
    filterSelect.addEventListener("change", updateFlights);

    updateFlights();
});
const clearButton = document.getElementById("clearFlightFilters");

if (clearButton) {
    clearButton.addEventListener("click", function () {
        sortSelect.value = "price-low";
        filterSelect.value = "all";
        updateFlights();
    });
}