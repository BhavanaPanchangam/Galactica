const sparklesWrapper = document.querySelector(".sparkles-wrapper");

function createSparkle() {
  const sparkle = document.createElement("div");
  sparkle.classList.add("sparkle");
  const size = Math.random() * 3 + 2;

  // Sparkle styles
  sparkle.style.width = `${size}px`;
  sparkle.style.height = `${size}px`;
  sparkle.style.position = "absolute";
  sparkle.style.borderRadius = "50%";
  sparkle.style.backgroundColor = " #9B87F5";
  sparkle.style.top = `${Math.random() * 100}%`;
  sparkle.style.left = `${Math.random() * 100}%`;
  sparkle.style.animation = `sparkleMove ${Math.random() * 10 + 20}s linear infinite`;

  sparklesWrapper.appendChild(sparkle);

  // Remove sparkle after animation
  sparkle.addEventListener("animationend", () => {
    sparkle.remove();
  });
}

// Generate sparkles at intervals
setInterval(createSparkle, 120); // Adjust interval for more or fewer sparkles

// CSS for sparkle animation
const style = document.createElement("style");
style.innerHTML = `
  @keyframes sparkleMove {
    0% {
      opacity: 1;
      transform: translateY(0) scale(1);
    }
    100% {
      opacity: 0;
      transform: translateY(100vh) scale(0.5);
    }
  }
  .sparkle {
    opacity: 0;
  }
`;
document.head.appendChild(style);



const dockItems = document.querySelectorAll(".dock-item");

dockItems.forEach(item => {
  item.addEventListener("mousemove", () => {
    item.style.transform = "translateY(-10px) scale(1.2)";
  });

  item.addEventListener("mouseleave", () => {
    item.style.transform = "translateY(0) scale(1)";
  });
});
