from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
A 42-year-old man comes to the office for preoperative evaluation prior to undergoing adrenalectomy scheduled in 2 weeks. One month ago, he received care in the emergency department for pain over his right flank following a motor vehicle collision. At that time, blood pressure was 160/100 mm Hg and CT scan of the abdomen showed an incidental 10-cm left adrenal mass. Results of laboratory studies, including complete blood count, serum electrolyte concentrations, and liver function tests, were within the reference ranges. The patient otherwise had been healthy and had never been told that he had elevated blood pressure. He takes no medications. A follow-up visit in the office 2 weeks ago disclosed elevated urinary normetanephrine and metanephrine and plasma aldosterone concentrations. The patient was referred to a surgeon, who recommended the adrenalectomy. Today, vital signs are temperature 36.6°C (97.9°F), pulse 100/min, respirations 14/min, and blood pressure 170/95 mm Hg. Physical examination discloses no significant findings. Initial preoperative preparation should include treatment with which of the following?
What of the following is the right choice? Explain your answer.
(A) Labetalol
(B) A loading dose of potassium chloride
(C) Nifedipine
(D) Phenoxybenzamine
Solution:
The patient presents with a left adrenal mass, elevated urinary metanephrines/normetanephrines, and hypertension, strongly suggestive of a **pheochromocytoma**. Preoperative management of pheochromocytoma focuses on preventing life-threatening hypertensive crises during surgery. This requires **alpha-adrenergic blockade** to counteract the effects of catecholamines released by the tumor. 

### Key Analysis of Options:
- **(A) Labetalol**: A combined alpha/beta-blocker. **Avoided as initial therapy** because beta-blockade without prior alpha-blockade can worsen hypertension due to unopposed alpha-mediated vasoconstriction.  
- **(B) Potassium chloride**: Unnecessary here, as the patient’s serum electrolytes (including potassium) are normal. While elevated aldosterone levels might suggest hypokalemia in primary hyperaldosteronism, this patient’s potassium is within range.  
- **(C) Nifedipine**: A calcium channel blocker. While sometimes used adjunctively, it is **not first-line** for pheochromocytoma preparation, as it does not prevent catecholamine-induced arrhythmias or vasoconstriction as effectively as alpha-blockers.  
- **(D) Phenoxybenzamine**: A **non-selective, irreversible alpha-blocker**. This is the **standard initial therapy** for preoperative management of pheochromocytoma. It provides sustained alpha-blockade, mitigating catecholamine-induced vasoconstriction and hypertension. Beta-blockers (if needed for tachycardia) are added only after adequate alpha-blockade.

### Conclusion:
The elevated aldosterone is likely secondary to catecholamine-driven renin release (secondary hyperaldosteronism) rather than a primary aldosteronoma, given the normal potassium and lack of hypokalemia. The priority is alpha-blockade to prepare for adrenalectomy. 

**Correct Answer: (D) Phenoxybenzamine**

Final Answer: The final answer is (D). I hope it is correct.

Problem:
A previously healthy 32-year-old woman comes to the physician 8 months after her husband was killed in a car crash. Since that time, she has had a decreased appetite and difficulty falling asleep. She states that she is often sad and cries frequently. She has been rechecking the door lock five times before leaving her house and has to count exactly five pieces of toilet paper before she uses it. She says that she has always been a perfectionist but these urges and rituals are new. Pharmacotherapy should be targeted to which of the following neurotransmitters?
What of the following is the right choice? Explain your answer.
(A) Dopamine
(B) Glutamate
(C) Norepinephrine
(D) Serotonin
Solution:
The patient presents with symptoms of both depression (decreased appetite, insomnia, sadness) and new-onset obsessive-compulsive behaviors (checking, counting rituals). While her depressive symptoms may stem from grief, the emergence of compulsive rituals suggests a diagnosis of Obsessive-Compulsive Disorder (OCD), likely triggered by the stress of her husband's death. 

**Key reasoning for the answer:**  
- OCD is primarily associated with dysregulation of **serotonin**, and first-line pharmacotherapy for OCD involves Selective Serotonin Reuptake Inhibitors (SSRIs).  
- Although depression can involve other neurotransmitters like norepinephrine, the presence of OCD symptoms specifically guides treatment toward serotonin-targeted therapy.  
- Dopamine and glutamate are less directly implicated in first-line OCD treatment, and norepinephrine is more relevant to depression without comorbid OCD.  

**Answer:** **(D) Serotonin**  
Pharmacotherapy should target serotonin to address the obsessive-compulsive symptoms, which are central to her current presentation.

Final Answer: The final answer is (D). I hope it is correct.

Problem:
A 44-year-old man comes to the office because of a 3-day history of sore throat, nonproductive cough, runny nose, and frontal headache. He says the headache is worse in the morning and ibuprofen does provide some relief. He has not had shortness of breath. Medical history is unremarkable. He takes no medications other than the ibuprofen for pain. Vital signs are temperature 37.4°C (99.4°F), pulse 88/min, respirations 18/min, and blood pressure 120/84 mm Hg. Examination of the nares shows erythematous mucous membranes. Examination of the throat shows erythema and follicular lymphoid hyperplasia on the posterior oropharynx. There is no palpable cervical adenopathy. Lungs are clear to auscultation. Which of the following is the most likely cause of this patient's symptoms?
What of the following is the right choice? Explain your answer.
(A) Allergic rhinitis
(B) Epstein-Barr virus
(C) Mycoplasma pneumoniae
(D) Rhinovirus
Solution:
The most likely cause of the patient's symptoms is **(D) Rhinovirus**. Here's the rationale:

1. **Clinical Presentation**: The patient has acute-onset upper respiratory symptoms (sore throat, nonproductive cough, runny nose, frontal headache) lasting 3 days, consistent with a viral upper respiratory infection (common cold). Rhinovirus is the most common cause of such infections.

2. **Key Findings**: 
   - **Low-grade fever** (37.4°C) and **morning headache** (likely due to sinus congestion from lying flat) align with a viral etiology. 
   - **Posterior oropharyngeal erythema with follicular lymphoid hyperplasia** is typical of viral pharyngitis. 
   - **Absence of cervical lymphadenopathy** and **clear lung auscultation** argue against bacterial pathogens (e.g., streptococcal pharyngitis) or lower respiratory involvement (e.g., *Mycoplasma pneumoniae*).

3. **Exclusion of Other Options**:
   - **(A) Allergic rhinitis**: Unlikely due to acute onset, lack of pruritus/sneezing, and presence of fever.
   - **(B) Epstein-Barr virus (EBV)**: Typically causes exudative pharyngitis, significant lymphadenopathy, and fatigue, which are absent here.
   - **(C) Mycoplasma pneumoniae**: More commonly associated with subacute cough, lower respiratory symptoms (e.g., crackles), and prolonged illness, which are not evident in this case.

4. **Support for Rhinovirus**: The self-limited, mild course, and symptom constellation (rhinorrhea, sore throat, cough, morning headache) strongly suggest rhinovirus, the predominant cause of the common cold. Ibuprofen’s partial relief aligns with managing inflammation from viral illness.

Final Answer: The final answer is (D). I hope it is correct.

Problem:
A 22-year-old male marathon runner presents to the office with the complaint of right-sided rib pain when he runs long distances. Physical examination reveals normal heart and lung findings and an exhalation dysfunction at ribs 4-5 on the right. Which of the following muscles or muscle groups will be most useful in correcting this dysfunction utilizing a direct method?
What of the following is the right choice? Explain your answer.
(A) anterior scalene
(B) latissimus dorsi
(C) pectoralis minor
(D) quadratus lumborum
Solution:
The correct answer is **(C) pectoralis minor**. 

**Explanation:**  
The patient presents with an exhalation dysfunction at ribs 4-5 on the right, meaning these ribs are likely restricted in their ability to depress during exhalation. The **pectoralis minor** attaches directly to the 3rd, 4th, and 5th ribs and plays a role in rib elevation during inhalation when the scapula is stabilized. If this muscle is hypertonic or shortened, it can restrict the downward movement of ribs 4-5 during exhalation. Using a **direct method** (e.g., muscle energy techniques, stretching, or inhibition) to release the pectoralis minor would address the restriction, allowing proper rib depression during exhalation. 

Other options are less relevant:  
- **(A) Anterior scalene** primarily affects the 1st rib (not 4-5).  
- **(B) Latissimus dorsi** acts on lower ribs (9-12) and is less involved in upper rib mechanics.  
- **(D) Quadratus lumborum** influences the 12th rib and lumbar spine, not mid-thoracic ribs.  

Thus, targeting the **pectoralis minor** directly addresses the dysfunctional ribs 4-5.

Final Answer: The final answer is (C). I hope it is correct."""

class MMLUProfessionalMedicine(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
