from .few_shot_prompting import FewShotPrompting

few_shot_prompt = """Answer the following multiple choice question. There is only one correct answer. The last line of your response should be in the format 'Answer: $LETTER' (without quotes), where LETTER is one of A, B, C, D, E, F, G, H, I, or J."""

class SFTSuperGPQAPrompt(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\nQuestion: {task_input}"
        return prompt.strip()

    def stop_words(self):
        return []
