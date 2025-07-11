from .few_shot_prompting import FewShotPrompting

few_shot_prompt = """Problem:
What is the number of peaks in the 1H NMR spectrum of a molecule with SMILES [START_SMILES]OCC1=CNC(=O)C1=O[END_SMILES]?

Solution:
The given SMILES string corresponds to the molecular structure of **4-hydroxy-2-pyridone** (OCC1=CNC(=O)C1=O).

To determine the number of peaks in its **¹H NMR spectrum**, we analyze the chemically distinct hydrogen environments:

1. **-OCH₂ (Methylene group, -OCH₂)**  
   - This **-OCH₂** group is attached to an oxygen, making the two protons likely equivalent.
   - Appears as a **singlet or multiplet** in the **3–5 ppm** region.

2. **Aromatic Ring Protons (Pyridone system)**  
   - The **pyridone ring** contains three proton-bearing carbon atoms.
   - The proton environments may differ based on electron-withdrawing effects of the adjacent carbonyl groups.
   - Likely results in **three separate peaks** in the **6–9 ppm** region.

### Conclusion:
- The total number of distinct proton environments in the **¹H NMR spectrum** is **4**.
- Expect **four peaks** in the spectrum.

Final Answer: The final answer is 4. I hope it is correct.

Problem:
What is the total electron count of \\ce{AgNO3}?

Solution:
To determine the total electron count of **silver nitrate (\(\ce{AgNO3}\))**, we need to sum the electrons from all the atoms in the molecule.

### Step 1: Identify Atomic Numbers
Each element's atomic number represents the number of electrons in its neutral state:

- **Silver (\(\ce{Ag}\))**: 47 electrons
- **Nitrogen (\(\ce{N}\))**: 7 electrons
- **Oxygen (\(\ce{O}\))**: 8 electrons per atom (3 oxygen atoms)

### Step 2: Sum of Electrons
Since \(\ce{AgNO3}\) is a neutral compound, the total electron count is simply the sum of all constituent atoms' electrons:

\[
47 + 7 + (3 \times 8)
\]

\[
= 47 + 7 + 24
\]

\[
= 78 \text{ electrons}
\]

Thus, the total electron count of \(\ce{AgNO3}\) is **78 electrons**.

Final Answer: The final answer is 78. I hope it is correct.

Problem:
What is the spin-only magnetic moment (in units of Bohr-magnetons) for the low-spin case of the metal complex \\ce{RhCl(CO)(PPh3)2}?

Solution:
To determine the spin-only magnetic moment (\(\mu_{\text{spin-only}}\)) for the low-spin case of the metal complex \(\ce{RhCl(CO)(PPh3)2}\), follow these steps:

1. **Determine the oxidation state of Rhodium (\(\ce{Rh}\)):**  
   - \(\ce{Cl}\) (chloride) has a charge of \(-1\).  
   - \(\ce{CO}\) (carbonyl) and \(\ce{PPh3}\) (triphenylphosphine) are neutral ligands.  
   - The overall charge of the complex is neutral.  
   - Thus, the oxidation state of \(\ce{Rh}\) is \(+1\).

2. **Determine the electron configuration of \(\ce{Rh+}\):**  
   - Neutral \(\ce{Rh}\) (Z = 45) has an electron configuration: \([\ce{Kr}] 4d^8 5s^1\).  
   - \(\ce{Rh+}\) loses one electron, leaving: \([\ce{Kr}] 4d^8\).

3. **Determine the crystal field environment and electron filling:**  
   - The complex is square planar, a common geometry for \(\ce{d^8}\) metal centers with strong field ligands (\(\ce{CO}\), \(\ce{PPh3}\), and \(\ce{Cl}\)).  
   - In a square planar crystal field splitting, the \(\ce{d}\) orbitals split as:  
     \[
     d_{x^2-y^2} > d_{xy} > d_{xz}, d_{yz} > d_{z^2}
     \]
   - Strong field ligands cause a large \(\Delta\), leading to a **low-spin configuration**, where all electrons pair up in the lower energy orbitals.

4. **Calculate the spin-only magnetic moment:**  
   - The number of unpaired electrons (\(n\)) in the low-spin square planar \(\ce{d^8}\) configuration is **zero**.
   - The spin-only magnetic moment formula is:
     \[
     \mu_{\text{spin-only}} = \sqrt{n(n+2)} \text{ Bohr magnetons}
     \]
   - Since \(n = 0\):
     \[
     \mu_{\text{spin-only}} = \sqrt{0(0+2)} = 0 \text{ Bohr magnetons}.
     \]

### Final Answer:
The spin-only magnetic moment for the low-spin case of \(\ce{RhCl(CO)(PPh3)2}\) is **0 Bohr magnetons**, indicating a diamagnetic complex.

Final Answer: The final answer is 0. I hope it is correct.

Problem:
Given that the average molar mass of the polymer chains in this sample of poly(lactic acid) (PLA) is \\pu{595 g mol^{-1}} using end-group analysis, where \\pu{0.1619 g} of PLA was dissolved in \\pu{25 cm^3} of benzyl alcohol and titrated with \\pu{0.0400 mol dm^{-3}} \\ce{KOH} solution. The volume of \\ce{KOH} solution required to reach the endpoint was \\pu{6.81 cm^3}. What is the average number of monomer units in each polymer chain of this sample?

Solution:
To determine the average number of monomer units in each polymer chain of poly(lactic acid) (PLA), we follow these steps:

### Step 1: Understanding the Given Data
- Average molar mass of PLA: \( M_n = \pu{595 g mol^{-1}} \)
- Mass of PLA dissolved: \( m = \pu{0.1619 g} \)
- Volume of benzyl alcohol: \( \pu{25 cm^3} \) (not directly needed)
- Concentration of \( \ce{KOH} \) solution: \( \pu{0.0400 mol dm^{-3}} \)
- Volume of \( \ce{KOH} \) solution used: \( V = \pu{6.81 cm^3} = \pu{6.81 × 10^{-3} dm^3} \)

### Step 2: Determine the Number of Moles of End Groups
Poly(lactic acid) (PLA) typically has carboxyl (-COOH) and hydroxyl (-OH) end groups. In end-group analysis, titration with \( \ce{KOH} \) neutralizes the carboxyl groups.

The moles of \( \ce{KOH} \) reacting:
\[
\text{moles of } \ce{KOH} = C \times V = (0.0400) \times (6.81 \times 10^{-3})
\]
\[
= 2.724 \times 10^{-4} \text{ mol}
\]

Since each PLA polymer chain has one carboxyl end group reacting with \( \ce{KOH} \), the number of polymer chains present is equal to the number of moles of \( \ce{KOH} \) used:

\[
n_{\text{chains}} = 2.724 \times 10^{-4} \text{ mol}
\]

### Step 3: Determine the Molar Mass of the Monomer
The repeating unit in PLA is lactic acid (\(\ce{C3H4O3}\)), with a molar mass of:

\[
M_{\text{monomer}} = \pu{72.06 g mol^{-1}}
\]

### Step 4: Calculate the Number of Monomer Units per Chain
The number of polymer chains in the sample:

\[
n_{\text{chains}} = \frac{\text{mass of PLA}}{\text{molar mass of PLA}}
\]

\[
= \frac{0.1619}{595}
\]

\[
= 2.72 \times 10^{-4} \text{ mol}
\]

Since each chain consists of \( N \) monomer units:

\[
N = \frac{M_n}{M_{\text{monomer}}} = \frac{595}{72.06}
\]

\[
\approx 8.26
\]

### Final Answer:
The average number of monomer units in each polymer chain is **8.26**, or approximately **8 monomers per chain**.

Final Answer: The final answer is 8. I hope it is correct.

Problem:
Assume all processes take place at \\pu{298 K}. The enthalpy change of formation of \\ce{CH4(g)} is \\pu{-74.8 kJ mol^{-1}} and of \\ce{H2O(l)} is \\pu{-285.8 kJ mol^{-1}}. What is the standard enthalpy change of combustion of \\ce{H2} in \\pu{kJ mol^{-1}}?

Solution:
The standard enthalpy change of combustion of hydrogen (\(\ce{H2}\)) refers to the enthalpy change when one mole of \(\ce{H2(g)}\) reacts completely with oxygen to form water (\(\ce{H2O(l)}\)) under standard conditions.

The balanced combustion reaction of hydrogen is:

\[
\ce{H2(g) + 1/2 O2(g) -> H2O(l)}
\]

Using the standard enthalpy of formation values:

- \(\Delta H_f^\circ (\ce{H2O(l)}) = \pu{-285.8 kJ mol^{-1}}\)
- \(\Delta H_f^\circ (\ce{H2(g)}) = \pu{0 kJ mol^{-1}}\) (by definition)
- \(\Delta H_f^\circ (\ce{O2(g)}) = \pu{0 kJ mol^{-1}}\) (by definition)

The enthalpy change of the reaction is calculated as:

\[
\Delta H^\circ = \sum \Delta H_f^\circ \text{(products)} - \sum \Delta H_f^\circ \text{(reactants)}
\]

\[
\Delta H^\circ = [\Delta H_f^\circ (\ce{H2O(l)})] - [\Delta H_f^\circ (\ce{H2(g)}) + \frac{1}{2} \Delta H_f^\circ (\ce{O2(g)})]
\]

\[
\Delta H^\circ = [\pu{-285.8 kJ mol^{-1}}] - [0 + 0]
\]

\[
\Delta H^\circ = \pu{-285.8 kJ mol^{-1}}
\]

Thus, the standard enthalpy change of combustion of \(\ce{H2}\) is **\(\pu{-285.8 kJ mol^{-1}}\)**.

Final Answer: The final answer is -285.8. I hope it is correct."""

class ChemBenchStrMatch(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\n\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
