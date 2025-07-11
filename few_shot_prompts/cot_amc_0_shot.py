from .few_shot_prompting import FewShotPrompting


few_shot_prompt = ""

class CoTAMCPrompt(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nQ: {task_input}\nA: {task_output}"
        return prompt.lstrip("\n")

    def stop_words(self):
        return ["\nQ:"]
