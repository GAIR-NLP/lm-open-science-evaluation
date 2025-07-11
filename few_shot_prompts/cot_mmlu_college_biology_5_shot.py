from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
Which of the following represents an accurate statement concerning arthropods?
What of the following is the right choice? Explain your answer.
(A) They possess an exoskeleton composed primarily of peptidoglycan.
(B) They possess an open circulatory system with a dorsal heart.
(C) They are members of a biologically unsuccessful phylum incapable of exploiting diverse habitats and nutrition sources.
(D) They lack paired, jointed appendages.
Solution:
The correct answer is **(B) They possess an open circulatory system with a dorsal heart.**

**Explanation:**  
- **(A)** Arthropods have an exoskeleton composed of **chitin**, not peptidoglycan (which is found in bacterial cell walls). This makes (A) incorrect.  
- **(B)** Arthropods do indeed have an **open circulatory system**, where hemolymph (blood-like fluid) circulates through body cavities. Their heart is located dorsally (along the upper side), making this statement accurate.  
- **(C)** Arthropods are the **most biologically successful phylum**, occupying nearly every habitat and exploiting diverse food sources. This directly contradicts (C), rendering it false.  
- **(D)** A defining feature of arthropods is their **paired, jointed appendages** (e.g., legs, antennae). The term "arthropod" itself means "jointed foot," so (D) is incorrect.  

Thus, **(B)** is the only accurate statement.

Final Answer: The final answer is (B). I hope it is correct.

Problem:
In a given population, 1 out of every 400 people has a cancer caused by a completely recessive allele, b. Assuming the population is in Hardy-Weinberg equilibrium, which of the following is the expected proportion of individuals who carry the b allele but are not expected to develop the cancer?
What of the following is the right choice? Explain your answer.
(A) 1/400
(B) 19/400
(C) 20/400
(D) 38/400
Solution:
The population is in Hardy-Weinberg equilibrium, and the frequency of individuals with the recessive genotype \( bb \) (who develop cancer) is given as \( \frac{1}{400} \). This corresponds to \( q^2 = \frac{1}{400} \), where \( q \) is the frequency of the recessive allele \( b \). Solving for \( q \):

\[
q = \sqrt{\frac{1}{400}} = \frac{1}{20}.
\]

The frequency of the dominant allele \( B \) is \( p = 1 - q = 1 - \frac{1}{20} = \frac{19}{20} \).

The proportion of heterozygous carriers (\( Bb \)) is calculated using \( 2pq \):

\[
2pq = 2 \times \frac{19}{20} \times \frac{1}{20} = \frac{38}{400}.
\]

Carriers (\( Bb \)) have the \( b \) allele but do not develop cancer. Thus, the expected proportion of carriers is \( \frac{38}{400} \).

**Answer:** (D) 38/400

Final Answer: The final answer is (D). I hope it is correct.

Problem:
The presence of homologous structures in two different organisms, such as the humerus in the front limb of a human and a bird, indicates that
What of the following is the right choice? Explain your answer.
(A) the human and bird are polyphyletic species
(B) a human's and bird's evolution is convergent
(C) the human and bird belong to a clade
(D) the human and bird developed by analogy
Solution:
The correct answer is **(C) the human and bird belong to a clade**.

**Explanation:**  
Homologous structures, like the humerus in humans and birds, are inherited from a common ancestor. These structures may serve different functions (e.g., human arms vs. bird wings), but their shared anatomical blueprint indicates evolutionary relatedness. A **clade** is a group of organisms that includes a common ancestor and all its descendants. Since homologous structures reflect shared ancestry, humans and birds must belong to the same clade. 

- **(A)** is incorrect because polyphyletic groups exclude the common ancestor of all members, which contradicts the idea of shared ancestry implied by homologous structures.  
- **(B)** refers to convergent evolution, which produces analogous structures (e.g., bat wings vs. insect wings), not homologous ones.  
- **(D)** is incorrect because "analogy" describes structures with similar functions but independent evolutionary origins, not homology.  

Thus, homologous structures directly support the conclusion that organisms share a clade.

Final Answer: The final answer is (C). I hope it is correct.

Problem:
According to the pressure-flow model of movement of phloem contents, photosynthate movement from source to sink is driven by
What of the following is the right choice? Explain your answer.
(A) an ATP-dependent pressure-flow pump
(B) a water-pressure potential gradient
(C) transpiration
(D) apoplastic diffusion
Solution:
The correct answer is **(B) a water-pressure potential gradient**. 

According to the pressure-flow model, the movement of photosynthates in the phloem is driven by a hydrostatic pressure gradient between the source (e.g., leaves) and sink (e.g., roots or fruits). Here's the explanation:

1. **Source to Sink Dynamics**: At the source, sugars are actively loaded into phloem sieve tubes, lowering the water potential inside. This causes water to enter the phloem from the xylem via osmosis, increasing turgor pressure. At the sink, sugars are unloaded, raising the water potential, which allows water to exit the phloem, reducing pressure. 

2. **Pressure Gradient Drives Flow**: The resulting pressure difference (high at the source, low at the sink) creates a bulk flow of phloem sap from areas of high pressure to low pressure. This gradient is fundamentally a water-pressure potential gradient, not directly ATP-dependent.

3. **Eliminating Other Options**:
   - **(A) ATP-dependent pump**: While ATP is used for active sugar loading/unloading, the flow itself is passive, driven by pressure, not ATP.
   - **(C) Transpiration**: This drives xylem water movement, not phloem transport.
   - **(D) Apoplastic diffusion**: Phloem transport involves bulk flow through sieve tubes, not diffusion through cell walls.

Thus, the pressure-flow model hinges on osmotic water movement creating a pressure gradient, making **(B)** the correct choice.

Final Answer: The final answer is (B). I hope it is correct.

Problem:
Which of the following contain DNA sequences required for the segregation of chromosomes in mitosis and meiosis?
What of the following is the right choice? Explain your answer.
(A) Telomeres
(B) Centromeres
(C) Nucleosomes
(D) Spliceosomes
Solution:
The correct answer is **(B) Centromeres**. 

**Explanation:**  
Centromeres are specialized DNA sequences on chromosomes where sister chromatids are held together. During mitosis and meiosis, spindle fibers attach to the kinetochore protein complex at the centromere, enabling the segregation of chromosomes to opposite poles of the cell. This process is critical for ensuring each daughter cell receives the correct number of chromosomes. 

- **(A) Telomeres** protect chromosome ends and prevent DNA degradation but are not involved in segregation.  
- **(C) Nucleosomes** organize DNA into chromatin but do not contain sequences required for segregation.  
- **(D) Spliceosomes** process RNA and are unrelated to chromosome mechanics.  

Thus, centromeres are the DNA sequences essential for proper chromosome segregation during cell division.

Final Answer: The final answer is (B). I hope it is correct."""

class MMLUCollegeBiology(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
