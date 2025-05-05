export async function main() {
  // Create canvas and add it to the document
  const canvas = document.createElement('canvas');
  document.body.appendChild(canvas);

  const ctx = canvas.getContext('2d');

  // Resize the canvas to fill the screen
  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();

  // Draw welcome message
  ctx.fillStyle = '#fff';
  ctx.font = 'bold 48px sans-serif';
  ctx.textAlign = 'center';
  ctx.fillText('Welcome to Math Quest!', canvas.width / 2, canvas.height / 2);
}
