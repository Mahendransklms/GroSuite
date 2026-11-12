import * as THREE from 'three';

const canvas = document.getElementById('hero-canvas');
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.1;

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(32, 1, 0.1, 50);
camera.position.z = 10;

const rig = new THREE.Group();
scene.add(rig);

const QUARTER = Math.PI / 2;
const GAP = 0.09;
const SEGMENTS = [
  { color: 0x17a34a, start: 0 },
  { color: 0xd7263d, start: QUARTER },
  { color: 0xdba21e, start: Math.PI },
  { color: 0x2a6df4, start: Math.PI + QUARTER },
];

const arc = new THREE.TorusGeometry(1.6, 0.36, 48, 96, QUARTER - GAP);

for (const { color, start } of SEGMENTS) {
  const material = new THREE.MeshPhysicalMaterial({
    color,
    metalness: 0.25,
    roughness: 0.32,
    clearcoat: 0.6,
    clearcoatRoughness: 0.25,
  });
  const mesh = new THREE.Mesh(arc, material);
  mesh.rotation.z = start + GAP / 2;
  rig.add(mesh);
}

const orbitMaterial = new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.07 });
const orbits = [
  { radius: 2.7, tilt: [0.9, 0.2], speed: 0.0012 },
  { radius: 3.4, tilt: [-0.6, 0.5], speed: -0.0008 },
  { radius: 4.2, tilt: [0.3, -0.8], speed: 0.0005 },
].map(({ radius, tilt, speed }) => {
  const ring = new THREE.Mesh(new THREE.TorusGeometry(radius, 0.008, 8, 160), orbitMaterial);
  ring.rotation.set(tilt[0], tilt[1], 0);
  ring.userData.speed = speed;
  scene.add(ring);
  return ring;
});

scene.add(new THREE.AmbientLight(0xffffff, 0.35));

const key = new THREE.DirectionalLight(0xffffff, 2.4);
key.position.set(4, 6, 6);
scene.add(key);

const rim = new THREE.DirectionalLight(0x8fb4ff, 1.6);
rim.position.set(-6, -3, -4);
scene.add(rim);

const fill = new THREE.PointLight(0xffffff, 6, 20);
fill.position.set(-3, 2, 5);
scene.add(fill);

rig.rotation.x = 0.35;

const pointer = new THREE.Vector2();
const target = new THREE.Vector2();
let baseY = 0;

addEventListener('pointermove', (e) => {
  target.set((e.clientX / innerWidth) * 2 - 1, -(e.clientY / innerHeight) * 2 + 1);
});

function layout() {
  const { clientWidth: w, clientHeight: h } = canvas.parentElement;
  renderer.setSize(w, h, false);
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
  baseY = 0;
  rig.position.set(0, baseY, 0);
  const scale = Math.min(1.2, (w / h) * 0.9);
  rig.scale.setScalar(scale);
  for (const o of orbits) {
    o.position.copy(rig.position);
    o.scale.setScalar(scale);
  }
}

new ResizeObserver(layout).observe(canvas.parentElement);
layout();

let t = 0;
let raf = 0;

function frame() {
  t += 1;
  pointer.lerp(target, 0.04);

  rig.rotation.y = t * 0.004 + pointer.x * 0.35;
  rig.rotation.x = 0.35 - pointer.y * 0.25;
  rig.position.y = baseY + Math.sin(t * 0.012) * 0.08;

  for (const o of orbits) {
    o.rotation.z += o.userData.speed;
    o.rotation.y += o.userData.speed * 0.6;
  }

  renderer.render(scene, camera);
  raf = reduceMotion ? 0 : requestAnimationFrame(frame);
}

new IntersectionObserver(([entry]) => {
  if (entry.isIntersecting) {
    if (!raf) frame();
  } else {
    cancelAnimationFrame(raf);
    raf = 0;
  }
}).observe(canvas);
