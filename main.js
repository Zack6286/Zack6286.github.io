window.onload = function() {
    const loadingMessage = document.getElementById('loading');
    const errorMessage = document.getElementById('error');

    // Initialize Pygbag to run the Python game
    const pygbagScript = document.createElement('script');
    pygbagScript.src = 'pygbag.js'; // Path to the pygbag runtime
    pygbagScript.onload = () => {
        // If pygbag loads successfully, run the Python game
        loadingMessage.innerText = '🧠 Game is ready!';
        import('./main.py').then(() => {
            console.log('Python game initialized');
        }).catch((err) => {
            console.error('Failed to load the Python game', err);
            errorMessage.style.display = 'block';
        });
    };

    pygbagScript.onerror = () => {
        // If pygbag fails to load, show an error message
        loadingMessage.innerText = '⚠️ Failed to load Pygbag.';
        errorMessage.style.display = 'block';
    };

    document.body.appendChild(pygbagScript);
};
