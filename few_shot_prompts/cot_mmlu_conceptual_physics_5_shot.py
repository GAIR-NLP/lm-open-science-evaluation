from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
Compared with the mass of a uranium atom undergoing fission, the combined masses of the products after fission are
What of the following is the right choice? Explain your answer.
(A) less
(B) more
(C) the same
(D) zero
Solution:
To determine the current through the resistor, when a uranium atom undergoes nuclear fission, it splits into smaller nuclei, free neutrons, and releases energy, with the total mass of these products being slightly less than the original uranium nucleus. This mass reduction (known as mass defect) directly corresponds to the energy released during fission through Einstein's mass-energy equivalence principle (E = mc²). The "missing" mass is converted into the kinetic energy of the fission fragments, radiation, and heat—powering nuclear reactors and atomic bombs—meaning the combined mass of post-fission products is measurably less than the original uranium atom's mass.
Final Answer: The final answer is (A). I hope it is correct.

Problem:
Things that are equivalent according to the equivalence principle are
What of the following is the right choice? Explain your answer.
(A) space and time.
(B) a traveling twin and a stay-at-home twin.
(C) gravity and acceleration.
(D) mass and energy.
Solution:
The equivalence principle, a cornerstone of Einstein's general relativity, establishes that gravity's effects cannot be locally distinguished from acceleration effects—essentially, an observer in a confined space like an elevator cannot determine whether they're experiencing gravitational force or equivalent acceleration. This principle differs from other relativistic concepts: it doesn't address the space-time interweaving (option A), has no connection to the twin paradox involving time dilation from velocity differences (option B), and is distinct from mass-energy equivalence expressed by E=mc² (option D). Therefore, the correct answer is (C) gravity and acceleration, as this directly describes the equivalence relationship the principle establishes.
Final Answer: The final answer is (C). I hope it is correct.

Problem:
Colors in a soap bubble result from light
What of the following is the right choice? Explain your answer.
(A) converted to a different frequency
(B) deflection
(C) interference
(D) polarization
Solution:
The colors in a soap bubble arise from light wave interference as waves reflect from both the outer and inner soap film surfaces. When light strikes the bubble, partial reflection occurs at the outer surface while some light passes through, reflects off the inner surface, and then rejoins the outer reflection. These reflected waves combine either constructively (producing bright colors) or destructively (creating diminished colors), with the specific outcome determined by both the film thickness and light wavelength, ultimately generating the bubble's characteristic rainbow patterns. Alternative explanations fail because: frequency conversion doesn't occur during this process; simple deflection changes direction but doesn't create colors; and polarization affects wave orientation without directly producing the colorful display—making interference the only accurate explanation for this optical phenomenon.
Final Answer: The final answer is (C). I hope it is correct.

Problem:
A model airplane flies slower when flying into the wind and faster with wind at its back. When launched at right angles to the wind a cross wind its groundspeed compared with flying in still air is
What of the following is the right choice? Explain your answer.
(A) the same
(B) greater
(C) less
(D) either greater or less depending on wind speed
Solution:
When a model airplane flies in still air, its groundspeed equals its airspeed, but with a crosswind (perpendicular to flight direction), the plane's motion combines both velocities through vector addition. Analyzing this with the Pythagorean theorem: if airspeed is v and perpendicular wind speed is w, then groundspeed = √(v² + w²). Since this mathematical relationship adds the wind as a perpendicular component, the resulting groundspeed must always be greater than the original airspeed v (except when w=0), making option (B) greater the correct answer.
Final Answer: The final answer is (B). I hope it is correct.

Problem:
Which of these three elements has the most mass per nucleon?
What of the following is the right choice? Explain your answer.
(A) Hydrogen
(B) Iron
(C) Uranium
(D) Same in each
Solution:
Nuclear binding energy determines mass per nucleon through mass-energy equivalence (E=mc²), with tightly bound nuclei having less mass per nucleon. Comparing the three elements: Hydrogen's protium (¹H) consists of a single proton with no binding energy loss, giving it the highest mass per nucleon (~1.0078 u). Iron-56 (⁵⁶Fe) is highly stable with significant binding energy (~8.8 MeV/nucleon), resulting in lower mass per nucleon than hydrogen. Uranium-238 (²³⁸U), despite being heavier, has lower binding energy per nucleon (~7.6 MeV) than iron, but still exhibits less mass per nucleon than hydrogen due to nuclear binding effects. Therefore, hydrogen has the highest mass per nucleon because it lacks any binding energy reduction, making (A) Hydrogen the correct answer.
Final Answer: The final answer is (A). I hope it is correct."""

class MMLUConceptualPhysics(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
