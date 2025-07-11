from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
I am packing a backpack. Which of clothes_hamper, egg, ice_cream, chocolate_cake should I put at the bottom?
What of the following is the right choice? Explain your answer.
(A) clothes_hamper
(B) egg
(C) ice_cream
(D) chocolate_cake
Solution:
When arranging items, we must consider weight, stability, and fragility simultaneously. A clothes hamper provides the ideal base because it's typically sturdy, non-fragile, and capable of supporting other objects without damage. The alternatives are impractical: eggs would crack under pressure, ice cream would melt (especially beneath heavier or warm items), and chocolate cake would get squished due to its soft, delicate structure. The clothes hamper's superior structural integrity makes it the only logical choice for the bottom position.
Final Answer: The final answer is (A). I hope it is correct.

Problem:
I am wrapping fragile gifts and want to protect them from impact. Which of pocket_watch, bath_towel, chalk, mirror should I choose for cushioning?
What of the following is the right choice? Explain your answer.
(A) pocket_watch
(B) bath_towel
(C) chalk
(D) mirror
Solution:
To protect a fragile gift, a bath towel is the optimal choice because it provides soft cushioning and impact absorption, unlike the unsuitable alternatives: a pocket watch (itself small and delicate), chalk (hard and brittle, potentially causing damage), and a mirror (fragile and counterproductive for protection). The towel's thickness and absorbent qualities make it ideally suited for wrapping and safeguarding delicate items during transport.
Final Answer: The final answer is (B). I hope it is correct.

Problem:
I need to prepare a work table as a play area for kids. Which of cone, helmet, dagger, water_cooler should I remove?
What of the following is the right choice? Explain your answer.
(A) cone
(B) helmet
(C) dagger
(D) water_cooler
Solution:
To determine the unsuitable item for a children's play area, I analyzed each object's purpose and safety implications. A cone serves as a play structure or obstacle, a helmet provides safety during physical activities, and a water cooler offers essential hydration, especially during extended play. However, a dagger, being a weapon, presents a significant safety risk to children. Therefore, removing the dagger is the logical choice to maintain a safe play environment while preserving useful items that facilitate healthy, protected physical activity.
Final Answer: The final answer is (C). I hope it is correct.

Problem:
I have a robot which sorts objects by tossing them to bins. Which of alcohol, diaper, cup, egg_yolk can be tossed safely?
What of the following is the right choice? Explain your answer.
(A) alcohol
(B) diaper
(C) cup
(D) egg_yolk
Solution:
To determine the safest item to toss, we analyze potential hazards: alcohol risks spillage and safety concerns if its container isn't throw-resistant; diapers, being soft, light, flexible, and impact-absorbing, won't break or spill, making them optimal for tossing; cups may shatter depending on their material (particularly glass), creating dangerous conditions; egg yolks are inherently fragile and would likely rupture when thrown, causing messy spills. Through this comparative assessment of physical properties and potential consequences, we conclude diapers present the safest tossing option due to their lightweight nature and inability to cause damage or create messes.
Final Answer: The final answer is (B). I hope it is correct."""

class NEWTONImplicitQuestions(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
