from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
Which of the following is not a way to form recombinant DNA?
What of the following is the right choice? Explain your answer.
(A) Translation
(B) Conjugation
(C) Specialized transduction
(D) Transformation
Solution:
The correct answer is **(A) Translation**. 

**Explanation:**  
Recombinant DNA is formed by combining genetic material from different sources. The processes involved in this include:  
- **Conjugation (B):** Direct transfer of DNA (e.g., plasmids) between bacteria via a pilus.  
- **Specialized transduction (C):** Transfer of specific bacterial genes via bacteriophages.  
- **Transformation (D):** Uptake of environmental DNA by a bacterium.  

**Translation (A)**, however, is the process of synthesizing proteins from mRNA, not DNA recombination. It occurs after transcription and does not involve altering or combining DNA molecules. Thus, it is unrelated to the formation of recombinant DNA.

Final Answer: The final answer is (A). I hope it is correct.

Problem:
A mutation in a bacterial enzyme changed a previously polar amino acid into a nonpolar amino acid. This amino acid was located at a site distant from the enzyme’s active site. How might this mutation alter the enzyme’s substrate specificity?
What of the following is the right choice? Explain your answer.
(A) By changing the enzyme’s pH optimum
(B) By changing the enzyme’s location in the cell
(C) By changing the shape of the protein
(D) An amino acid change away from the active site cannot alter the enzyme’s substrate specificity.
Solution:
The correct answer is **(C) By changing the shape of the protein**. 

### Explanation:
Enzymes rely on their precise three-dimensional structure to function. A mutation converting a polar amino acid to a nonpolar one, even if distant from the active site, can disrupt local hydrophobic/hydrophilic interactions critical for proper folding. This alteration may propagate through the protein’s structure (via secondary or tertiary interactions), leading to a conformational change. Such a structural shift could indirectly modify the active site’s geometry, thereby altering substrate binding affinity or specificity. 

**Rejecting other options:**  
- **(A)** pH optimum is tied to ionizable groups in the active site or other critical regions, not necessarily a distant nonpolar mutation.  
- **(B)** Protein localization typically depends on signal sequences or post-translational modifications, which are unrelated to this mutation.  
- **(D)** While substrate specificity is primarily determined by the active site, distant mutations can still influence it via structural changes (e.g., allostery or misfolding).  

Thus, the mutation likely alters substrate specificity by perturbing the enzyme’s overall shape, affecting the active site indirectly.

Final Answer: The final answer is (C). I hope it is correct.

Problem:
In animal cells, which of the following represents the most likely pathway that a secretory protein takes as it is synthesized in a cell?
What of the following is the right choice? Explain your answer.
(A) Plasma membrane–Golgi apparatus–ribosome–secretory vesicle–rough ER
(B) Ribosome–Golgi apparatus–rough ER–secretory vesicle–plasma membrane
(C) Plasma membrane–Golgi apparatus–ribosome–secretory vesicle–rough ER
(D) Ribosome–rough ER–Golgi apparatus–secretory vesicle–plasma membrane
Solution:
The correct answer is **(D) Ribosome–rough ER–Golgi apparatus–secretory vesicle–plasma membrane**. Here's the breakdown:

1. **Ribosome**: Secretory proteins are synthesized by ribosomes attached to the **rough ER**. The ribosome begins translating mRNA into a polypeptide chain, which is directly threaded into the ER lumen.

2. **Rough ER**: The protein undergoes initial modifications (e.g., folding, glycosylation) in the ER. It is then packaged into transport vesicles that bud off from the ER membrane.

3. **Golgi Apparatus**: These vesicles fuse with the Golgi apparatus, where further processing (e.g., additional glycosylation, sorting) occurs. The Golgi packages the mature protein into **secretory vesicles**.

4. **Secretory Vesicle**: These vesicles transport the protein toward the plasma membrane.

5. **Plasma Membrane**: The secretory vesicles fuse with the plasma membrane via exocytosis, releasing the protein outside the cell.

**Why other options are incorrect**:
- **(A) & (C)**: Start with the plasma membrane, which is illogical since synthesis begins at ribosomes.
- **(B)**: Places the Golgi before the rough ER, reversing the actual order of the pathway. Proteins must first enter the ER before reaching the Golgi. 

Thus, **(D)** accurately reflects the secretory pathway in animal cells.

Final Answer: The final answer is (D). I hope it is correct.

Problem:
Which of the following is not known to be involved in the control of cell division?
What of the following is the right choice? Explain your answer.
(A) Cyclins
(B) Protein kinases
(C) Checkpoints
(D) Fibroblast cells
Solution:
The correct answer is **(D) Fibroblast cells**.  

**Explanation:**  
- **(A) Cyclins** are proteins that regulate the cell cycle by activating cyclin-dependent kinases (CDKs), which drive progression through cell cycle phases. They are directly involved in control mechanisms.  
- **(B) Protein kinases**, particularly CDKs, phosphorylate target proteins to advance the cell cycle. This enzymatic activity is central to cell division regulation.  
- **(C) Checkpoints** are surveillance mechanisms (e.g., G1, S, M checkpoints) that ensure genomic integrity before proceeding to subsequent phases. They are critical for controlling cell division.  
- **(D) Fibroblast cells** are connective tissue cells involved in producing extracellular matrix and collagen. While fibroblasts themselves divide (e.g., during wound healing), they are not part of the **intrinsic regulatory machinery** (cyclins, kinases, checkpoints) that controls cell division. Their role is functional (e.g., tissue repair) rather than regulatory.  

Thus, fibroblasts are not known to directly control cell division, making **(D)** the correct answer.

Final Answer: The final answer is (D). I hope it is correct.

Problem:
Homologous structures are often cited as evidence for the process of natural selection. All of the following are examples of homologous structures EXCEPT
What of the following is the right choice? Explain your answer.
(A) the wings of a bird and the wings of a bat
(B) the flippers of a whale and the arms of a man
(C) the pectoral fins of a porpoise and the flippers of a seal
(D) the forelegs of an insect and the forelimbs of a dog
Solution:
The correct answer is **(D) the forelegs of an insect and the forelimbs of a dog**. Here's the explanation:

**Homologous structures** are those that share a common evolutionary origin, even if they now serve different functions. The key criterion is ancestry, not function. Let’s analyze each option:

- **(A) Bird wings and bat wings**: These are **homologous** because both evolved from the forelimbs of a common tetrapod ancestor. Despite serving the same function (flight), their structural similarity (e.g., humerus, radius, ulna) reflects shared ancestry. They are also **analogous** (same function, different origin) in the context of flight, but homology focuses on structural ancestry.

- **(B) Whale flippers and human arms**: These are **homologous** as both are derived from the same mammalian forelimb structure, even though their functions (swimming vs. grasping) differ.

- **(C) Porpoise pectoral fins and seal flippers**: These are **homologous** because they originate from the same ancestral tetrapod limb, adapted for aquatic life in both species.

- **(D) Insect forelegs and dog forelimbs**: These are **not homologous**. Insects (arthropods) and dogs (mammals) diverged evolutionarily over 500 million years ago. Insect legs are exoskeletal and lack the bone structure of vertebrate limbs, indicating independent evolutionary origins. Their limbs do not derive from a common ancestor’s structure.

**Conclusion**: The exception is **(D)** because homologous structures require a shared evolutionary origin, which is absent between insect and vertebrate limbs.

Final Answer: The final answer is (D). I hope it is correct."""

class MMLUHighSchoolBiology(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
