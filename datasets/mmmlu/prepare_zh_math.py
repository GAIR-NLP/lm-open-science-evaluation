
# 1. read the csv file using pandas
import pandas as pd
import json
df = pd.read_csv("mmlu_ZH-CN.csv")

data = []
# 2. for each row, extract the question, options, answer, subject
for i, row in df.iterrows():
    question = row["Question"]
    options = [row["A"], row["B"], row["C"], row["D"]]
    answer = row["Answer"]
    subject = row["Subject"]
    # print(question, options, answer, subject)
    # organize the data into a jsonl file like {"question": "Chlorine gas reacts most readily with", "options": ["toluene", "ethylene", "ethanoic acid", "ethane"], "answer": "B", "topic": "high_school_chemistry", "id": 2705}
    item = {
        "question": question,
        "options": options,
        "answer": answer,
        "topic": subject,
        "id": i
    }
    # if subject in ['college_mathematics', 'high_school_mathematics', 'elementary_mathematics', 'abstract_algebra',]:
    #     data.append(item)
    if subject in ['computer_security',  'astronomy', 'conceptual_physics', 'high_school_computer_science', 'college_computer_science', 'electrical_engineering', 'college_physics',  'machine_learning', 'college_biology', 'high_school_physics', 'high_school_chemistry',  'high_school_biology', 'college_chemistry', 'high_school_statistics', 'college_mathematics', 'high_school_mathematics', 'elementary_mathematics', 'abstract_algebra',]:
        data.append(item)

# 3. save the data into a jsonl file
# with open("mmmlu_zh_math_test.jsonl", "w", encoding="utf-8") as f:
#     for item in data:
#         f.write(json.dumps(item, ensure_ascii=False) + "\n")
with open("mmmlu_zh_stem_test.jsonl", "w", encoding="utf-8") as f:
    for item in data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
