import regex
import random
import json

from data_processing.answer_extraction import extract_math_answer, strip_string
from utils import parse_math_answer, remove_not, cal_not,parse_not

def process_gsm8k_test(item):
    sample = {
        'dataset': 'gsm8k-cot',
        'id': item['id'],
        'messages': [
            {'role': 'user', 'content': item['question']},
            {'role': 'assistant', 'content': regex.sub(r"<<[^<>]*>>", "", item['cot']) + "\nSo the answer is $\\boxed{" + item['answer'].strip() + "}$."}
        ],
        'answer': item['answer'].replace(',', '')
    }
    yield sample

def process_math_test(item):
    question = item["problem"]
    try:
        answer = extract_math_answer(question, item['solution'])
    except:
        return
    sample = {
        "dataset": "math-cot",
        "id": item['id'],
        "level": item["level"],
        "type": item["type"],
        "category": item["category"],
        "messages": [
            {"role": "user", "content": question},
            {"role": "assistant", "content": "\n".join(regex.split(r"(?<=\.) (?=[A-Z])", item["solution"]))}
        ],
        "answer": answer
    }
    yield sample

def process_math500(item):
    question = item["problem"]
    try:
        answer = item["answer"]
    except:
        return
    sample = {
        "dataset": "math500-cot",
        "id": item['id'],
        "level": item["level"],
        "subject": item["subject"],
        "messages": [
            {"role": "user", "content": question},
            {"role": "assistant", "content": "\n".join(regex.split(r"(?<=\.) (?=[A-Z])", item["solution"]))}
        ],
        "answer": answer
    }
    yield sample

def process_olympiad_bench(item):
    question = item['question']
    answer = item['final_answer']
    sample = {
        'dataset': 'olympiad_bench',
        'id': str(item['id']),
        "category": item['subfield'],
        "messages": [
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer}
        ],
        "answer": answer[0]
    }
    yield sample

def process_amc(item):
    question = item['problem']
    answer = item['answer']
    sample = {
        'dataset': 'amc',
        'id': str(item['id']),
        "messages": [
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer}
        ],
        "answer": str(answer)
    }
    yield sample

def process_math_sat(item):
    options = item['options'].strip()
    assert 'A' == options[0]
    options = '(' + options
    for ch in 'BCDEFG':
        if f' {ch}) ' in options:
            options = regex.sub(f' {ch}\) ', f" ({ch}) ", options)
    question = f"{item['question'].strip()}\nWhat of the following is the right choice? Explain your answer.\n{options.strip()}"
    messages = [
        {'role': 'user', 'content': question},
        {'role': 'assistant', 'content': item['Answer']}
    ]
    item = {
        'dataset': 'math_sat',
        'id': item['id'],
        'language': 'en',
        'messages': messages,
        'answer': item['Answer'],
    }
    yield item

def process_ocwcourses(item):
    messages = [
        {'role': 'user', 'content': item['problem'].strip()},
        {'role': 'assistant', 'content': item['solution'].strip()}
    ]
    item = {
        "dataset": "OCWCourses",
        "id": item['id'],
        "language": "en",
        "messages": messages,
        "answer": item['answer']
    }
    yield item

def process_mmlu_stem(item):
    options = item['options']
    for i, (label, option) in enumerate(zip('ABCD', options)):
        options[i] = f"({label}) {str(option).strip()}"
    options = ", ".join(options)
    question = f"{item['question'].strip()}\nWhat of the following is the right choice? Explain your answer.\n{options}"
    messages = [
        {'role': 'user', 'content': question},
        {'role': 'assistant', 'content': item['answer']}
    ]
    item = {
        "dataset": "MMLU-STEM",
        "id": item['id'],
        "language": "en",
        "messages": messages,
        "answer": item['answer']
    }
    yield item

def process_mmmlu_zh_math(item):
    question = item['question'].strip()
    options = item['options']
    for i, (label, option) in enumerate(zip('ABCD', options)):
        options[i] = f"({label}) {str(option).strip()}"
    options = ", ".join(options)
    question = f"{question}\n以下哪个选项是正确的？给出简单解释\n{options}"
    messages = [
        {'role': 'user', 'content': question},
        {'role': 'assistant', 'content': item['answer']}
    ]
    item = {
        "dataset": "MMMLU-ZH-MATH",
        "id": item['id'],
        "language": "zh",
        "messages": messages,
        "answer": item['answer']
    }
    yield item

def process_mgsm_zh(item):
    item['answer'] = item['answer'].replace(',', '')
    yield item

def process_cmath(item):
    item = {
        'dataset': 'cmath',
        'id': item['id'],
        'grade': item['grade'],
        'reasoning_step': item['reasoning_step'],
        'messages': [
            {'role': 'user', 'content': item['question'].strip()},
            {'role': 'assistant', 'content': ''}
        ],
        'answer': item['golden'].strip().replace(",", "")
    }
    yield item

def process_agieval_gaokao_math_cloze(item):
    item = {
        'dataset': 'agieval-gaokao-math-cloze',
        'id': item['id'],
        'messages': [
            {'role': 'user', 'content': item['question'].strip()},
            {'role': 'assistant', 'content': ''}
        ],
        'answer': [strip_string(ans) for ans in item['answer'].strip().split(";")]
    }
    yield item

def process_agieval_gaokao_mathqa(item):
    question = item['question'].strip()
    options = []
    for option in item['options']:
        option = option.strip()
        assert option[0] == '('
        assert option[2] == ')'
        assert option[1] in 'ABCD'
        option = f"{option[1]}: {option[3:].strip()}"
        options.append(option.strip())
    question = f"{question}\n{options}"
    item = {
        'dataset': 'agieval-gaokao-mathqa',
        'id': item['id'],
        'messages': [
            {'role': 'user', 'content': question},
            {'role': 'assistant', 'content': ''}
        ],
        "answer": item['label']
    }
    yield item

def process_agieval_gaokao_mathqa_few_shot_cot_test(item):
    question = item['question'].strip().rstrip('\\')
    options = " ".join([opt.strip() for opt in item['options']])
    question = f"{question}\n从以下选项中选择:    {options}"
    item = {
        'dataset': 'agieval-gaokao-mathqa',
        'id': item['id'],
        'messages': [
            {'role': 'user', 'content': question},
            {'role': 'assistant', 'content': ''}
        ],
        "answer": item['label']
    }
    yield item

def process_minif2f_isabelle(item):
    question = f"(*### Problem\n\n{item['informal_statement'].strip()}\n\n### Solution\n\n{item['informal_proof'].strip()} *)\n\nFormal:\n{item['formal_statement'].strip()}"
    item = {
        'dataset': 'minif2f-isabelle',
        'id': item['id'],
        'messages': [
            {'role': 'user', 'content': question},
            {'role': 'assistant', 'content': ''}
        ],
        "answer": "placeholder"
    }
    yield item

def process_tabmwp(item):
    title_str = f'regarding "{item["table_title"]}" ' if item['table_title'] else ''
    question = f'Read the following table {title_str}and answer a question:\n'
    question += f'{item["table"]}\n{item["question"]}'
    if item['choices']:
        question += f' Please select from the following options: {item["choices"]}'
    item = {
        'dataset': 'tabmwp',
        'id': item['id'],
        'messages': [
            {'role': 'user', 'content': question},
            {'role': 'assistant', 'content': ''}
        ],
        'type': 'multiple-choice' if item['choices'] else 'short-answer',
        "answer": item['answer']
    }
    yield item

def process_mathqa(item):
    question = item['problem'].strip()
    question = question[0].upper() + question[1:]
    # turn a ) 5600 , b ) 6000 , c ) 237 , d ) 7200 , e ) 8600
    # to (A) 5600, (B) 6000, (C) 237, (D) 7200, (E) 8600
    options = item['options']
    options = regex.sub(r'([a-z])\s*\)\s*([^,]+)\s*,?\s*', 
                        lambda m: f"({m.group(1).upper()}) {m.group(2).strip()}, ", 
                        options).strip().rstrip(',')
    
    question = f"{question}\nWhat of the following is the right choice? Explain your answer.\n{options}"
    gt_answer = item['correct']
    item = {
        'dataset': 'mathqa',
        'id': item['id'],
        'messages': [
            {'role': 'user', 'content': question},
            {'role': 'assistant', 'content': ''}
        ],
        "answer": str(gt_answer)
    }
    yield item


def process_svamp(item):
    body = item['Body'].strip()
    if not body.endswith('.'):
        body += '.'
    question = f'{body} {item["Question"].strip()}'
    item = {
        'dataset': 'svamp',
        'id': item['id'],
        'messages': [
            {'role': 'user', 'content': question},
            {'role': 'assistant', 'content': str(item['Answer'])}
        ],
        "answer": str(item['Answer'])
    }
    yield item

def process_asdiv(item):
    gt_answer = item['answer']
    gt_answer = regex.sub(r"\(.*?\)", "", gt_answer)
    question = f"{item['body'].strip()} {item['question'].strip()}"
    item = {
        'dataset': 'asdiv',
        'id': item['id'],
        'messages': [
            {'role': 'user', 'content': question},
            {'role': 'assistant', 'content': ''}
        ],
        "answer": gt_answer
    }
    yield item

def process_mawps(item):
    gt_answer = item['target']
    question = item['input']
    item = {
        'dataset': 'mawps',
        'id': item['id'],
        'messages': [
            {'role': 'user', 'content': question},
            {'role': 'assistant', 'content': ''}
        ],
        "answer": str(gt_answer)
    }
    yield item

def process_gpqa(item):
    options = [
        item["Correct Answer"],
        item["Incorrect Answer 1"],
        item["Incorrect Answer 2"],
        item["Incorrect Answer 3"]
    ]
    random.seed(42)
    random.shuffle(options)
    correct_index = options.index(item["Correct Answer"])
    option_dict = {
        'A': options[0],
        'B': options[1],
        'C': options[2],
        'D': options[3]
    }
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    
    formatted_item = {
        "dataset": "gpqa",
        "id": item['id'],
        'answer': chr(65 + correct_index),  # 将索引转换为A、B、C、D
        'messages': [
            {'role': 'user', 'content': f"{item['Question'].strip()}\nWhat of the following is the right choice? Explain your answer.\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_medqa(item):
    question = item["question"]
    option_dict = item["options"]
    answer = item["answer_idx"]
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "medqa",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\nWhat of the following is the right choice? Explain your answer.\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_medmcqa(item):
    question = item['question']
    option_dict = {
        'A': item['opa'],
        'B': item['opb'],
        'C': item['opc'],
        'D': item['opd']
    }
    answer = chr(65 + item['cop'])
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "medmcqa",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\nWhat of the following is the right choice? Explain your answer.\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_pubmedqa(item):
    question = item['question']
    context = item['context']['contexts']
    context_str = ""
    for c in context:
        context_str = context_str + "- " + c + "\n"
    context_str = context_str.strip()
    answer = item['final_decision']
    
    # context_str = "\n".join(context).strip()
    formatted_item = {
        "dataset": "pubmedqa",
        "id": item['id'],
        'answer': answer,
        'messages': [
            {'role': 'user', 'content': f"Given the following information and a question, analyze the information step by step using your internal knowledge. Consider all relevant details before arriving at an answer. The final response should only be one of [yes, no, maybe].\nInformation:\n{context_str.strip()}\n\nQuestion:\n{question.strip()}\n"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item
    
def process_mmlu(item):
    question = item['question']
    option_dict = {
        'A': item['choices'][0],
        'B': item['choices'][1],
        'C': item['choices'][2],
        'D': item['choices'][3]
    }
    answer = chr(65 + item['answer'])
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "mmlu-medicine",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\nWhat of the following is the right choice? Explain your answer.\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item
    
def process_ChemBench_multi_choise(item):
    question = item["examples"][0]["input"]
    target_scores = json.loads(item["examples"][0]["target_scores"])
    choices = list(target_scores.keys())
    option_dict = {
        chr(65 + i): choice 
        for i, choice in enumerate(choices)
    }
    answer_index = list(target_scores.values()).index(1.0)
    answer = chr(65 + answer_index)
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "ChemBench_multi_choise",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\nWhat of the following is the right choice? Explain your answer.\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_ChemBench_str_match(item):
    question = item["examples"][0]["input"]
    answer = item["examples"][0]["target"]
    
    sample = {
        "dataset": "ChemBench_str_match",
        "id": item['id'],
        "answer": answer,
        "messages": [
            {"role": "user", "content": question},
            {"role": "assistant", "content": ""}
        ]
    }
    yield sample

def process_newton_confident_questions(item):
    question = item["question"]
    option_dict = {
        'A': item['option_1'],
        'B': item['option_2'],
        'C': item['option_3'],
    }
    answer = chr(65 + int(float(item["result_majority"])) - 1)
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "newton_confident_questions",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\nWhat of the following is the right choice? Explain your answer.\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_newton_explicit_questions(item):
    question = item["question"]
    if item["q_type"] == "boolean":
        option_dict = {
            'A': item['choice_1'],
            'B': item['choice_2']
        }
    elif item["q_type"] == "MC":
        option_dict = {
            'A': item['choice_1'],
            'B': item['choice_2'],
            'C': item['choice_3'],
            'D': item['choice_4']
        }
    for key, value in option_dict.items():
        if value == item["gt"]:
            answer = key
        
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "newton_explicit_questions",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\nWhat of the following is the right choice? Explain your answer.\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_newton_implicit_questions(item):
    question = item["context"] + " " + item["question"]
    option_dict = {
        'A': item['choice_1'],
        'B': item['choice_2'],
        'C': item['choice_3'],
        'D': item['choice_4']
    }
    for key, value in option_dict.items():
        if value == item["gt"]:
            answer = key
        
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "newton_implicit_questions",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\nWhat of the following is the right choice? Explain your answer.\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item
    
def process_piqa(item):
    question = item["goal"]
    option_dict = {
        'A': item['sol1'],
        'B': item['sol2']
    }
    
    answer_index = item["label"]
    answer = chr(65 + answer_index)
        
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "piqa",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\nWhat of the following is the right choice? Explain your answer.\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item
    
def process_scibench(item):
    question = item["problem_text"]
    answer = item["answer_number"].strip().lstrip("+")
    
    sample = {
        "dataset": "scibench-physics",
        "id": item['id'],
        "answer": answer,
        "messages": [
            {"role": "user", "content": question},
            {"role": "assistant", "content": ""}
        ],
        "subject": item["subject"],
        "source": item["source"]
    }
    yield sample
    
def process_scibench_sft(item):
    answer = item["answer_number"].strip()
    unit_prob=item["unit"].strip()
    if remove_not(item["unit"].strip()):
        unit_prob=remove_not(item["unit"]).strip()
    if unit_prob:
        question=item["problem_text"].strip() + " The unit of the answer is " + unit_prob + "."
    else:
        question=item["problem_text"].strip()
        
    sample = {
        "dataset": "scibench",
        "id": item['id'],
        "unit": item["unit"].strip(),
        "unit_prob": unit_prob.strip(),
        "answer": answer,
        "messages": [
            {"role": "user", "content": question},
            {"role": "assistant", "content": ""}
        ],
        "subject": item["subject"],
        "source": item["source"]
    }
    yield sample

def process_cs_bench_multiple_choice(item):
    question = item['Question']
    option_dict = {
        'A': item["A"],
        'B': item["B"],
        'C': item["C"],
        'D': item["D"]
    }
    answer = item["Answer"]
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "cs_bench_multiple_choice",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\nWhat of the following is the right choice? Explain your answer.\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_cs_bench_assertion(item):
    question = item['Question']
    option_dict = {
        'A': "True",
        'B': "False",
    }
    answer = "A" if item["Answer"] == "True" else "B"
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "cs_bench_assertion",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\nPlease determine whether the statement is correct. What of the following is the right choice? Explain your answer.\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_mmlu_sft(item):
    question = item['question']
    option_dict = {
        'A': item['choices'][0],
        'B': item['choices'][1],
        'C': item['choices'][2],
        'D': item['choices'][3]
    }
    answer = chr(65 + item['answer'])
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "mmlu",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        'options': item['choices'],
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ],
        'subject': item['subject']
    }
    yield formatted_item

def process_gpqa_sft(item):
    options = [
        item["Correct Answer"].strip(),
        item["Incorrect Answer 1"].strip(),
        item["Incorrect Answer 2"].strip(),
        item["Incorrect Answer 3"].strip()
    ]
    random.seed(42)
    random.shuffle(options)
    correct_index = options.index(item["Correct Answer"].strip())
    option_dict = {
        'A': options[0],
        'B': options[1],
        'C': options[2],
        'D': options[3]
    }
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    
    formatted_item = {
        "dataset": "gpqa",
        "id": item['id'],
        'answer': chr(65 + correct_index),  # 将索引转换为A、B、C、D
        'options': options,
        'messages': [
            {'role': 'user', 'content': f"{item['Question'].strip()}\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ],
        'subject': item['High-level domain']
    }
    yield formatted_item


def process_super_gpqa(item):
    options = item["options"]
    correct_index = item["answer_letter"]
    option_dict = {
        chr(65 + i): choice 
        for i, choice in enumerate(options)
    }
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}{k}) {v}\n"
    
    formatted_item = {
        "dataset": "super_gpqa",
        "id": item['uuid'],
        'answer': correct_index,  # 将索引转换为A、B、C、D
        'options': options,
        'messages': [
            {'role': 'user', 'content': f"{item['question'].strip()}\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ],
        'discipline': item["discipline"],
        'field': item['field'],
        'subfield': item['subfield'],
        'difficulty': item['difficulty'],
        'is_calculation': item['is_calculation']
    }
    yield formatted_item

def process_mmlu_pro(item):
    options = item["options"]
    correct_index = item["answer"]
    option_dict = {
        chr(65 + i): choice 
        for i, choice in enumerate(options)
    }
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    
    formatted_item = {
        "dataset": "mmlu_pro",
        "id": item['question_id'],
        'answer': correct_index,  # 将索引转换为A、B、C、D
        'options': options,
        'messages': [
            {'role': 'user', 'content': f"{item['question'].strip()}\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ],
        "category": item["category"]
    }
    yield formatted_item

def process_ChemBench_multi_choise_sft(item):
    question = item["examples"][0]["input"]
    target_scores = json.loads(item["examples"][0]["target_scores"])
    choices = list(target_scores.keys())
    option_dict = {
        chr(65 + i): choice 
        for i, choice in enumerate(choices)
    }
    answer_index = list(target_scores.values()).index(1.0)
    answer = chr(65 + answer_index)
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "ChemBench_multi_choise",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        "options": choices,
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_cs_bench_assertion_sft(item):
    question = item['Question']
    option_dict = {
        'A': "True",
        'B': "False",
    }
    answer = "A" if item["Answer"] == "True" else "B"
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "cs_bench_assertion",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        "options": ["True", "False"],
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_cs_bench_multiple_choice_sft(item):
    question = item['Question']
    option_dict = {
        'A': item["A"],
        'B': item["B"],
        'C': item["C"],
        'D': item["D"]
    }
    answer = item["Answer"]
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "cs_bench_multiple_choice",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        "options": [item["A"], item["B"], item["C"], item["D"]],
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_medqa_sft(item):
    question = item["question"]
    option_dict = item["options"]
    answer = item["answer_idx"]
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "medqa",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D、E
        'options': [v.strip() for k, v in option_dict.items()],
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_medmcqa_sft(item):
    question = item['question']
    option_dict = {
        'A': item['opa'],
        'B': item['opb'],
        'C': item['opc'],
        'D': item['opd']
    }
    answer = chr(65 + item['cop'])
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "medmcqa",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        'options': [item['opa'], item['opb'], item['opc'], item['opd']],
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_pubmedqa_sft(item):
    question = item['question']
    context = item['context']['contexts']
    context_str = ""
    for c in context:
        context_str = context_str + "- " + c + "\n"
    context_str = context_str.strip()
    answer = chr(65 + ['yes', 'no', 'maybe'].index(item['final_decision']))
    option_dict = {
        'A': "Yes",
        'B': "No",
        'C': "Maybe"
    }
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    
    # context_str = "\n".join(context).strip()
    formatted_item = {
        "dataset": "pubmedqa",
        "id": item['id'],
        'answer': answer,
        "options": [v.strip() for k, v in option_dict.items()],
        'messages': [
            {'role': 'user', 'content': f"Information:\n{context_str.strip()}\n\nQuestion:\n{question.strip()}\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_newton_confident_questions_sft(item):
    question = item["question"]
    option_dict = {
        'A': item['option_1'],
        'B': item['option_2'],
        'C': item['option_3'],
    }
    answer = chr(65 + int(float(item["result_majority"])) - 1)
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "newton_confident_questions",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        "options": [v.strip() for k, v in option_dict.items()],
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_newton_explicit_questions_bool_sft(item):
    question = item["question"]
    option_dict = {
        'A': item['choice_1'],
        'B': item['choice_2']
        }

    for key, value in option_dict.items():
        if value == item["gt"]:
            answer = key
        
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "newton_explicit_questions_bool",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        "options": [v.strip() for k, v in option_dict.items()],
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item
    
def process_newton_explicit_questions_mc_sft(item):
    question = item["question"]
    option_dict = {
            'A': item['choice_1'],
            'B': item['choice_2'],
            'C': item['choice_3'],
            'D': item['choice_4']
        }

    for key, value in option_dict.items():
        if value == item["gt"]:
            answer = key
        
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "newton_explicit_questions_bool",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        "options": [v.strip() for k, v in option_dict.items()],
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_newton_implicit_questions_sft(item):
    question = item["context"] + " " + item["question"]
    option_dict = {
        'A': item['choice_1'],
        'B': item['choice_2'],
        'C': item['choice_3'],
        'D': item['choice_4']
    }
    for key, value in option_dict.items():
        if value == item["gt"]:
            answer = key
        
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "newton_implicit_questions",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        "options": [v.strip() for k, v in option_dict.items()],
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_piqa_sft(item):
    question = item["goal"]
    option_dict = {
        'A': item['sol1'],
        'B': item['sol2']
    }
    
    answer_index = item["label"]
    answer = chr(65 + answer_index)
        
    option_str = ""
    for k, v in option_dict.items():
        option_str = f"{option_str}({k}) {v}\n"
    formatted_item = {
        "dataset": "piqa",
        "id": item['id'],
        'answer': answer,  # 将索引转换为A、B、C、D
        "options": [v.strip() for k, v in option_dict.items()],
        'messages': [
            {'role': 'user', 'content': f"{question.strip()}\n{option_str.strip()}"},
            {'role': 'assistant', 'content': ''}
        ]
    }
    yield formatted_item

def process_olympic_arena_sft(item):
    question = item["problem"].strip()
    prompt = item["prompt"].strip()
    subject = item["subject"]
    answer_type = item["answer_type"]
    type_sequence = item["type_sequence"]
    unit = item["unit"]
    answer_sequence = item["answer_sequence"]
    answer = item["answer"]
    
    sample = {
        "dataset": "olympic_arena",
        "id": item['id'],
        "subject": subject,
        "unit": unit,
        "answer": answer,
        "answer_type": answer_type,
        "type_sequence": type_sequence,
        "answer_sequence": answer_sequence,
        "problem": question,
        "messages": [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": ""}
        ]
    }
    yield sample

if __name__ == "__main__":
    # test mathqa processor
    pass