from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
SHA-1 has a message digest of
What of the following is the right choice? Explain your answer.
(A) 160 bits
(B) 512 bits
(C) 628 bits
(D) 820 bits
Solution:
The correct answer is:  

**(A) 160 bits**  

### Explanation:  
SHA-1 (Secure Hash Algorithm 1) is a cryptographic hash function that processes an input message and produces a **fixed-size message digest** of **160 bits** (20 bytes).  

- The algorithm processes data in **512-bit blocks**, but the final output (message digest) is always **160 bits**.  
- The incorrect choices:  
  - **512 bits (B)**: This is the block size of SHA-1, not the output size.  
  - **628 bits (C) and 820 bits (D)**: These values are unrelated to SHA-1’s output size.  

Thus, the correct answer is **(A) 160 bits**.

Final Answer: The final answer is (A). I hope it is correct.

Problem:
_____________ can modify data on your system – so that your system doesn’t run correctly or you can no longer access specific data, or it may even ask for ransom in order to give your access.
What of the following is the right choice? Explain your answer.
(A) IM – Trojans
(B) Backdoor Trojans
(C) Trojan-Downloader
(D) Ransom Trojan
Solution:
The correct answer is:  

**(D) Ransom Trojan**  

### Explanation:  
A **Ransom Trojan (Ransomware)** is a type of malicious software that **modifies, encrypts, or locks data on a system**, preventing the user from accessing their files or system. The attacker then demands a ransom payment (usually in cryptocurrency) to restore access.  

#### Why not the other options?  
- **(A) IM – Trojans**: These Trojans are used to steal information through instant messaging applications rather than modifying system data.  
- **(B) Backdoor Trojans**: These create unauthorized access points (backdoors) in a system for hackers but do not necessarily modify or ransom data.  
- **(C) Trojan-Downloader**: These Trojans are designed to download and install other malicious programs but do not directly modify or ransom data.  

Thus, **Ransom Trojan (D)** is the best choice since it directly aligns with the description in the question.

Final Answer: The final answer is (D). I hope it is correct.

Problem:
What is ethical hacking?
What of the following is the right choice? Explain your answer.
(A) \"Hacking\" ethics so they justify unintended selfish behavior
(B) Hacking systems (e.g., during penetration testing) to expose vulnerabilities so they can be fixed, rather than exploited
(C) Hacking into systems run by those whose ethics you disagree with
(D) A slang term for rapid software development, e.g., as part of hackathons
Solution:
The correct answer is:  

**(B) Hacking systems (e.g., during penetration testing) to expose vulnerabilities so they can be fixed, rather than exploited.**  

### Explanation:  
Ethical hacking refers to the practice of testing computer systems, networks, or applications for security vulnerabilities **with permission** from the owner. The goal is to identify and fix weaknesses before malicious hackers can exploit them. Ethical hackers, also known as **white-hat hackers**, follow a strict code of conduct and often work as **penetration testers** or **security consultants** to help organizations improve their cybersecurity.  

#### Why the other options are incorrect:
- **(A)**: This misinterprets the term by suggesting it means manipulating ethics rather than conducting cybersecurity testing.  
- **(C)**: Hacking systems based on personal disagreements is **illegal** and considered cybercrime, not ethical hacking.  
- **(D)**: While "hackathons" involve rapid software development, this is **not** what "ethical hacking" refers to.  

Would you like any additional details on ethical hacking?

Final Answer: The final answer is (B). I hope it is correct.

Problem:
Exploitation of the Heartbleed bug permits
What of the following is the right choice? Explain your answer.
(A) overwriting cryptographic keys in memory
(B) a kind of code injection
(C) a read outside bounds of a buffer
(D) a format string attack
Solution:
The correct answer is:  

**(C) a read outside bounds of a buffer**  

### Explanation:  
The **Heartbleed** bug (CVE-2014-0160) is a vulnerability in OpenSSL's implementation of the **TLS/DTLS heartbeat extension**. It arises from improper bounds checking, allowing an attacker to read **up to 64 KB of memory** from the server or client.  

- The bug occurs because OpenSSL does not properly validate the payload length in the heartbeat request. This enables an attacker to craft a malicious request that causes OpenSSL to return more memory than intended, leading to an **out-of-bounds read** (a classic buffer over-read vulnerability).  
- This can expose **sensitive information** stored in memory, such as cryptographic keys, passwords, and private data.  

### Why the other options are incorrect:
- **(A) Overwriting cryptographic keys in memory** → Incorrect. Heartbleed does not overwrite memory; it only reads memory beyond intended bounds.  
- **(B) A kind of code injection** → Incorrect. Heartbleed does not involve injecting or executing arbitrary code, only reading data.  
- **(D) A format string attack** → Incorrect. Format string vulnerabilities involve improper handling of format specifiers (e.g., `%s`, `%x`) in functions like `printf()`, which is unrelated to Heartbleed.  

Thus, **(C) a read outside bounds of a buffer** is the correct answer.

Final Answer: The final answer is (C). I hope it is correct.

Problem:
The ____________ is anything which your search engine cannot search.
What of the following is the right choice? Explain your answer.
(A) Haunted web
(B) World Wide Web
(C) Surface web
(D) Deep Web
Solution:
The correct answer is:  

**(D) Deep Web**  

### Explanation:  
The **Deep Web** refers to parts of the internet that are not indexed by standard search engines like Google, Bing, or Yahoo. This includes private databases, academic journals behind paywalls, personal emails, banking records, government records, and any content that requires authentication or is not linked publicly. Since search engines rely on web crawlers to index content, anything that is not accessible through standard links remains outside their reach.  

#### Why Not the Other Options?  
- **(A) Haunted web** – This is not a recognized term in internet terminology.  
- **(B) World Wide Web** – The World Wide Web (WWW) includes both the Surface Web and the Deep Web, so it is too broad.  
- **(C) Surface Web** – The Surface Web refers to the part of the internet that is publicly accessible and indexed by search engines, making it searchable.  

Thus, the correct choice is **Deep Web (D)** because it consists of all the content that search engines cannot index.

Final Answer: The final answer is (D). I hope it is correct."""

class MMLUComputerSecurity(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
