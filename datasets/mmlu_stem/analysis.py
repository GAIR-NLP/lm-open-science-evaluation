import json

all_sub_topics = set()

with open("test.jsonl", "r") as f:
    for line in f:
        data = json.loads(line)
        all_sub_topics.add(data["topic"])

print(all_sub_topics)

# 'computer_security',  'astronomy', 'conceptual_physics', 'high_school_computer_science', 'college_computer_science', 'electrical_engineering', 'college_physics',  'machine_learning', 'college_biology', 'high_school_physics', 'high_school_chemistry',  'high_school_biology', 'college_chemistry', 'high_school_statistics'

# 'college_mathematics', 'high_school_mathematics', 'elementary_mathematics', 'abstract_algebra',