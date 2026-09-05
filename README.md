AI Product Manager & Server ODM Portfolio
Study and practice project for a Server CEM/ODM Product Manager role — covering AI-PM concepts, the server manufacturing (NPI) product life cycle in English / 中文 / pinyin, and a hands-on data-analyst toolkit.
🔗 Live page
Interactive lifecycle + glossary + data-analyst dashboard:

https://YOUR-USERNAME.github.io/ai-pm-portfolio/server_odm_product_lifecycle.html

Replace YOUR-USERNAME with your GitHub username. To turn it on: repo Settings → Pages → Deploy from branch → main → Save, then open the link above. You can also just open server_odm_product_lifecycle.html locally in a browser.
What's inside
File / folder
What it is
server_odm_product_lifecycle.html
Interactive page: Pipeline · Matrix · Glossary · Data · Mermaid views, bilingual (EN/中文/pinyin)
data/AI_PM_Examples.xlsx
Dataset of AI-PM skills & cross-industry examples (4 sheets)
analyze.py + charts/
Python analysis of the AI-PM examples (bar chart, skill heatmap)
data_analyst/
Data-analyst practice kit — synthetic factory data, scripts, charts, how-to guide

The 5 data-analyst analyses (in data_analyst/)
Yield trend — is the line ramping to target?
First-pass yield by station — which station to fix first?
Defect Pareto (柏拉圖) — the vital few causes (80/20)
Cycle-time bottleneck — what limits throughput?
RMA by cause — what fails in the field (feeds CAPA)?

Each is explained in data_analyst/README.md with the question, the pandas code, and how to read the chart. All five are also viewable in the Data tab of the live page.
Run the analysis yourself
pip install -r requirements.txt

cd data_analyst

python3 make_dataset.py       # creates the practice data

python3 analyze_factory.py    # runs all 5 analyses -> charts/
Topics covered
AI-PM skills (AI literacy · data strategy · responsible AI · cross-functional · experimentation) · NPI product life cycle (Concept → Prototype → EVT → DVT → PVT → Mass Production → Sustaining/EOL) · factory & PM glossary (BOM, SMT, SKU, yield 良率, Pareto 柏拉圖, RMA 退貨, FMEA, CAPA, …) · pandas + matplotlib data analysis.

