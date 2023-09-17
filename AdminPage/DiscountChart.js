let myChart; 

        document.getElementById("submitBtn").addEventListener("click", function() {
            const selectedMonthYear = document.getElementById("monthYearInput").value;

            // AJAX request
            fetch(`FetchDiscountDay.php?monthYear=${selectedMonthYear}`)
                .then(response => response.json())
                .then(data => {
                    
                    const daysInMonth = getDaysInMonth(selectedMonthYear);

                    // Clear an yparxei hdh
                    if (myChart) {
                        myChart.destroy();
                    }

                    // Create the chart with data, including missing days
                    createChart(data, daysInMonth);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });

        function createChart(data, daysInMonth) {
            const ctx = document.getElementById("chart").getContext("2d");

            // Extract the days and entry counts from the data
            const days = Object.keys(data);
            const entryCounts = Object.values(data);

            // pinakas me ola ta entries sto discount gia oles ti meres tou mhna
            const allEntryCounts = daysInMonth.map(day => (data[day] || 0));

            myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: daysInMonth,
                    datasets: [{
                        label: 'Number of Entries',
                        data: allEntryCounts,
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Number of Entries'
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Day of the Month'
                            }
                        }
                    }
                }
            });
        }
//lista me oles tis meres anexarthta apo to an exoun entry 
        function getDaysInMonth(selectedMonthYear) {
            const [year, month] = selectedMonthYear.split('-');
            const lastDay = new Date(year, month, 0).getDate();
            const daysInMonth = [];

            for (let day = 1; day <= lastDay; day++) {
                daysInMonth.push(`${year}-${month}-${day.toString().padStart(2, '0')}`);
            }

            return daysInMonth;
        }