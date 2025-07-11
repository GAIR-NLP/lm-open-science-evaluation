from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
Why is it essential to use a rotary evaporator with a collecting flask made of borosilicate glass instead of regular glass?
What of the following is the right choice? Explain your answer.
(A) Borosilicate glass is lighter than regular glass, making it easier to handle
(B) Borosilicate glass is more resistant to thermal shock, reducing the risk of breakage during the evaporation process
(C) Regular glass can react with certain solvents, contaminating the sample
(D) Regular glass is more expensive than borosilicate glass, increasing the cost of the experiment
Solution:
The correct answer is **(B) Borosilicate glass is more resistant to thermal shock, reducing the risk of breakage during the evaporation process**.

**Explanation:**  
Rotary evaporators subject the collecting flask to rapid temperature changes, such as heating from a water bath and cooling from condensation. **Borosilicate glass** contains boron oxide, which gives it a low coefficient of thermal expansion. This property allows it to withstand sudden temperature fluctuations without cracking, unlike regular soda-lime glass, which is prone to thermal stress and breakage under similar conditions. While chemical resistance (C) and cost (D) are secondary considerations, the primary advantage of borosilicate glass in this context is its **thermal shock resistance**, ensuring durability and safety during evaporation. Option (A) is incorrect, as borosilicate glass is not significantly lighter than regular glass.

Final Answer: The final answer is (B). I hope it is correct.

Problem:
One of the deviations from the plug flow systems is caused by whirlpools and other similar behaviors that can happen inside the reactor. Which of the following statements describes the correct steps to properly model a real reactor that behaves like this plug flow system?
What of the following is the right choice? Explain your answer.
(A) Include both axial and radial dispersion terms to the original plug flow system, and then solve the energy balance
(B) Include both axial and radial dispersion terms to the original plug flow system, and then solve the mass balance
(C) Only include the radial dispersion term since the axial term is already described by the plug flow system
(D) Solve the balances, and then add the radial dispersion term that is not included in the original plug flow system
Solution:
The correct answer is **(B) Include both axial and radial dispersion terms to the original plug flow system, and then solve the mass balance**.

### Explanation:
In an **ideal plug flow reactor (PFR)**, axial and radial dispersion are neglected. The model assumes no backmixing (axial dispersion) and perfect uniformity in the radial direction. However, real reactors often deviate due to phenomena like whirlpools, which introduce **both axial and radial dispersion**. 

- **Axial dispersion** accounts for deviations in the flow direction (e.g., backmixing or turbulence), while **radial dispersion** addresses cross-sectional mixing. These terms are **added to the mass balance equation** to model non-ideal behavior. 
- The original PFR already includes axial advection (flow velocity), but dispersion terms are distinct and must be explicitly incorporated. Radial dispersion is not part of the ideal PFR model either.
- Since the question focuses on flow-related deviations (not thermal effects), solving the **mass balance** (not energy balance) is the priority after adding these terms. 

**Why other options are incorrect:**
- **(A)** Energy balance is unnecessary unless temperature gradients are specified.
- **(C)** Axial dispersion is not inherently included in the PFR model; it must be added alongside radial dispersion.
- **(D)** Dispersion terms must be included in the governing equations *before* solving, not afterward.

Final Answer: The final answer is (B). I hope it is correct.

Problem:
Can alkali metals burn in nitrogen gas?
What of the following is the right choice? Explain your answer.
(A) Yes
(B) No
Solution:
The correct answer is **(A) Yes**. 

**Explanation:**  
Alkali metals, while generally known for their reactivity with oxygen and water, can also react with nitrogen under certain conditions. Specifically, **lithium** (the lightest alkali metal) reacts with nitrogen gas at room temperature to form lithium nitride (Li₃N):  
\[ 6\text{Li} + \text{N}_2 \rightarrow 2\text{Li}_3\text{N} \]  
This reaction is exothermic and qualifies as "burning" in nitrogen. Heavier alkali metals like sodium or potassium do not react readily with nitrogen under standard conditions due to their larger atomic size and weaker tendency to form stable nitrides. However, the question asks about alkali metals *in general*, and since at least one member of the group (lithium) can burn in nitrogen, the answer is **Yes**.  

**Note:** If the question had specified "all alkali metals," the answer would differ, but as phrased, the inclusion of lithium justifies **(A)**.

Final Answer: The final answer is (A). I hope it is correct.

Problem:
Imagine an early virtual screening campaign setting (accounting for simple aspects such as oral availability and small molecular profile, but no other modalities such as covalency or bifunctionality). Which of the following two candidates would you prefer for further development?
What of the following is the right choice? Explain your answer.
(A) [START_SMILES]CN(CCN(C)C(=O)n1cc(C#N)cn1)Cc1ccc(OCc2ccccc2)cc1[END_SMILES]
(B) [START_SMILES]Cc1ccc(C(=O)NCC2CC2)cc1-c1ccc(C(=O)NCC2CC2)cc1[END_SMILES]
Solution:
The right choice for further development in an early virtual screening campaign, considering oral availability and a small molecular profile, is **Candidate B**. Here's the breakdown:

### **Key Factors Favoring Candidate B**:
1. **Oral Availability (Rule of Five Compliance)**:
   - **Molecular Weight**: Both candidates are under 500 Da (A: ~300–350, B: ~382), but B’s slightly higher weight is still acceptable.
   - **H-Bond Donors/Acceptors**: 
     - B has **2 H-bond donors** (amide NH groups) and **2 H-bond acceptors** (amide O), aligning with Lipinski’s criteria (≤5 donors, ≤10 acceptors). 
     - A lacks H-bond donors (tertiary amines/amide, nitrile, ether), which may hinder solubility despite having ~4–5 acceptors (triazole N, carbonyl O, ether O). Poor solubility can limit oral absorption.

2. **Lipophilicity (LogP)**:
   - B’s amide groups enhance polarity, likely lowering LogP compared to A’s aromatic-rich structure (two benzene rings + triazole). A’s nitrile and triazole offer moderate polarity, but its three aromatic rings may increase LogP, risking poor solubility.

3. **Structural Complexity**:
   - **Rotatable Bonds**: B has **5 rotatable bonds** (amide and biphenyl bonds), while A has ~5–7 (branched amine, ether linker). Fewer rotatable bonds (B) correlate with better bioavailability.
   - **Aromatic Rings**: B has **2 benzene rings** vs. A’s **3 aromatic systems** (two benzene + triazole). Excessive aromaticity (A) raises LogP and metabolic instability risks.

4. **Metabolic Considerations**:
   - B’s **amide groups** and **cyclopropane** may enhance metabolic stability. Amides resist oxidation, and cyclopropane’s rigidity can block enzymatic degradation.
   - A’s **nitrile** (C#N) poses potential metabolic liabilities (e.g., cyanide release) and may require additional safety profiling.

### **Conclusion**:
Candidate B balances better solubility (via H-bond donors), lower aromatic burden, and structural rigidity, all critical for oral bioavailability. While A has a lower molecular weight, its lack of H-bond donors and higher aromaticity make it less favorable. B’s profile aligns more closely with early-stage prioritization for oral drug development. 

Final Answer: The final answer is (B). I hope it is correct.

Problem:
How many distinct signals are observed for the aldehyde \\ce{(CH3)3CCH2CHO} in 1H NMR and 13C NMR spectra?
What of the following is the right choice? Explain your answer.
(A) five 1H signals and four 13C signals
(B) five 1H signals and six 13C signals
(C) three 1H signals and four 13C signals
(D) three 1H signals and six 13C signals
Solution:
The molecule in question, (CH3)3CCH2CHO, has the following structure: a tertiary butyl group ((CH3)3C) attached to a CH2 group, which is connected to an aldehyde (CHO). To determine the number of distinct signals in its 1H and 13C NMR spectra:

### **1H NMR Analysis**
1. **Aldehyde Proton (CHO):**  
   The aldehyde proton is in a unique environment and appears as a triplet due to coupling with the adjacent CH2 protons. This accounts for **1 signal**.

2. **CH2 Protons:**  
   The two protons on the CH2 group adjacent to the aldehyde are equivalent due to free rotation around the C-C bond. They couple with the aldehyde proton, resulting in a doublet. This gives **1 signal**.

3. **Tertiary Butyl CH3 Protons:**  
   The three methyl groups attached to the central quaternary carbon are equivalent due to symmetry. All nine protons from these methyl groups resonate as **1 signal**.

**Total 1H Signals:** 3 (aldehyde triplet, CH2 doublet, CH3 singlet).

---

### **13C NMR Analysis**
1. **Aldehyde Carbon (CHO):**  
   The carbonyl carbon of the aldehyde is distinct and appears as **1 signal**.

2. **CH2 Carbon:**  
   The carbon in the CH2 group adjacent to the aldehyde is unique and gives **1 signal**.

3. **Quaternary Carbon (C):**  
   The central carbon bonded to three CH3 groups and the CH2 group is a quaternary carbon, contributing **1 signal**.

4. **Methyl Carbons (CH3):**  
   The three methyl carbons attached to the quaternary carbon are equivalent due to symmetry, producing **1 signal**.

**Total 13C Signals:** 4 (carbonyl, CH2, quaternary, CH3).

---

### **Correct Answer**
- **1H NMR:** 3 signals.  
- **13C NMR:** 4 signals.  

This corresponds to **Option (C): three 1H signals and four 13C signals**. 

**Key Reasoning:**  
- Symmetry in the tertiary butyl group ensures equivalence of its CH3 protons and carbons.  
- Free rotation around the C-C bond makes the CH2 protons equivalent.  
- Distinct environments for the aldehyde, CH2, quaternary carbon, and CH3 carbons account for the 13C signals.  

Final Answer: The final answer is (C). I hope it is correct."""

class ChemBenchMultiChoise(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
