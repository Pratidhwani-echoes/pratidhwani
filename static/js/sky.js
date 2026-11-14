/* The only behaviour JavaScript owns: pointer parallax. Everything else is Python. */
(() => {
  const root = document.documentElement;
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  let frame = 0;
  let targetX = 0;
  let targetY = 0;

  if (reduce.matches) {
    return;
  }

  const apply = () => {
    frame = 0;
    root.style.setProperty("--mx", targetX.toFixed(4));
    root.style.setProperty("--my", targetY.toFixed(4));
  };

  const onMove = (event) => {
    const width = window.innerWidth || 1;
    const height = window.innerHeight || 1;
    targetX = (event.clientX / width - 0.5) * 2;
    targetY = (event.clientY / height - 0.5) * 2;
    if (!frame) {
      frame = window.requestAnimationFrame(apply);
    }
  };

  window.addEventListener("pointermove", onMove, { passive: true });
  window.addEventListener("pointerleave", () => {
    targetX = 0;
    targetY = 0;
    if (!frame) {
      frame = window.requestAnimationFrame(apply);
    }
  });
  reduce.addEventListener("change", (event) => {
    if (event.matches) {
      targetX = 0;
      targetY = 0;
      apply();
    }
  });
})();
