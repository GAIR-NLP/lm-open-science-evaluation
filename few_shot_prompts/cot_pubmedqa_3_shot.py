from .few_shot_prompting import FewShotPrompting

# training set the first 5 data
few_shot_prompt = """Given the following information and a question, analyze the information step by step using your internal knowledge. Consider all relevant details before arriving at an answer. The final response should only be one of [yes, no, maybe].
Information:
- To assess quality of storage of vaccines in the community.
- Questionnaire survey of general practices and child health clinics, and monitoring of storage temperatures of selected refrigerators.
- Central Manchester and Bradford health districts.
- 45 general practices and five child health clinics, of which 40 (80%) responded. Eight practices were selected for refrigeration monitoring.
- Adherence to Department of Health guidelines for vaccine storage, temperature range to which vaccines were exposed over two weeks.
- Of the 40 respondents, only 16 were aware of the appropriate storage conditions for the vaccines; eight had minimum and maximum thermometers but only one of these was monitored daily. In six of the eight practices selected for monitoring of refrigeration temperatures the vaccines were exposed to either subzero temperatures (three fridges) or temperatures up to 16 degrees C (three). Two of these were specialised drug storage refrigerators with an incorporated thermostat and external temperature gauges.

Question:
Storage of vaccines in the community: weak link in the cold chain?
Solution:
Vaccines were exposed to temperatures that may reduce their potency. Safe storage of vaccines in the clinics cannot be ensured without adhering to the recommended guidelines. Provision of adequate equipment and training for staff in maintaining the "cold chain" and the use and care of equipment are important components of a successful immunisation programme.
Final Answer: The final answer is (maybe). I hope it is correct.

Given the following information and a question, analyze the information step by step using your internal knowledge. Consider all relevant details before arriving at an answer. The final response should only be one of [yes, no, maybe].
Information:
- To assess the acceptability to patients of the use of patients' first names by doctors and doctors' first names by patients in general practice.
- An administered questionnaire survey.
- 5 General practices in Lothian.
- 475 Patients consulting 30 general practitioners.
- Response by patients to questionnaire on attitude to use of first names.
- Most of the patients either liked (223) or did not mind (175) being called by their first names. Only 77 disliked it, most of whom were aged over 65. Most patients (324) did not, however, want to call the doctor by his or her first name.

Question:
Should general practitioners call patients by their first names?
Solution:
General practitioners should consider using patients' first names more often, particularly with younger patients.
Final Answer: The final answer is (yes). I hope it is correct.

Given the following information and a question, analyze the information step by step using your internal knowledge. Consider all relevant details before arriving at an answer. The final response should only be one of [yes, no, maybe].
Information:
- The accepted treatment protocol for necrotizing fasciitis (NF) consists of extensive surgery and wide spectrum antibiotics. Hyperbaric oxygenation (HBO) has been recommended as adjuvant therapy for NF, improving patient mortality and outcome. However, the beneficial effect of HBO for NF remains controversial.
- A retrospective evaluation of treatment outcome in 37 patients treated for NF between 1984 and 1993 was carried out. The mortality rate, morbidity criteria, and risk factors for grave prognosis were compared between a group of 25 patients who received HBO as part of their treatment protocol and a group of the remaining 12 patients treated by surgical excision and antibiotics alone.
- The two groups were found to be similar with regard to age, gender, the incidence of individual risk factors for ominous prognosis, and the Acute Physiology and Chronic Health Evaluation (APACHE) II score for disease's severity on presentation. The mortality rate among the HBO-treated patients was 36%, as opposed to 25% in the non-HBO group. The mean number of surgical débridements required per patient was significantly higher in the HBO group: 3.3 compared with 1.5 in the non-HBO-treated patients. Although the average length of hospitalization for survivors was shorter for the HBO group, the difference between the groups did not reach statistical significance.

Question:
Necrotizing fasciitis: an indication for hyperbaric oxygenation therapy?
Solution:
The results of this study cast doubt on the suggested advantage of HBO in reducing patient mortality and morbidity when used as adjuvant therapy for NF.
Final Answer: The final answer is (no). I hope it is correct."""

class PubMedQAPrompt(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
