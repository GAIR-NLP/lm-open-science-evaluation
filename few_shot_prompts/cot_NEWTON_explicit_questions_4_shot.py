from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
tortilla is less hard on the surface than button.What of the following is the right choice? 
What of the following is the right choice? Explain your answer.
(A) True
(B) False
Solution:
Tortillas are soft, pliable flatbreads made from flour that yield to pressure. Buttons, functioning as fasteners, are deliberately manufactured to be rigid and durable. Even considering variations (stale tortillas or softer button materials), the general principle holds that buttons are harder than tortillas.
Final Answer: The final answer is (A). I hope it is correct.

Problem:
Which object is the least soft?
What of the following is the right choice? Explain your answer.
(A) dishtowel
(B) short_pants
(C) beanbag
(D) toolbox
Solution:
To determine the least soft object, I examine the material composition and relative rigidity of each option: a dishtowel (fabric, inherently soft), short pants (fabric, characteristically pliable), beanbag (filled with soft materials like foam or beads, yielding upon pressure), and toolbox (typically constructed from metal or hard plastic, structurally rigid). By analyzing these physical properties, I conclude that the toolbox represents the least soft option because its constituent materials lack the flexibility and compressibility present in the fabric-based dishtowel and short pants or the malleable filling of the beanbag, making it comparatively hard and unyielding to touch or pressure. Therefore, the answer is (D) Toolbox.
Final Answer: The final answer is (D). I hope it is correct.

Problem:
cake is more hard on the surface than bunk_bed
What of the following is the right choice? Explain your answer.
(A) True
(B) False
Solution:
A cake's surface, whether sponge or cheesecake variety, presents a soft or slightly firm outer texture, potentially including a crust or icing, but fundamentally remains far softer than solid furniture. In contrast, bunk beds are constructed from robust wood or metal materials that possess substantially greater hardness than any cake component. Therefore, the claim that "cake is more hard on the surface than bunk_bed" contradicts physical reality and is demonstrably false.
Final Answer: The final answer is (B). I hope it is correct.

Problem:
Which object is the most elastic?
What of the following is the right choice? Explain your answer.
(A) coil
(B) cookie
(C) yogurt
(D) ladle
Solution:
Elasticity—an object's ability to restore its original shape after deformation—requires analyzing each option through this lens: A coil displays quintessential elasticity by returning to its original shape when stretched or compressed due to its restoring force; cookies exhibit brittleness, breaking rather than returning to form when deformed; yogurt lacks a fixed shape as a fluid-like substance, making restoration to an original form impossible; and ladles, typically metal or plastic, either remain rigid or deform permanently rather than demonstrating meaningful elasticity. Therefore, a coil (A) uniquely demonstrates true elasticity among these options.
Final Answer: The final answer is (A). I hope it is correct."""

class NEWTONExplicitQuestions(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
