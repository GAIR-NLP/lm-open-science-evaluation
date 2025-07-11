from .few_shot_prompting import FewShotPrompting

few_shot_prompt = """You are a highly skilled student proficient in solving scientific problems."""

class SFTOlympicArenaPrompt(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n{task_input}"
        return prompt.strip()

    def stop_words(self):
        return []
