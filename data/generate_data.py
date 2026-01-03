import numpy as np
import pandas as pd
import random
import os

np.random.seed(42)
N = 1200

def normal_session():
    return {
        "url_length": np.random.randint(20, 60),
        "url_entropy": np.random.uniform(2.5, 3.8),
        "num_subdomains": np.random.randint(0, 3),
        "contains_ip": 0,
        "suspicious_tokens": np.random.randint(0, 2),
        "num_redirects": np.random.randint(0, 2),
        "external_domain_calls": np.random.randint(1, 4),
        "https_used": 1,
        "script_count": np.random.randint(3, 10),
        "script_density": np.random.uniform(0.1, 0.4),
        "inline_script_ratio": np.random.uniform(0.05, 0.2),
        "permission_requests": 0,
        "auto_downloads": 0,
        "popup_count": 0,
        "time_on_page": np.random.uniform(20, 180),
        "repeat_visits": np.random.randint(1, 5),
        "session_frequency": np.random.randint(1, 4),
    }

def anomalous_session():
    return {
        "url_length": np.random.randint(80, 150),
        "url_entropy": np.random.uniform(4.2, 5.5),
        "num_subdomains": np.random.randint(4, 8),
        "contains_ip": random.choice([0, 1]),
        "suspicious_tokens": np.random.randint(3, 6),
        "num_redirects": np.random.randint(3, 8),
        "external_domain_calls": np.random.randint(6, 15),
        "https_used": random.choice([0, 1]),
        "script_count": np.random.randint(15, 40),
        "script_density": np.random.uniform(0.6, 0.95),
        "inline_script_ratio": np.random.uniform(0.4, 0.9),
        "permission_requests": np.random.randint(2, 6),
        "auto_downloads": random.choice([0, 1]),
        "popup_count": np.random.randint(3, 10),
        "time_on_page": np.random.uniform(1, 10),
        "repeat_visits": 0,
        "session_frequency": np.random.randint(6, 12),
    }

data = []
for _ in range(int(N * 0.88)):
    data.append(normal_session())
for _ in range(int(N * 0.12)):
    data.append(anomalous_session())

df = pd.DataFrame(data).sample(frac=1).reset_index(drop=True)

os.makedirs("data", exist_ok=True)
df.to_csv("data/synthetic_sessions.csv", index=False)

print("Dataset generated:", df.shape)
