window.addEventListener("load", () => {
  const loadingMessage = document.getElementById('loading');
  const errorMessage = document.getElementById('error');

  // Fetch the main.data file (JSON format)
  fetch('main.data')  // Assuming 'main.data' is a JSON file in the same directory
    .then(response => response.json())  // Parse the response as JSON
    .then(data => {
      // If the data contains the required keys, update the messages
      loadingMessage.textContent = data.loadingMessage || '🔄 Loading game...';  // Default loading message
      errorMessage.textContent = data.errorMessage || '❌ Failed to load the game.';  // Default error message

      console.log('Game data loaded:', data);
    })
    .catch(err => {
      // If fetching the data fails or JSON is malformed, show error
      console.error("Error loading data:", err);
      loadingMessage.style.display = 'none';  // Hide loading message if error occurs
      errorMessage.style.display = 'block';  // Show error message
    });

  // Event listener for when pygbag (game) is ready
  window.addEventListener("pygbag:ready", () => {
    loadingMessage.textContent = '🧠 Game running!';  // Update loading message when game is ready
    errorMessage.style.display = 'none';  // Hide error message when game is ready
  });

  // Timeout to handle situations where pygbag might not load correctly
  setTimeout(() => {
    if (!window.pygbag) {
      // If pygbag is not loaded after 10 seconds, show error message
      loadingMessage.style.display = 'none';
      errorMessage.style.display = 'block';  // Show error message
    }
  }, 10000);  // Timeout after 10 seconds
});
