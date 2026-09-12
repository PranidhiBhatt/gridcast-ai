"use strict";
const $ = id => document.getElementById(id);
const fields = {wind: new Map(), solar: new Map()};
let ready = false, busy = false;
const number = value => typeof value === "number" && Number.isFinite(value);
const fmt = (value, unit = "") => number(value) ? `${new Intl.NumberFormat(undefined, {maximumFractionDigits: 2}).format(value)}${unit ? ` ${unit}` : ""}` : "Unavailable";
function el(tag, text, className) {
  const node = document.createElement(tag);
  if (text !== undefined) node.textContent = text;
  if (className) node.className = className;
  return node;
}
function message(text) { $("message").textContent = text; $("message").hidden = !text; }
async function api(path, options = {}) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 60000);
  try {
    const response = await fetch(path, {...options, signal: controller.signal});
    const data = await response.json().catch(() => null);
    if (!response.ok) {
      const fallback = response.status === 503 ? "A required model is unavailable. Check component availability and try again." : response.status === 422 ? "Please review the inputs and required feature fields." : "The analysis could not be completed. Please try again.";
      const issues = data?.error?.issues?.map(x => `${x.location.join(" → ")}: ${x.message}`).join("; ");
      throw new Error(`${data?.error?.message || fallback}${issues ? ` ${issues}` : ""}`);
    }
    if (!data) throw new Error("The API returned an unreadable response.");
    return data;
  } catch (error) {
    if (error.name === "AbortError") throw new Error("The request timed out. The server may still be processing it; check availability before retrying.");
    if (error instanceof TypeError) throw new Error("Cannot reach the API. Check that the GridCast AI application is running.");
    throw error;
  } finally { clearTimeout(timer); }
}
function updateControls() {
  $("run").disabled = !ready || busy;
  $("example").disabled = !ready || busy;
  $("refresh").disabled = busy;
  $("input-fields").disabled = busy;
  $("run").textContent = busy ? "Analysing your inputs…" : "Run Grid Analysis →";
  $("analysis-form").setAttribute("aria-busy", String(busy));
}
function buildFields(source, info) {
  const old = new Map([...fields[source]].map(([name, input]) => [name, input.value]));
  fields[source].clear(); $(source + "-inputs").replaceChildren();
  const names = info?.required_features;
  if (info?.availability !== "AVAILABLE" || !Array.isArray(names) || !names.length || !names.every(x => typeof x === "string")) {
    $(source + "-inputs").append(el("p", "Model input contract unavailable. Refresh status after the model becomes available.", "muted"));
    $(source + "-count").textContent = "Unavailable";
    return false;
  }
  names.forEach((name, i) => {
    const label = el("label", name), input = document.createElement("input");
    input.type = "number"; input.step = "any"; input.required = true;
    input.id = `${source}-feature-${i}`; label.htmlFor = input.id;
    input.value = old.get(name) ?? "";
    label.append(input); $(source + "-inputs").append(label); fields[source].set(name, input);
  });
  $(source + "-count").textContent = `${names.length} prepared features`;
  return true;
}
function renderModels(data) {
  $("model-info").replaceChildren();
  for (const source of ["wind", "solar"]) {
    const info = data[source], article = el("article");
    article.append(el("h3", `${source === "wind" ? "Wind" : "Solar"} model · ${info?.model_name || "Unavailable"}`));
    article.append(el("p", info?.task || "Model information unavailable."));
    const list = el("ul"); (info?.limitations || []).forEach(text => list.append(el("li", text))); article.append(list);
    if (info?.required_features) {
      const details = el("details"); details.append(el("summary", `Required features (${info.required_features.length})`));
      const names = el("ul"); info.required_features.forEach(name => names.append(el("li", name))); details.append(names); article.append(details);
    }
    $("model-info").append(article);
  }
}
async function refresh() {
  busy = true; updateControls(); message("");
  const [status, models] = await Promise.allSettled([api("/project/status"), api("/model/info")]);
  $("system-status").replaceChildren();
  if (status.status === "fulfilled") {
    const labels = {wind_model: "Wind Model", solar_model: "Solar Model", renewable_aggregation: "Renewable Aggregation", grid_intelligence: "Grid Intelligence", impact_engine: "Impact Engine"};
    Object.entries(labels).forEach(([key, label]) => {
      const available = status.value[key] === "AVAILABLE", item = el("div", label, "status-item");
      item.append(el("strong", available ? "● AVAILABLE" : "○ UNAVAILABLE", available ? "available" : "unavailable")); $("system-status").append(item);
    });
  } else $("system-status").append(el("p", "Component status unavailable. Check the API and refresh.", "unavailable"));
  if (models.status === "fulfilled") {
    const windReady = buildFields("wind", models.value.wind), solarReady = buildFields("solar", models.value.solar);
    ready = windReady && solarReady; renderModels(models.value);
  } else {
    ready = false; buildFields("wind", null); buildFields("solar", null); renderModels({}); message(models.reason.message);
  }
  busy = false; updateControls();
}
function changed() { if (!$("results").hidden) $("stale").hidden = false; }
$("analysis-form").addEventListener("input", changed);
$("refresh").addEventListener("click", refresh);
$("example").addEventListener("click", async () => {
  busy = true; updateControls(); message("");
  try {
    const sample = await api("/static/example.json");
    for (const source of ["wind", "solar"]) for (const name of fields[source].keys()) {
      if (!number(sample[source]?.features?.[name])) throw new Error("Example does not match this model's feature contract. Please enter values manually.");
    }
    for (const source of ["wind", "solar"]) for (const [name, input] of fields[source]) input.value = sample[source].features[name];
    $("timestamp").value = sample.timestamp; $("demand").value = sample.grid.demand_mw; $("interval").value = sample.impact.interval_hours;
    $("example-note").hidden = false; changed();
  } catch (error) { message(error.message); }
  finally { busy = false; updateControls(); }
});
function valueRow(container, label, value) {
  const row = el("div", undefined, "value-row"); row.append(el("span", label), el("strong", value)); container.append(row);
}
function render(data) {
  const {wind, solar, renewable, grid, impact} = data;
  if (!wind || !solar || !renewable || !grid || !impact) throw new Error("The API response is incomplete. No results were displayed.");
  $("result-time").textContent = data.timestamp || "Timestamp unavailable";
  $("cards").replaceChildren();
  const states = {SURPLUS: "↑ SURPLUS", BALANCED: "≈ BALANCED", DEFICIT: "↓ DEFICIT"};
  const cards = [["Wind power estimate", fmt(wind.wind_power_mw), "MW"], ["Solar power estimate", fmt(solar.solar_power_mw), "MW"], ["Total renewable estimate", fmt(renewable.total_renewable_power_mw), "MW", "total"], ["Reported electricity demand", fmt(grid.demand_mw), "MW"], ["Supply-demand gap", fmt(grid.supply_gap_mw), "MW"], ["Grid status", states[grid.grid_status] || "Unavailable", "Rule-based classification", states[grid.grid_status] ? grid.grid_status : ""]];
  cards.forEach(([label, value, unit, style]) => {
    const card = el("div", undefined, `metric ${style || ""}`); card.append(el("p", label), el("strong", value), el("small", value === "Unavailable" ? "No available value" : unit)); $("cards").append(card);
  });
  const wm = renewable.wind_mix_percentage, sm = renewable.solar_mix_percentage;
  const validMix = number(wm) && number(sm) && wm >= 0 && sm >= 0 && wm <= 100 && sm <= 100;
  $("wind-bar").style.width = validMix ? `${wm}%` : "0"; $("solar-bar").style.width = validMix ? `${sm}%` : "0";
  $("mix-labels").replaceChildren(el("span", `≋ Wind · ${fmt(wm, "%")}`), el("span", `☼ Solar · ${fmt(sm, "%")}`));
  $("mix-total").textContent = fmt(renewable.total_renewable_power_mw, "MW total");
  $("grid-badge").textContent = states[grid.grid_status] || "Unavailable";
  $("grid-badge").className = `badge ${states[grid.grid_status] ? grid.grid_status : ""}`;
  $("gap-detail").textContent = `Gap: ${fmt(grid.supply_gap_mw, "MW")} · ${fmt(grid.supply_gap_percentage, "% of reported demand")}`;
  $("explanation").textContent = grid.explanation || "Explanation unavailable.";
  $("recommendations").replaceChildren();
  (grid.recommendations || []).forEach(r => { const article = el("article"); article.append(el("h4", r.action), el("p", r.reason)); $("recommendations").append(article); });
  if (!grid.recommendations?.length) $("recommendations").append(el("p", "No recommendations available."));
  $("economic").replaceChildren(); $("environmental").replaceChildren();
  valueRow($("economic"), "Renewable energy estimate", fmt(impact.renewable_energy_mwh, "MWh"));
  valueRow($("economic"), "Estimated avoided generation cost", fmt(impact.estimated_avoided_generation_cost, impact.currency_unit || ""));
  valueRow($("economic"), "Avoided generation cost factor", fmt(impact.avoided_generation_cost_per_mwh, `${impact.currency_unit || "currency units"}/MWh`));
  valueRow($("environmental"), "Estimated avoided emissions", fmt(impact.estimated_avoided_emissions_kg_co2, "kg CO₂"));
  valueRow($("environmental"), "Emission factor used", fmt(impact.emission_factor_kg_co2_per_mwh, "kg CO₂/MWh"));
  valueRow($("environmental"), "Reported demand covered by renewable supply", fmt(impact.renewable_demand_coverage_percentage, "%"));
  valueRow($("environmental"), "Potential surplus · not measured curtailment", fmt(impact.potential_surplus_mw, "MW"));
  $("assumptions").replaceChildren();
  const list = el("ul"); Object.entries(impact.assumptions_used || {}).forEach(([key, value]) => list.append(el("li", `${key.replaceAll("_", " ")}: ${value}`)));
  (impact.limitations || []).forEach(text => list.append(el("li", text))); $("assumptions").append(list);
  $("empty").hidden = true; $("results").hidden = false; $("stale").hidden = true;
}
$("analysis-form").addEventListener("submit", async event => {
  event.preventDefault(); if (busy || !ready) return;
  document.querySelectorAll(".input-group").forEach(d => d.open = true);
  if (!$("analysis-form").reportValidity()) return;
  const request = {timestamp: $("timestamp").value, grid: {demand_mw: Number($("demand").value)}, impact: {interval_hours: Number($("interval").value)}};
  for (const source of ["wind", "solar"]) request[source] = {features: Object.fromEntries([...fields[source]].map(([key, input]) => [key, Number(input.value)]))};
  if (![request.grid.demand_mw, request.impact.interval_hours, ...Object.values(request.wind.features), ...Object.values(request.solar.features)].every(number)) { message("All numeric inputs must be finite numbers."); return; }
  busy = true; updateControls(); message("");
  $("results").hidden = true; $("empty").hidden = false;
  try {
    const data = await api("/analyze", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(request)});
    render(data);
    $("results").scrollIntoView({behavior: "auto", block: "start"});
  } catch (error) { message(error.message); $("message").focus(); }
  finally { busy = false; updateControls(); }
});
refresh();
