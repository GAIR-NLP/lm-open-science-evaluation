from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
Which of the following regular expressions is equivalent to (describes the same set of strings as) (a* + b)*(c + d)?
What of the following is the right choice? Explain your answer.
(A) a*(c + d)+ b(c + d)
(B) a*(c + d)* + b(c + d)*
(C) a*(c + d)+ b*(c + d)
(D) (a + b)*c +(a + b)*d
Solution:
The original regular expression is (a* + b)*(c + d). Breaking this down:

1. **(a* + b)***: This represents any number of repetitions where each element is either a sequence of a's (including none) or a single b. This is equivalent to **(a + b)*** because:
   - Each a* can generate any number of a's (including zero), and alternating with b allows any combination of a's and b's.
   - Thus, **(a* + b)*** simplifies to **(a + b)***.

2. **(c + d)**: This matches either a single c or d.

Combining these, the original expression simplifies to **(a + b)*(c + d)**, which matches any string of a's and b's followed by a single c or d.

**Analysis of Options**:
- **(A) a*(c + d) + b(c + d)**: Only allows sequences of a's (with no b's) or a single b followed by c/d. Fails to handle mixed a's and b's (e.g., "abba").
- **(B) a*(c + d)* + b(c + d)***: Permits multiple c/d's (including none), which the original does not allow.
- **(C) a*(c + d) + b*(c + d)**: Restricts to either all a's or all b's before c/d, disallowing mixed sequences like "ab".
- **(D) (a + b)*c + (a + b)*d**: Equivalent to **(a + b)*(c + d)**, correctly matching any mix of a's and b's followed by exactly one c or d.

Final Answer: The final answer is (D). I hope it is correct.

Problem:
The Singleton design pattern is used to guarantee that only a single instance of a class may be instantiated. Which of the following is (are) true of this design pattern? I. The Singleton class has a static factory method to provide its instance. II. The Singleton class can be a subclass of another class. III. The Singleton class has a private constructor.
What of the following is the right choice? Explain your answer.
(A) I only
(B) II only
(C) III only
(D) I, II, and III
Solution:
The Singleton design pattern ensures a class has only one instance and provides global access to it. Let's analyze each statement:

**I. The Singleton class has a static factory method to provide its instance.**  
True. A static method (e.g., `getInstance()`) is used to control access to the Singleton instance, ensuring only one instance exists.

**II. The Singleton class can be a subclass of another class.**  
True. The Singleton class can extend another class if the superclass has an accessible constructor (e.g., public or protected). The Singleton's private constructor can call `super()` to invoke the superclass constructor, provided it is accessible.

**III. The Singleton class has a private constructor.**  
True. A private constructor prevents external instantiation, enforcing the single-instance constraint.

**Conclusion:** All three statements (I, II, III) are correct.  

Final Answer: The final answer is (D). I hope it is correct.

Problem:
A compiler generates code for the following assignment statement. G := (A + B) * C - (D + E) * F The target machine has a single accumulator and a single-address instruction set consisting of instructions load, store, add, subtract, and multiply. For the arithmetic operations, the left operand is taken from the accumulator and the result appears in the accumulator. The smallest possible number of instructions in the resulting code is
What of the following is the right choice? Explain your answer.
(A) 5
(B) 6
(C) 7
(D) 9
Solution:
To determine the smallest possible number of instructions for computing the assignment statement:

\[
G := (A + B) * C - (D + E) * F
\]

on a target machine with a single accumulator and a single-address instruction set, we analyze step by step.

### Given Instructions:
- **LOAD X** → Load value of X into the accumulator.
- **STORE X** → Store value of the accumulator into memory location X.
- **ADD X** → Add value of X to the accumulator.
- **SUB X** → Subtract value of X from the accumulator.
- **MUL X** → Multiply accumulator by X.

### Breakdown of Computation:

1. Compute **(A + B) * C**:
   - `LOAD A` → Accumulator = A
   - `ADD B` → Accumulator = A + B
   - `MUL C` → Accumulator = (A + B) * C  
   - `STORE T1` → Store intermediate result in memory (T1)

2. Compute **(D + E) * F**:
   - `LOAD D` → Accumulator = D
   - `ADD E` → Accumulator = D + E
   - `MUL F` → Accumulator = (D + E) * F  
   - `STORE T2` → Store intermediate result in memory (T2)

3. Compute final result **(A + B) * C - (D + E) * F**:
   - `LOAD T1` → Load (A + B) * C into the accumulator
   - `SUB T2` → Subtract (D + E) * F
   - `STORE G` → Store result in G

### Total Number of Instructions:
- **First term computation**: 4 instructions (LOAD, ADD, MUL, STORE)
- **Second term computation**: 4 instructions (LOAD, ADD, MUL, STORE)
- **Final computation**: 3 instructions (LOAD, SUB, STORE)

\[
4 + 4 + 3 = 9
\]

### Answer:
The smallest possible number of instructions is **9**, so the correct choice is:

**(D) 9**

Final Answer: The final answer is (D). I hope it is correct.

Problem:
Consider a computer design in which multiple processors, each with a private cache memory, share global memory using a single bus. This bus is the critical system resource. Each processor can execute one instruction every 500 nanoseconds as long as memory references are satisfied by its local cache. When a cache miss occurs, the processor is delayed for an additional 2,000 nanoseconds. During half of this additional delay, the bus is dedicated to serving the cache miss. During the other half, the processor cannot continue, but the bus is free to service requests from other processors. On average, each instruction requires 2 memory references. On average, cache misses occur on 1 percent of references. What proportion of the capacity of the bus would a single processor consume, ignoring delays due to competition from other processors?
What of the following is the right choice? Explain your answer.
(A) 1/50
(B) 1/27
(C) 1/25
(D) 2/27
Solution:
To determine the proportion of the bus capacity consumed by a single processor, we need to consider the following steps:

1. **Instruction Execution Time Without Cache Misses**: Each instruction takes 500 nanoseconds (ns) if all memory references are satisfied by the local cache.

2. **Cache Miss Rate**: Each instruction requires 2 memory references, and the cache miss rate is 1% per reference. Therefore, the expected number of cache misses per instruction is \(2 \times 0.01 = 0.02\).

3. **Delay Due to Cache Misses**: Each cache miss causes an additional 2000 ns delay. However, the bus is only dedicated to serving the cache miss for half of this time (1000 ns). The other half does not consume the bus.

4. **Total Bus Usage Per Instruction**: Each cache miss uses the bus for 1000 ns. With 0.02 cache misses per instruction, the total bus usage per instruction is \(0.02 \times 1000 \, \text{ns} = 20 \, \text{ns}\).

5. **Total Instruction Time Including Delays**: The average delay per instruction due to cache misses is \(0.02 \times 2000 \, \text{ns} = 40 \, \text{ns}\). Therefore, the total time per instruction is \(500 \, \text{ns} + 40 \, \text{ns} = 540 \, \text{ns}\).

6. **Proportion of Bus Capacity Consumed**: The proportion of the bus capacity consumed is the ratio of bus usage time to the total instruction time:
   \[
   \frac{20 \, \text{ns}}{540 \, \text{ns}} = \frac{20}{540} = \frac{1}{27}
   \]

Thus, the proportion of the capacity of the bus that a single processor would consume is \(\boxed{B}\).

Final Answer: The final answer is (B). I hope it is correct."""

class MMLUCollegeComputerScience(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
