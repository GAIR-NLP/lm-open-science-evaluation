from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
Large triplet repeat expansions can be detected by:
What of the following is the right choice? Explain your answer.
(A) polymerase chain reaction.
(B) single strand conformational polymorphism analysis.
(C) Southern blotting.
(D) Western blotting.
Solution:
The correct answer is **(C) Southern blotting**.

**Explanation:**  
Large triplet repeat expansions, such as those seen in disorders like Huntington's disease or Fragile X syndrome, often exceed the size limits of standard PCR amplification. **Polymerase chain reaction (PCR) (A)** struggles with very large DNA fragments due to inefficiencies in amplifying lengthy sequences. **Single-strand conformational polymorphism (SSCP) analysis (B)** is designed to detect small sequence variations (e.g., point mutations) by observing changes in DNA conformation, but it is not sensitive to large repeat expansions. **Western blotting (D)** analyzes proteins and is irrelevant to detecting DNA abnormalities. 

**Southern blotting (C)** is the gold standard for detecting large triplet repeats. It involves digesting genomic DNA with restriction enzymes, separating fragments by gel electrophoresis, transferring them to a membrane, and hybridizing with a probe specific to the repeat region. This method can resolve large DNA fragments without requiring amplification, making it ideal for identifying expanded repeats that PCR cannot handle. 

**Answer:** (C) Southern blotting.

Final Answer: The final answer is (C). I hope it is correct.

Problem:
DNA ligase is
What of the following is the right choice? Explain your answer.
(A) an enzyme that joins fragments in normal DNA replication
(B) an enzyme of bacterial origin which cuts DNA at defined base sequences
(C) an enzyme that facilitates transcription of specific genes
(D) an enzyme which limits the level to which a particular nutrient reaches
Solution:
The correct answer is **(A) an enzyme that joins fragments in normal DNA replication**.

**Explanation:**  
DNA ligase plays a critical role in DNA replication by catalyzing the formation of phosphodiester bonds between adjacent nucleotides. During replication, the lagging strand is synthesized discontinuously as Okazaki fragments, which must be joined to form a continuous strand. DNA ligase seals the "nicks" between these fragments, ensuring the integrity of the DNA molecule. 

- **Option B** incorrectly describes restriction enzymes, which cut DNA at specific sequences.  
- **Option C** refers to transcription-related proteins like RNA polymerase or transcription factors, not DNA ligase.  
- **Option D** is unrelated to DNA ligase's function, as it does not regulate nutrient levels.  

Thus, **(A)** is the only accurate description of DNA ligase's role in normal DNA replication.

Final Answer: The final answer is (A). I hope it is correct.

Problem:
A gene showing codominance
What of the following is the right choice? Explain your answer.
(A) has both alleles independently expressed in the heterozygote
(B) has one allele dominant to the other
(C) has alleles tightly linked on the same chromosome
(D) has alleles expressed at the same time in development
Solution:
The correct answer is **(A) has both alleles independently expressed in the heterozygote**.  

**Explanation:**  
Codominance occurs when both alleles in a heterozygote are fully and distinctly expressed, resulting in a phenotype that displays both traits simultaneously. For example, in the ABO blood group system, individuals with the AB genotype express both A and B antigens on their red blood cells. This contrasts with **incomplete dominance** (where traits blend) and **complete dominance** (where one allele masks the other).  

**Analysis of Options:**  
- **(A)** Correct: Codominance is defined by the independent expression of both alleles in the heterozygote, leading to distinct phenotypic traits.  
- **(B)** Incorrect: This describes complete dominance, not codominance.  
- **(C)** Incorrect: Tight linkage refers to genes being physically close on a chromosome, which is unrelated to codominance.  
- **(D)** Incorrect: While codominant alleles are expressed simultaneously, this is a consequence of their independent expression (as in A), not the defining feature of codominance itself.  

Thus, the key distinction for codominance is the independent expression of both alleles in the heterozygote, making **(A)** the correct choice.

Final Answer: The final answer is (A). I hope it is correct.

Problem:
Which of the following conditions does not show multifactorial inheritance?
What of the following is the right choice? Explain your answer.
(A) Pyloric stenosis
(B) Schizophrenia
(C) Spina bifida (neural tube defects)
(D) Marfan syndrome
Solution:
The correct answer is **(D) Marfan syndrome**. Here's the explanation:

- **Multifactorial inheritance** involves both genetic and environmental factors, with multiple genes contributing to the condition. 
- **Marfan syndrome (D)** is caused by a mutation in the *FBN1* gene, inherited in an **autosomal dominant** pattern. It is a **monogenic disorder** (single-gene), not multifactorial.
- **Pyloric stenosis (A)**, **Schizophrenia (B)**, and **Spina bifida (C)** are all multifactorial. They involve interactions between multiple genetic loci and environmental influences (e.g., diet, prenatal exposures, lifestyle).

Thus, Marfan syndrome stands out as the only single-gene disorder among the options, making **(D)** the correct choice.

Final Answer: The final answer is (D). I hope it is correct.

Problem:
The stage of meiosis in which chromosomes pair and cross over is:
What of the following is the right choice? Explain your answer.
(A) prophase I
(B) metaphase I
(C) prophase II
(D) metaphase II
Solution:
The correct answer is **(A) prophase I**. Here's why:

1. **Prophase I**:  
   - **Pairing (Synapsis)**: Homologous chromosomes pair up, forming structures called tetrads. This pairing ensures genetic recombination.  
   - **Crossing Over**: Non-sister chromatids of homologous chromosomes exchange genetic material at chiasmata. This is a defining event of prophase I and increases genetic diversity.  

2. **Other Stages**:  
   - **Metaphase I (B)**: Homologous pairs align at the metaphase plate, but pairing and crossing over have already occurred in prophase I.  
   - **Prophase II (C)** and **Metaphase II (D)**: These stages occur in meiosis II, which involves haploid cells. No homologous chromosomes are present to pair or cross over.  

Thus, **prophase I** is the only stage where both pairing and crossing over occur.

Final Answer: The final answer is (A). I hope it is correct."""

class MMLUMedicalGenetics(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
