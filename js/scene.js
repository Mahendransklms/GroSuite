import * as THREE from "three";

const canvas = document.getElementById("hero-canvas");

if (canvas && canvas.parentElement) {
  const reduceMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;

  let renderer;

  try {
    renderer = new THREE.WebGLRenderer({
      canvas,
      antialias: true,
      alpha: true
    });
  } catch (error) {
    console.warn(
      "GroSuite animation unavailable. The CSS circle will remain visible.",
      error
    );
  }

  if (renderer) {
    renderer.setPixelRatio(
      Math.min(window.devicePixelRatio || 1, 2)
    );

    // Transparent background preserves the CSS outer circle.
    renderer.setClearColor(0x000000, 0);

    const scene = new THREE.Scene();

    const camera = new THREE.PerspectiveCamera(
      32,
      1,
      0.1,
      60
    );

    camera.position.z = 10;

    /*
     * INNER 3D RING REMOVED.
     *
     * Do not create the coloured segments or the central
     * TorusGeometry ring here.
     *
     * Only the animated orbit lines are retained below.
     */

    // Animated orbit rings.
    const orbitMaterial = new THREE.MeshBasicMaterial({
      color: 0xaec9ff,
      transparent: true,
      opacity: 0.12
    });

    const orbitSettings = [
      {
        radius: 2.7,
        tilt: [0.9, 0.2],
        speed: 0.0012
      },
      {
        radius: 3.4,
        tilt: [-0.6, 0.5],
        speed: -0.0008
      },
      {
        radius: 4.1,
        tilt: [0.3, -0.8],
        speed: 0.0005
      }
    ];

    const orbits = orbitSettings.map(
      ({ radius, tilt, speed }) => {
        const geometry = new THREE.TorusGeometry(
          radius,
          0.007,
          8,
          160
        );

        const orbit = new THREE.Mesh(
          geometry,
          orbitMaterial
        );

        orbit.rotation.set(
          tilt[0],
          tilt[1],
          0
        );

        orbit.userData.speed = speed;

        scene.add(orbit);

        return orbit;
      }
    );

    // Mouse interaction.
    const pointer = new THREE.Vector2();
    const target = new THREE.Vector2();

    let frameId = 0;
    let tick = 0;
    let inView = false;

    // Resize the canvas and maintain the correct camera aspect.
    function layout() {
      const width = Math.max(
        canvas.parentElement.clientWidth,
        1
      );

      const height = Math.max(
        canvas.parentElement.clientHeight,
        1
      );

      renderer.setSize(width, height, false);

      camera.aspect = width / height;
      camera.updateProjectionMatrix();

      const scale = Math.min(
        1.12,
        (width / height) * 0.9
      );

      orbits.forEach((orbit) => {
        orbit.scale.setScalar(scale);
      });

      // Draw one static frame for reduced-motion users.
      if (reduceMotion) {
        renderer.render(scene, camera);
      }
    }

    // Update the mouse position.
    window.addEventListener(
      "pointermove",
      (event) => {
        target.set(
          (event.clientX / window.innerWidth) * 2 - 1,
          -(event.clientY / window.innerHeight) * 2 + 1
        );
      },
      { passive: true }
    );

    // Animate only the orbit lines.
    function animate() {
      frameId = 0;

      if (!inView || reduceMotion) {
        return;
      }

      tick += 1;

      pointer.lerp(target, 0.04);

      orbits.forEach((orbit, index) => {
        const speed = orbit.userData.speed;

        // Continuous rotation.
        orbit.rotation.z += speed;
        orbit.rotation.y += speed * 0.6;

        // Subtle mouse interaction.
        orbit.rotation.x +=
          (orbitSettings[index].tilt[0] +
            pointer.y * 0.025 -
            orbit.rotation.x) * 0.002;

        orbit.rotation.y +=
          pointer.x * 0.0008;
      });

      renderer.render(scene, camera);

      frameId = window.requestAnimationFrame(animate);
    }

    // Start or stop animation safely.
    function updateAnimation(isVisible) {
      inView = isVisible;

      if (inView && !reduceMotion) {
        if (!frameId) {
          frameId = window.requestAnimationFrame(animate);
        }
      } else {
        if (frameId) {
          window.cancelAnimationFrame(frameId);
          frameId = 0;
        }
      }
    }

    // Watch changes to the hero container size.
    const resizeObserver = new ResizeObserver(layout);

    resizeObserver.observe(canvas.parentElement);

    layout();

    // Pause animation when the hero leaves the viewport.
    const visibilityObserver = new IntersectionObserver(
      ([entry]) => {
        updateAnimation(entry.isIntersecting);
      }
    );

    visibilityObserver.observe(canvas);
  }
}