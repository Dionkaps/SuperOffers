
        const itemsPerPage = 10;
        let currentPage = 1;

        function displayData(data) {
            const leaderboardBody = document.getElementById('leaderboard-body');
            leaderboardBody.innerHTML = '';

            const startIndex = (currentPage - 1) * itemsPerPage;
            const endIndex = startIndex + itemsPerPage;

            for (let i = startIndex; i < endIndex && i < data.length; i++) {
                const user = data[i];
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${i + 1}</td>
                    <td>${user.username}</td>
                    <td>${user.total_score}</td>
                    <td>${user.token_count}</td>
                `;
                leaderboardBody.appendChild(row);
            }
        }

        function displayPagination(data) {
            const paginationDiv = document.getElementById('pagination');
            paginationDiv.innerHTML = '';

            const numPages = Math.ceil(data.length / itemsPerPage);

            for (let i = 1; i <= numPages; i++) {
                const pageButton = document.createElement('button');
                pageButton.textContent = i;
                pageButton.addEventListener('click', () => {
                    currentPage = i;
                    displayData(data);
                });
                paginationDiv.appendChild(pageButton);
            }
        }

        // Fetch user data from PHP 
        fetch('fetchScore.php')
            .then(response => response.json())
            .then(data => {
                displayData(data);
                displayPagination(data);
            })
            .catch(error => console.error(error));