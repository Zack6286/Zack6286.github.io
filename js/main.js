// Your custom JavaScript logic goes here
window.addEventListener("load", () => {
  const loadingMessage = document.getElementById('loading');
  const errorMessage = document.getElementById('error');

  window.addEventListener("pygbag:ready", () => {
    loadingMessage.textContent = '🧠 Game running!';
  });

  setTimeout(() => {
    if (!window.pygbag) {
      loadingMessage.style.display = 'none';
      errorMessage.style.display = 'block';
    }
  }, 10000); // Timeout after 10 seconds
});
