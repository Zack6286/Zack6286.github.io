window.main = async function () {
  console.log("Starting Math Quest...");

  // Show canvas for the game
  document.getElementById("canvas").style.display = "block";

  // Simulate async setup (you can replace this with actual loading hooks if needed)
  await new Promise(resolve => setTimeout(resolve, 1000));

  // Hide loading UI
  document.getElementById("loading").style.display = "none";
  document.getElementById("loading-container").style.display = "none";

  console.log("Math Quest ready.");
};

document.addEventListener("DOMContentLoaded", () => {
  if (typeof window.main === "function") {
    window.main().catch(err => {
      console.error("Load failed:", err);
      document.getElementById("loading").style.display = "none";
      document.getElementById("error").style.display = "block";
    });
  }
});
