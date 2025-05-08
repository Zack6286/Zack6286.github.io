window.addEventListener("load", () => {
  const loadingMessage = document.getElementById('loading');
  const errorMessage = document.getElementById('error');
  const generalErrors = document.getElementById('general-errors');

  // Attempt to fetch dynamic messages from main.data (JSON)
  fetch('main.data')
    .then(response => {
      if (!response.ok) {
        throw new Error("main.data not found");
      }
      return response.json();
    })
    .then(data => {
      // Update messages if values exist
      loadingMessage.textContent = data.loadingMessage || '🔄 Loading game...';
      errorMessage.textContent = data.errorMessage || '❌ Failed to load the game.';
      if (data.generalErrors) {
        generalErrors.textContent = data.generalErrors;
        generalErrors.style.display = 'block';
      }
      console.log('✅ Game data loaded:', data);
    })
    .catch(err => {
      console.warn("⚠️ Could not load main.data:", err);
      loadingMessage.textContent = '🔄 Loading game...';  // Default fallback
    });

  // Show success message when Pygbag signals it's ready
  window.addEventListener("pygbag:ready", () => {
    loadingMessage.textContent = '🧠 Game running!';
    errorMessage.style.display = 'none';
    generalErrors.style.display = 'none';
  });

  // Fallback timeout: Show error message if pygbag doesn't initialize
  setTimeout(() => {
    if (!window.pygbag || !window.pygbag.main) {
      loadingMessage.style.display = 'none';
      errorMessage.style.display = 'block';
      generalErrors.textContent = '⚠️ Game engine failed to initialize.';
      generalErrors.style.display = 'block';
    }
  }, 10000); // 10-second timeout
});
