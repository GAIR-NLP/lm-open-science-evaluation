from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
What is the embryological origin of the hyoid bone?
What of the following is the right choice? Explain your answer.
(A) The first pharyngeal arch
(B) The first and second pharyngeal arches
(C) The second pharyngeal arch
(D) The second and third pharyngeal arches
Solution:
The correct answer is:

**(D) The second and third pharyngeal arches.**

### Explanation:
The hyoid bone develops from the **second (hyoid) pharyngeal arch** and the **third pharyngeal arch** during embryogenesis:

1. **Second pharyngeal arch:**
   - Contributes to the upper part of the hyoid bone, specifically the **lesser horn (cornu)** and the **upper body** of the hyoid bone.

2. **Third pharyngeal arch:**
   - Contributes to the lower part of the hyoid bone, specifically the **greater horn (cornu)** and the **lower body** of the hyoid bone.

This distribution arises because the structures of the hyoid bone originate from mesenchymal tissue within these pharyngeal arches, each of which is associated with distinct skeletal, muscular, and neural components during development.

#### Why the other options are incorrect:
- **(A) The first pharyngeal arch:** Incorrect because it contributes to structures such as the maxilla, mandible, malleus, and incus, not the hyoid bone.
- **(B) The first and second pharyngeal arches:** Incorrect because the hyoid bone does not involve the first pharyngeal arch.
- **(C) The second pharyngeal arch:** Partially correct but incomplete, as the third pharyngeal arch also contributes to the hyoid bone.

Final Answer: The final answer is (D). I hope it is correct.

Problem:
Which of these branches of the trigeminal nerve contain somatic motor processes?
What of the following is the right choice? Explain your answer.
(A) The supraorbital nerve
(B) The infraorbital nerve
(C) The mental nerve
(D) None of the above
Solution:
The correct answer is **(D) None of the above**.

### Explanation:
The trigeminal nerve (cranial nerve V) has three main branches:
1. **Ophthalmic nerve (V1)**: purely sensory
2. **Maxillary nerve (V2)**: purely sensory
3. **Mandibular nerve (V3)**: mixed (both sensory and motor)

The **somatic motor processes** of the trigeminal nerve are only found in the mandibular branch (V3). These motor fibers innervate the muscles of mastication (e.g., temporalis, masseter, medial and lateral pterygoid muscles) and other small muscles such as the mylohyoid, anterior belly of the digastric, tensor veli palatini, and tensor tympani.

Now, let's analyze the options:
- **(A) Supraorbital nerve**: This is a branch of the ophthalmic nerve (V1), which is purely sensory. It provides sensation to the forehead and scalp.
- **(B) Infraorbital nerve**: This is a branch of the maxillary nerve (V2), which is also purely sensory. It supplies sensation to the skin of the cheek, upper lip, and lower eyelid.
- **(C) Mental nerve**: This is a branch of the mandibular nerve (V3), but it is a sensory branch. It supplies sensation to the chin and lower lip. It does not carry motor fibers.

Since none of these branches carry somatic motor processes, the correct answer is **(D) None of the above**.

Final Answer: The final answer is (D). I hope it is correct.

Problem:
The pleura
What of the following is the right choice? Explain your answer.
(A) have no sensory innervation.
(B) are separated by a 2 mm space.
(C) extend into the neck.
(D) are composed of respiratory epithelium.
Solution:
The correct choice is:

**(C) extend into the neck.**

### Explanation:

The pleura are a pair of serous membranes that enclose the lungs and line the thoracic cavity. Here's an analysis of each option:

---

**(A) have no sensory innervation.**  
- This is **incorrect.**  
  The pleura have sensory innervation:
  - The **parietal pleura** (lining the thoracic cavity) has rich sensory innervation from the **intercostal nerves** and the **phrenic nerve**, which makes it very sensitive to pain. 
  - The **visceral pleura** (covering the lungs) has no pain fibers but is innervated by autonomic nerves, primarily for visceral sensation.

---

**(B) are separated by a 2 mm space.**  
- This is **incorrect.**  
  The pleural cavity (the potential space between the visceral and parietal pleurae) typically contains a small amount of serous fluid (approximately 5–10 mL). While it is a thin space, its dimensions vary depending on physiological conditions like breathing and are not fixed at 2 mm.

---

**(C) extend into the neck.**  
- This is **correct.**  
  The pleura extend above the level of the **first rib** into the neck region. This part is called the **cervical pleura** (or pleural cupola) and is reinforced by the suprapleural membrane (Sibson's fascia). It is clinically significant because injuries in the neck region can affect the pleura.

---

**(D) are composed of respiratory epithelium.**  
- This is **incorrect.**  
  The pleura are composed of a **mesothelium** (a single layer of flat, squamous cells) supported by connective tissue. Respiratory epithelium, characterized by ciliated pseudostratified columnar cells with goblet cells, is found in the conducting airways, such as the trachea and bronchi, but not in the pleura.

---

Final Answer: The final answer is (C). I hope it is correct.

Problem:
In Angle's Class II Div 2 occlusion there is
What of the following is the right choice? Explain your answer.
(A) excess overbite of the upper lateral incisors.
(B) negative overjet of the upper central incisors.
(C) excess overjet of the upper lateral incisors.
(D) excess overjet of the upper central incisors.
Solution:
In Angle's Class II Division 2 occlusion, the key features include retroclined upper central incisors and proclined upper lateral incisors. Here's the breakdown of the options:

- **(A) Excess overbite of the upper lateral incisors**: Incorrect. While a deep overbite (excess vertical overlap) is characteristic of Class II Div 2, it primarily involves the retroclined **central** incisors, not the laterals. The lateral incisors are proclined and may have reduced vertical overlap.

- **(B) Negative overjet of the upper central incisors**: Incorrect. Negative overjet (lower teeth ahead of upper teeth) is a Class III trait. In Class II Div 2, the central incisors are retroclined but still positioned anterior to the lower teeth, so their overjet is not negative.

- **(C) Excess overjet of the upper lateral incisors**: **Correct**. The proclined (labially inclined) upper lateral incisors in Class II Div 2 result in increased horizontal projection, leading to excess overjet specifically in the lateral incisors.

- **(D) Excess overjet of the upper central incisors**: Incorrect. The retroclined upper central incisors are tipped backward, which reduces their horizontal projection. Excess overjet of the centrals is typical of Class II Div 1, not Div 2.

**Answer**: **(C) Excess overjet of the upper lateral incisors.**  
In Class II Div 2, the retroclined central incisors contribute to a deep overbite, while the proclined lateral incisors exhibit increased horizontal overjet.

Final Answer: The final answer is (C). I hope it is correct.

Problem:
Which of the following is the body cavity that contains the pituitary gland?
What of the following is the right choice? Explain your answer.
(A) Abdominal
(B) Cranial
(C) Pleural
(D) Spinal
Solution:
The correct answer is: **(B) Cranial**.

### Explanation:
The **pituitary gland** is a small, pea-shaped gland located in the brain. It is housed in a bony cavity called the **sella turcica**, which is part of the **sphenoid bone** in the skull. Since the pituitary gland is located within the skull, it resides in the **cranial cavity**, which is the body cavity that encloses the brain and other associated structures.

#### Why not the other options?
- **(A) Abdominal**: This cavity houses organs such as the stomach, liver, intestines, and kidneys. It is unrelated to the location of the pituitary gland.
- **(C) Pleural**: This cavity surrounds the lungs within the thoracic cavity. It has no connection to the brain or the pituitary gland.
- **(D) Spinal**: This cavity contains the spinal cord and is located within the vertebral column, separate from the cranial cavity where the pituitary gland resides.

Thus, the pituitary gland is in the **cranial cavity** because it is located in the skull, beneath the brain.

Final Answer: The final answer is (B). I hope it is correct."""

class MMLUAnatomy(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
