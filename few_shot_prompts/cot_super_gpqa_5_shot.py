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
To find the number of legal ways to tetrahedralize a regular triangular prism, I examine the structure with 6 vertices (labeled A,B,C on the bottom face and D,E,F on the top, with D above A, E above B, F above C), 9 edges, and 5 faces. A key insight is that this prism can be divided into 3 tetrahedra without adding new vertices. The critical approach involves cutting the prism with diagonal faces connecting edges between the top and bottom triangular faces. By systematically identifying all possible diagonal arrangements, I find exactly 6 distinct tetrahedralizations: (1) using diagonal ACE yields tetrahedra ABCE, ACDE, ACEF; (2) using ADF yields ABDF, ABCF, ADEF; (3) using BDF yields ABDF, BDEF, BCDF; (4) using CEF yields ACEF, BCEF, CDEF; (5) using BEC yields ABEC, BCDE, BCEF; (6) using AED yields ABED, AEFD, ACDE. Therefore, the answer is 6 different ways.
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
To solve this problem, I examine the equation of motion for multi-support excitation with spatial variation, starting with the standard form **Mü + Cú + Ku = F** where **F** represents effective forces from ground acceleration, typically expressed as **-[M r + M₉] ü₉**. Analyzing the left-hand side (LHS), I identify that only Option (I) correctly represents mass × acceleration (**Mü**), damping × velocity (**Cú**), and stiffness × displacement (**Ku**), while all other options contain inconsistencies like **Cü** instead of **Cú**. For the right-hand side (RHS), Option (H) properly captures multi-support excitation with **-[M r + M₉] ü₉**, but its LHS incorrectly uses **Cü**. Weighing these factors and assuming a typographical error in Option (H)'s damping term, I select Option (H) as the most reasonable answer for multi-support excitation despite its technical flaw: **(H) $\mathrm{M \ddot{u}+C \ddot{u}+K {u}=-[ M r+M_{g} ] \ddot{u}_{g}}$**.
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
In credit transactions where buying/selling is separated from payment, money transitions from its role as a medium of exchange (A) to functioning as a means of payment (F). This distinction arises because the exchange and payment occur at different times, with money becoming an independent step that finalizes the transaction rather than facilitating the immediate exchange. When payment is deferred, money specifically serves to settle debts or obligations created during the initial exchange—precisely the definition of a means of payment. The other options fail to capture this function: measure of value (B) only quantifies prices without addressing the temporal aspect; medium of deferred payment (C) is less precise than the standard economic term; store of wealth (D) relates to value retention over time rather than debt settlement; and medium of deferred exchange (E) is not a standard economic concept. The key insight is that the separation of exchange and payment highlights money's fundamental role as a means of payment (F), which directly describes its function in resolving obligations created by deferred transactions.
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
To design a reduced-order observer for this system with poles at -10, I begin by analyzing the system matrices A = [[-5, 0], [1, 0]], b = [[100], [0]], and c^T = [0, 1], where y = x₂ directly measures the second state. Since only x₁ needs estimation, I partition the system equations: ẋ₁ = -5x₁ + 100u and ẋ₂ = x₁. For a reduced-order observer, I construct the form ẋ̂₁ = A₁₁x̂₁ + A₁₂y + b₁u + L(ẏ - A₂₁x̂₁ - A₂₂y - b₂u), which simplifies to ẋ̂₁ = -5x̂₁ + 100u + L(ẏ - x̂₁) given our system parameters. To place the observer pole at -10, I set -5 - L = -10, yielding L = 5. Substituting this gain into the observer equation produces ẋ̂₁ = -5x̂₁ + 100u + 5(ẏ - x̂₁) = -10x̂₁ + 100u + 5ẏ, which matches option (E).
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
To solve this problem, we examine each I/O method against our key constraints: the CPU must process the data without waiting, and peripherals don't need constant readiness. Polling methods (H, E) are eliminated immediately as they force the CPU to repeatedly check peripheral status, directly violating our "no waiting" requirement. DMA methods (G, J) bypass the CPU for direct peripheral-memory transfers, contradicting our need for CPU processing. This leaves interrupt-based methods (A, C, D, F, I), which allow peripherals to signal the CPU only when ready, enabling the CPU to perform other tasks until needed and removing the requirement for constant peripheral readiness. Among these options, the "Interrupt Method" (C) represents the standard terminology for this approach, while other terms like "Interrupt Transfer" or "Interrupt Request" merely describe components of the broader interrupt-driven I/O process rather than the complete method itself. Therefore, the Interrupt Method (C) best satisfies all our criteria.
Final Answer: The final answer is (C). I hope it is correct."""

class SuperGPQAPrompt(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
