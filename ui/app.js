const PERIOD_LABELS = {
  1: "Period 1 (1864–1883)",
  2: "Period 2 (1884–1903)",
  3: "Period 3 (1904–1923)",
  4: "Period 4 (1924–1943)",
  5: "Period 5 (1944–1963)",
  6: "Period 6 (1964–1983)",
  7: "Period 7 (1984–2003)",
  8: "Period 8 (2004–2023)",
  9: "Period 9 (2024–2043)",
};

const ALL_FACINGS = [
  "N1", "N2", "N3",
  "NE1", "NE2", "NE3",
  "E1", "E2", "E3",
  "SE1", "SE2", "SE3",
  "S1", "S2", "S3",
  "SW1", "SW2", "SW3",
  "W1", "W2", "W3",
  "NW1", "NW2", "NW3",
];

const FACING_LABELS = {
  N1: "N1 Ren (337.6°–352.5°)",
  N2: "N2 Zi (352.6°–7.5°)",
  N3: "N3 Gui (7.6°–22.5°)",
  NE1: "NE1 Chou (22.6°–37.5°)",
  NE2: "NE2 Gen (37.6°–52.5°)",
  NE3: "NE3 Yin (52.6°–67.5°)",
  E1: "E1 Jia (67.6°–82.5°)",
  E2: "E2 Mao (82.6°–97.5°)",
  E3: "E3 Yi (97.6°–112.5°)",
  SE1: "SE1 Chen (112.6°–127.5°)",
  SE2: "SE2 Xun (127.6°–142.5°)",
  SE3: "SE3 Si (142.6°–157.5°)",
  S1: "S1 Bing (157.6°–172.5°)",
  S2: "S2 Wu (172.6°–187.5°)",
  S3: "S3 Ding (187.6°–202.5°)",
  SW1: "SW1 Wei (202.6°–217.5°)",
  SW2: "SW2 Kun (217.6°–232.5°)",
  SW3: "SW3 Shen (232.6°–247.5°)",
  W1: "W1 Geng (247.6°–262.5°)",
  W2: "W2 You (262.6°–277.5°)",
  W3: "W3 Xin (277.6°–292.5°)",
  NW1: "NW1 Xu (292.6°–307.5°)",
  NW2: "NW2 Qian (307.6°–322.5°)",
  NW3: "NW3 Hai (322.6°–337.5°)",
  SE: "SE — legacy validated case",
};

const DISPLAY_POSITIONS = [
  ["top-left", "top-center", "top-right"],
  ["middle-left", "center", "middle-right"],
  ["bottom-left", "bottom-center", "bottom-right"],
];

const ORIENTATION_ROWS = {
  north: [["NW", "N", "NE"], ["W", "C", "E"], ["SW", "S", "SE"]],
  south: [["SE", "S", "SW"], ["E", "C", "W"], ["NE", "N", "NW"]],
  east: [["NE", "E", "SE"], ["N", "C", "S"], ["NW", "W", "SW"]],
  west: [["SW", "W", "NW"], ["S", "C", "N"], ["SE", "E", "NE"]],
};

const ORIENTATION_LABELS = {
  north: "North on Top",
  south: "South on Top",
  east: "East on Top",
  west: "West on Top",
};

const COMPASS_RING = ["NW", "N", "NE", "E", "SE", "S", "SW", "W"];
const LO_SHU_FLIGHT_PATH = ["C", "NW", "W", "NE", "S", "N", "SW", "E", "SE"];

const ANNUAL_CENTER_STARS = {
  2025: 2,
  2026: 1,
};

const MONTHLY_CENTER_STARS = {
  2025: {
    1: 3,
    2: 2,
    3: 1,
    4: 9,
    5: 8,
    6: 7,
    7: 6,
    8: 5,
    9: 4,
    10: 3,
    11: 2,
    12: 1,
  },
  2026: {
    1: 9,
    2: 8,
    3: 7,
    4: 6,
    5: 5,
    6: 4,
    7: 3,
    8: 2,
    9: 1,
    10: 9,
    11: 8,
    12: 7,
  },
};

let charts = {};
let currentChart = null;
let ringShift = 0;
let natalChartLocked = false;
let annualOverlayEnabled = false;
let monthlyOverlayEnabled = false;
let annualStars = null;
let monthlyStars = null;
const initialParams = new URLSearchParams(window.location.search);

const periodSelect = document.getElementById("periodSelect");
const facingSelect = document.getElementById("facingSelect");
const orientationSelect = document.getElementById("orientationSelect");
const selectedLabel = document.getElementById("selectedLabel");
const orientationLabel = document.getElementById("orientationLabel");
const shiftLabel = document.getElementById("shiftLabel");
const chartGrid = document.getElementById("chartGrid");
const traceOutput = document.getElementById("traceOutput");
const availabilityMessage = document.getElementById("availabilityMessage");
const caseStatus = document.getElementById("caseStatus");
const generateBtn = document.getElementById("generateBtn");
const shiftCwBtn = document.getElementById("shiftCwBtn");
const shiftCcwBtn = document.getElementById("shiftCcwBtn");
const resetBtn = document.getElementById("resetBtn");
const lockChartBtn = document.getElementById("lockChartBtn");
const annualToggle = document.getElementById("annualToggle");
const annualYearSelect = document.getElementById("annualYearSelect");
const monthlyToggle = document.getElementById("monthlyToggle");
const monthlyYearSelect = document.getElementById("monthlyYearSelect");
const monthSelect = document.getElementById("monthSelect");
const applyOverlaysBtn = document.getElementById("applyOverlaysBtn");
const clearOverlaysBtn = document.getElementById("clearOverlaysBtn");
const temporalStatus = document.getElementById("temporalStatus");

function starAfterSteps(centerStar, steps) {
  return ((centerStar - 1 + steps) % 9) + 1;
}

function flyStarsFromCenter(centerStar) {
  if (!Number.isInteger(centerStar) || centerStar < 1 || centerStar > 9) {
    throw new Error("centerStar must be an integer from 1 to 9");
  }

  return Object.fromEntries(
    LO_SHU_FLIGHT_PATH.map((palace, offset) => [
      palace,
      starAfterSteps(centerStar, offset),
    ])
  );
}

function getAnnualStars() {
  const year = Number(annualYearSelect.value);
  const centerStar = ANNUAL_CENTER_STARS[year];

  if (!centerStar) {
    throw new Error(`Unsupported annual year: ${year}`);
  }

  return flyStarsFromCenter(centerStar);
}

function getMonthlyStars() {
  const year = Number(monthlyYearSelect.value);
  const month = Number(monthSelect.value);
  const centerStar = MONTHLY_CENTER_STARS[year]?.[month];

  if (!centerStar) {
    throw new Error(`Unsupported monthly selection: ${year}-${month}`);
  }

  return flyStarsFromCenter(centerStar);
}

function composeChartWithOverlays(chart) {
  if (!chart) return null;

  const composedGrid = Object.fromEntries(
    Object.entries(chart.grid).map(([palace, natalStars]) => [
      palace,
      {
        ...natalStars,
        annual: annualOverlayEnabled ? annualStars?.[palace] ?? null : null,
        monthly: monthlyOverlayEnabled ? monthlyStars?.[palace] ?? null : null,
      },
    ])
  );

  return {
    ...chart,
    grid: composedGrid,
  };
}

function normalizeShift(steps) {
  return ((steps % 8) + 8) % 8;
}

function incrementRingShift(currentSteps) {
  return currentSteps + 1;
}

function decrementRingShift(currentSteps) {
  return currentSteps - 1;
}

function chartKey(period, facing) {
  return `${period}|${facing}`;
}

function setCaseStatus(available, conflictReviewRequired = false) {
  if (available && conflictReviewRequired) {
    caseStatus.textContent = "Available · Source conflict noted";
    caseStatus.className = "case-status conflict";
    return;
  }
  caseStatus.textContent = available ? "Available" : "Pending validation";
  caseStatus.className = `case-status ${available ? "available" : "pending"}`;
}

function getSelectedPeriod() {
  return Number(periodSelect.value);
}

function getSelectedFacing() {
  const option = facingSelect.options[facingSelect.selectedIndex];
  return option?.dataset?.facing || option?.value || facingSelect.value;
}

function getSelectedFacingLabel() {
  const option = facingSelect.options[facingSelect.selectedIndex];
  return option?.textContent || FACING_LABELS[getSelectedFacing()] || getSelectedFacing();
}

function selectedDebug(period, facing) {
  const lookupKey = chartKey(period, facing);
  return {
    selectedPeriod: period,
    selectedFacing: facing,
    selectedOptionLabel: getSelectedFacingLabel(),
    lookupKey,
    availability: Boolean(charts[lookupKey]) ? "Available" : "Pending validation",
    conflictReviewRequired: Boolean(charts[lookupKey]?.conflict_review_required),
  };
}

function orientationIndex(orientation) {
  const rows = ORIENTATION_ROWS[orientation];
  return Object.fromEntries(rows.flatMap((row, r) => row.map((palace, c) => [palace, [r, c]])));
}

function applyRingShift(chart, steps) {
  const normalized = normalizeShift(steps);
  const displayByPalace = {};

  placeShiftedCell(displayByPalace, chart, "C", "C", steps, normalized);
  COMPASS_RING.forEach((sourcePalace, sourceIndex) => {
    const destinationPalace = COMPASS_RING[(sourceIndex + normalized) % COMPASS_RING.length];
    placeShiftedCell(displayByPalace, chart, sourcePalace, destinationPalace, steps, normalized);
  });

  return displayByPalace;
}

function placeShiftedCell(displayByPalace, chart, sourcePalace, destinationPalace, rawSteps, normalizedSteps) {
  const stars = chart.grid[sourcePalace];
  displayByPalace[destinationPalace] = {
    display_palace: destinationPalace,
    canonical_palace: sourcePalace,
    mountain: stars.mountain,
    water: stars.water,
    base: stars.base,
    annual: stars.annual ?? null,
    monthly: stars.monthly ?? null,
    orientation_mode: "ring_shift",
    ring_shift_steps: rawSteps,
    normalized_ring_shift_steps: normalizedSteps,
  };
}

function buildDisplayGrid(chart, steps, orientation) {
  const shifted = applyRingShift(chart, steps);
  const rows = ORIENTATION_ROWS[orientation];
  return rows.map((row, r) => row.map((displayPalace, c) => ({
    ...shifted[displayPalace],
    display_position: DISPLAY_POSITIONS[r][c],
    orientation,
  })));
}

function populateSelectors() {
  periodSelect.innerHTML = Object.entries(PERIOD_LABELS)
    .map(([period, label]) => `<option value="${period}">${label}</option>`)
    .join("");
  periodSelect.value = initialParams.get("period") || "9";
  populateFacingOptions();
  const requestedFacing = initialParams.get("facing") || "SE2";
  if ([...facingSelect.options].some((option) => option.value === requestedFacing)) facingSelect.value = requestedFacing;
}

function populateFacingOptions() {
  const period = Number(periodSelect.value);
  const availableFacings = new Set(
    Object.values(charts)
      .filter((chart) => chart.period === period)
      .map((chart) => chart.facing)
  );
  const legacyFacings = [...availableFacings].filter((facing) => !ALL_FACINGS.includes(facing));
  const facings = [...ALL_FACINGS, ...legacyFacings];

  facingSelect.disabled = false;
  generateBtn.disabled = false;
  facingSelect.innerHTML = facings
    .map((facing) => {
      const key = chartKey(period, facing);
      const conflict = charts[key]?.conflict_review_required ? " — Source conflict noted" : "";
      const status = availableFacings.has(facing) ? ` — Available${conflict}` : " — Not extracted";
      return `<option value="${facing}" data-facing="${facing}">${FACING_LABELS[facing] || facing}${status}</option>`;
    })
    .join("");
}

function generateChart({ resetShift = false } = {}) {
  const period = getSelectedPeriod();
  const facing = getSelectedFacing();
  const key = chartKey(period, facing);
  currentChart = charts[key] || null;
  if (resetShift) {
    ringShift = 0;
  } else if (initialParams.has("shift")) {
    ringShift = Number(initialParams.get("shift") || 0);
  }
  redrawUnavailableOrChart(period, facing);
}

function redrawUnavailableOrChart(period, facing) {
  if (!currentChart) {
    renderUnavailable(period, facing);
    return;
  }
  redraw();
}

function renderUnavailable(period, facing) {
  const facingLabel = FACING_LABELS[facing] || facing;
  const normalized = normalizeShift(ringShift);
  selectedLabel.textContent = `${PERIOD_LABELS[period]} / ${facingLabel}`;
  orientationLabel.textContent = ORIENTATION_LABELS[orientationSelect.value];
  shiftLabel.textContent = String(normalized);
  setCaseStatus(false);
  availabilityMessage.textContent = `Chart not extracted for Period ${period} / ${facing}. Please select one of the 24 validated mountain facings.`;
  chartGrid.innerHTML = `<div class="empty-state">Chart not extracted for Period ${period} / ${facing}.<br><span>Please select one of the 24 validated mountain facings.</span></div>`;
  traceOutput.textContent = `${JSON.stringify(selectedDebug(period, facing), null, 2)}\n\nNo extracted chart for Period ${period} / ${facing}.`;
}

function redraw() {
  if (!currentChart) {
    renderUnavailable(getSelectedPeriod(), getSelectedFacing());
    return;
  }

  availabilityMessage.textContent = currentChart.conflict_review_required ? "Source conflict noted for this case; chart uses extracted 216-corpus values pending manual review." : "";
  setCaseStatus(true, Boolean(currentChart.conflict_review_required));

  const orientation = orientationSelect.value;
  const composedChart = composeChartWithOverlays(currentChart);
  const grid = buildDisplayGrid(composedChart, ringShift, orientation);
  const normalized = normalizeShift(ringShift);
  const selectedFacingLabel = FACING_LABELS[currentChart.facing] || currentChart.facing;

  selectedLabel.textContent = `${PERIOD_LABELS[currentChart.period]} / ${selectedFacingLabel}`;
  orientationLabel.textContent = ORIENTATION_LABELS[orientation];
  shiftLabel.textContent = String(normalized);

  chartGrid.innerHTML = grid.flat().map((cell) => `
    <article class="cell ${cell.display_palace === "C" ? "center" : ""}">
      <div class="palace">${cell.canonical_palace}</div>
      <div class="display-note">display position: ${cell.display_palace}</div>
      <div class="mw-pair">
        <span>${cell.mountain}</span>
        <span>${cell.water}</span>
      </div>
      <div class="mw-label">mountain · water</div>
      <div class="base-star">${cell.base}</div>
      <div class="base-label">base</div>

      ${(cell.annual !== null || cell.monthly !== null) ? `
        <div class="temporal-stars">
          ${cell.annual !== null ? `
            <div class="temporal-star annual-star">
              <span class="temporal-key">Y</span>
              <span class="temporal-value">${cell.annual}</span>
            </div>
          ` : ""}
          ${cell.monthly !== null ? `
            <div class="temporal-star monthly-star">
              <span class="temporal-key">M</span>
              <span class="temporal-value">${cell.monthly}</span>
            </div>
          ` : ""}
        </div>
      ` : ""}
    </article>
  `).join("");

  const debug = JSON.stringify(selectedDebug(currentChart.period, currentChart.facing), null, 2);
  traceOutput.textContent = debug + "\n\n" + grid.flat()
    .map((cell) => `[${cell.canonical_palace}→${cell.display_palace}] screen=${cell.display_position} orientation=${ORIENTATION_LABELS[orientation]} ring_shift=${ringShift} normalized=${normalized}`)
    .join("\n");
}

periodSelect.addEventListener("change", () => {
  populateFacingOptions();
  generateChart({ resetShift: true });
});
facingSelect.addEventListener("input", () => generateChart({ resetShift: true }));
facingSelect.addEventListener("change", () => generateChart({ resetShift: true }));
orientationSelect.addEventListener("change", redraw);
generateBtn.addEventListener("click", () => {
  initialParams.delete("shift");
  generateChart({ resetShift: true });
});
shiftCwBtn.addEventListener("click", () => {
  if (!currentChart) generateChart();
  ringShift = incrementRingShift(ringShift);
  redraw();
});
shiftCcwBtn.addEventListener("click", () => {
  if (!currentChart) generateChart();
  ringShift = decrementRingShift(ringShift);
  redraw();
});
resetBtn.addEventListener("click", () => {
  ringShift = 0;
  redraw();
});

function updateLockState() {
  periodSelect.disabled = natalChartLocked;
  facingSelect.disabled = natalChartLocked;
  generateBtn.disabled = natalChartLocked;

  lockChartBtn.textContent = natalChartLocked
    ? "Unlock Natal Chart"
    : "Lock Natal Chart";

  annualToggle.disabled = !natalChartLocked;
  annualYearSelect.disabled = !natalChartLocked;
  monthlyToggle.disabled = !natalChartLocked;
  monthlyYearSelect.disabled = !natalChartLocked;
  monthSelect.disabled = !natalChartLocked;
  applyOverlaysBtn.disabled = !natalChartLocked;
  clearOverlaysBtn.disabled = !natalChartLocked;

  if (!natalChartLocked) {
    temporalStatus.textContent =
      "Lock the natal chart before applying annual or monthly overlays.";
  }
}

lockChartBtn.addEventListener("click", () => {
  if (!currentChart) {
    temporalStatus.textContent = "Generate a natal chart first.";
    return;
  }

  natalChartLocked = !natalChartLocked;

  if (!natalChartLocked) {
    annualOverlayEnabled = false;
    monthlyOverlayEnabled = false;
    annualStars = null;
    monthlyStars = null;
    annualToggle.checked = false;
    monthlyToggle.checked = false;
  }

  updateLockState();
  redraw();
});

applyOverlaysBtn.addEventListener("click", () => {
  if (!natalChartLocked) {
    temporalStatus.textContent = "Lock the natal chart first.";
    return;
  }

  annualOverlayEnabled = annualToggle.checked;
  monthlyOverlayEnabled = monthlyToggle.checked;

  annualStars = annualOverlayEnabled ? getAnnualStars() : null;
  monthlyStars = monthlyOverlayEnabled ? getMonthlyStars() : null;

  const statusParts = [];

  if (annualOverlayEnabled) {
    statusParts.push(`Annual ${annualYearSelect.value}`);
  }

  if (monthlyOverlayEnabled) {
    const monthName =
      monthSelect.options[monthSelect.selectedIndex]?.textContent
      || monthSelect.value;
    statusParts.push(`Monthly ${monthName} ${monthlyYearSelect.value}`);
  }

  temporalStatus.textContent = statusParts.length
    ? `Applied: ${statusParts.join(" · ")}`
    : "No temporal overlays selected.";

  redraw();
});

clearOverlaysBtn.addEventListener("click", () => {
  annualOverlayEnabled = false;
  monthlyOverlayEnabled = false;
  annualStars = null;
  monthlyStars = null;
  annualToggle.checked = false;
  monthlyToggle.checked = false;
  temporalStatus.textContent = "Annual and monthly overlays cleared.";
  redraw();
});

annualYearSelect.addEventListener("change", () => {
  if (annualOverlayEnabled) {
    annualStars = getAnnualStars();
    redraw();
  }
});

monthlyYearSelect.addEventListener("change", () => {
  if (monthlyOverlayEnabled) {
    monthlyStars = getMonthlyStars();
    redraw();
  }
});

monthSelect.addEventListener("change", () => {
  if (monthlyOverlayEnabled) {
    monthlyStars = getMonthlyStars();
    redraw();
  }
});

fetch("data/charts.json")
  .then((response) => response.json())
  .then((data) => {
    charts = data.charts;
    populateSelectors();
    const requestedOrientation = initialParams.get("orientation");
    if (requestedOrientation && ORIENTATION_ROWS[requestedOrientation]) orientationSelect.value = requestedOrientation;
    generateChart();
    updateLockState();
    initialParams.delete("shift");
    if (initialParams.get("showFacingList") === "1") {
      facingSelect.size = Math.min(24, facingSelect.options.length);
      facingSelect.classList.add("expanded-facing-list");
    }
  })
  .catch((error) => {
    traceOutput.textContent = `Failed to load chart data: ${error}`;
  });
