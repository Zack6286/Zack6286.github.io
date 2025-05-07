window.addEventListener("load", () => {
  const loadingMessage = document.getElementById('loading');
  const errorMessage = document.getElementById('error');

  // Fetch the main.data file
  fetch('main.data')  // Assuming 'main.data' is a JSON file located in the same directory
    .then(response => response.json())  // Parse the JSON content
    .then(data => {
      // Update the loading message and error message with the data from main.data
      loadingMessage.textContent = data.loadingMessage || '🔄 Loading game...';  // Fallback message if the property is missing
      errorMessage.textContent = data.errorMessage || '❌ Failed to load the game.';  // Fallback message

      // You can add additional data handling here if you have more fields in your JSON
      console.log('Game data loaded:', data);
    })
    .catch(err => {
      // Handle error if the fetch fails or data is corrupted
      console.error("Error loading data:", err);
      loadingMessage.style.display = 'none';
      errorMessage.style.display = 'block';  // Show error message if loading fails
    });

  // Wait for pygbag to be ready (game loading)
  window.addEventListener("pygbag:ready", () => {
    loadingMessage.textContent = '🧠 Game running!';
    errorMessage.style.display = 'none';  // Hide error message if the game is successfully loaded
  });

  // Timeout to handle situations where pygbag might not load correctly
  setTimeout(() => {
    if (!window.pygbag) {
      loadingMessage.style.display = 'none';
      errorMessage.style.display = 'block';  // Show the error message if pygbag does not load after timeout
    }
  }, 10000);  // 10 seconds timeout
});
