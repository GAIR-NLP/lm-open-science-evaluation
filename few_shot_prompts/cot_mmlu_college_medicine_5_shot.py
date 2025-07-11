from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
Glucose is transported into the muscle cell:
What of the following is the right choice? Explain your answer.
(A) via protein transporters called GLUT4.
(B) only in the presence of insulin.
(C) via hexokinase.
(D) via monocarbylic acid transporters.
Solution:
The correct answer is **(A) via protein transporters called GLUT4**.

**Explanation:**  
Glucose is a polar molecule and requires specific transporters to enter cells. In muscle cells, **GLUT4** is the primary glucose transporter. These transporters are insulin-sensitive, meaning insulin promotes their translocation to the cell membrane to facilitate glucose uptake. However, insulin is **not the sole mechanism** for GLUT4 activation. During exercise, muscle contraction triggers GLUT4 translocation independently of insulin. This makes option **(B)** ("only in the presence of insulin") incorrect, as glucose can enter muscle cells even without insulin under certain conditions.

**Why other options are incorrect:**  
- **(C) Hexokinase** is an enzyme that phosphorylates glucose inside the cell (trapping it there), but it does not mediate transport across the membrane.  
- **(D) Monocarboxylic acid transporters** transport molecules like lactate or pyruvate, not glucose.  

Thus, while insulin enhances GLUT4 activity, the fundamental mechanism of glucose transport into muscle cells is via **GLUT4 transporters**, making **(A)** the correct choice.

Final Answer: The final answer is (A). I hope it is correct.

Problem:
Which of the following is not a true statement?
What of the following is the right choice? Explain your answer.
(A) Muscle glycogen is broken down enzymatically to glucose-1-phosphate
(B) Elite endurance runners have a high proportion of Type I fibres in their leg muscles
(C) Liver glycogen is important in the maintenance of the blood glucose concentration
(D) Insulin promotes glucose uptake by all tissues in the body
Solution:
The correct answer is **(D) Insulin promotes glucose uptake by all tissues in the body**.

**Explanation:**  
- **(A)** Muscle glycogen is indeed enzymatically broken down to glucose-1-phosphate via glycogen phosphorylase. This process fuels muscle energy needs, as muscles lack glucose-6-phosphatase to release free glucose into the bloodstream. **True.**  
- **(B)** Elite endurance runners rely heavily on Type I (slow-twitch) muscle fibers, which are fatigue-resistant and optimized for sustained aerobic activity. **True.**  
- **(C)** Liver glycogen is critical for maintaining blood glucose levels, especially during fasting. The liver releases glucose via glycogenolysis and gluconeogenesis, unlike muscle glycogen. **True.**  
- **(D)** Insulin primarily promotes glucose uptake in **muscle, adipose tissue, and the liver** (via indirect mechanisms). However, **not all tissues** require insulin for glucose uptake. For example, the brain, red blood cells, and kidneys use insulin-independent glucose transporters (e.g., GLUT1). **False.**  

Thus, **(D)** is the incorrect statement because it inaccurately generalizes insulin's role to "all tissues."

Final Answer: The final answer is (D). I hope it is correct.

Problem:
In a genetic test of a newborn, a rare genetic disorder is found that has X-linked recessive transmission. Which of the following statements is likely true regarding the pedigree of this disorder?
What of the following is the right choice? Explain your answer.
(A) All descendants on the maternal side will have the disorder.
(B) Females will be approximately twice as affected as males in this family.
(C) All daughters of an affected male will be affected.
(D) There will be equal distribution of males and females affected.
Solution:
The question concerns the pedigree of an X-linked recessive disorder found in a newborn. Here's the analysis of each option:

### **(A) All descendants on the maternal side will have the disorder.**
- **Incorrect.** X-linked recessive disorders are passed through the maternal line, but not all descendants are affected. Sons of a carrier mother have a 50% chance of inheriting the affected X and being affected, while daughters have a 50% chance of being carriers. Thus, **not all descendants** on the maternal side will have the disorder.

### **(B) Females will be approximately twice as affected as males in this family.**
- **Incorrect.** X-linked recessive disorders predominantly affect males because they have only one X chromosome. Females require two copies of the defective gene (one from each parent) to manifest the disorder, which is rare. Males are far more likely to be affected than females.

### **(C) All daughters of an affected male will be affected.**
- **Partially Correct but Misleading.** An affected male passes his X chromosome (with the defective gene) to all his daughters. However, for a daughter to **be affected**, she must inherit another affected X from her mother. If the mother is not a carrier, daughters are **carriers**, not affected. If the mother is a carrier, daughters have a 50% chance of being affected. Since the newborn has the disorder, the mother must be a carrier (if the newborn is male) or the father is affected and the mother is a carrier (if the newborn is female). **Even in this family, not all daughters of an affected male are guaranteed to be affected**, as it depends on the mother’s X. The statement "all daughters will be affected" is **not universally true** and depends on the mother’s genotype, which is not guaranteed in the question.

### **(D) There will be equal distribution of males and females affected.**
- **Incorrect.** Males are disproportionately affected by X-linked recessive disorders due to their single X chromosome. Females require two defective copies, making them far less likely to be affected.

### **Conclusion:**
The most plausible answer is **(C)**. While it is not strictly true in all cases, the question’s context (a newborn with the disorder) implies the mother is a carrier. In this specific family, daughters of an affected male would inherit his X and have a 50% chance of being affected (if the mother is a carrier). However, the phrasing "all daughters" in (C) is misleading, as it suggests certainty rather than probability. Despite this, **(C)** aligns most closely with the inheritance pattern of X-linked recessive disorders compared to the other options.

Final Answer: The final answer is (C). I hope it is correct.

Problem:
A high school science teacher fills a 1 liter bottle with pure nitrogen and seals the lid. The pressure is 1.70 atm, and the room temperature is 25°C. Which two variables will both increase the pressure of the system, if all other variables are held constant?
What of the following is the right choice? Explain your answer.
(A) Increasing temperature, increasing moles of gas
(B) Increasing temperature, increasing volume
(C) Decreasing volume, decreasing temperature
(D) Decreasing moles of gas, increasing volume
Solution:
The correct answer is **(A) Increasing temperature, increasing moles of gas**. 

**Explanation:**  
Using the ideal gas law, \( PV = nRT \), pressure (\( P \)) is directly proportional to the number of moles of gas (\( n \)) and temperature (\( T \)), and inversely proportional to volume (\( V \)). Since the bottle is sealed, volume is constant. However, the question asks hypothetically which variables, **if increased**, would raise pressure while other variables are held constant.  

- **Increasing temperature (\( T \))**: Raises \( P \) because \( P \propto T \).  
- **Increasing moles of gas (\( n \))**: Raises \( P \) because \( P \propto n \).  

Other options fail because:  
- **(B)** Increasing volume (\( V \)) would *decrease* \( P \), conflicting with the temperature increase.  
- **(C)** Decreasing temperature (\( T \)) would *lower* \( P \), conflicting with the volume decrease.  
- **(D)** Both decreasing \( n \) and increasing \( V \) would *reduce* \( P \).  

Thus, **(A)** is the only pair where both actions increase pressure.

Final Answer: The final answer is (A). I hope it is correct.

Problem:
An expected side effect of creatine supplementation is:
What of the following is the right choice? Explain your answer.
(A) muscle weakness.
(B) gain in body mass.
(C) muscle cramps.
(D) loss of electrolytes.
Solution:
The correct answer is **(B) gain in body mass**. 

**Explanation:**  
Creatine supplementation is widely recognized for increasing intramuscular water retention, leading to a rapid gain in body mass (typically 1-3 kg within the first week). This occurs because creatine draws water into muscle cells, enhancing hydration and energy production. While muscle cramps (C) and electrolyte imbalances (D) are sometimes cited, they are not consistently supported by evidence and often relate to inadequate hydration rather than creatine itself. Muscle weakness (A) is unlikely, as creatine typically improves strength and power output. Thus, the most expected and well-documented side effect is **body mass gain**. 

**Answer:** (B) gain in body mass.

Final Answer: The final answer is (B). I hope it is correct."""

class MMLUCollegeMedicine(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
