from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
For a stationary autoregressive process, shocks will
What of the following is the right choice? Explain your answer.
(A) Eventually die away
(B) Persist indefinitely
(C) Grow exponentially
(D) Never occur
Solution:
For a stationary autoregressive (AR) process, the key characteristic is that the effects of shocks diminish over time. This occurs because the coefficients in a stationary AR model satisfy conditions (roots of the characteristic equation outside the unit circle) ensuring that past shocks decay geometrically. Specifically:

- **Option A (Eventually die away)** is correct. In a stationary AR process, the impact of a shock at time \( t \) on future values \( Y_{t+k} \) diminishes as \( k \) increases. For example, in an AR(1) model \( Y_t = \phi Y_{t-1} + \varepsilon_t \) with \( |\phi| < 1 \), the effect of \( \varepsilon_t \) on \( Y_{t+k} \) is \( \phi^k \varepsilon_t \), which approaches zero as \( k \to \infty \).

- **Option B (Persist indefinitely)** applies to non-stationary processes with unit roots (e.g., random walks), but the question specifies a stationary process, ruling this out.

- **Option C (Grow exponentially)** describes explosive non-stationary processes where \( |\phi| > 1 \), which violates stationarity.

- **Option D (Never occur)** is incorrect because shocks (\( \varepsilon_t \)) are inherent to AR models; without them, the process would be deterministic.

**Answer:** (A) Eventually die away.  
**Explanation:** In a stationary AR process, shocks decay geometrically due to the model's coefficients, ensuring their effects vanish over time.

Final Answer: The final answer is (A). I hope it is correct.

Problem:
Consider the following AR(1) model with the disturbances having zero mean and unit variance yt = 0.2 + 0.4 yt-1 + ut The (unconditional) mean of y will be given by
What of the following is the right choice? Explain your answer.
(A) 0.2
(B) 0.4
(C) 0.5
(D) 0.33
Solution:
To find the unconditional mean of the AR(1) model \( y_t = 0.2 + 0.4 y_{t-1} + u_t \) where the disturbances \( u_t \) have zero mean and unit variance, we start by noting that the process is stationary because the autoregressive coefficient \( 0.4 \) is less than 1 in absolute value.

For a stationary AR(1) process, the unconditional mean \( \mu \) is given by the formula:
\[
\mu = \frac{c}{1 - \phi}
\]
where \( c \) is the constant term and \( \phi \) is the autoregressive coefficient. Here, \( c = 0.2 \) and \( \phi = 0.4 \).

Plugging in these values:
\[
\mu = \frac{0.2}{1 - 0.4} = \frac{0.2}{0.6} = \frac{1}{3} \approx 0.33
\]

To verify, we take expectations on both sides of the AR(1) equation:
\[
E[y_t] = E[0.2 + 0.4 y_{t-1} + u_t]
\]
Since \( E[u_t] = 0 \) and \( E[y_t] = E[y_{t-1}] = \mu \) for a stationary process, we get:
\[
\mu = 0.2 + 0.4 \mu
\]
Solving for \( \mu \):
\[
\mu - 0.4 \mu = 0.2 \implies 0.6 \mu = 0.2 \implies \mu = \frac{0.2}{0.6} = \frac{1}{3} \approx 0.33
\]

Thus, the correct answer is \(\boxed{D}\).

Final Answer: The final answer is (D). I hope it is correct.

Problem:
Suppose that a test statistic has associated with it a p-value of 0.08. Which one of the following statements is true? (i) If the size of the test were exactly 8%, we would be indifferent between rejecting and not rejecting the null hypothesis (ii) The null would be rejected if a 10% size of test were used (iii) The null would not be rejected if a 1% size of test were used (iv) The null would be rejected if a 5% size of test were used.
What of the following is the right choice? Explain your answer.
(A) (ii) and (iv) only
(B) (i) and (iii) only
(C) (i), (ii), and (iii) only
(D) (i), (ii), (iii), and (iv)
Solution:
Given a test statistic with a p-value of 0.08, we need to determine which of the statements (i) to (iv) are true. Here is the breakdown:

1. **Statement (i): If the size of the test were exactly 8%, we would be indifferent between rejecting and not rejecting the null hypothesis.**
   - The size of the test (alpha) is 8%. The p-value is 0.08, which equals alpha. According to standard hypothesis testing, we reject the null hypothesis if the p-value is less than or equal to alpha. Therefore, we would reject the null hypothesis, not be indifferent. However, some might consider the term "indifferent" as being at the boundary. This is a point of ambiguity, but strictly speaking, we should reject. Hence, this statement is considered false.

2. **Statement (ii): The null would be rejected if a 10% size of test were used.**
   - The significance level (alpha) is 10%. The p-value (0.08) is less than 0.10, so we reject the null hypothesis. This statement is true.

3. **Statement (iii): The null would not be rejected if a 1% size of test were used.**
   - The significance level (alpha) is 1%. The p-value (0.08) is greater than 0.01, so we do not reject the null hypothesis. This statement is true.

4. **Statement (iv): The null would be rejected if a 5% size of test were used.**
   - The significance level (alpha) is 5%. The p-value (0.08) is greater than 0.05, so we do not reject the null hypothesis. This statement is false.

Given the analysis, statements (ii) and (iii) are true. However, considering the provided answer choices and potential ambiguity in interpreting statement (i), the closest answer is:

\(\boxed{C}\)

Final Answer: The final answer is (C). I hope it is correct.

Problem:
What would be then consequences for the OLS estimator if heteroscedasticity is present in a regression model but ignored?
What of the following is the right choice? Explain your answer.
(A) It will be biased
(B) It will be inconsistent
(C) It will be inefficient
(D) All of (a), (b) and (c) will be true.
Solution:
The correct answer is:

**(C) It will be inefficient.**  

### Explanation:
If heteroscedasticity (non-constant variance of error terms) is present in a regression model but ignored, the consequences for the Ordinary Least Squares (OLS) estimator are:

1. **Unbiasedness**: OLS estimates remain **unbiased** even in the presence of heteroscedasticity. This is because the Gauss-Markov theorem states that OLS is the Best Linear Unbiased Estimator (BLUE) under the assumption of homoscedasticity, but heteroscedasticity does not introduce bias in the estimated coefficients.

2. **Consistency**: The OLS estimator remains **consistent** despite heteroscedasticity, meaning that as the sample size increases, the estimates converge to the true parameter values.

3. **Efficiency**: OLS is no longer **efficient** because the standard errors of the estimates are incorrect when heteroscedasticity is present. This means that OLS is not the minimum variance unbiased estimator (MVUE) in this case, and more efficient estimators (such as Generalized Least Squares (GLS) or heteroscedasticity-robust standard errors) should be used.

Thus, the correct answer is **(C) It will be inefficient** since heteroscedasticity affects efficiency but does not cause bias or inconsistency.

Final Answer: The final answer is (C). I hope it is correct."""

class MMLUEconometrics(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
