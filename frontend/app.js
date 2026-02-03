const out = document.getElementById("out");
const limitInput = document.getElementById("limit");

function show(obj) {
  out.textContent = typeof obj === "string" ? obj : JSON.stringify(obj, null, 2);
}

async function previewETL() {
  try {
    show("Preview ETL...");
    const r = await fetch("/api/etl/preview?n=3");
    show(await r.json());
  } catch (e) {
    show("Erreur: " + e.message);
  }
}

async function runETL() {
  try {
    show("ETL en cours...");
    const r = await fetch("/api/etl/run", { method: "POST" });
    show(await r.json());
  } catch (e) {
    show("Erreur: " + e.message);
  }
}

async function loadPosts() {
  try {
    const limit = Number(limitInput.value || 10);
    show("Chargement des posts...");
    const r = await fetch(`/api/posts?limit=${limit}`);
    show(await r.json());
  } catch (e) {
    show("Erreur: " + e.message);
  }
}

async function statsDB() {
  try {
    show("Stats DB...");
    const r = await fetch("/api/stats");
    show(await r.json());
  } catch (e) {
    show("Erreur: " + e.message);
  }
}

document.getElementById("preview").addEventListener("click", previewETL);
document.getElementById("run").addEventListener("click", runETL);
document.getElementById("load").addEventListener("click", loadPosts);
document.getElementById("stats").addEventListener("click", statsDB);
