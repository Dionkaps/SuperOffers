
function fetchUserData() {
  fetch('fetchUserData.php')
  .then(response => response.json())
  .then(data => {
      if (data.status === 'success') {
          const userData = data.data;
          const userDataContainer = document.getElementById('userData');
          userDataContainer.innerHTML = ''; // Clear previous data

          const userRow = document.createElement('tr');
          const currentTokens = document.createElement('td');
          const currentScore = document.createElement('td');
          const totalScore = document.createElement('td');

          currentTokens.textContent = userData.current_tokens;
          currentScore.textContent = userData.current_score;
          totalScore.textContent = userData.total_score;

          userRow.appendChild(currentTokens);
          userRow.appendChild(currentScore);
          userRow.appendChild(totalScore);

          userDataContainer.appendChild(userRow);
      } else {
          alert(data.message); // Display an error alert
      }
  })
  .catch(error => {
      console.error('Error fetching user data:', error);
  });
}


document.addEventListener('DOMContentLoaded', function () {
  const updateForm = document.getElementById('updateForm');

  updateForm.addEventListener('submit', function (e) {
      e.preventDefault(); // Prevent the form from submitting normally
      submitForm(); // Call the submitForm function
  });
  function fetchRatingData() {
    fetch('fetch_userRating.php')
    .then(response => response.json())
    .then(data => {
        const ratingData = document.getElementById('ratingData');
        ratingData.innerHTML = ''; // Clear previous data

        if (data.status === 'success') {
            const ratingDataArray = data.odata;
            console.log(ratingDataArray);
            if (Array.isArray(ratingDataArray) && ratingDataArray.length > 0) {
                ratingDataArray.forEach(entry => {
                    const row = document.createElement('tr');
                    const productId = document.createElement('td');
                    const shopId = document.createElement('td');
                    const date = document.createElement('td');

                    productId.textContent = entry.product_id;
                    shopId.textContent = entry.shop_id;
                    date.textContent = entry.date;

                    row.appendChild(productId);
                    row.appendChild(shopId);
                    row.appendChild(date);

                    ratingData.appendChild(row);
                });
            } else {
                const noDataRow = document.createElement('tr');
                const noDataCell = document.createElement('td');
                noDataCell.colSpan = 3;
                noDataCell.textContent = 'No rating data available.';
                noDataRow.appendChild(noDataCell);
                ratingData.appendChild(noDataRow);
            }
        } else {
            alert(data.message); // Display an error alert
        }
    })
    .catch(error => {
        console.error('Error fetching rating data:', error);
    });
}

  // Initial fetch and display of user data and rating data
  fetchUserData();
  fetchRatingData()
});