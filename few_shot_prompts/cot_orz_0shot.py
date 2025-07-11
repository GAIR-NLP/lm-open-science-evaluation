from .few_shot_prompting import FewShotPrompting

orz_0shot_prompt = """
A conversation between User and Assistant. The user asks a question, and the Assistant solves it. The assistant first thinks about the reasoning process in the mind and then provides the user with the answer. User: You must put your answer inside \\boxed{} and Your final answer will be extracted automatically by the \\boxed{} tag.
""".strip()


class ORZMathPrompt(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{orz_0shot_prompt}\n{task_input}\nAssistant: {task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["User:", "Assistant:"]
