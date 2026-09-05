"""
Server-line data analysis — the 5 analyses a server ODM PM/analyst faces most.
Run:  python3 make_dataset.py   (once, to create data/)
      python3 analyze_factory.py
Each function: loads a CSV, computes the answer, saves a chart, prints the takeaway.
"""
import pandas as pd, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
os.makedirs("charts", exist_ok=True)
BLUE="#4F81BD"; RED="#C0504D"; GREEN="#2E8B57"

# 1) YIELD TREND — is the line improving?  (line chart + 7-day moving average)
def yield_trend():
    df = pd.read_csv("data/production_daily.csv", parse_dates=["date"])
    df["yield_ma7"] = df["yield"].rolling(7).mean()          # smooth out daily noise
    plt.figure(figsize=(9,4.5))
    plt.plot(df.date, df["yield"]*100, color="#9db8d6", lw=1, label="Daily yield")
    plt.plot(df.date, df["yield_ma7"]*100, color=BLUE, lw=2.5, label="7-day average")
    plt.axhline(95, color=RED, ls="--", lw=1, label="Target 95%")
    plt.ylabel("Yield (%)"); plt.title("1. Yield trend — is the line ramping?")
    plt.legend(); plt.tight_layout(); plt.savefig("charts/1_yield_trend.png", dpi=150); plt.close()
    print(f"[1] Yield rose from {df['yield'].iloc[:7].mean():.1%} to {df['yield'].iloc[-7:].mean():.1%}; crossed 95% target mid-ramp.")

# 2) FIRST-PASS YIELD BY STATION — which station is the weak point?
def fpy_by_station():
    df = pd.read_csv("data/station_fpy.csv").sort_values("first_pass_yield")
    worst = df.iloc[0]
    colors = [RED if v==worst.first_pass_yield else BLUE for v in df.first_pass_yield]
    plt.figure(figsize=(9,4.5))
    plt.barh(df.station, df.first_pass_yield*100, color=colors)
    plt.xlim(90,100); plt.xlabel("First-pass yield (%)")
    plt.title("2. First-pass yield by station — worst = focus area")
    for i,v in enumerate(df.first_pass_yield): plt.text(v*100+0.05, i, f"{v:.1%}", va="center", fontsize=9)
    plt.tight_layout(); plt.savefig("charts/2_fpy_by_station.png", dpi=150); plt.close()
    print(f"[2] Worst station: {worst.station} at {worst.first_pass_yield:.1%} — biggest yield-improvement lever.")

# 3) DEFECT PARETO — which few causes drive most defects? (80/20)
def defect_pareto():
    df = pd.read_csv("data/defects.csv").sort_values("count", ascending=False).reset_index(drop=True)
    df["cum_pct"] = df["count"].cumsum()/df["count"].sum()*100
    fig, ax1 = plt.subplots(figsize=(10,5))
    ax1.bar(df.defect_cause, df["count"], color=BLUE)
    ax1.set_ylabel("Defect count", color=BLUE); ax1.tick_params(axis="x", rotation=40)
    for lbl in ax1.get_xticklabels(): lbl.set_ha("right")
    ax2 = ax1.twinx()
    ax2.plot(df.defect_cause, df["cum_pct"], color=RED, marker="o", lw=2)
    ax2.axhline(80, color="gray", ls="--", lw=1)
    ax2.set_ylabel("Cumulative %", color=RED); ax2.set_ylim(0,105)
    plt.title("3. Defect Pareto (80/20) - the vital few causes")
    plt.tight_layout(); plt.savefig("charts/3_defect_pareto.png", dpi=150); plt.close()
    n80 = (df["cum_pct"]<=80).sum()+1
    top = ", ".join(df.defect_cause.head(n80))
    print(f"[3] {n80} of {len(df)} causes explain ~80% of defects: {top}.")

# 4) CYCLE-TIME BOTTLENECK — which station limits throughput?
def bottleneck():
    df = pd.read_csv("data/cycle_time.csv").sort_values("cycle_time_sec")
    slow = df.iloc[-1]
    colors=[RED if v==slow.cycle_time_sec else BLUE for v in df.cycle_time_sec]
    plt.figure(figsize=(9,4.5))
    plt.bar(df.station, df.cycle_time_sec, color=colors)
    plt.ylabel("Cycle time (sec)"); plt.title("4. Cycle time by station — bottleneck = tallest bar")
    for i,v in enumerate(df.cycle_time_sec): plt.text(i, v+8, str(v), ha="center", fontsize=9)
    plt.xticks(rotation=25, ha="right"); plt.tight_layout()
    plt.savefig("charts/4_bottleneck.png", dpi=150); plt.close()
    line_rate = 3600/slow.cycle_time_sec
    print(f"[4] Bottleneck: {slow.station} at {slow.cycle_time_sec}s -> line max ~{line_rate:.1f} units/hr. Speeding others up won't help until this improves.")

# 5) RMA BY CAUSE — what fails in the field? (feeds CAPA)
def rma_analysis():
    df = pd.read_csv("data/rma.csv").sort_values("returns", ascending=False)
    plt.figure(figsize=(9,4.5))
    plt.bar(df.rma_cause, df.returns, color=GREEN)
    plt.ylabel("Field returns"); plt.title("5. RMA (field returns) by cause - drives CAPA")
    plt.xticks(rotation=30, ha="right")
    for i,v in enumerate(df.returns): plt.text(i, v+0.4, str(v), ha="center", fontsize=9)
    plt.tight_layout(); plt.savefig("charts/5_rma_by_cause.png", dpi=150); plt.close()
    print(f"[5] Top field failure: {df.iloc[0].rma_cause} ({df.iloc[0].returns} returns) — same theme as production defects (thermal).")

if __name__ == "__main__":
    print("=== Server-line analysis ===")
    yield_trend(); fpy_by_station(); defect_pareto(); bottleneck(); rma_analysis()
    print("\nCharts saved in charts/. Open them to see each answer.")
