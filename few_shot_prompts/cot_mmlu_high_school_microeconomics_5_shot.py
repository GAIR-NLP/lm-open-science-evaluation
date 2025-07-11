from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
In a competitive labor market for housepainters, which of the following would increase the demand for housepainters?
What of the following is the right choice? Explain your answer.
(A) An effective minimum wage imposed on this labor market.
(B) An increase in the price of gallons of paint.
(C) An increase in the construction of new houses.
(D) An increase in the price of mechanical painters so long as the output effect exceeds the substitution effect.
Solution:
The correct answer is:  

**(C) An increase in the construction of new houses.**  

### Explanation:  
The demand for labor, including housepainters, is derived demand—meaning it depends on the demand for the final product or service. If more houses are being built, there will be a greater need for housepainters, leading to an increase in the demand for their labor.  

#### Why the other options are incorrect:  
- **(A) An effective minimum wage imposed on this labor market:**  
  A minimum wage affects the supply and price of labor, but it does not increase the demand for housepainters. If anything, a higher wage might reduce demand if employers decide to hire fewer workers due to increased costs.  

- **(B) An increase in the price of gallons of paint:**  
  If paint becomes more expensive, the overall cost of painting rises. This could lead to a decrease in the demand for painting services, thereby reducing the demand for housepainters.  

- **(D) An increase in the price of mechanical painters so long as the output effect exceeds the substitution effect:**  
  This option is more complex. If mechanical painters (machines that paint houses) become more expensive, businesses might choose to hire more human painters instead. However, this depends on whether the increase in costs leads to a strong enough shift toward manual labor. This is uncertain, whereas new house construction directly increases the need for painters.  

Thus, **(C) an increase in the construction of new houses** is the best answer because it directly increases the demand for housepainters.

Final Answer: The final answer is (C). I hope it is correct.

Problem:
If the government subsidizes producers in a perfectly competitive market, then
What of the following is the right choice? Explain your answer.
(A) the demand for the product will increase
(B) the demand for the product will decrease
(C) the consumer surplus will increase
(D) the consumer surplus will decrease
Solution:
The correct answer is:  

**(C) the consumer surplus will increase**  

### Explanation:  
In a perfectly competitive market, if the government **subsidizes producers**, it effectively reduces their cost of production. This leads to an **increase in supply**, shifting the supply curve **to the right**. As a result:  

1. **The market equilibrium price decreases**, making the product cheaper for consumers.  
2. **The equilibrium quantity increases**, meaning more of the product is available in the market.  
3. **Consumer surplus is the area between the demand curve and the price level**—when the price falls, consumers gain more benefit because they are paying less than they were willing to pay. Thus, consumer surplus **increases**.  

#### Why not the other options?  
- **(A) The demand for the product will increase** → Incorrect. The demand curve does not shift because consumer preferences, income, and other demand factors remain unchanged. The quantity demanded increases due to the lower price, but the demand curve itself does not move.  
- **(B) The demand for the product will decrease** → Incorrect. A decrease in demand would mean the demand curve shifts left, which does not happen due to a subsidy.  
- **(D) The consumer surplus will decrease** → Incorrect. Lower prices benefit consumers, increasing their surplus, not decreasing it.  

Thus, the right choice is **(C) the consumer surplus will increase**.

Final Answer: The final answer is (C). I hope it is correct.

Problem:
The concentration ratio for a monopoly is
What of the following is the right choice? Explain your answer.
(A) 0
(B) 5
(C) 10
(D) 100
Solution:
The correct answer is:  

**(D) 100**  

### Explanation:  
The **concentration ratio** is a measure of market power that indicates the percentage of total market output produced by the largest firms in an industry. The most commonly used concentration ratio is the **CR4 (four-firm concentration ratio)** or **CR1 (one-firm concentration ratio)** for monopolies.  

- A **monopoly** exists when a single firm dominates the entire market, meaning it holds **100% of the market share**.  
- The **concentration ratio for a monopoly is 100**, as there are no other competitors in the market.  

**Why not the other options?**  
- **(A) 0** → A concentration ratio of 0 means the market is highly competitive, with no dominant firms, which contradicts the definition of a monopoly.  
- **(B) 5** and **(C) 10** → These suggest that the largest firms hold only 5% or 10% of the market, indicating a highly competitive or oligopolistic market rather than a monopoly.  

Thus, the correct answer is **100** for a monopoly.

Final Answer: The final answer is (D). I hope it is correct.

Problem:
Which of the following is true of a price floor?
What of the following is the right choice? Explain your answer.
(A) The price floor shifts the demand curve to the left.
(B) An effective floor creates a shortage of the good.
(C) The price floor shifts the supply curve of the good to the right.
(D) To be an effective floor, it must be set above the equilibrium price.
Solution:
The correct choice is:

**(D) To be an effective floor, it must be set above the equilibrium price.**

### Explanation:
- A **price floor** is the minimum price set by the government for a good or service. For the floor to be effective, it must be set **above the equilibrium price**, meaning the price where the supply and demand curves intersect.
- If the price floor is above the equilibrium price, it creates a situation where the quantity supplied exceeds the quantity demanded, leading to a **surplus** of the good, not a shortage.
  
Let’s break down the other options:

- **(A)**: The price floor does not shift the demand curve. It only affects the price at which the good is bought and sold, not the demand itself.
- **(B)**: A price floor typically creates a **surplus**, not a shortage, because it prevents prices from falling to the equilibrium level, resulting in excess supply.
- **(C)**: The price floor doesn’t shift the supply curve either. It only establishes a price that must be respected, affecting the market's outcome rather than the curve itself.

Final Answer: The final answer is (D). I hope it is correct.

Problem:
Which of the following is necessarily a characteristic of oligopoly?
What of the following is the right choice? Explain your answer.
(A) Free entry into and exit from the market
(B) A few large producers
(C) One producer of a good with no close substitutes
(D) A homogenous product
Solution:
The correct answer is **(B) A few large producers**.

Explanation:
An oligopoly is a market structure characterized by a small number of large firms that dominate the market. These firms have significant market power, meaning that their actions (such as setting prices or output levels) can influence the market as a whole. The key feature of an oligopoly is the concentration of market share among a few large producers.

Here's why the other choices are not correct:
- **(A) Free entry into and exit from the market**: In an oligopoly, entry barriers are typically high, which prevents easy entry or exit for firms. This is contrary to perfect competition, where firms can freely enter or exit the market.
- **(C) One producer of a good with no close substitutes**: This describes a monopoly, not an oligopoly. A monopoly has only one firm that dominates the market, whereas an oligopoly has several firms.
- **(D) A homogenous product**: While some oligopolistic markets may have homogenous products (like oil), many oligopolies involve differentiated products (such as cars or mobile phones). Therefore, a homogenous product is not necessarily a characteristic of oligopoly.

Final Answer: The final answer is (B). I hope it is correct."""

class MMLUHighSchoolMicroeconomics(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
