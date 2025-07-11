import re
import regex
import timeout_decorator
from utils import parse_math_answer, remove_not, cal_not,parse_not


def _fix_fracs(string):
    substrs = string.split("\\frac")
    new_str = substrs[0]
    if len(substrs) > 1:
        substrs = substrs[1:]
        for substr in substrs:
            new_str += "\\frac"
            if len(substr) > 0 and substr[0] == "{":
                new_str += substr
            else:
                try:
                    assert len(substr) >= 2
                except:
                    return string
                a = substr[0]
                b = substr[1]
                if b != "{":
                    if len(substr) > 2:
                        post_substr = substr[2:]
                        new_str += "{" + a + "}{" + b + "}" + post_substr
                    else:
                        new_str += "{" + a + "}{" + b + "}"
                else:
                    if len(substr) > 2:
                        post_substr = substr[2:]
                        new_str += "{" + a + "}" + b + post_substr
                    else:
                        new_str += "{" + a + "}" + b
    string = new_str
    return string

def _normalize_answer(final_answer):
    special_signal_map = {
        "\\left": "",
        "\\right": "",
        "∶": ":",
        "，": ",",
        "$": "",
        "\\approx": "=",
        "\\simeq": "=",
        "\\sim": "=",
        "^\\prime": "'",
        "^{\\prime}": "'",
        "^\\circ": "",
        "%": "",
    }
    for signal in special_signal_map:
        final_answer = final_answer.replace(signal, special_signal_map[signal])
    final_answer = re.sub(r'\\(?:mathrm|mathbf)\{~?([^}]*)\}', '\\1', final_answer)
    final_answer = re.sub(r'(\\text\{)(.*?)(\})', '\\2', final_answer)
    final_answer = re.sub(r'(\\textbf\{)(.*?)(\})', '\\2', final_answer)
    final_answer = re.sub(
        r'(frac)([^{])(.)', 'frac{\\2}{\\3}', final_answer)
    final_answer = re.sub(
        r'(sqrt)([^{])', 'sqrt{\\2}', final_answer)
    final_answer = final_answer.strip()
    final_answer = final_answer.strip("$")
    final_answer = final_answer.strip()
    return final_answer

def _fix_a_slash_b(string):
    if len(string.split("/")) != 2:
        return string
    a = string.split("/")[0]
    b = string.split("/")[1]
    try:
        if "sqrt" not in a:
            a = int(a)
        if "sqrt" not in b:
            b = int(b)
        assert string == "{}/{}".format(a, b)
        new_string = "\\frac{" + str(a) + "}{" + str(b) + "}"
        return new_string
    except:
        return string


def _fix_sqrt(string):
    _string = re.sub(r"\\sqrt(-?[0-9.a-zA-Z]+)", r"\\sqrt{\1}", string)
    _string = re.sub(r"\\sqrt\s+(\w+)$", r"\\sqrt{\1}", _string)
    return _string


def _fix_tan(string):
    _string = re.sub(r"\\tan(-?[0-9.a-zA-Z]+)", r"\\tan{\1}", string)
    _string = re.sub(r"\\tan\s+(\w+)$", r"\\tan{\1}", _string)
    return _string


def strip_string(string):
    string = str(string).strip()
    # linebreaks
    string = string.replace("\n", "")

    # right "."
    string = string.rstrip(".")

    # remove inverse spaces
    string = string.replace("\\!", "")
    # string = string.replace("\\ ", "")

    # replace \\ with \
    # string = string.replace("\\\\", "\\")
    # string = string.replace("\\\\", "\\")

    if string.startswith("\\text{") and string.endswith("}"):
        string = string.split("{", 1)[1][:-1]

    # replace tfrac and dfrac with frac
    string = string.replace("tfrac", "frac")
    string = string.replace("dfrac", "frac")
    string = string.replace("cfrac", "frac")

    # remove \left and \right
    string = string.replace("\\left", "")
    string = string.replace("\\right", "")

    # Remove unit: miles, dollars if after is not none
    _string = re.sub(r"\\text{.*?}$", "", string).strip()
    if _string != "" and _string != string:
        # print("Warning: unit not removed: '{}' -> '{}'".format(string, _string))
        string = _string

    # Remove circ (degrees)
    string = string.replace("^{\\circ}", "").strip()
    string = string.replace("^\\circ", "").strip()

    string = regex.sub(r"\{(c|m)?m\}(\^(2|3))?", "", string).strip()
    string = regex.sub(r"p\.m\.$", "", string).strip()
    string = regex.sub(r"(\d)\s*t$", r"\1", string).strip()

    # remove dollar signs
    string = string.replace("\\$", "")
    string = string.replace("$", "")

    # string = string.replace("\\text", "")
    string = string.replace("x\\in", "")

    # remove percentage
    string = string.replace("\\%", "%")
    string = string.replace("\%", "%")
    # string = string.replace("%", "")

    # " 0." equivalent to " ." and "{0." equivalent to "{." Alternatively, add "0" if "." is the start of the string
    string = string.replace(" .", " 0.")
    string = string.replace("{.", "{0.")

    # cdot
    string = string.replace("\\cdot", "")

    # inf
    string = string.replace("infinity", "\\infty")
    if "\\infty" not in string:
        string = string.replace("inf", "\\infty")
    string = string.replace("+\\inity", "\\infty")

    # and 
    # string = string.replace("and", "")
    string = string.replace("\\mathbf", "")
    string = string.replace("\\mathrm", "")

    # use regex to remove \mbox{...}
    string = re.sub(r"\\mbox{.*?}", "", string)

    # quote
    string.replace("'", "")
    string.replace("\"", "")
    
    # i, j
    if "j" in string and "i" not in string:
        string = string.replace("j", "i")

    # replace a.000b where b is not number or b is end, with ab, use regex
    string = re.sub(r"(\d+)\.0+([^\d])", r"\1\2", string)
    string = re.sub(r"(\d+)\.0+$", r"\1", string)

    # if empty, return empty string
    if len(string) == 0:
        return string
    if string[0] == ".":
        string = "0" + string

    # to consider: get rid of e.g. "k = " or "q = " at beginning
    # if len(string.split("=")) == 2:
    #     if len(string.split("=")[0]) <= 2:
    #         string = string.split("=")[1]

    string = _fix_sqrt(string)
    string = _fix_tan(string)
    string = string.replace(" ", "")

    # \frac1b or \frac12 --> \frac{1}{b} and \frac{1}{2}, etc. Even works with \frac1{72} (but not \frac{72}1). Also does a/b --> \\frac{a}{b}
    string = _fix_fracs(string)

    # NOTE: X/Y changed to \frac{X}{Y} in dataset, but in simple cases fix in case the model output is X/Y
    string = _fix_a_slash_b(string)

    string = regex.sub(r"(\\|,|\.)+$", "", string)

    return string

def extract_boxed_answers(text):
    answers = []
    for piece in text.split('boxed{')[1:]:
        n = 0
        for i in range(len(piece)):
            if piece[i] == '{':
                n += 1
            elif piece[i] == '}':
                n -= 1
                if n < 0:
                    if i + 1 < len(piece) and piece[i + 1] == '%':
                        answers.append(piece[: i + 1])
                    else:
                        answers.append(piece[:i])
                    break
    return answers

def extract_program_output(pred_str):
    """
    extract output between the last ```output\n...\n```
    """
    if "```output" not in pred_str:
        return ""
    if '```output' in pred_str:
        pred_str = pred_str.split('```output')[-1]
    if '```' in pred_str:
        pred_str = pred_str.split('```')[0]
    output = pred_str.strip()
    return output

def extract_answer(pred_str, exhaust=False):
    pred = []
    if 'final answer is $' in pred_str and '$. I hope' in pred_str:
        tmp = pred_str.split('final answer is $', 1)[1]
        pred = [tmp.split('$. I hope', 1)[0].strip()]
    elif 'boxed' in pred_str:
        pred = extract_boxed_answers(pred_str)
    elif ('he answer is' in pred_str):
        pred = [pred_str.split('he answer is')[-1].strip()]
    else:
        program_output = extract_program_output(pred_str)
        if program_output != "":
            # fall back to program
            pred.append(program_output)
        else: # use the last number
            pattern = '-?\d*\.?\d+'
            ans = re.findall(pattern, pred_str.replace(",", ""))
            if(len(ans) >= 1):
                ans = ans[-1]
            else:
                ans = ''
            if ans:
                pred.append(ans)

    # multiple line
    _pred = []
    for ans in pred:
        ans = ans.strip().split("\n")[0]
        ans = ans.lstrip(":")
        ans = ans.rstrip(".")
        ans = ans.rstrip("/")
        ans = strip_string(ans)
        _pred.append(ans)
    if exhaust:
        return _pred
    else:
        return _pred[-1] if _pred else ""

def _extract_last_single_answer(reasoning):
    return extract_answer(reasoning, exhaust=False)

def _extract_last_choice_mmlu_few_shot_answer(reasoning):
    if 'Problem:' in reasoning:
        reasoning = reasoning.split("Problem:", 1)[0]
    patt = re.findall(r"\(([abcd])\)", reasoning.lower(), re.IGNORECASE)
    if patt:
        return patt[-1].upper()
    return 'placeholder'

def _extract_last_choice_super_gpqa_few_shot_answer(reasoning):
    if 'Problem:' in reasoning:
        reasoning = reasoning.split("Problem:", 1)[0]
    patt = re.findall(r"\(([abcdefghij])\)", reasoning.lower(), re.IGNORECASE)
    if patt:
        return patt[-1].upper()
    return 'placeholder'

def _extract_sat_few_shot_answer(reasoning):
    if 'Problem:' in reasoning:
        reasoning = reasoning.split("Problem:", 1)[0]
    patt = regex.search(r"the final answer is \(?(?P<ans>[abcd])\)?", reasoning.lower())
    if patt is not None:
        return patt.group('ans').upper()
    return 'placeholder'

def extract_math_answer(question, reasoning):
    answer = []
    for ans in extract_answer(reasoning, exhaust=True):
        if 'separated by commas' in question and all(ch not in ans for ch in '()[]'):
            answer.extend([a.strip() for a in ans.split(",")])
        elif regex.search(r"\\text\{\s*and\s*\}", ans):
            answer.extend([a.strip() for a in regex.sub(r"\\text\{\s*and\s*\}", "[SEP]", ans).split("[SEP]")])
        else:
            answer.append(ans.strip())
    return answer

def extract_math_few_shot_cot_answer(item):
    question = item.get('messages')[-2]['content']
    reasoning = item.get("model_output")
    if 'Problem:' in reasoning:
        reasoning = reasoning.split("Problem:", 1)[0]
    return extract_math_answer(question, reasoning)

def extract_olympiad_math_answer(item):
    reasoning = item.get("model_output")
    reasoning = reasoning.split("Final Answer:")[-1]
    reasoning = reasoning.replace("The final answer is ", "")
    reasoning = reasoning.split("I hope it is correct.")[0]
    reasoning = reasoning.replace("\n", "")
    return ["\\boxed{" + reasoning.strip() + "}"]

def extract_last_single_answer(item):
    reasoning = item.get("model_output")
    return extract_answer(reasoning, exhaust=False)

def extract_gsm_few_shot_cot_answer(item):
    reasoning = item.get("model_output")
    if 'Q: ' in reasoning:
        reasoning = reasoning.split("Q: ", 1)[0]
    pred = [s for s in regex.findall(r'-?\d+\.?\d*', reasoning)]
    if pred:
        return pred[-1]
    else:
        return "[invalid]"

def extract_agieval_gaokao_mathcloze_few_shot_cot_test(item):
    reasoning = item.get("model_output")
    if '问题 ' in reasoning:
        reasoning = reasoning.split("问题 ", 1)[0]
    if '答案是' in reasoning:
        ans = reasoning.split('答案是', 1)[1].strip()
        ans = ans.split("\n")[0].strip()
        ans = [ans.strip("$")]
    else:
        ans = ['placeholder']
    return ans

def extract_agieval_gaokao_mathqa_few_shot_cot_test(item):
    reasoning = item.get("model_output")
    if '问题 ' in reasoning:
        reasoning = reasoning.split("问题 ", 1)[0]
    if '答案是' in reasoning:
        ans = reasoning.split('答案是', 1)[1].strip()
        ans = ans.split("\n")[0].strip()
    else:
        ans = 'placeholder'
    return ans

def extract_sat_few_shot_answer(item):
    reasoning = item.get("model_output")
    if 'Problem:' in reasoning:
        reasoning = reasoning.split("Problem:", 1)[0]
    patt = regex.search(r"the final answer is \(?(?P<ans>[abcd])\)?", reasoning.lower())
    if patt is not None:
        return patt.group('ans').upper()
    return 'placeholder'

def extract_ocwcourses_few_shot_answer(item):
    reasoning = item.get("model_output")
    if 'Problem:' in reasoning:
        reasoning = reasoning.split("Problem:", 1)[0]
    patt = regex.search(r"final answer is (?P<ans>.*)\. I hope it is correct.", reasoning)
    if patt is None:
        pred = "[invalid]"
        print(f"DEBUG >>>\n{reasoning}", flush=True)
    else:
        pred = patt.group('ans')
    return pred

def extract_mmlu_stem(item):
    reasoning = item.get("model_output")
    if 'Problem:' in reasoning:
        reasoning = reasoning.split("Problem:", 1)[0]
    return _extract_last_choice_mmlu_few_shot_answer(reasoning)

def extract_super_gpqa_few_shot_answer(item):
    reasoning = item.get("model_output")
    if 'Problem:' in reasoning:
        reasoning = reasoning.split("Problem:", 1)[0]
    patt = regex.search(r"the final answer is \(?(?P<ans>[abcdefghij])\)?", reasoning.lower())
    if patt is not None:
        return patt.group('ans').upper()
    return 'placeholder'

def extract_super_gpqa(item):
    reasoning = item.get("model_output")
    if 'Problem:' in reasoning:
        reasoning = reasoning.split("Problem:", 1)[0]
    return _extract_last_choice_super_gpqa_few_shot_answer(reasoning)

def extract_mmmlu_zh_math(item):
    reasoning = item.get("model_output")
    if '问题：' in reasoning:
        reasoning = reasoning.split("问题：", 1)[0]
    patt = regex.search(r"所以答案是： \((?P<ans>[ABCD])\)", reasoning)

def extract_medqa(item):
    reasoning = item.get("model_output")
    if 'Problem:' in reasoning:
        reasoning = reasoning.split("Problem:", 1)[0]
    patt = re.findall(r"\(([abcde])\)", reasoning.lower(), re.IGNORECASE)
    if patt:
        return patt[-1].upper()
    return 'placeholder'

def extract_pubmedqa(item):
    reasoning = item.get("model_output")
    if 'Question:' in reasoning:
        reasoning = reasoning.split("Question:", 1)[0]
    patt = re.findall(r"\((yes|no|maybe)\)", reasoning.lower(), re.IGNORECASE)
    if patt:
        return patt[-1].lower()
    return 'placeholder'

def extract_minif2f_isabelle(item):
    reasoning = item.get("model_output")
    if 'Informal:' in reasoning:
        reasoning = reasoning.split("Informal:", 1)[0]
    return reasoning.strip()

def extract_cmath_few_shot_test(item):
    reasoning = item.get("model_output")
    if '问题：' in reasoning:
        reasoning = reasoning.split("问题：", 1)[0]
    if '答案是' in reasoning:
        ans = reasoning.split('答案是', 1)[1].strip()
        ans = ans.split("\n")[0]
        ans = ans.strip("：")
        ans = ans.strip("。")
        try:
            ans = [s for s in regex.findall(r'-?\d+\.?\d*', ans)][-1]
        except:
            print(f"DEBUG CMATH: {reasoning}", flush=True)
            ans = "[invalid]"
    else:
        ans = _extract_last_single_answer(reasoning)
    return ans

def extract_mathqa_few_shot_answer(item):
    reasoning = item.get("model_output")
    if 'Problem:' in reasoning:
        reasoning = reasoning.split("Problem:", 1)[0]
    return _extract_sat_few_shot_answer(reasoning)

def extract_tabmwp_few_shot_answer(item):
    question = item.get('messages')[-2]['content']
    reasoning = item.get("model_output")
    # multiple-choice, e.g., 'short-cut or long-cut', so extract the last word
    print('-' * 100, flush=True)
    print(f"DEBUG TABMWP: {question}", flush=True)
    print(f"DEBUG TABMWP: {reasoning}", flush=True)
    print('Please select from the following options:' in question, flush=True)
    if 'Please select from the following options:' in question:
        # identify the option wrapped by [ ]
        options = regex.findall(r'\[(.*?)\]', question)
        options = eval(f'[{options[0]}]')
        # sort with item word length
        options = sorted(options, key=lambda x: len(x.split()), reverse=True)
        print(options, flush=True)

        extracted_answer = ''
        for option in options:
            option = option.strip('.').lower()
            reasoning_words = reasoning.rstrip('.').split()
            word_group = [' '.join(reasoning_words[i:i+len(option.split())]).rstrip('.').lower() for i in range(len(reasoning_words) - len(option.split()) + 1)]
            print(word_group, flush=True)
            if option in word_group:
                print(f"DEBUG TABMWP: {option}", flush=True)
                extracted_answer = option
        if extracted_answer != '':
            return extracted_answer
        print("DEBUG TABMWP: [invalid]", flush=True)
        return "[invalid]"
    else:
        return _extract_last_single_answer(reasoning)

# The following is for super-gpqa
@timeout_decorator.timeout(5)  # 5 seconds timeout
def safe_regex_search(pattern, text, flags=0):
    """
    TODO: The optimal solution for timeout detection is to use the 'regex' library instead of 're' for regular expression matching.
    However, since the 'regex' and 're' libraries handle regex parsing differently, it has not been adopted for now.
    
    Issue: The current implementation using 'timeout_decorator' does not work on Windows platforms.
    Reason: 'timeout_decorator' relies on signal-based timeouts, which are only supported on Unix-based systems and do not work on Windows.
    """
    try:
        return re.search(pattern, text, flags)
    except timeout_decorator.TimeoutError:
        print(f"Regex match timeout: pattern={pattern}, text={text[:100]}...")
        return None
    except Exception as e:
        print(f"Regex match error: {str(e)}")
        return None

def extract_option_labels(text, options='ABCDEFGHIJ'):
    if not isinstance(text, str) or not isinstance(options, str):
        return 'error'
    
    text = text.rstrip()
    last_line = text.split('\n')[-1]
    
    option_str = ''.join([chr(65 + i) for i in range(len(options))]) if options else 'ABCDEFGHIJ'
    
    patterns = [
        # e.g. "The final answer to this question is: A."
        #      "The best option is $\boxed{B}:"
        #      "The correct answer is (C)."
        f'[Tt]he\s+(?:\w+\s+)?(?:answer|option|choice|result)(?:\w+\s+)?\s+is?:?\s*(?:[\*\$\\{{(\[\\\\(]*?(?:(?:\\\\boxed|\\\\mathbf|\\\\mathrm|\\\\text){{)?)*\s*([{option_str}])(?:\\\\?\}}?\$?\)?\]?\}}?)*(?:[\s:\.\*)]|$)',

        # e.g. "ANSWER: A"
        #      "Answer: $\boxed{B}."
        #      "ANSWER: (C):"
        f'(?i:Answer)[\*\s]*:\s*(?:[\*\$\\{{(\[\\\\(]*?(?:(?:\\\\boxed|\\\\mathbf|\\\\mathrm|\\\\text){{)?)*\s*([{option_str}])(?:\\\\?\}}?\$?\)?\]?\}}?)*(?:[\s:\.\*)]|$)',
        f'(?i:Option)[\*\s]*:\s*(?:[\*\$\\{{(\[\\\\(]*?(?:(?:\\\\boxed|\\\\mathbf|\\\\mathrm|\\\\text){{)?)*\s*([{option_str}])(?:\\\\?\}}?\$?\)?\]?\}}?)*(?:[\s:\.\*)]|$)',
        f'(?i:Choice)[\*\s]*:\s*(?:[\*\$\\{{(\[\\\\(]*?(?:(?:\\\\boxed|\\\\mathbf|\\\\mathrm|\\\\text){{)?)*\s*([{option_str}])(?:\\\\?\}}?\$?\)?\]?\}}?)*(?:[\s:\.\*)]|$)',
        f'(?i:Result)[\*\s]*:\s*(?:[\*\$\\{{(\[\\\\(]*?(?:(?:\\\\boxed|\\\\mathbf|\\\\mathrm|\\\\text){{)?)*\s*([{option_str}])(?:\\\\?\}}?\$?\)?\]?\}}?)*(?:[\s:\.\*)]|$)',

        # answer should be A
        # Answer must be A
        f'(?:[Aa]nswer|option|choice|result)(?:\w+\s+)?\s+(?:should be|must be)?:?\s*(?:[\*\$\\{{(\[\\\\(]*?(?:(?:\\\\boxed|\\\\mathbf|\\\\mathrm|\\\\text){{)?)*\s*([{option_str}])(?:\\\\?\}}?\$?\)?\]?\}}?)*(?:[\s:\.\*)]|$)',

        # Answer is probably A
        f'(?:[Aa]nswer|option|choice|result)(?:\w+\s+)?\s+is?\s+probably?:?\s*(?:[\*\$\\{{(\[\\\\(]*?(?:(?:\\\\boxed|\\\\mathbf|\\\\mathrm|\\\\text){{)?)*\s*([{option_str}])(?:\\\\?\}}?\$?\)?\]?\}}?)*(?:[\s:\.\*)]|$)',

        # A is correct
        # A seems correct
        f'(?:[\*\$\\{{(\[\\\\(]*?(?:(?:\\\\boxed|\\\\mathbf|\\\\mathrm|\\\\text){{)?)*\s*([{option_str}])(?:\\\\?\}}?\$?\)?\]?\}}?)*\s+(?:is|seems)?\s+correct',

        # A is the right answer
        f'(?:[\*\$\\{{(\[\\\\(]*?(?:(?:\\\\boxed|\\\\mathbf|\\\\mathrm|\\\\text){{)?)*\s*([{option_str}])(?:\\\\?\}}?\$?\)?\]?\}}?)*\s+(?:is|seems)?\s+the?\s+(?:right|correct)?\s+(?:answer|option|choice|result)',

        # answer is A
        f'(?:[Aa]nswer|option|choice|result)(?:\w+\s+)?\s+is?:?\s*(?:[\*\$\\{{(\[\\\\(]*?(?:(?:\\\\boxed|\\\\mathbf|\\\\mathrm|\\\\text){{)?)*\s*([{option_str}])(?:\\\\?\}}?\$?\)?\]?\}}?)*(?:[\s:\.\*)]|$)',

        # e.g. "A"
        #      "$\boxed{B}$"
        #      "(C)."
        #      "[D]:"
        # f'^[^\w\r\n]*(?:[\*\$\\{{(\[\\\\(]*?(?:(?:\\\\boxed|\\\\mathbf|\\\\mathrm|\\\\text){{)?)*\s*([{option_str}])(?:\\\\?\}}?\$?\)?\]?\}}?)*(?:[\s:\.\*)]|$)',
        r'\\(?:boxed|mathbf|mathrm|text)\{([' + option_str + '])\}'
    ]

    for pattern in patterns:
        match = safe_regex_search(pattern, last_line, re.IGNORECASE)
        if match:
            return match.group(1)
    
    for pattern in patterns:
        match = safe_regex_search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)
    
    return None

def extract_option_content(text, options_content=None):
    if not isinstance(text, str) or not isinstance(options_content, list):
        return 'error'
    
    escaped_options_content = [re.escape(option_content) for option_content in options_content]
    escaped_options_content_str = '|'.join(escaped_options_content)
    
    text = text.rstrip()
    last_line = text.split('\n')[-1]
        
    patterns = [
        f'[Tt]he\s+(?:\w+\s+)?(?:answer|option)(?:\w+\s+)?\s+is:?\s*(?:[\*\$\\{{\(\[\\\\(]*?(?:(?:\\\\boxed|\\\\mathbf|\\\\mathrm|\\\\text){{)?)*\s*({escaped_options_content_str})(?:\\\\?\}}?\$?\)?\]?\}}?)*(?:[\s:\.\*)]|$)',
        
        f'(?i:Answer)\s*(?:[\*\$\\{{\(\[\\\\(]*?(?:(?:\\\\boxed|\\\\mathbf|\\\\mathrm|\\\\text){{)?)*\s*({escaped_options_content_str})(?:\\\\?\}}?\$?\)?\]?\}}?)*(?:[\s:\.\*)]|$)',
        
        f'^[^\w\r\n]*(?:[\*\$\\{{\(\[\\\\(]*?(?:(?:\\\\boxed|\\\\mathbf|\\\\mathrm|\\\\text){{)?)*\s*({escaped_options_content_str})(?:\\\\?\}}?\$?\)?\]?\}}?)*(?:[\s:\.\*)]|$)',
    ]
    
    for pattern in patterns:
        match = safe_regex_search(pattern, last_line)
        if match:
            if match.group(1) in escaped_options_content:
                return options_content[escaped_options_content.index(match.group(1))]
            else:
                return match.group(1)
    
    for pattern in patterns:
        match = safe_regex_search(pattern, text)
        if match:
            if match.group(1) in escaped_options_content:
                return options_content[escaped_options_content.index(match.group(1))]
            else:
                return match.group(1)
    
    return None

def extract_super_gpqa_sft_answer(item):
    question = item.get('messages')[-2]['content']
    reasoning = item.get("model_output")
    options = item.get("options")
    predict = extract_option_labels(reasoning, 'ABCDEFGHIJ')
    if predict == None:
        predict = extract_option_content(reasoning, options)
        predict = chr(options.index(predict) + 65) if predict else None
    return predict if predict else 'placeholder'

def extract_mmlu_pro_sft_answer(item):
    return extract_super_gpqa_sft_answer(item)

def extract_mmlu_sft_answer(item):
    question = item.get('messages')[-2]['content']
    reasoning = item.get("model_output")
    options = item.get("options")
    predict = extract_option_labels(reasoning, 'ABCD')
    if predict == None:
        predict = extract_option_content(reasoning, options)
        predict = chr(options.index(predict) + 65) if predict else None
    return predict if predict else 'placeholder'

def extract_gpqa_sft_answer(item):
    return extract_mmlu_sft_answer(item)

def extract_two_choice_sft_answer(item):
    question = item.get('messages')[-2]['content']
    reasoning = item.get("model_output")
    options = item.get("options")
    predict = extract_option_labels(reasoning, 'AB')
    if predict == None:
        predict = extract_option_content(reasoning, options)
        predict = chr(options.index(predict) + 65) if predict else None
    return predict if predict else 'placeholder'

def extract_five_choice_sft_answer(item):
    question = item.get('messages')[-2]['content']
    reasoning = item.get("model_output")
    options = item.get("options")
    predict = extract_option_labels(reasoning, 'ABCDE')
    if predict == None:
        predict = extract_option_content(reasoning, options)
        predict = chr(options.index(predict) + 65) if predict else None
    return predict if predict else 'placeholder'

def extract_three_choice_sft_answer(item):
    question = item.get('messages')[-2]['content']
    reasoning = item.get("model_output")
    options = item.get("options")
    predict = extract_option_labels(reasoning, 'ABC')
    if predict == None:
        predict = extract_option_content(reasoning, options)
        predict = chr(options.index(predict) + 65) if predict else None
    return predict if predict else 'placeholder'

def extract_adaptive_mc_sft_answer(item):
    question = item.get('messages')[-2]['content']
    reasoning = item.get("model_output")
    options = item.get("options")
    if not options:
        raise ValueError("No Options!")
    choices = "".join([chr(65+i) for i in range(len(options))])
    predict = extract_option_labels(reasoning, choices)
    if predict == None:
        predict = extract_option_content(reasoning, options)
        predict = chr(options.index(predict) + 65) if predict else None
    return predict if predict else 'placeholder'

def extract_scibench_sft_answer(item):
    question = item.get('messages')[-2]['content']
    reasoning = item.get("model_output")
    return parse_math_answer(reasoning)

def extract_olympic_arena_sft_answer(item):
    reasoning = item.get("model_output")
    
    # find all \boxed{
    matches = []
    start_pos = 0
    while True:
        match = re.search(r'\\boxed{', reasoning[start_pos:])
        if not match:
            break
        actual_pos = start_pos + match.start()
        matches.append(start_pos + match.end())  #sive the position of { 
        start_pos = actual_pos + 1
    
    if not matches:
        return reasoning
    # process the last \boxed{
    start_index = matches[-1]
    end_index = start_index
    stack = 1
    
    start_index = matches[-1]
    end_index = start_index
    stack = 1
    while stack > 0 and end_index < len(reasoning):
        if reasoning[end_index] == '{':
            stack += 1
        elif reasoning[end_index] == '}':
            stack -= 1
        end_index += 1
    if stack == 0:
        content = reasoning[start_index:end_index - 1]
        if not content:
            return reasoning
        else:
            content = _normalize_answer(content)
            return content
    return reasoning