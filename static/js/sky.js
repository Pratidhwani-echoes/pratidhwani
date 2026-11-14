/* The Unfinished Constellation - Celestial Atmosphere, Parallax & Audio */
(() => {
  const root = document.documentElement;
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  let frame = 0;
  let targetX = 0;
  let targetY = 0;

  const apply = () => {
    frame = 0;
    root.style.setProperty("--mx", targetX.toFixed(4));
    root.style.setProperty("--my", targetY.toFixed(4));
  };

  const onMove = (event) => {
    if (reduce.matches) return;
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

  /* -------------------------------------------------- Random Shooting Stars */
  const shootingContainer = document.getElementById("shooting-stars") || document.querySelector(".sky");
  let shootingTimer = null;
  let twinTimer = null;

  function clearAllShootingStars() {
    if (shootingTimer) {
      clearTimeout(shootingTimer);
      shootingTimer = null;
    }
    if (twinTimer) {
      clearTimeout(twinTimer);
      twinTimer = null;
    }
    if (shootingContainer) {
      const activeStars = shootingContainer.querySelectorAll(".shooting-star");
      activeStars.forEach((star) => star.remove());
    }
  }

  function spawnShootingStar() {
    // If window is inactive or reduced motion requested, do NOT spawn
    if (document.hidden || reduce.matches || !shootingContainer) return;

    // Guard against accumulation: max 3 active stars at once
    if (shootingContainer.querySelectorAll(".shooting-star").length >= 3) return;

    const star = document.createElement("span");
    star.className = "shooting-star";

    // Randomize starting location in upper/right sky
    const startX = Math.random() * 70 + 25; // 25% to 95%
    const startY = Math.random() * 40 - 5;  // -5% to 35%

    // Classic shooting star diagonal angle (around 315deg / -45deg)
    // with slight natural variation between 311deg and 319deg
    const angle = 315 + (Math.random() * 8 - 4);

    // Travel distance: negative because it travels down-left, opposite of the tail
    const distance = -(Math.random() * 260 + 380); // -380px to -640px

    // Tail length & speed
    const tailLength = Math.random() * 80 + 100; // 100px - 180px
    const duration = (Math.random() * 0.45 + 0.85).toFixed(2); // 0.85s - 1.30s

    star.style.left = `${startX}%`;
    star.style.top = `${startY}%`;
    star.style.setProperty("--tail-length", `${tailLength.toFixed(0)}px`);
    star.style.setProperty("--angle", `${angle.toFixed(1)}deg`);
    star.style.setProperty("--travel", `${distance.toFixed(0)}px`);
    star.style.animation = `shooting-star-streak ${duration}s cubic-bezier(0.2, 0.7, 0.4, 1) forwards`;

    // 25% chance of warm accent tint instead of electric white/blue
    if (Math.random() < 0.25) {
      star.classList.add("is-gold");
    }

    shootingContainer.appendChild(star);

    // Guaranteed removal on animation end OR safety timer
    const maxLifetime = parseFloat(duration) * 1000 + 350;
    const safetyTimeout = setTimeout(() => {
      star.remove();
    }, maxLifetime);

    star.addEventListener("animationend", () => {
      clearTimeout(safetyTimeout);
      star.remove();
    }, { once: true });
  }

  function scheduleNextShootingStar(delay) {
    if (document.hidden || reduce.matches) return;
    if (shootingTimer) clearTimeout(shootingTimer);

    const nextDelay = delay !== undefined ? delay : (Math.random() * 3000 + 2200); // 2.2s to 5.2s
    shootingTimer = setTimeout(() => {
      if (document.hidden || reduce.matches) return;
      spawnShootingStar();

      // 30% chance for a rapid twin shooting star
      if (Math.random() < 0.3) {
        twinTimer = setTimeout(() => {
          if (!document.hidden && !reduce.matches) {
            spawnShootingStar();
          }
        }, Math.random() * 280 + 160);
      }
      scheduleNextShootingStar();
    }, nextDelay);
  }

  // Handle window visibility: stop spawning & clean up when hidden, resume fresh when visible
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) {
      clearAllShootingStars();
    } else {
      if (!reduce.matches) {
        scheduleNextShootingStar(800);
      }
    }
  });

  window.addEventListener("blur", () => {
    clearAllShootingStars();
  });

  window.addEventListener("focus", () => {
    if (!document.hidden && !reduce.matches) {
      scheduleNextShootingStar(1000);
    }
  });

  if (!document.hidden && !reduce.matches) {
    // Initial shooting stars shortly after page load
    scheduleNextShootingStar(700);
  }

  /* -------------------------------------------------- Background Music (BGM) */
  const bgm = document.getElementById("bgm");
  const audioToggle = document.getElementById("audio-toggle");
  const audioIcon = document.getElementById("audio-icon");
  const audioLabel = document.getElementById("audio-label");

  if (bgm && audioToggle) {
    const STORAGE_KEY = "pratidhwani_bgm_state";
    let isPlaying = false;
    let pausedForVisibility = false;

    const updateAudioUI = (playing) => {
      isPlaying = playing;
      if (playing) {
        audioToggle.classList.add("is-playing");
        if (audioIcon) audioIcon.className = "bi bi-volume-up-fill";
        if (audioLabel) audioLabel.textContent = "Music";
        audioToggle.setAttribute("title", "Mute background music");
      } else {
        audioToggle.classList.remove("is-playing");
        if (audioIcon) audioIcon.className = "bi bi-volume-mute-fill";
        if (audioLabel) audioLabel.textContent = "Muted";
        audioToggle.setAttribute("title", "Play background music");
      }
    };

    const playBgm = () => {
      bgm.volume = 0.45;
      const playPromise = bgm.play();
      if (playPromise !== undefined) {
        playPromise
          .then(() => {
            updateAudioUI(true);
            localStorage.setItem(STORAGE_KEY, "playing");
          })
          .catch(() => {
            // Browser autoplay policy blocked until gesture
            updateAudioUI(false);
          });
      }
    };

    const pauseBgm = () => {
      bgm.pause();
      updateAudioUI(false);
      localStorage.setItem(STORAGE_KEY, "muted");
    };

    audioToggle.addEventListener("click", () => {
      if (bgm.paused) {
        playBgm();
      } else {
        pauseBgm();
      }
    });

    // Check remembered state across page transitions
    const savedState = localStorage.getItem(STORAGE_KEY);
    if (savedState === "playing") {
      playBgm();
      const resumeOnGesture = () => {
        if (localStorage.getItem(STORAGE_KEY) === "playing" && bgm.paused) {
          playBgm();
        }
        window.removeEventListener("pointerdown", resumeOnGesture);
        window.removeEventListener("keydown", resumeOnGesture);
      };
      window.addEventListener("pointerdown", resumeOnGesture, { once: true });
      window.addEventListener("keydown", resumeOnGesture, { once: true });
    } else {
      updateAudioUI(false);
    }

    // Pause audio when window is hidden, resume when visible if it was playing
    document.addEventListener("visibilitychange", () => {
      if (document.hidden) {
        if (!bgm.paused) {
          bgm.pause();
          pausedForVisibility = true;
        }
      } else {
        if (pausedForVisibility) {
          pausedForVisibility = false;
          if (localStorage.getItem(STORAGE_KEY) === "playing") {
            playBgm();
          }
        }
      }
    });
  }

  /* ------------------------------------- Bright Added Star Celebration Particle FX */
  const newStar = document.querySelector(".star.is-new");
  if (newStar) {
    setTimeout(() => {
      const rect = newStar.getBoundingClientRect();
      const originX = rect.left + rect.width / 2;
      const originY = rect.top + rect.height / 2;

      // Create burst container fixed over viewport
      const particleContainer = document.createElement("div");
      particleContainer.className = "star-burst-particles";
      particleContainer.setAttribute("aria-hidden", "true");
      document.body.appendChild(particleContainer);

      const particleCount = 30;
      const accent = getComputedStyle(newStar).getPropertyValue("--accent") || "#ffd9a3";

      for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement("span");
        particle.className = "burst-particle";
        const pAngle = (Math.PI * 2 * i) / particleCount + (Math.random() - 0.5) * 0.4;
        const pDist = Math.random() * 95 + 45;
        const pX = Math.cos(pAngle) * pDist;
        const pY = Math.sin(pAngle) * pDist;
        const pSize = Math.random() * 3.5 + 2;
        const pDur = (Math.random() * 0.6 + 1.2).toFixed(2);

        particle.style.left = `${originX}px`;
        particle.style.top = `${originY}px`;
        particle.style.width = `${pSize}px`;
        particle.style.height = `${pSize}px`;
        particle.style.setProperty("--px", `${pX.toFixed(1)}px`);
        particle.style.setProperty("--py", `${pY.toFixed(1)}px`);
        particle.style.setProperty("--pcolor", i % 2 === 0 ? "#ffffff" : accent.trim());
        particle.style.animation = `particle-burst-fly ${pDur}s cubic-bezier(0.12, 0.8, 0.3, 1) forwards`;

        particleContainer.appendChild(particle);
      }

      setTimeout(() => {
        particleContainer.remove();
      }, 2600);
    }, 350);
  }
})();
