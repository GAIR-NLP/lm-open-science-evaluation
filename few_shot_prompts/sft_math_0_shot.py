from .few_shot_prompting import FewShotPrompting

few_shot_prompt = """"""

class SFTMATH0ShotPrompt(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"Question: {task_input}\nPlease reason step by step, and put your final answer within " + "\\boxed{}."
        return prompt.strip()

    def stop_words(self):
        return []
