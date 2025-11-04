import requests
import time
import csv
import matplotlib.pyplot as plt
import pandas as pd

URL = "http://pra5ml-env.eba-eywyijci.us-east-2.elasticbeanstalk.com/predict"

test_cases = [
    {"name": "fake1", "text": "Breaking: celebrity claims Earth is flat and NASA is lying!"},
    {"name": "fake2", "text": "Government secretly replaced all streetlights with spy devices."},
    {"name": "real1", "text": "Canada announces new funding for renewable energy projects."},
    {"name": "real2", "text": "NASA's Artemis mission aims to return humans to the Moon by 2026."},
]

rows = []

NUM_REQUESTS = 100

for case in test_cases:
    for i in range(NUM_REQUESTS):
        start_time = time.time()
        response = requests.post(URL, json={"message": case["text"]})
        elapsed_ms = (time.time() - start_time) * 1000  # convert seconds to milliseconds
        
        # Save for CSV
        rows.append([case["name"], i + 1, elapsed_ms])

        # if (i + 1) % 10 == 0:
        #     print(f"{case['name']} request {i+1}/{NUM_REQUESTS} done, last latency: {elapsed_ms:.2f} ms")

csv_file = "api_latency_results.csv"
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["test_case", "request_num", "latency_ms"])
    writer.writerows(rows)

print(f"Latency results saved to {csv_file}")

df = pd.read_csv(csv_file)
plt.figure(figsize=(10, 6))
df.boxplot(column="latency_ms", by="test_case")

avg_latency = df.groupby("test_case")["latency_ms"].mean()
print("average latency: \n")
print(avg_latency)

plt.title("API Latency per Test Case")
plt.suptitle("")  # remove the automatic 'by' title
plt.ylabel("Latency (ms)")
plt.show()

