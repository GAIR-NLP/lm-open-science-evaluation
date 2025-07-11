from .few_shot_prompting import FewShotPrompting

few_shot_prompt = '''
Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

Answer in Python:
```
def solution():
    money_initial = 23
    bagels = 5
    bagel_cost = 3
    money_spent = bagels * bagel_cost
    money_left = money_initial - money_spent
    result = money_left
    return result
```


Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?

Answer in Python:
```
def solution():
    golf_balls_initial = 58
    golf_balls_lost_tuesday = 23
    golf_balls_lost_wednesday = 2
    golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
    result = golf_balls_left
    return result
```


Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

Answer in Python:
```
def solution():
    computers_initial = 9
    computers_per_day = 5
    num_days = 4  # 4 days between monday and thursday
    computers_added = computers_per_day * num_days
    computers_total = computers_initial + computers_added
    result = computers_total
    return result
```


Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
Answer in Python:
```
def solution():
    toys_initial = 5
    mom_toys = 2
    dad_toys = 2
    total_received = mom_toys + dad_toys
    total_toys = toys_initial + total_received
    result = total_toys
    return result
```


Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
Answer in Python:
```
def solution():
    jason_lollipops_initial = 20
    jason_lollipops_after = 12
    denny_lollipops = jason_lollipops_initial - jason_lollipops_after
    result = denny_lollipops
    return result
```


Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
Answer in Python:
```
def solution():
    leah_chocolates = 32
    sister_chocolates = 42
    total_chocolates = leah_chocolates + sister_chocolates
    chocolates_eaten = 35
    chocolates_left = total_chocolates - chocolates_eaten
    result = chocolates_left
    return result
```


Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
Answer in Python:
```
def solution():
    cars_initial = 3
    cars_arrived = 2
    total_cars = cars_initial + cars_arrived
    result = total_cars
    return result
```

Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
Answer in Python:
```
def solution():
    trees_initial = 15
    trees_after = 21
    trees_added = trees_after - trees_initial
    result = trees_added
    return result
```
'''.strip()

# few_shot_prompt = '''Problem:
# Find the value of $x$ that satisfies $\\frac{\\sqrt{3x+5}}{\\sqrt{6x+5}}=\\frac{\\sqrt{5}}{3}$. Express your answer as a common fraction.

# You are an expert programmer. Solve the above mathematical problem by writing a Python program. Express your answer as a numeric type or a SymPy object.
# ```
# # Initialize x
# x = symbols('x')

# # Define the equation
# equation = Eq(sqrt(3*x + 5)/sqrt(6*x + 5), sqrt(5)/3)

# # Solve for x
# answer = solve(equation, x)
# ```
# The imports required for this program are
# ```
# from sympy import symbols, Eq, solve, sqrt
# ```
# I hope my solution is correct.

# Problem:
# If $\\det \\mathbf{A} = 2$ and $\\det \\mathbf{B} = 12,$ then find $\\det (\\mathbf{A} \\mathbf{B}).$

# You are an expert programmer. Solve the above mathematical problem by writing a Python program. Express your answer as a numeric type or a SymPy object.
# ```
# # Given det(A) = 2 and det(B) = 12
# det_A = 2
# det_B = 12

# # Use the property det(AB) = det(A)*det(B)
# det_AB = det_A * det_B

# answer = det_AB
# ```
# The imports required for this program are
# ```

# ```
# I hope my solution is correct. 

# Problem:
# Terrell usually lifts two 20-pound weights 12 times. If he uses two 15-pound weights instead, how many times must Terrell lift them in order to lift the same total weight?

# You are an expert programmer. Solve the above mathematical problem by writing a Python program. Express your answer as a numeric type or a SymPy object.
# ```
# # Calculate the total weight lifted initially, which is 2*20*12 pounds
# total_weight = 2 * 20 * 12

# # Since Terrell lifts two 15-pound weights, divide the total weight by 2 * 15
# repetitions = total_weight / (2*15)

# answer = n_value 
# ```
# The imports required for this program are
# ```

# ```
# I hope my solution is correct. 

# Problem:
# If Anna flips 8 coins, what is the probability that she gets more heads than tails?

# You are an expert programmer. Solve the above mathematical problem by writing a Python program. Express your answer as a numeric type or a SymPy object.
# ```
# # There are 2**8 possible outcomes
# n = 8
# total_outcomes = 2 ** n

# # There are binom(n, k) ways to get k heads
# favorable_outcomes = 0
# for k in range((n // 2) + 1, n + 1):
#     favorable_outcomes += math.comb(n, k)
    
# probability = favorable_outcomes / total_outcomes

# answer = probability
# ```
# The imports required for this program are
# ```
# import math
# ```
# I hope my solution is correct.

# Problem:
# Evaluate $\\left\\lceil3\\left(6-\\frac12\\right)\\right\\rceil$.

# You are an expert programmer. Solve the above mathematical problem by writing a Python program. Express your answer as a numeric type or a SymPy object.
# ```
# # Calculate 3 * (6 - 1/2)
# result = 3 * (6 - 0.5)

# # Apply the ceiling function
# ceiling_result = math.ceil(result)

# answer = ceiling_result
# ```
# The imports required for this program are
# ```
# import math
# ```
# I hope my solution is correct.
# '''.strip()

class PALGSMPrompt(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\n\nQ: {task_input}\nAnswer in Python:\n``\ndef solution():\n"
        # prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\n\nYou are an expert programmer. Solve the above mathematical problem by writing a Python program. Express your answer as a numeric type or a SymPy object.\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        # return ["\nProblem:", "Problem:"]
        return ["\nQ:", "Q: "]
