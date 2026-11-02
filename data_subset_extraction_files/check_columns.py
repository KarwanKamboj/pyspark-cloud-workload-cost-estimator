
import pandas as pd

df = pd.read_csv(
    r"D:\CloudOptimizer\task_usage.csv.gz",
    compression="gzip",
    header=None,
    nrows=5
)

print("Actual first 5 rows:")
print(df.to_string(index=False, header=False))
print("\nShape:", df.shape)
