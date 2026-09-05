# AI Product Manager & Server ODM Portfolio

Study and practice project for a **Server CEM/ODM Product Manager** role — AI-PM concepts,
the server manufacturing (NPI) product life cycle in English / 中文 / pinyin, and a hands-on
data-analyst toolkit.

## 🔗 Live interactive page

The full interactive version (clickable pipeline, glossary search, data dashboard) can't run
inside this README — GitHub doesn't execute HTML/JavaScript in Markdown. It runs as a hosted
page instead:

**➡️ https://YOUR-USERNAME.github.io/ai-pm-portfolio/**

> Replace `YOUR-USERNAME` with your GitHub username. Turn it on: repo **Settings → Pages →
> Deploy from branch → `main` → Save**. Locally, just open `index.html` in a browser.

---

## Product life cycle (NPI)

```mermaid
graph LR
    C[1. Concept & Requirements<br/>概念與需求]
    D[2. Design & Prototype<br/>設計與樣機]
    E[3. EVT<br/>工程驗證]
    V[4. DVT<br/>設計驗證]
    P[5. PVT<br/>生產驗證]
    M[6. Mass Production<br/>量產]
    S[7. Sustaining / EOL<br/>維護與退場]

    C -->|Spec & BOM| D
    D -->|Prototype| E
    E -->|Design bugs fixed| V
    V -->|Spec & thermal pass| P
    P -->|Process & yield proven| M
    M -->|Field data / RMA| S

    style C fill:#0c4a6e,stroke:#38bdf8,color:#fff
    style D fill:#1e1b4b,stroke:#818cf8,color:#fff
    style E fill:#3b0764,stroke:#c084fc,color:#fff
    style V fill:#451a03,stroke:#fbbf24,color:#fff
    style P fill:#422006,stroke:#f59e0b,color:#fff
    style M fill:#064e3b,stroke:#34d399,color:#fff
    style S fill:#4c0519,stroke:#fb7185,color:#fff
```

---

## Data-analyst toolkit — the 5 analyses a Server ODM PM answers with data

### 1. Yield trend — is the line ramping?
![Yield trend](1_yield_trend.png)

### 2. First-pass yield by station — which station to fix first?
![FPY by station](2_fpy_by_station.png)

### 3. Defect Pareto (柏拉圖) — the vital few causes
![Defect Pareto](3_defect_pareto.png)

### 4. Cycle-time bottleneck — what limits throughput?
![Bottleneck](4_bottleneck.png)

### 5. RMA by cause — what fails in the field?
![RMA by cause](5_rma_by_cause.png)

### AI-PM skill emphasis
![Skill heatmap](skill_heatmap.png)

---

## Run the analysis yourself

```bash
pip install -r requirements.txt
python3 make_dataset.py       # creates the practice data
python3 analyze_factory.py    # runs all 5 analyses -> chart PNGs
```

## Files

`index.html` — interactive page (Pipeline · Matrix · Glossary · Data · Mermaid) ·
`AI_PM_Examples.xlsx` — AI-PM examples dataset ·
`make_dataset.py` / `analyze_factory.py` — the data-analyst scripts.![Defect Pareto](data_analyst/charts/3_defect_pareto.png)

### 4. Cycle-time bottleneck — what limits throughput?
![Bottleneck](data_analyst/charts/4_bottleneck.png)

### 5. RMA by cause — what fails in the field?
![RMA by cause](data_analyst/charts/5_rma_by_cause.png)

---

## What's in this repo

| File / folder | What it is |
|---|---|
| `index.html` / `server_odm_product_lifecycle.html` | Interactive page: Pipeline · Matrix · Glossary · Data · Mermaid views (EN/中文/pinyin) |
| `data/AI_PM_Examples.xlsx` | AI-PM skills & cross-industry examples (4 sheets) |
| `analyze.py` + `charts/` | Python analysis of the AI-PM examples |
| `data_analyst/` | Practice kit — synthetic factory data, scripts, charts, how-to guide |

## Run the analysis yourself

```bash
pip install -r requirements.txt
cd data_analyst
python3 make_dataset.py
python3 analyze_factory.py
```
