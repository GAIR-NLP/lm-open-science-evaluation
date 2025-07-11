from .few_shot_prompting import FewShotPrompting

few_shot_prompt = """"""

class SFTGSM0ShotPrompt(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"Question: {task_input}\nLet's think step by step"
        return prompt.strip()

    def stop_words(self):
        return []
