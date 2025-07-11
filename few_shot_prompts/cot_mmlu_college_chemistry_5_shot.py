from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
Which of the following statements about the lanthanide elements is NOT true?
What of the following is the right choice? Explain your answer.
(A) The most common oxidation state for the lanthanide elements is +3.
(B) Lanthanide complexes often have high coordination numbers (> 6).
(C) All of the lanthanide elements react with aqueous acid to liberate hydrogen.
(D) The atomic radii of the lanthanide elements increase across the period from La to Lu.
Solution:
The correct answer is:  

**(D) The atomic radii of the lanthanide elements increase across the period from La to Lu.**  

### Explanation:
- **(A) The most common oxidation state for the lanthanide elements is +3. (TRUE)**  
  The lanthanides typically exhibit a +3 oxidation state due to the loss of three electrons (two from the 6s orbital and one from the 4f or 5d orbitals). Though some lanthanides can show +2 and +4 oxidation states, +3 is the most stable and prevalent.

- **(B) Lanthanide complexes often have high coordination numbers (> 6). (TRUE)**  
  Lanthanide ions are large and can accommodate multiple ligands, often forming complexes with coordination numbers ranging from 7 to 9 (sometimes even higher).

- **(C) All of the lanthanide elements react with aqueous acid to liberate hydrogen. (TRUE)**  
  Lanthanides are reactive metals that readily react with acids such as hydrochloric acid (HCl) to produce hydrogen gas and soluble lanthanide salts.

- **(D) The atomic radii of the lanthanide elements increase across the period from La to Lu. (FALSE)**  
  The atomic radii actually **decrease** across the period from La to Lu due to the **lanthanide contraction**. This occurs because as the nuclear charge increases, the added electrons go into the inner 4f orbitals, which do not shield the increasing nuclear charge effectively. This results in a gradual decrease in atomic and ionic radii across the series.

Thus, **(D) is the incorrect statement and the correct answer choice.**

Final Answer: The final answer is (D). I hope it is correct.

Problem:
A 0.217 g sample of HgO (molar mass = 217 g) reacts with excess iodide ions according to the reaction shown above. Titration of the resulting solution requires how many mL of 0.10 M HCl to reach equivalence point?
What of the following is the right choice? Explain your answer.
(A) 1.0 mL
(B) 10 mL
(C) 20 mL
(D) 50 mL
Solution:
To determine the volume of 0.10 M HCl required to titrate the resulting solution from the reaction of 0.217 g HgO with excess iodide ions, we start by calculating the moles of HgO. The molar mass of HgO is 217 g/mol, so:

\[
\text{Moles of HgO} = \frac{0.217 \text{ g}}{217 \text{ g/mol}} = 0.001 \text{ mol} = 1 \text{ mmol}
\]

The reaction of HgO with excess iodide ions is assumed to produce hydroxide ions (OH⁻). A typical reaction is:

\[
\text{HgO} + 2\text{I}^- + \text{H}_2\text{O} \rightarrow \text{HgI}_2^{2-} + 2\text{OH}^-
\]

From this reaction, 1 mole of HgO produces 2 moles of OH⁻. Therefore, 1 mmol of HgO produces 2 mmol of OH⁻. To neutralize 2 mmol of OH⁻ with 0.10 M HCl (which provides H⁺ ions), the required volume of HCl is:

\[
\text{Volume of HCl} = \frac{\text{Moles of H}^+}{\text{Concentration of HCl}} = \frac{2 \text{ mmol}}{0.10 \text{ M}} = \frac{2 \text{ mmol}}{0.10 \text{ mol/L}} = 20 \text{ mL}
\]

Thus, the volume of 0.10 M HCl required to reach the equivalence point is:

\[
\boxed{C}
\]

Final Answer: The final answer is (C). I hope it is correct.

Problem:
Predict the number of lines in the EPR spectrum of a solution of 13C-labelled methyl radical (13CH3•), assuming the lines do not overlap.
What of the following is the right choice? Explain your answer.
(A) 4
(B) 3
(C) 6
(D) 24
Solution:
The EPR spectrum of a 13C-labeled methyl radical (13CH3•) arises from hyperfine interactions between the unpaired electron and nuclei with non-zero spin. Here's the analysis:

1. **Protons (1H):**  
   The three equivalent protons (I = 1/2) split the EPR signal. For \( n \) equivalent nuclei with spin \( I \), the number of lines is \( 2nI + 1 \). Substituting \( n = 3 \) and \( I = 1/2 \):  
   \[
   2 \times 3 \times \frac{1}{2} + 1 = 4 \, \text{lines}.
   \]  
   This results in a 1:3:3:1 quartet due to equivalent proton coupling.

2. **13C Nucleus:**  
   While 13C has \( I = 1/2 \), the unpaired electron in the planar methyl radical resides in a p-orbital, which has a node at the carbon nucleus. This minimizes the Fermi contact interaction, rendering the hyperfine coupling to 13C negligible. Thus, no additional splitting from 13C is observed.

3. **Conclusion:**  
   The EPR spectrum is dominated by the splitting from the three equivalent protons, yielding **4 distinct lines** (quartet). The 13C coupling does not contribute significantly under typical conditions.  

**Answer:** (A) 4.

Final Answer: The final answer is (A). I hope it is correct.

Problem:
3 Cl−(aq) + 4 CrO_4^2−(aq) + 23 H+(aq) → 3 HClO2(aq) + 4 Cr3+(aq) + 10 H2O(l). In the reaction shown above, Cl−(aq) behaves as
What of the following is the right choice? Explain your answer.
(A) an acid
(B) a base
(C) a catalyst
(D) a reducing agent
Solution:
The correct answer is:

**(D) a reducing agent.**

### Explanation:

In this reaction, **Cl⁻ (chloride ion) is oxidized to HClO₂ (chlorous acid)**. Oxidation is the **loss of electrons**, meaning Cl⁻ donates electrons in this reaction. Specifically:

- **Oxidation state of Cl in Cl⁻**: -1
- **Oxidation state of Cl in HClO₂**: +3

Since the oxidation state of chlorine increases from -1 to +3, Cl⁻ is losing electrons, which means it is undergoing **oxidation**. 

A **reducing agent** is a substance that **loses electrons and gets oxidized**, thereby reducing another species. Here, **Cl⁻ is reducing CrO₄²⁻ (chromate), which gets reduced to Cr³⁺**.

Thus, Cl⁻ acts as a **reducing agent** in this reaction.

Final Answer: The final answer is (D). I hope it is correct.

Problem:
Which of the following lists the hydrides of group-14 elements in order of thermal stability, from lowest to highest?
What of the following is the right choice? Explain your answer.
(A) PbH4 < SnH4 < GeH4 < SiH4 < CH4
(B) PbH4 < SnH4 < CH4 < GeH4 < SiH4
(C) CH4 < SiH4 < GeH4 < SnH4 < PbH4
(D) CH4 < PbH4 < GeH4 < SnH4 < SiH4
Solution:
The correct answer is:  

**(A) PbH₄ < SnH₄ < GeH₄ < SiH₄ < CH₄**  

### Explanation:  
The thermal stability of hydrides of Group-14 elements (carbon family) **decreases down the group** due to the following factors:

1. **Bond Strength:**  
   - As we move down the group (C → Si → Ge → Sn → Pb), the atomic size increases, leading to weaker **M–H** (metal-hydrogen) bonds.
   - Weaker bonds require less energy to break, reducing thermal stability.

2. **Electronegativity:**  
   - Carbon is the most electronegative in Group-14, forming the most stable bond with hydrogen.
   - Lead is the least electronegative, leading to the weakest **Pb–H** bond, making **PbH₄** the least stable.

3. **Covalent Character:**  
   - The lighter elements (C, Si) form stronger covalent bonds, while heavier elements (Ge, Sn, Pb) show increasing metallic character, weakening the bond with hydrogen.

### Correct Order of Stability:  
- **Methane (CH₄)** is the most stable because **C–H** bonds are the strongest.  
- **Silane (SiH₄)** is less stable than CH₄ but more stable than GeH₄.  
- **Germane (GeH₄)** follows, with a further decrease in stability.  
- **Stannane (SnH₄)** is even less stable.  
- **Plumbane (PbH₄)** is the least stable due to the weakest Pb–H bonds.  

Thus, the correct order from **lowest to highest stability** is:  
**PbH₄ < SnH₄ < GeH₄ < SiH₄ < CH₄**  
which matches option **(A)**.

Final Answer: The final answer is (A). I hope it is correct."""

class MMLUCollegeChemistry(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
