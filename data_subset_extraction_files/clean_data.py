
import pandas as pd

input_file = r"D:\CloudOptimizer\cloud_workload_100k.csv"
output_file = r"D:\CloudOptimizer\cloud_workload_clean.csv"

columns = [
    "start_time",
    "end_time",
    "job_id",
    "task_index",
    "machine_id",
    "cpu_usage",
    "canonical_memory_usage",
    "assigned_memory",
    "unmapped_page_cache",
    "page_cache_memory",
    "max_memory_usage",
    "mean_disk_io_time",
    "mean_local_disk_space",
    "max_cpu_rate",
    "max_disk_io_time",
    "cycles_per_instruction",
    "memory_accesses_per_instruction",
    "sample_rate",
    "aggregation_type",
    "random_sample_cpu_usage"
]

df = pd.read_csv(input_file, header=0, names=columns)

print("Original shape:", df.shape)

df = df.dropna(
    subset=["cpu_usage", "canonical_memory_usage"]
)

df.to_csv(output_file, index=False)

print("Clean shape:", df.shape)
print("Saved to:", output_file)
print(df[["cpu_usage", "canonical_memory_usage"]].head())
