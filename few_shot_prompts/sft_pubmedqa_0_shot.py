from .few_shot_prompting import FewShotPrompting

few_shot_prompt = """Answer the following multiple choice question. Given the following information and a question, analyze the information step by step using your internal knowledge. Consider all relevant details before arriving at an answer. There is only one correct answer. The last line of your response should be in the format 'Answer: $LETTER' (without quotes), where LETTER is one of A, B, or C."""

class SFTPubmedQAPrompt(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n{task_input}"
        return prompt.strip()

    def stop_words(self):
        return []
