from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
When boiling butter, when it's ready, you can
What of the following is the right choice? Explain your answer.
(A) Pour it onto a plate
(B) Pour it into a jar
Solution:
To clarify butter, boil it to remove water and separate milk solids from the pure fat, then strain. For proper storage, an airtight container like a jar (option B) is essential—not a plate (option A)—as it protects the clarified butter from air exposure, contamination, and odors while maintaining freshness during refrigeration or room temperature storage.
Final Answer: The final answer is (B). I hope it is correct.

Problem:
To permanently attach metal legs to a chair, you can
What of the following is the right choice? Explain your answer.
(A) Weld the metal together to get it to stay firmly in place
(B) Nail the metal together to get it to stay firmly in place
Solution:
To permanently join metal chair legs, welding outperforms nailing by creating molecular-level fusion that withstands stress long-term. Unlike nails, which loosen over time and are ineffective for metal-to-metal connections since they require softer materials to grip into, welding forms a continuous bond without introducing structural weak points from fasteners or holes. Though requiring specialized equipment, welding's superior permanence and structural integrity make it the clearly superior method (option A) when durability is the primary concern.
Final Answer: The final answer is (A). I hope it is correct.

Problem:
how do you shake something?
What of the following is the right choice? Explain your answer.
(A) move it up and down and side to side quickly.
(B) stir it very quickly.
Solution:
To "shake" something denotes rapid, irregular back-and-forth or up-and-down movement, typically forceful in nature—as with shaking a bottle, hands, or a dust-filled rug. This differs fundamentally from (B) "stir it very quickly", which describes a controlled, circular rotation of substances using implements like spoons. The key distinction lies in motion characteristics: shaking involves vigorous, chaotic movement, while stirring, even when done rapidly, maintains a smoother, more controlled circular pattern.
Final Answer: The final answer is (A). I hope it is correct.

Problem:
Clean tires
What of the following is the right choice? Explain your answer.
(A) Pour water, cape off caked on dirt. Use  speed wool to clean out crevices and sparrow spaces.
(B) Pour water, scrape off caked on dirt. Use a steel wool to clean out crevices and narrow spaces.
Solution:
To clean tough, caked-on dirt from narrow spaces, you should scrape off the dirt using steel wool. "Cape off" is incorrect as "cape" is a noun (clothing/landform) not applicable to dirt removal; "scrape off" correctly describes removing material by rubbing or scratching. "Speed wool" doesn't exist as a cleaning material, while "steel wool" is a standard abrasive cleaning tool. "Sparrow spaces" is nonsensical since "sparrow" refers to a bird; "narrow spaces" correctly describes small, tight areas where dirt accumulates. Option (B) is therefore correct.
Final Answer: The final answer is (B). I hope it is correct.

Problem:
how do you taste something?
What of the following is the right choice? Explain your answer.
(A) smell it enough to taste it.
(B) place it in your mouth to taste.
Solution:
To taste something, the substance must physically contact taste buds on the tongue and dissolve in saliva to activate taste receptors that detect sweet, sour, salty, bitter, and umami flavors. While smell significantly contributes to overall flavor perception and enhances the eating experience, it cannot independently trigger taste sensation without direct tongue contact. Therefore, placing food in the mouth is necessary for actual tasting, making option (B) correct.
Final Answer: The final answer is (B). I hope it is correct."""

class PIQA(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
