
import pandas as pd

file_path = r"D:\CloudOptimizer\task_usage.csv.gz"
output_path = r"D:\CloudOptimizer\cloud_workload_100k.csv"

df = pd.read_csv(
    file_path,
    compression="gzip",
    header=None,
    nrows=100000
)

df.to_csv(output_path, index=False)

print("Dataset created successfully!")
print("Rows and columns:", df.shape)
print(df.head())
