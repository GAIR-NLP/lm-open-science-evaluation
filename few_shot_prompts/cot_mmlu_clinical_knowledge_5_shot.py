from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
The energy for all forms of muscle contraction is provided by:
What of the following is the right choice? Explain your answer.
(A) ATP.
(B) ADP.
(C) phosphocreatine.
(D) oxidative phosphorylation.
Solution:
The correct answer is **(A) ATP**. Here's the explanation:

- **ATP (Adenosine Triphosphate)** is the direct source of energy for all forms of muscle contraction. When a muscle contracts, ATP is hydrolyzed to ADP (Adenosine Diphosphate) and inorganic phosphate, releasing energy that powers the sliding of actin and myosin filaments, which is the basis of muscle contraction.  
- **ADP (B)** is a byproduct of ATP breakdown and does not provide energy itself.  
- **Phosphocreatine (C)** acts as a rapid reservoir to regenerate ATP during short bursts of activity (e.g., sprinting), but it is not the direct energy source.  
- **Oxidative phosphorylation (D)** is a metabolic pathway that produces ATP during aerobic respiration, but it is a process that generates ATP rather than directly providing energy for contraction.  

Thus, while other systems (like phosphocreatine or oxidative phosphorylation) contribute to ATP replenishment, **ATP itself is the immediate energy currency** used for muscle contraction in all scenarios.

Final Answer: The final answer is (A). I hope it is correct.

Problem:
What is the difference between a male and a female catheter?
What of the following is the right choice? Explain your answer.
(A) Male and female catheters are different colours.
(B) Male catheters are longer than female catheters.
(C) Male catheters are bigger than female catheters.
(D) Female catheters are longer than male catheters.
Solution:
The correct answer is **(B) Male catheters are longer than female catheters.**

**Explanation:**  
The primary anatomical difference between male and female urethras dictates catheter design. Males have a longer urethra (15–20 cm) due to its path through the penis, while females have a much shorter urethra (4 cm). To safely reach the bladder, **male catheters are typically 16–18 inches (40–45 cm)** long, whereas **female catheters are shorter, around 6–8 inches (15–20 cm)**. 

**Why other options are incorrect:**  
- **(A)** Color is not standardized for gender differentiation; it varies by brand or purpose.  
- **(C)** Diameter (size) is measured in French units (Fr) and depends on clinical need, not gender.  
- **(D)** Female catheters are shorter, not longer, due to anatomical differences.  

Thus, the key distinction is **length**, making **(B)** the correct choice.

Final Answer: The final answer is (B). I hope it is correct.

Problem:
In the assessment of the hand function which of the following is true?
What of the following is the right choice? Explain your answer.
(A) Abduction of the thumb is supplied by spinal root T2
(B) Opposition of the thumb by opponens policis is supplied by spinal root T1
(C) Finger adduction is supplied by the median nerve
(D) Finger abduction is mediated by the palmar interossei
Solution:
The correct answer is **(B) Opposition of the thumb by opponens pollicis is supplied by spinal root T1**. Here's the breakdown:

1. **Option (A):** Thumb abduction is performed by the abductor pollicis brevis, innervated by the **median nerve** (not T2). The median nerve originates from spinal roots **C5-T1**, making T2 incorrect.  
2. **Option (B):** The opponens pollicis (responsible for thumb opposition) is innervated by the median nerve. The median nerve’s spinal roots include **T1**, so this statement is **correct**.  
3. **Option (C):** Finger adduction is mediated by the **palmar interossei**, which are innervated by the **ulnar nerve** (not the median nerve). Thus, this is incorrect.  
4. **Option (D):** Finger abduction is performed by the **dorsal interossei** (mnemonic: DAB—Dorsal interossei ABduct). The palmar interossei adduct (PAD), so this statement is false.  

**Conclusion:** Only **(B)** is correct, as the opponens pollicis relies on spinal root T1 via the median nerve.

Final Answer: The final answer is (B). I hope it is correct.

Problem:
How many attempts should you make to cannulate a patient before passing the job on to a senior colleague, according to the medical knowledge of 2020?
What of the following is the right choice? Explain your answer.
(A) 4
(B) 3
(C) 2
(D) 1
Solution:
The correct answer is **(C) 2**, based on 2020 medical guidelines. Here's the rationale:

1. **Evidence-Based Guidelines**: Organizations like the UK's NHS and the Infusion Nurses Society (INS) recommend limiting peripheral intravenous (IV) cannulation attempts to **two** before seeking senior assistance. This minimizes patient trauma, preserves vein health, and reduces complications (e.g., hematoma, infection).

2. **Rationale for Two Attempts**: 
   - **Patient Comfort**: Repeated failed attempts cause unnecessary pain and anxiety.
   - **Vein Preservation**: Excessive punctures damage veins, complicating future access.
   - **Skill Recognition**: After two failed attempts, escalating to a colleague with more experience improves success rates and patient outcomes.

3. **Why Other Options Are Incorrect**:
   - **(A) 4**: Excessively high; increases complications and violates standard protocols.
   - **(B) 3**: Some older practices allowed three attempts, but modern guidelines prioritize patient safety with stricter limits.
   - **(D) 1**: Unrealistically low; a second attempt is reasonable if the practitioner adjusts technique (e.g., vein selection, needle angle).

In summary, **two attempts** balance clinical judgment with patient-centered care, aligning with 2020 best practices.

Final Answer: The final answer is (C). I hope it is correct.

Problem:
Glycolysis is the name given to the pathway involving the conversion of:
What of the following is the right choice? Explain your answer.
(A) glycogen to glucose-1-phosphate.
(B) glycogen or glucose to fructose.
(C) glycogen or glucose to pyruvate or lactate.
(D) glycogen or glucose to pyruvate or acetyl CoA.
Solution:
The correct answer is **(C) glycogen or glucose to pyruvate or lactate**. Here's the reasoning:

1. **Glycolysis Definition**: Glycolysis is the metabolic pathway that converts **glucose** into **pyruvate** (under aerobic conditions) or **lactate** (under anaerobic conditions). This process occurs in the cytoplasm and does not directly involve glycogen.

2. **Glycogenolysis vs. Glycolysis**: Glycogen breakdown (glycogenolysis) converts glycogen into **glucose-1-phosphate**, which is then converted to glucose-6-phosphate. This molecule can enter glycolysis. While glycogenolysis is a separate process, some sources may conflate it with glycolysis when describing the complete pathway from stored glycogen to pyruvate/lactate.

3. **Eliminating Incorrect Options**:
   - **(A)** Glycogen to glucose-1-phosphate is part of glycogenolysis, not glycolysis.
   - **(B)** Conversion to fructose is unrelated to glycolysis; fructose metabolism is a distinct pathway.
   - **(D)** Acetyl CoA is formed from pyruvate in the mitochondria (via pyruvate dehydrogenase), which occurs after glycolysis, not during it.

4. **Justifying (C)**: Although glycolysis strictly begins with glucose, the question includes glycogen as a starting point. This implies a broader context where glycogenolysis and glycolysis are combined. The end products (pyruvate or lactate) align with glycolysis, making **(C)** the most accurate choice. Acetyl CoA (in option D) is excluded because it is not a direct product of glycolysis.

**Conclusion**: Glycolysis primarily converts glucose to pyruvate/lactate. While glycogenolysis precedes glycolysis when starting from glycogen, option **(C)** appropriately captures the combined pathway in contexts where glycogen is the initial substrate.

Final Answer: The final answer is (C). I hope it is correct."""

class MMLUClinicalKnowledge(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
