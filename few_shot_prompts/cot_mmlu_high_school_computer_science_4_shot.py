from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
Which of the following is an example of the use of a device on the Internet of Things (IoT) ?
What of the following is the right choice? Explain your answer.
(A) A car alerts a driver that it is about to hit an object.
(B) A hiker uses a G P S watch to keep track of her position.
(C) A refrigerator orders milk from an online delivery service when the milk in the refrigerator is almost gone.
(D) A runner uses a watch with optical sensors to monitor his heart rate.
Solution:
The correct answer is **(C) A refrigerator orders milk from an online delivery service when the milk in the refrigerator is almost gone**.

**Explanation:**  
The Internet of Things (IoT) refers to devices embedded with sensors, software, and internet connectivity to exchange data and perform automated actions without direct human intervention.  

- **(A)** A car alerting the driver about an obstacle may use sensors, but unless the car communicates this data externally via the internet (e.g., to a cloud service or other devices), it is not necessarily IoT. This is more likely an onboard safety system.  
- **(B)** A GPS watch tracking a hiker’s location relies on satellite signals, not internet connectivity. While some GPS devices sync data to the cloud, the core function described here does not inherently involve IoT.  
- **(C)** A refrigerator autonomously ordering milk via the internet is a classic IoT example. The fridge uses sensors to detect low milk levels, connects to the internet, and triggers an online transaction—all without human input.  
- **(D)** A heart rate monitor in a watch uses optical sensors locally. Unless the watch transmits data to the internet (e.g., for analysis or storage), this is a standalone device, not IoT.  

Option **(C)** best exemplifies IoT because it combines sensors, internet connectivity, and automated interaction with an external service, fulfilling the core definition of IoT.

Final Answer: The final answer is (C). I hope it is correct.

Problem:
Many Web browsers allow users to open anonymous windows. During a browsing session in an anonymous window, the browser does not record a browsing history or a list of downloaded files. When the anonymous window is exited, cookies created during the session are deleted. Which of the following statements about browsing sessions in an anonymous window is true?
What of the following is the right choice? Explain your answer.
(A) The activities of a user browsing in an anonymous window will not be visible to people who monitor the user's network, such as the system administrator.
(B) Items placed in a Web store's shopping cart for future purchase during the anonymous browsing session will not be saved on the user's computer.
(C) A user will not be able to log in to e-mail or social media accounts during the anonymous browsing session.
(D) A user browsing in an anonymous window will be protected from viruses launched from any web sites visited or files downloaded.
Solution:
The correct choice is:  

**(B) Items placed in a Web store's shopping cart for future purchase during the anonymous browsing session will not be saved on the user's computer.**  

### Explanation:
When using an anonymous (incognito or private) browsing window, the browser does not store history, cookies, or cached files after the session ends. This means that any items placed in a shopping cart **using session-based cookies** will not be saved once the window is closed. If the website relies on cookies for the cart, the items will disappear after exiting the session.

### Why the other choices are incorrect:
- **(A) Incorrect:** Incognito mode does not hide browsing activity from network administrators, ISPs, or websites. It only prevents the browser from storing local history, cookies, or form data. Network-level monitoring (such as by a workplace or ISP) can still track user activity.  
- **(C) Incorrect:** A user **can** log in to accounts like email or social media. However, once the anonymous session is closed, login data and cookies will be erased.  
- **(D) Incorrect:** Incognito mode does **not** provide protection against viruses or malware from malicious websites or downloads. If a user downloads an infected file, it can still harm the system.  

Thus, **option (B) is the best answer** as it correctly describes the effect of anonymous browsing on session-based data like shopping carts.

Final Answer: The final answer is (B). I hope it is correct.

Problem:
What is the output of "abc"[::-1] in Python 3?
What of the following is the right choice? Explain your answer.
(A) Error
(B) abc
(C) cba
(D) c
Solution:
The correct answer is:

**(C) cba**

### Explanation:

In Python, the slicing syntax for strings is:

```python
string[start:stop:step]
```

- `start`: The starting index (inclusive).
- `stop`: The ending index (exclusive).
- `step`: The step size (how much to move between indices).

Now, let's analyze `"abc"[::-1]`:

- `[::-1]` means:
  - `start` and `stop` are left empty, meaning it takes the whole string.
  - `step = -1` means it traverses the string in reverse order.

Thus, `"abc"[::-1]` reverses `"abc"`, producing `"cba"`.

So, the correct choice is **(C) cba**.

Final Answer: The final answer is (C). I hope it is correct.

Problem:
In the program below, the initial value of x is 5 and the initial value of y is 10. IF (X < O) { DISPLAY ("Foxtrot") } ELSE { IF (X > y) { DISPLAY ("Hotel") } ELSE { IF (y > O) { DISPLAY ("November") } ELSE { DISPLAY ("Yankee") } } } What is displayed as a result of running the program?
What of the following is the right choice? Explain your answer.
(A) Foxtrot
(B) Hotel
(C) November
(D) Yankee
Solution:
Let's analyze the given conditional statements step by step.

### Given initial values:
- \( x = 5 \)
- \( y = 10 \)

The program logic:

```plaintext
IF (X < 0) { 
    DISPLAY ("Foxtrot") 
} ELSE { 
    IF (X > y) { 
        DISPLAY ("Hotel") 
    } ELSE { 
        IF (y > 0) { 
            DISPLAY ("November") 
        } ELSE { 
            DISPLAY ("Yankee") 
        } 
    } 
}
```

#### Step 1: Evaluate `IF (X < 0)`
- \( x = 5 \) is **not** less than 0.
- So, the `ELSE` block executes.

#### Step 2: Evaluate `IF (X > y)`
- \( x = 5 \) and \( y = 10 \), so \( 5 > 10 \) is **false**.
- So, we move to the next `ELSE` block.

#### Step 3: Evaluate `IF (y > 0)`
- \( y = 10 \) is **greater than** 0.
- So, `"November"` is displayed.

### Correct Answer:
**(C) November**

Final Answer: The final answer is (C). I hope it is correct."""

class MMLUHighSchoolComputerScience(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
