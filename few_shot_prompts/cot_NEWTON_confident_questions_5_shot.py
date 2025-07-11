from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
Brittleness: How easy is it for an adhesive_tape to break (shatter, crack) when a sudden impact force is applied?
What of the following is the right choice? Explain your answer.
(A) Low: object can withstand most impact forces (drop, smash, etc.).
(B) Moderate: object can withstand minor impact forces.
(C) High: object shatters easily with impact force.
Solution:
Brittleness is a material's tendency to fracture under stress without deformation. Adhesive tapes are made from flexible materials (polypropylene, PVC, cloth) designed to deform under stress rather than crack. When impacted, these materials stretch or tear instead of shattering. Common tapes exhibit low brittleness as their flexibility allows them to absorb impacts without catastrophic failure. Options B and C suggest fragility, contradicting adhesive tapes' inherent properties. Therefore, A is correct.
Final Answer: The final answer is (A). I hope it is correct.

Problem:
Elasticity: If you were to deform an aerosol (by squeezing, hitting, etc.) can it recover to its original form?
What of the following is the right choice? Explain your answer.
(A) No: Object will not be able to return to its original form.
(B) Somewhat: Object may recover to its original form but will have signs of previous deformations.
(C) Yes: Object is capable of recovering near perfectly to the original form.
Solution:
# Aerosol Can Deformation Analysis
Aerosol cans (steel/aluminum) undergo permanent changes when damaged because:
1. **Elastic vs. Plastic Deformation**: While metals have elastic properties, typical forces from squeezing or hitting exceed the elastic limit, causing permanent (plastic) deformation.
2. **Pressure Limitations**: Internal pressure (2-8 atm) is insufficient to reverse dents, as it cannot overcome the metal's yield strength (~10,000 psi for aluminum).
3. **Material Properties**: Unlike elastic materials (e.g., rubber), metals maintain deformation once their structure is altered.
Therefore, everyday deformation of aerosol cans is irreversible, making **(A)** correct.
Final Answer: The final answer is (A). I hope it is correct.

Problem:
Surface smoothness: What is the surface smoothness of an aerosol?
What of the following is the right choice? Explain your answer.
(A) Low: majority of surface is very rough, or has many bumps.
(B) Moderate: some parts of surface are smooth, while some parts are not.
(C) High: majority of surface is smooth.
Solution:
Aerosol surface smoothness depends on particle state:
- **Liquid aerosols** (mist, fog, spray droplets): **high smoothness** due to surface tension forming spherical shapes
- **Solid aerosols** (dust, soot): irregular, rough surfaces
Without specified aerosol type, the reasonable assumption is that common liquid-based aerosols (sprays, inhalers, atmospheric water droplets) are being referenced, which typically have smooth surfaces.
Final Answer: The final answer is (C). I hope it is correct.

Problem:
Brittleness: How easy is it for an alcohol to break (shatter, crack) when a sudden impact force is applied?
What of the following is the right choice? Explain your answer.
(A) Low: object can withstand most impact forces (drop, smash, etc.).
(B) Moderate: object can withstand minor impact forces.
(C) High: object shatters easily with impact force.
Solution:
## Analysis of Alcohol Object Brittleness
The term "alcohol" creates ambiguity since alcohols are typically liquids that cannot exhibit brittleness.
Possible interpretations:
1. **Liquid Alcohol**: Not brittle (A), but inconsistent with "object" terminology
2. **Frozen/Solid Alcohol**: Likely behaves as brittle crystalline solid (C)
3. **Translation Error**: Possibly meant to refer to glass, a classic brittle material (C)
4. **Alcohol-based Polymer**: Some formulations are brittle (C)
## Conclusion
The most reasonable interpretation (either as a contextual error referring to glass or as solid alcohol) supports high brittleness.
**Answer: (C) High: object shatters easily with impact force.**
Final Answer: The final answer is (C). I hope it is correct.

Problem:
Softness: What is the softness (fluffyness, squishiness) of an aerosol?
What of the following is the right choice? Explain your answer.
(A) Low: object is hard.
(B) Moderate: some parts of the object are soft.
(C) High: the majority of the object is soft.
Solution:
Softness depends on resistance to compression and tactile feedback. For aerosols:
1. **Standard Aerosols**: Dispersed particles in gas lack cohesive structure, offering minimal resistance when touched. They feel insubstantial rather than soft (e.g., fog feels like moist air, not a soft object).
2. **Foam Exception**: Some deposited aerosols form structured foams (shaving cream, whipped cream) which are soft, but the question likely addresses airborne aerosols pre-deposition.
3. **Option Analysis**:
   - **(A) Low**: Aerosols yield without resistance due to their gaseous nature. While not "hard" like solids, they lack the structural integrity required for softness.
   - **(B) Moderate**: Implies partial softness, but aerosols are predominantly gas with sparse particles insufficient to create moderate softness.
   - **(C) High**: Incorrect as aerosols are mostly gas, which is not soft. Particles are too dispersed to create a soft tactile experience.
**Conclusion**: **(A) Low** is most accurate. Though "hard" is imprecise (aerosols aren't rigid), they lack the cohesive structure necessary for softness, making "low softness" the most appropriate characterization.
Final Answer: The final answer is (A). I hope it is correct."""

class NEWTONConfidentQuestions(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
