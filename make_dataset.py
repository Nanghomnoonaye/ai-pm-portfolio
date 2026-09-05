"""Generate realistic (synthetic) server-line data for practice."""
import numpy as np, pandas as pd, os
np.random.seed(42)
os.makedirs("data", exist_ok=True)

# 1) Daily production & yield over 12 weeks
days = pd.date_range("2026-06-01", periods=84, freq="D")
built = np.random.randint(80, 140, len(days))
# yield improves over time (line ramp/learning curve) + noise
base = np.linspace(0.86, 0.965, len(days)) + np.random.normal(0, 0.015, len(days))
base = np.clip(base, 0.80, 0.99)
good = (built*base).round().astype(int)
prod = pd.DataFrame({"date":days,"units_built":built,"units_good":good})
prod["yield"] = (prod.units_good/prod.units_built).round(4)
prod.to_csv("data/production_daily.csv", index=False)

# 2) First-pass yield by station (SMT -> assembly -> test -> burn-in)
stations = ["SMT","PCBA_Test","Assembly","Function_Test","Burn_In","Packing"]
fpy = [0.985, 0.972, 0.991, 0.948, 0.963, 0.997]  # Function_Test worst
pd.DataFrame({"station":stations,"first_pass_yield":fpy,
             "units_tested":[9800,9600,9300,9200,8700,8500]}).to_csv("data/station_fpy.csv", index=False)

# 3) Defect records (for Pareto)
causes = ["Solder bridge","Cold solder","GPU thermal fail","Connector loose",
          "Firmware flash fail","Coolant leak","Missing component","Label error",
          "Power module fault","Cosmetic scratch"]
weights = [32, 24, 18, 11, 9, 8, 6, 4, 3, 2]  # long-tail -> Pareto
counts = (np.array(weights)*3 + np.random.randint(0,8,len(causes)))
pd.DataFrame({"defect_cause":causes,"count":counts}).to_csv("data/defects.csv", index=False)

# 4) Cycle time per station (seconds) -> find bottleneck
ct = {"SMT":210,"PCBA_Test":180,"Assembly":320,"Function_Test":540,"Burn_In":720,"Packing":150}
pd.DataFrame({"station":list(ct),"cycle_time_sec":list(ct.values())}).to_csv("data/cycle_time.csv", index=False)

# 5) RMA (field returns) by cause over the quarter
rma = {"GPU thermal fail":41,"Coolant leak":33,"Power module fault":22,
       "Connector loose":15,"Firmware issue":12,"No fault found":9,"Other":6}
pd.DataFrame({"rma_cause":list(rma),"returns":list(rma.values())}).to_csv("data/rma.csv", index=False)

print("Datasets written to data/:")
for f in sorted(os.listdir("data")): print("  ", f)
