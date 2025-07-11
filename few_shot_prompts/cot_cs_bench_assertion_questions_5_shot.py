from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
The Data Link Layer in the OSI reference model does not have congestion control capabilities.
Please determine whether the statement is correct. What of the following is the right choice? Explain your answer.
(A) True
(B) False
Solution:
The **Data Link Layer** in the **OSI reference model** is primarily responsible for **framing, error detection, error correction, and MAC (Medium Access Control) mechanisms**. It ensures reliable node-to-node communication within a local network but does not have end-to-end congestion control mechanisms.

#### **Why is congestion control not a part of the Data Link Layer?**
1. **Scope Limitation**:  
   - Congestion occurs due to excessive traffic in a network, which is typically managed at higher layers (e.g., the Transport Layer).  
   - The Data Link Layer only operates on a **local** or **point-to-point** basis, meaning it does not have a global view of network congestion.

2. **Responsibility of Higher Layers**:  
   - The **Transport Layer (Layer 4)** (e.g., TCP) is responsible for end-to-end congestion control mechanisms like **TCP congestion control (slow start, congestion avoidance, etc.)**.
   - The **Network Layer (Layer 3)** (e.g., IP) may implement congestion avoidance techniques like **packet queuing and dropping** in routers.

3. **MAC-level Flow Control vs. Congestion Control**:  
   - The Data Link Layer may implement **flow control mechanisms** (e.g., stop-and-wait, sliding window) to prevent overwhelming a receiver.  
   - However, **flow control is different from congestion control**, as it only manages data transmission between two directly connected devices, not across the network.

Thus, since the **Data Link Layer does not handle network-wide congestion control**, the given statement is **correct**, making the answer **(A) True**.

Final Answer: The final answer is (A). I hope it is correct.

Problem:
Baud rate is equal to the number of bytes transmitted per second.
Please determine whether the statement is correct. What of the following is the right choice? Explain your answer.
(A) True
(B) False
Solution:
 The **baud rate** refers to the number of signal changes (symbols) per second in a communication channel, not necessarily the number of bytes transmitted per second.  

However, the **bit rate** (bps) is the actual number of bits transmitted per second. The relationship between baud rate and bit rate depends on the number of bits per symbol:  

\[
\text{Bit Rate} = \text{Baud Rate} \times \text{Bits per Symbol}
\]

For example:  
- If a system uses **1 bit per symbol**, the **bit rate = baud rate**.
- If a system uses **4 bits per symbol**, the **bit rate = 4 × baud rate**.

Since 1 byte = 8 bits, the number of bytes transmitted per second depends on the bit rate, not the baud rate directly. Therefore, saying that "baud rate is equal to the number of bytes transmitted per second" is incorrect.

Final Answer: The final answer is (B). I hope it is correct.

Problem:
The path value of MTU is determined by the frame length of the data link layer.
Please determine whether the statement is correct. What of the following is the right choice? Explain your answer.
(A) True
(B) False
Solution:
The **Maximum Transmission Unit (MTU)** is the largest size of a packet that can be transmitted over a network without needing fragmentation. It is determined by the **frame length of the data link layer (Layer 2 in the OSI model)** because different network technologies (such as Ethernet, Wi-Fi, or MPLS) have different frame size limitations.

For example:  
- **Ethernet** typically has an MTU of **1500 bytes** (excluding headers).  
- **Jumbo Frames** can increase the MTU to **9000 bytes** in some networks.  
- **PPP (Point-to-Point Protocol)** may have different MTU sizes depending on configuration.

Since the MTU is **directly constrained by the maximum frame length of the data link layer**, the statement is **true**.

Final Answer: The final answer is (A). I hope it is correct.

Problem:
Frame CRC checking is used to detect errors in a frame.
Please determine whether the statement is correct. What of the following is the right choice? Explain your answer.
(A) True
(B) False
Solution:
Frame **Cyclic Redundancy Check (CRC)** is a widely used error-detection technique in data transmission. It helps verify the integrity of a transmitted frame by detecting errors that may have occurred during transmission.  

1. **How CRC Works**:  
   - Before sending a frame, the sender computes a CRC value (checksum) based on the frame's data using a predetermined polynomial.
   - This CRC value is appended to the frame and transmitted.
   - The receiver performs the same CRC computation on the received data and compares it with the transmitted CRC.
   - If the computed and received CRC values do not match, it indicates an error in the frame.

2. **Error Detection**:  
   - CRC is effective in detecting common types of errors such as bit flips, burst errors, and single-bit errors.
   - However, it cannot correct errors—only detect them.

Since **Frame CRC is used to detect errors in a frame**, the given statement is **correct**, making **option (A) the right choice**.

Final Answer: The final answer is (A). I hope it is correct.

Problem:
The OSPF protocol supports broadcast routing.
Please determine whether the statement is correct. What of the following is the right choice? Explain your answer.
(A) True
(B) False
Solution:
OSPF (Open Shortest Path First) is a **link-state routing protocol**, which is designed to compute the shortest path to destinations using the **Dijkstra algorithm**. OSPF does not support traditional **broadcast routing**, which is a method where packets are sent to all nodes in a network without explicit routing.

Instead, OSPF supports the following:
1. **Multicast**: OSPF uses multicast addresses (e.g., **224.0.0.5** for all OSPF routers and **224.0.0.6** for designated routers) for communication rather than broadcasting packets to all nodes.
2. **Unicast**: OSPF routers can also communicate using unicast in certain cases, such as database exchange between neighbors.
3. **Broadcast Network Type**: OSPF does define a **broadcast network type**, which allows routers to form adjacencies efficiently over Ethernet networks. However, this does not mean OSPF itself supports general-purpose **broadcast routing**.

**Conclusion:**  
Since OSPF does not support generic **broadcast routing** but rather uses multicast and unicast for communication, the statement is **false**.

Final Answer: The final answer is (B). I hope it is correct."""

class CSBenchAssertion(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
