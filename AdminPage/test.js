document.addEventListener("DOMContentLoaded", function () {
    const chartForm = document.getElementById("chartForm");
    const chartContainer = document.getElementById("chartContainer");
    const discountChart = document.getElementById("discountChart");

    chartForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const selectedMonth = document.getElementById("month").value;
        const selectedYear = document.getElementById("year").value;

        // Make an AJAX request to fetch data from PHP
        fetch(`test.php?month=${selectedMonth}&year=${selectedYear}`)
            .then(response => response.json())
            .then(data => {
                // Data format: { "1": 10, "2": 15, "3": 5, ... }

                const labels = Object.keys(data).map(day => `${selectedYear}-${selectedMonth}-${day}`);
                const discounts = Object.values(data);

                // Create the chart using Chart.js
                new Chart(discountChart, {
                    type: "line",
                    data: {
                        labels: labels,
                        datasets: [{
                            label: "Discounts",
                            data: discounts,
                            borderColor: "blue",
                            fill: false
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false
                    }
                });

                // Show the chart container
                chartContainer.style.display = "block";
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
    });
});
