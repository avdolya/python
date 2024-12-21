import json
import sys

list = [line.strip() for line in sys.stdin]
with open("scoring.json", "r", encoding="UTF-8") as input_file:
    data = json.load(input_file)
pattern_list = []
for test_group in data:
    p = test_group["points"] // len(test_group["tests"])
    for test in test_group["tests"]:
        pattern_list.append((test["pattern"], p))
else:
    result_score = 0
    for i in range(len(pattern_list)):
        answer = list[i]
        pattern = pattern_list[i][0]
        points = pattern_list[i][1]
        if answer == pattern:
            result_score += points
    print(result_score)

