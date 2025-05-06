window.main = async function () {
  console.log("Starting Math Quest...");

  // Hide loading
  document.getElementById("loading").style.display = "none";
  document.getElementById("loading-container").style.display = "none";

  console.log("Math Quest initialized.");
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
