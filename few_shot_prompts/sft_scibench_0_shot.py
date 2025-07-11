from .few_shot_prompting import FewShotPrompting

few_shot_prompt = """Please provide a clear and step-by-step solution for a scientific problem in the categories of Chemistry, Physics, or Mathematics. The problem will specify the unit of measurement, which should not be included in the answer. Express the final answer as a decimal number with three digits after the decimal point. Conclude the answer by stating \"The answer is therefore \\boxed{[ANSWER]}.\""""

class SFTScibenchPrompt(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\nQuestion: {task_input}\nLet's think step by step."
        return prompt.strip()

    def stop_words(self):
        return []
