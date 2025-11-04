import requests

URL = "http://pra5ml-env.eba-eywyijci.us-east-2.elasticbeanstalk.com/predict"

test_cases = [
    {"text": "Breaking: celebrity claims Earth is flat and NASA is lying!", "expected": "FAKE"},
    {"text": "Government secretly replaced all streetlights with spy devices.", "expected": "FAKE"},
    {"text": "Canada announces new funding for renewable energy projects.", "expected": "REAL"},
    {"text": "Canada summer tourism hits all time high", "expected": "REAL"},
]

for case in test_cases:
    response = requests.post(URL, json={"message": case["text"]})
    if response.status_code == 200:
        data = response.json()
        label = data.get("label")
        print(f"Input: {case['text']}")
        print(f"Predicted Label: {label}, Expected: {case['expected']}")
        print("-" * 60)
        assert label == case["expected"], "Prediction does not match expected"
    else:
        print(f"Request failed with status {response.status_code}")

    
