from .few_shot_prompting import FewShotPrompting

few_shot_prompt = """Problem:
If we tetrahedralize a regular triangular prism, how many ways of tetrahedralization are legal? (Each vertex is different)
What of the following is the right choice? Explain your answer.
(A) 5
(B) 8
(C) 12
(D) 10
(E) 11
(F) 4
(G) 6
(H) 7
(I) 9
(J) 3
Solution:
A regular triangular prism has 6 vertices (3 on each of the two triangular bases). When tetrahedralizing—dividing the volume entirely into tetrahedra whose vertices are among those 6—you must choose sets of 4 vertices such that the tetrahedra fill the prism without overlapping.

It turns out (after considering all the combinatorial possibilities and the geometric constraints imposed by the faces of the prism) that there are exactly 6 distinct ways to “tetrahedralize” a triangular prism (up to symmetry). In each legal tetrahedralization, the tetrahedra share faces in a way that completely fills the prism, and no tetrahedron uses any vertex more than once.

Thus, among the given options, (G) 6 is the correct answer.

Final Answer: The final answer is (G). I hope it is correct.

Problem:
What is the equation of motion for multi support excitation and spatial variation?
What of the following is the right choice? Explain your answer.
(A) $\\mathrm{M \\ddot{u}+K \\ddot{u}+C {u}=-[ M_{g} r+M ] \\ddot{u}_{g}}$
(B) $\\mathrm{M \\ddot{u}+K \\dot{u}+C {u}=-[ M_{g} r+M ] \\ddot{u}_{g}}$
(C) $\\mathrm{M \\ddot{u}+C \\ddot{u}+K \\dot{u}=[ M r+M_{g} ] \\ddot{u}_{\\mathrm{g}}}$
(D) $\\mathrm{K \\ddot{u}+C \\ddot{u}+M {u}=-[ M r+M_{g} ] u_{\\mathrm{g}}}$
(E) $\\mathrm{M \\dot{u}+C \\ddot{u}+K {u}=-[ M r+M_{g} ] \\ddot{u}_{\\mathrm{g}}}$
(F) $\\mathrm{M \\ddot{u}+C \\ddot{u}+K {u}=[ M r+M_{g} ] \\ddot{U}_{g}}$
(G) $\\mathrm{C \\ddot{u}+M \\ddot{u}+K {u}=[ r M+M_{g} ] \\ddot{u}_{g}}$
(H) $\\mathrm{M \\ddot{u}+C \\ddot{u}+K {u}=-[ M r+M_{g} ] \\ddot{u}_{g}}$
(I) $\\mathsf{M} \\ddot{\\mathsf{u}}+\\mathsf{C} \\dot{\\mathsf{u}}+\\mathsf{K} \\mathsf{u}=\\mathsf{f}$
(J) $\\mathrm{M u+C \\ddot{u}+K {u}=-[ M_{g} r+M ] \\ddot{u}_{g}}$
Solution:
The equation of motion for multi-support excitation and spatial variation must account for the dynamic response of the structure subjected to spatially varying ground motions. The standard form of the equation of motion is **Mü + Cú + Ku = F**, where **F** represents the effective forces due to ground acceleration. For multi-support excitation, **F** is typically expressed as **- [M r + M₉] ü₉**, where **M** is the mass matrix, **r** is an influence matrix, **M₉** accounts for support mass contributions, and **ü₉** is the ground acceleration vector. 

### Analysis of Options:
1. **Left-Hand Side (LHS):**  
   The correct terms should be **Mü** (mass × acceleration), **Cú** (damping × velocity), and **Ku** (stiffness × displacement).  
   - Only **Option (I)** has the correct LHS: **Mü + Cú + Ku**.  
   - All other options (A–H, J) have inconsistent terms (e.g., **Cü** instead of **Cú**, or incorrect ordering).

2. **Right-Hand Side (RHS):**  
   For multi-support excitation, the RHS should explicitly include terms related to ground acceleration.  
   - **Option (H)** has the RHS **-[M r + M₉] ü₉**, which matches the expected form for multi-support excitation.  
   - However, **Option (H)** incorrectly uses **Cü** (damping × acceleration) instead of **Cú** (damping × velocity) on the LHS.

### Conclusion:
While **Option (I)** is the only one with a correct LHS, it uses a generic **f** for the RHS, which does not explicitly address multi-support excitation. **Option (H)** has the correct RHS form but an invalid LHS due to the **Cü** term. Assuming a typographical error in the damping term (intending **Cú** instead of **Cü**), **Option (H)** is the most reasonable choice for multi-support excitation.

**Answer:**  
**(H) $\mathrm{M \ddot{u}+C \ddot{u}+K {u}=-[ M r+M_{g} ] \ddot{u}_{g}}$**

Final Answer: The final answer is (H). I hope it is correct.

Problem:
When the act of buying and selling goods is separated from the act of paying for them, money is no longer a medium of exchange in the circulation of goods, but becomes an independent link to complete the exchange. At this point, money functions as ().
What of the following is the right choice? Explain your answer.
(A) medium of circulation
(B) measure of value
(C) medium of deferred payment
(D) store of wealth
(E) medium of deferred exchange
(F) means of payment
Solution:
The correct answer is **(F) means of payment**. Here's the breakdown:

1. **Context**: When buying/selling goods is separated from paying (e.g., credit transactions), money no longer acts as a **medium of exchange** (ruling out A) because the exchange of goods and payment occur at different times. Instead, money becomes an independent step to finalize the transaction.

2. **Key Function**: In deferred payment scenarios, money serves to settle debts or obligations created by the initial exchange. This aligns with the **means of payment** function. When payment is deferred, money is not used immediately as a medium of exchange but rather to discharge the debt later, making it distinct from direct transactions.

3. **Eliminating Other Options**:
   - **(B) Measure of value**: Money quantifies prices but does not address the deferred payment aspect.
   - **(C) Medium of deferred payment**: While related, this term is less precise. The "standard of deferred payment" (not listed) refers to money being the unit for future obligations, but the actual settlement uses money as a **means of payment** (F).
   - **(D) Store of wealth**: This involves retaining value over time, unrelated to completing deferred exchanges.
   - **(E) Medium of deferred exchange**: Not a standard economic term.
   - **(F) Means of payment**: Directly describes money’s role in settling debts after a deferred transaction, fitting the question’s emphasis on completing the exchange independently.

**Conclusion**: The separation of exchange and payment highlights money’s role as a **means of payment** (F), resolving obligations created by deferred transactions.

Final Answer: The final answer is (F). I hope it is correct.

Problem:
Given the coefficient matrix of the controlled system (sum(A, b, c^T)) as ( A=left[ begin{matrix} -5 & 0 1 & 0 end{matrix} right] , b=left[ begin{matrix} 100 0 end{matrix} right], c^T=left[ begin{matrix} 0 &1 end{matrix} right] ), design a reduced-order observer so that the poles of the observer are -10. Which of the following observers meets the requirement?
What of the following is the right choice? Explain your answer.
(A) (dot{hat{x}_1}=-10hat{x}_1+100u+10dot{y})
(B) (dot{hat{x}_1}=-10hat{x}_1+100u+2dot{y})
(C) (dot{hat{x}_1}=-10hat{x}_1+100u-4dot{y})
(D) (dot{hat{x}_1}=-10hat{x}_1+100u-10dot{y})
(E) (dot{hat{x}_1}=-10hat{x}_1+100u+5dot{y})
(F) (dot{hat{x}_1}=-10hat{x}_1+100u+3dot{y})
(G) (dot{hat{x}_1}=-10hat{x}_1+100u-5dot{y})
(H) (dot{hat{x}_1}=-10hat{x}_1+100u+6dot{y})
(I) (dot{hat{x}_1}=-10hat{x}_1+100u+4dot{y})
(J) (dot{hat{x}_1}=-10hat{x}_1+100u-2dot{y})
Solution:
To design a reduced-order observer for the given system with the coefficient matrices \( A \), \( b \), and \( c^T \), we need to ensure the observer pole is at -10. The system is given by:

\[
A = \begin{bmatrix} -5 & 0 \\ 1 & 0 \end{bmatrix}, \quad b = \begin{bmatrix} 100 \\ 0 \end{bmatrix}, \quad c^T = \begin{bmatrix} 0 & 1 \end{bmatrix}
\]

The output \( y \) is \( x_2 \), so we need to estimate \( x_1 \). The goal is to find the observer gain \( L \) such that the error dynamics have a pole at -10. The error dynamics are governed by the matrix \( A_{11} - L A_{21} \), where \( A_{11} = -5 \), \( A_{21} = 1 \), \( A_{12} = 0 \), \( A_{22} = 0 \), \( b_1 = 100 \), and \( b_2 = 0 \).

To place the pole at -10, we solve:
\[
A_{11} - L A_{21} = -10 \implies -5 - L = -10 \implies L = 5
\]

The observer equation is:
\[
\dot{\hat{x}}_1 = (A_{11} - L A_{21}) \hat{x}_1 + (A_{12} - L A_{22}) y + (b_1 - L b_2) u + L \dot{y}
\]

Substituting the values:
\[
\dot{\hat{x}}_1 = -10 \hat{x}_1 + 100u + 5 \dot{y}
\]

Thus, the correct answer is:
\[
\boxed{E}
\]

Final Answer: The final answer is (E). I hope it is correct.

Problem:
Which of the following input/output methods is processed through the CPU and avoids the disadvantages of 'peripheral devices always needing to be ready' and 'the CPU having to wait during processing?'
What of the following is the right choice? Explain your answer.
(A) Interrupt Transfer
(B) Unconditional Transfer
(C) Interrupt Method
(D) Interrupt Request Transfer
(E) Polling Transfer
(F) Interrupt Transfer Method
(G) DMA Method
(H) Polling Method
(I) Interrupt Request Method
(J) Direct Memory Access Method
Solution:
The correct answer is **(C) Interrupt Method**. Here's the explanation:

1. **Eliminating Polling Methods (H, E)**: Polling requires the CPU to repeatedly check if a peripheral is ready, forcing it to wait. This directly contradicts the requirement to "avoid the CPU waiting."

2. **DMA Methods (G, J)**: DMA bypasses the CPU entirely, allowing direct data transfers between peripherals and memory. However, the question specifies the method must be "processed through the CPU," ruling out DMA.

3. **Interrupt-Based Methods (A, C, D, F, I)**: 
   - Interrupts allow peripherals to signal the CPU when they are ready, freeing the CPU to perform other tasks instead of waiting. 
   - The CPU processes the transfer only when notified (via an interrupt), avoiding the need for the peripheral to "always be ready" and eliminating CPU waiting.
   - Among the options, **(C) Interrupt Method** is the standard term for this approach. Terms like "Interrupt Transfer" or "Interrupt Request" are components of the broader interrupt-driven I/O process but are less precise in describing the method itself.

**Conclusion**: The **Interrupt Method** (C) best satisfies the criteria of involving the CPU while avoiding waiting and peripheral readiness issues.

Final Answer: The final answer is (C). I hope it is correct."""

class SuperGPQAPromptLong(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]