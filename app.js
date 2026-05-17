const DISPLAY_ROWS = [
  ["SE", "S", "SW"],
  ["E", "C", "W"],
  ["NE", "N", "NW"],
];

const DISPLAY_POSITIONS = [
  ["top-left", "top-center", "top-right"],
  ["middle-left", "center", "middle-right"],
  ["bottom-left", "bottom-center", "bottom-right"],
];

const COMPASS_RING = ["NW", "N", "NE", "E", "SE", "S", "SW", "W"];
const PALACE_TO_INDEX = Object.fromEntries(
  DISPLAY_ROWS.flatMap((row, r) => row.map((palace, c) => [palace, [r, c]]))
);

let charts = {};
let currentChart = null;
let ringShift = 0;

const periodSelect = document.getElementById("periodSelect");
const facingSelect = document.getElementById("facingSelect");
const selectedLabel = document.getElementById("selectedLabel");
const shiftLabel = document.getElementById("shiftLabel");
const chartGrid = document.getElementById("chartGrid");
const traceOutput = document.getElementById("traceOutput");

function normalizeShift(steps) {
  return ((steps % 8) + 8) % 8;
}

function incrementRingShift(currentSteps) {
  return currentSteps + 1;
}

function decrementRingShift(currentSteps) {
  return currentSteps - 1;
}

function applyRingShift(chart, steps) {
  const normalized = normalizeShift(steps);
  const output = Array.from({ length: 3 }, () => Array(3).fill(null));

  placeCell(output, chart, "C", "C", steps, normalized);
  COMPASS_RING.forEach((sourcePalace, sourceIndex) => {
    const destinationPalace = COMPASS_RING[(sourceIndex + normalized) % COMPASS_RING.length];
    placeCell(output, chart, sourcePalace, destinationPalace, steps, normalized);
  });

  return output;
}

function placeCell(output, chart, sourcePalace, destinationPalace, rawSteps, normalizedSteps) {
  const [row, col] = PALACE_TO_INDEX[destinationPalace];
  const stars = chart.grid[sourcePalace];
  output[row][col] = {
    display_position: DISPLAY_POSITIONS[row][col],
    display_palace: destinationPalace,
    canonical_palace: sourcePalace,
    mountain: stars.mountain,
    water: stars.water,
    base: stars.base,
    orientation_mode: "ring_shift",
    ring_shift_steps: rawSteps,
    normalized_ring_shift_steps: normalizedSteps,
  };
}

function chartKey(period, facing) {
  return `${period}|${facing}`;
}

function populateSelectors() {
  const cases = Object.values(charts).sort((a, b) => a.period - b.period || a.facing.localeCompare(b.facing));
  const periods = [...new Set(cases.map((chart) => chart.period))];

  periodSelect.innerHTML = periods.map((period) => `<option value="${period}">Period ${period}</option>`).join("");
  periodSelect.value = periods.includes(9) ? "9" : String(periods[0]);
  populateFacingOptions();
  if ([...facingSelect.options].some((option) => option.value === "SE")) facingSelect.value = "SE";
}

function populateFacingOptions() {
  const period = Number(periodSelect.value);
  const facings = Object.values(charts)
    .filter((chart) => chart.period === period)
    .map((chart) => chart.facing)
    .sort();
  facingSelect.innerHTML = facings.map((facing) => `<option value="${facing}">${facing}</option>`).join("");
}

function generateChart() {
  const key = chartKey(Number(periodSelect.value), facingSelect.value);
  currentChart = charts[key];
  ringShift = 0;
  redraw();
}

function redraw() {
  if (!currentChart) return;
  const grid = applyRingShift(currentChart, ringShift);
  const normalized = normalizeShift(ringShift);

  selectedLabel.textContent = `P${currentChart.period} / ${currentChart.facing}`;
  shiftLabel.textContent = String(normalized);

  chartGrid.innerHTML = grid.flat().map((cell) => `
    <article class="cell ${cell.display_palace === "C" ? "center" : ""}">
      <div class="position">${cell.display_position} · display ${cell.display_palace}</div>
      <div class="palace">${cell.canonical_palace} → ${cell.display_palace}</div>
      <div class="stars">${cell.mountain} ${cell.water} ${cell.base}</div>
      <div class="legend">mountain · water · base</div>
    </article>
  `).join("");

  traceOutput.textContent = grid.flat()
    .map((cell) => `[${cell.canonical_palace}→${cell.display_palace}] ring_shift=${ringShift} normalized=${normalized}`)
    .join("\n");
}

periodSelect.addEventListener("change", () => {
  populateFacingOptions();
});
document.getElementById("generateBtn").addEventListener("click", generateChart);
document.getElementById("shiftCwBtn").addEventListener("click", () => {
  if (!currentChart) generateChart();
  ringShift = incrementRingShift(ringShift);
  redraw();
});
document.getElementById("shiftCcwBtn").addEventListener("click", () => {
  if (!currentChart) generateChart();
  ringShift = decrementRingShift(ringShift);
  redraw();
});
document.getElementById("resetBtn").addEventListener("click", () => {
  ringShift = 0;
  redraw();
});

fetch("data/charts.json")
  .then((response) => response.json())
  .then((data) => {
    charts = data.charts;
    populateSelectors();
    generateChart();
  })
  .catch((error) => {
    traceOutput.textContent = `Failed to load chart data: ${error}`;
  });
