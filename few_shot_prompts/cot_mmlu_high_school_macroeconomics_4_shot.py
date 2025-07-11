from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
The short-run Phillips curve indicates a
What of the following is the right choice? Explain your answer.
(A) direct relation between unemployment and inflation
(B) direct relation between price and quantity demanded
(C) inverse relation between price and quantity demanded
(D) inverse relation between unemployment and inflation
Solution:
The correct answer is:  

**(D) inverse relation between unemployment and inflation**  

### Explanation:  
The **short-run Phillips curve** represents an **inverse relationship** between **unemployment and inflation**. This means that when inflation is high, unemployment tends to be low, and when inflation is low, unemployment tends to be high.  

This relationship is based on the idea that higher inflation, often caused by increased demand, leads to more production and job creation, thus reducing unemployment. Conversely, lower inflation (or deflation) is associated with reduced economic activity and higher unemployment.  

### Why the other choices are incorrect:  
- **(A) Direct relation between unemployment and inflation** → Incorrect. The short-run Phillips curve shows an inverse (negative) relationship, not a direct (positive) one.  
- **(B) Direct relation between price and quantity demanded** → Incorrect. This describes the law of supply, not the Phillips curve.  
- **(C) Inverse relation between price and quantity demanded** → Incorrect. This describes the law of demand, not the Phillips curve.  

Thus, **(D) inverse relation between unemployment and inflation** is the correct answer.

Final Answer: The final answer is (D). I hope it is correct.

Problem:
A federal deficit occurs when
What of the following is the right choice? Explain your answer.
(A) exports exceed imports.
(B) imports exceed exports.
(C) federal tax collections exceed spending.
(D) federal spending exceeds federal tax revenues.
Solution:
The correct answer is:  

**(D) federal spending exceeds federal tax revenues.**  

### Explanation:  
A **federal deficit** occurs when the government **spends more money** than it collects in revenue. The primary source of government revenue is **federal tax collections**, including income taxes, corporate taxes, and other forms of taxation. When **federal spending (on programs like defense, social security, and healthcare) exceeds tax revenues**, the government runs a **deficit** and must borrow money to cover the shortfall.  

#### Why the other choices are incorrect:
- **(A) Exports exceed imports** – This describes a **trade surplus**, not a federal deficit.  
- **(B) Imports exceed exports** – This refers to a **trade deficit**, which is different from a federal budget deficit.  
- **(C) Federal tax collections exceed spending** – This would result in a **budget surplus**, not a deficit.  

So, the correct answer is **(D).**

Final Answer: The final answer is (D). I hope it is correct.

Problem:
Holding all else equal which of the following monetary policies would be used to boost U.S. exports?
What of the following is the right choice? Explain your answer.
(A) Increasing the discount rate
(B) Increasing the reserve ratio
(C) Buying government securities
(D) Lowering tariffs
Solution:
The correct answer is:  

**(C) Buying government securities**  

### Explanation:  
To boost U.S. exports, the Federal Reserve (the central bank of the U.S.) would need to implement an expansionary monetary policy to lower interest rates and weaken the U.S. dollar. A weaker dollar makes U.S. goods cheaper for foreign buyers, increasing exports.  

- **(C) Buying government securities** – This is an expansionary monetary policy known as **open market operations**. When the Fed buys government securities, it increases the money supply in the economy, lowers interest rates, and leads to a depreciation of the U.S. dollar. A weaker dollar makes U.S. exports more competitive internationally, boosting exports.  

### Why the other options are incorrect:  
- **(A) Increasing the discount rate** – This is a contractionary policy that makes borrowing more expensive, reduces the money supply, raises interest rates, strengthens the U.S. dollar, and makes exports more expensive. This would hurt, rather than help, exports.  
- **(B) Increasing the reserve ratio** – This is also a contractionary policy. A higher reserve ratio means banks must hold more reserves and lend less, reducing the money supply, increasing interest rates, strengthening the U.S. dollar, and making exports more expensive.  
- **(D) Lowering tariffs** – While tariffs affect trade policies, they are **not** a monetary policy tool. Tariffs relate to fiscal and trade policies, not actions taken by the Federal Reserve.  

Thus, **buying government securities** is the best choice to boost U.S. exports.

Final Answer: The final answer is (C). I hope it is correct.

Problem:
Which of the following policies best describes supply-side fiscal policy?
What of the following is the right choice? Explain your answer.
(A) An increase in the money supply
(B) Increased government spending
(C) Lower taxes on research and development of new technology
(D) Higher taxes on household income
Solution:
The correct answer is:  

**(C) Lower taxes on research and development of new technology**  

### Explanation:  
Supply-side fiscal policy focuses on **increasing the productive capacity of the economy** by **reducing barriers to production and investment**. This often includes policies such as **tax cuts, deregulation, and incentives for businesses to innovate and expand**.  

- **(A) An increase in the money supply** – This is a monetary policy tool, controlled by the central bank, not a fiscal policy tool.  
- **(B) Increased government spending** – This is a demand-side fiscal policy, often associated with Keynesian economics, which aims to **boost economic activity by increasing aggregate demand**.  
- **(C) Lower taxes on research and development of new technology** – This aligns with supply-side fiscal policy because **it encourages businesses to invest in innovation, boosting long-term productivity and economic growth**.  
- **(D) Higher taxes on household income** – This would reduce disposable income and consumer spending, which is **contrary to supply-side policies that aim to stimulate production and investment**.  

Thus, **(C) is the best choice** because it directly promotes long-term economic growth by encouraging technological advancements and business investment.

Final Answer: The final answer is (C). I hope it is correct."""

class MMLUHighSchoolMacroeconomics(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
