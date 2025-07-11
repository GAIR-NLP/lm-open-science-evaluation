from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
Which of the following is considered an acid anhydride?
What of the following is the right choice? Explain your answer.
(A) HCl
(B) H2SO3
(C) SO2
(D) Al(NO3)3
Solution:
The correct answer is:  

**(C) SO₂**  

### Explanation:  

An **acid anhydride** is a nonmetal oxide that reacts with water to form an acid. In other words, it is the **dehydrated form of an acid**.  

Now, let's analyze each option:  

- **(A) HCl (Hydrogen chloride)**  
  - HCl is a strong acid in aqueous solution, but it is not an anhydride because it is already an acid and does not form another acid by reacting with water.  

- **(B) H₂SO₃ (Sulfurous acid)**  
  - H₂SO₃ is already an acid, not an anhydride. Instead, **SO₂** is the anhydride of H₂SO₃.  

- **(C) SO₂ (Sulfur dioxide)** 
  - SO₂ is an acid anhydride because it reacts with water to form **sulfurous acid (H₂SO₃)**:  
    \[
    SO₂ + H₂O \rightarrow H₂SO₃
    \]  

- **(D) Al(NO₃)₃ (Aluminum nitrate)**  
  - This is a salt, not an anhydride. It does not react with water to form an acid.  

### Conclusion:  
Since SO₂ reacts with water to form an acid (H₂SO₃), it is considered an **acid anhydride**. Thus, the correct choice is **(C) SO₂**.

Final Answer: The final answer is (C). I hope it is correct.

Problem:
Which of the following is expected to be a polar molecule?
What of the following is the right choice? Explain your answer.
(A) PCl4F
(B) BF3
(C) CO2
(D) Si(CH3)4
Solution:
To determine which molecule is expected to be **polar**, we need to evaluate its **molecular geometry** and **bond dipoles**. A molecule is polar if it has an uneven distribution of electron density, meaning it has a **net dipole moment**. 

Let's analyze each choice:

### (A) **PCl₄F**  
- **Structure**: Phosphorus (P) has **5 valence electrons**, and it forms **five bonds** (four with Cl and one with F). The molecule adopts a **trigonal bipyramidal** geometry.  
- **Dipole Moment**: The fluorine (F) atom is more **electronegative** than chlorine (Cl), creating an **uneven charge distribution**. Since F and Cl are in **different positions** in the geometry, their dipole moments do not cancel out completely.  
- **Conclusion**: **Polar molecule**  

---

### (B) **BF₃**  
- **Structure**: Boron (B) has **three valence electrons** and forms **three bonds** with fluorine, resulting in a **trigonal planar** geometry.  
- **Dipole Moment**: The dipoles of the **three B-F bonds** are **symmetrically arranged** at **120°** angles, canceling out each other.  
- **Conclusion**: **Nonpolar molecule**  

---

### (C) **CO₂**  
- **Structure**: Carbon (C) forms **double bonds** with two oxygen (O) atoms, resulting in a **linear** geometry (**O=C=O**).  
- **Dipole Moment**: Although **C=O bonds** are polar, they are arranged **symmetrically** in opposite directions, so the dipoles cancel out.  
- **Conclusion**: **Nonpolar molecule**  

---

### (D) **Si(CH₃)₄** (Tetramethylsilane)  
- **Structure**: Silicon (Si) forms **four bonds** with methyl (CH₃) groups, adopting a **tetrahedral** geometry.  
- **Dipole Moment**: The **C-Si bonds** are slightly polar, but because of the **tetrahedral symmetry**, the bond dipoles cancel out.  
- **Conclusion**: **Nonpolar molecule**  

---

### **Final Answer:**  
The correct choice is **(A) PCl₄F**, as it has an asymmetric geometry with a net dipole moment, making it a **polar molecule**.

Final Answer: The final answer is (A). I hope it is correct.

Problem:
From the solubility rules, which of the following is true?
What of the following is the right choice? Explain your answer.
(A) All chlorides, bromides, and iodides are soluble
(B) All sulfates are soluble
(C) All hydroxides are soluble
(D) All ammonium-containing compounds are soluble
Solution:
The correct answer is:  

**(D) All ammonium-containing compounds are soluble.**  

### Explanation:  

1. **(A) All chlorides, bromides, and iodides are soluble** → **False**  
   - While most **chlorides (Cl⁻), bromides (Br⁻), and iodides (I⁻) are soluble**, there are exceptions.  
   - **Exceptions:** Ag⁺, Pb²⁺, and Hg₂²⁺ salts are **insoluble** (e.g., AgCl, PbBr₂).  

2. **(B) All sulfates are soluble** → **False**  
   - Most **sulfates (SO₄²⁻) are soluble**, but there are exceptions.  
   - **Exceptions:** BaSO₄, PbSO₄, SrSO₄, and CaSO₄ (low solubility).  

3. **(C) All hydroxides are soluble** → **False**  
   - Most **hydroxides (OH⁻) are insoluble**, except those of Group 1 metals (LiOH, NaOH, KOH) and **slightly soluble** Ca(OH)₂, Sr(OH)₂, and Ba(OH)₂.  

4. **(D) All ammonium-containing compounds are soluble** → **True**  
   - **NH₄⁺ (Ammonium ion) forms soluble compounds with all anions**, making this statement correct.  

Thus, the correct choice is **(D).**

Final Answer: The final answer is (D). I hope it is correct.

Problem:
A new compound is synthesized and found to be a monoprotic acid with a molar mass of 248 g/mol. When 0.0050 mol of this acid are dissolved in 0.500 L of water, the pH is measured as 3.89. What is the pKa of this acid?
What of the following is the right choice? Explain your answer.
(A) 3.89
(B) 7.78
(C) 5.78
(D) 2.33
Solution:
To determine the pKa of the acid, we use the relationship between pH, Ka, and the dissociation of a monoprotic acid (HA):

### **Step 1: Define Variables and Relationships**
For a weak acid dissociating in water:

\[
HA \rightleftharpoons H^+ + A^-
\]

The acid dissociation constant \( K_a \) is given by:

\[
K_a = \frac{[H^+][A^-]}{[HA]}
\]

Since we are given the pH, we can find \([H^+]\):

\[
[H^+] = 10^{-\text{pH}} = 10^{-3.89} = 1.29 \times 10^{-4} \text{ M}
\]

### **Step 2: Set Up an ICE Table**
Let the initial concentration of the acid be:

\[
C = \frac{0.0050 \text{ mol}}{0.500 \text{ L}} = 0.0100 \text{ M}
\]

Let **x** represent the concentration of dissociated \( H^+ \) ions, which is equal to \( [A^-] \).

| Species  | Initial (M) | Change (M) | Equilibrium (M) |
|----------|------------|------------|----------------|
| HA       | 0.0100     | -x         | 0.0100 - x     |
| H⁺       | 0          | +x         | x              |
| A⁻       | 0          | +x         | x              |

From the pH calculation, we already found:

\[
x = [H^+] = 1.29 \times 10^{-4} \text{ M}
\]

Thus, the concentration of undissociated acid is:

\[
[HA] = 0.0100 - 1.29 \times 10^{-4} \approx 0.00987 \text{ M}
\]

### **Step 3: Calculate \( K_a \)**
\[
K_a = \frac{(1.29 \times 10^{-4})^2}{0.00987}
\]

\[
K_a = \frac{1.66 \times 10^{-8}}{0.00987} = 1.68 \times 10^{-6}
\]

### **Step 4: Find pKa**
\[
pK_a = -\log K_a = -\log (1.68 \times 10^{-6})
\]

\[
pK_a \approx 5.78
\]

### **Step 5: Choose the Correct Answer**
The correct choice is:

\[
\mathbf{(C) \ 5.78}
\]

Final Answer: The final answer is (C). I hope it is correct.

Problem:
A solution contains 2.00 mole of acetic acid, CH3COOH, and 1.00 mole of calcium acetate, Ca(CH3COO)2. The solution is able to resist the addition of a small amount of strong acid or strong base with only minor changes in the pH of the solution. Larger quantities of strong acid or strong base can cause a significant change in pH. How many moles of nitric acid, HNO3, may be added before the pH begins to change significantly?
What of the following is the right choice? Explain your answer.
(A) 0.500 mole
(B) 1.00 mole
(C) 2.00 mole
(D) 3.00 mole
Solution:
This solution is a **buffer solution** because it contains a **weak acid** (acetic acid, CH₃COOH) and its **conjugate base** (acetate ion, CH₃COO⁻), supplied by calcium acetate, Ca(CH₃COO)₂.

### **Buffer Capacity Against Strong Acid (HNO₃)**
A buffer solution resists pH changes by neutralizing added strong acids or bases until one of the buffer components is depleted.

1. **Reaction with Strong Acid (HNO₃)**  
   - When HNO₃ is added, it donates protons (H⁺), which react with the **acetate ions (CH₃COO⁻)** to form **acetic acid (CH₃COOH)**:
     \[
     \text{CH₃COO⁻} + \text{H⁺} \rightarrow \text{CH₃COOH}
     \]
   - The buffer can neutralize **up to the total amount of acetate ions (CH₃COO⁻) present** before the pH starts to change significantly.

2. **Initial Moles of CH₃COO⁻ (Conjugate Base)**
   - The calcium acetate (Ca(CH₃COO)₂) provides **2 acetate ions per formula unit**:
     \[
     1.00 \text{ mole of Ca(CH₃COO)₂} \times 2 = 2.00 \text{ moles of CH₃COO⁻}
     \]

3. **Maximum Moles of HNO₃ Before pH Changes Significantly**
   - Since each HNO₃ molecule donates **one H⁺**, it can react **one-to-one** with CH₃COO⁻.
   - The buffer can neutralize up to **2.00 moles** of HNO₃ before all acetate ions are converted into acetic acid.
   - After this point, any additional HNO₃ will cause a rapid pH drop since there will be no more CH₃COO⁻ to neutralize it.

### **Correct Answer: (C) 2.00 moles**

Final Answer: The final answer is (C). I hope it is correct."""

class MMLUHighSchoolChemistry(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
