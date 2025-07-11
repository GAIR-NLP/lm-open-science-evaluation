from .few_shot_prompting import FewShotPrompting

# dev: 1, 2, 4, 5, 6
few_shot_prompt = """Problem:
A 21-year-old sexually active male complains of fever, pain during urination, and inflammation and pain in the right knee. A culture of the joint fluid shows a bacteria that does not ferment maltose and has no polysaccharide capsule. The physician orders antibiotic therapy for the patient. The mechanism of action of action of the medication given blocks cell wall synthesis, which of the following was given?
What of the following is the right choice? Explain your answer.
(A) Chloramphenicol
(B) Gentamicin
(C) Ciprofloxacin
(D) Ceftriaxone
(E) Trimethoprim
Solution:
Let me solve this step by step:

1. First, let's analyze the patient's symptoms:
   - 21-year-old sexually active male
   - Fever
   - Dysuria (pain during urination)
   - Right knee inflammation and pain
   - Bacterial culture shows:
     * No maltose fermentation
     * No polysaccharide capsule

2. These symptoms and bacterial characteristics strongly suggest Neisseria gonorrhoeae infection (gonorrhea):
   - The bacteria is non-maltose fermenting
   - Common in young sexually active individuals
   - Can cause disseminated gonococcal infection (DGI) with joint involvement
   - N. gonorrhoeae lacks a polysaccharide capsule

3. The question asks for an antibiotic that blocks cell wall synthesis. Let's analyze each option:

   - Chloramphenicol: Inhibits protein synthesis
   - Gentamicin: Inhibits protein synthesis
   - Ciprofloxacin: Inhibits DNA gyrase
   - Ceftriaxone: Blocks cell wall synthesis (β-lactam antibiotic)
   - Trimethoprim: Inhibits folic acid synthesis

4. The correct answer is (D) Ceftriaxone because:
   - It's a third-generation cephalosporin that blocks cell wall synthesis
   - It's the current first-line treatment for gonorrhea
   - It has excellent penetration into joint spaces
   - It's highly effective against N. gonorrhoeae
   - It matches the mechanism of action mentioned in the question (cell wall synthesis inhibition)

Final Answer: The final answer is (D). I hope it is correct.

Problem:
A 5-year-old girl is brought to the emergency department by her mother because of multiple episodes of nausea and vomiting that last about 2 hours. During this period, she has had 6–8 episodes of bilious vomiting and abdominal pain. The vomiting was preceded by fatigue. The girl feels well between these episodes. She has missed several days of school and has been hospitalized 2 times during the past 6 months for dehydration due to similar episodes of vomiting and nausea. The patient has lived with her mother since her parents divorced 8 months ago. Her immunizations are up-to-date. She is at the 60th percentile for height and 30th percentile for weight. She appears emaciated. Her temperature is 36.8°C (98.8°F), pulse is 99/min, and blood pressure is 82/52 mm Hg. Examination shows dry mucous membranes. The lungs are clear to auscultation. Abdominal examination shows a soft abdomen with mild diffuse tenderness with no guarding or rebound. The remainder of the physical examination shows no abnormalities. Which of the following is the most likely diagnosis?
What of the following is the right choice? Explain your answer.
(A) Cyclic vomiting syndrome
(B) Gastroenteritis
(C) Hypertrophic pyloric stenosis
(D) Gastroesophageal reflux disease
(E) Acute intermittent porphyria
Solution:
Let's analyze this case step by step:

Key Clinical Features:
1. 5-year-old girl with episodic nausea and vomiting
2. Episodes last about 2 hours with 6-8 episodes of bilious vomiting
3. Preceded by fatigue
4. Asymptomatic between episodes
5. Multiple hospitalizations for dehydration
6. Recent parental divorce (psychosocial stressor)
7. Physical exam shows signs of dehydration but otherwise normal
8. No fever or other signs of infection

The most likely diagnosis is (A) Cyclic Vomiting Syndrome (CVS). Here's why:

1. Pattern of symptoms:
- Recurrent episodes of intense vomiting
- Well-defined episodes with symptom-free intervals
- Stereotypical pattern (preceded by fatigue)
- No other underlying cause identified

2. Age and timing:
- Common in school-age children
- Often triggered by psychological stressors (divorce in this case)

3. Why other options are less likely:
- Gastroenteritis (B): Would typically have diarrhea, fever, and continuous symptoms rather than episodic
- Hypertrophic pyloric stenosis (C): Occurs in infants 2-6 weeks old, not in 5-year-olds
- GERD (D): Would have more continuous symptoms, not episodic severe vomiting
- Acute intermittent porphyria (E): Rare in children, would have neurological symptoms and abdominal pain as predominant features

CVS is often associated with:
- Psychological stressors (parental divorce in this case)
- Multiple ED visits/hospitalizations
- Dehydration during episodes
- Normal physical exam between episodes

Treatment involves:
1. Supportive care during episodes
2. Prophylactic medications
3. Trigger avoidance
4. Psychological support

Therefore, (A) Cyclic Vomiting Syndrome is the most likely diagnosis given the age, presentation pattern, and clinical features.
Final Answer: The final answer is (A). I hope it is correct.

Problem:
A 37-year-old female with a history of type II diabetes mellitus presents to the emergency department complaining of blood in her urine, left-sided flank pain, nausea, and fever. She also states that she has pain with urination. Vital signs include: temperature is 102 deg F (39.4 deg C), blood pressure is 114/82 mmHg, pulse is 96/min, respirations are 18, and oxygen saturation of 97% on room air. On physical examination, the patient appears uncomfortable and has tenderness on the left flank and left costovertebral angle. Which of the following is the next best step in management?
What of the following is the right choice? Explain your answer.
(A) Obtain an abdominal CT scan
(B) Obtain blood cultures
(C) Obtain a urine analysis and urine culture
(D) Begin intravenous treatment with ceftazidime
(E) No treatment is necessary
Solution:
Let's think through this step by step:

1. Key Symptoms and Signs:
- Blood in urine (hematuria)
- Left flank pain
- Costovertebral angle tenderness
- Fever (102°F)
- Dysuria (pain with urination)
- Nausea

2. Risk Factors:
- Type II diabetes mellitus (increased risk for infections)

3. Pattern Recognition:
- This constellation of symptoms strongly suggests pyelonephritis (kidney infection)
- Classic triad: flank pain, fever, and costovertebral angle tenderness

4. Analyzing Options:
(A) CT scan - While useful to rule out complications, not the first step
(B) Blood cultures - Important but not the initial step
(C) Urinalysis and culture - This is essential for diagnosis and guiding treatment
(D) IV ceftazidime - Premature without confirming infection and susceptibilities
(E) No treatment - Inappropriate given severe symptoms

The correct answer is (C) Obtain a urinalysis and urine culture.

Explanation:
- A urinalysis and culture is the crucial first step because it:
  1. Confirms the diagnosis
  2. Identifies the causative organism
  3. Determines antibiotic susceptibilities
  4. Guides appropriate antibiotic therapy
  5. Is less expensive and invasive than other options

While blood cultures and antibiotics will likely be needed, and a CT scan might be indicated if complications are suspected, obtaining a urine sample for analysis and culture should be the first step in management. This allows for targeted therapy based on culture results while other supportive measures are initiated.

Additionally, in a diabetic patient where infection patterns can be more complex, having culture data is particularly important for appropriate antibiotic selection.
Final Answer: The final answer is (C). I hope it is correct.

Problem:
A 19-year-old boy presents with confusion and the inability to speak properly. The patient's mother says that, a few hours ago, she noticed a change in the way he talked and that he appeared to be in a daze. He then lost consciousness, and she managed to get him to the hospital. She is also concerned about the weight he has lost over the past few months. His blood pressure is 80/55 mm Hg, pulse is 115/min, temperature is 37.2°C (98.9°F), and respiratory rate is 18/min. On physical examination, the patient is taking rapid, deep breaths, and his breath has a fruity odor. Dry mucous membranes and dry skin are noticeable. He is unable to cooperate for a mental status examination. Results of his arterial blood gas analysis are shown.\nPco2 16 mm Hg\nHCO3–  10 mEq/L\nPo2 91 mm Hg\npH 7.1\nHis glucose level is 450 mg/dL, and his potassium level is 4.1 mEq/L. Which of the following should be treated first in this patient?
What of the following is the right choice? Explain your answer.
(A) Hypoperfusion
(B) Hyperglycemia
(C) Metabolic acidosis
(D) Hypokalemia
(E) Hypophosphatemia
Solution:
Let's solve this step by step.

1) First, let's analyze the patient's presentation:
   * Young adult with confusion and speech problems
   * Recent weight loss
   * Low blood pressure (80/55)
   * Tachycardia (115/min)
   * Kussmaul breathing (rapid, deep breaths)
   * Fruity breath odor
   * High glucose (450 mg/dL)
   * Acidotic pH (7.1)

2) This clinical picture strongly suggests Diabetic Ketoacidosis (DKA)

3) Looking at the treatment options:
   * (A) Hypoperfusion - manifested by low BP and tachycardia
   * (B) Hyperglycemia - glucose 450 mg/dL
   * (C) Metabolic acidosis - pH 7.1, low HCO3-
   * (D) Hypokalemia - K+ is actually normal at 4.1
   * (E) Hypophosphatemia - not provided in labs

4) The correct answer is (A) Hypoperfusion

Reasoning:
* In DKA, while all these issues need addressing, fluid replacement to treat hypoperfusion is the first priority
* The patient is showing signs of significant volume depletion:
  - Low blood pressure
  - Tachycardia
  - Dry mucous membranes
  - Dry skin

* The ABC (Airway, Breathing, Circulation) principle of emergency medicine dictates that circulation must be addressed first
* Without adequate tissue perfusion, other treatments will be less effective
* IV fluid resuscitation will help:
  - Improve tissue perfusion
  - Lower glucose through dilution
  - Help correct acidosis
  - Improve mental status

While hyperglycemia and acidosis are serious problems, they cannot be effectively treated until circulation is restored. The patient's very low blood pressure (80/55) makes this the most urgent priority.
Final Answer: The final answer is (A). I hope it is correct.

Problem:
A 41-year-old woman presents to her primary care physician with complaints of fatigue and weakness. She denies any personal history of blood clots or bleeding problems in her past, but she says that her mother has had to be treated for breast cancer recently and is starting to wear her down. Her past medical history is significant for preeclampsia, hypertension, polycystic ovarian syndrome, and hypercholesterolemia. She currently smokes 1 pack of cigarettes per day, drinks a glass of wine per day, and currently denies any illicit drug use. Her vital signs include: temperature, 36.7°C (98.0°F); blood pressure, 126/74 mm Hg; heart rate, 111/min; and respiratory, rate 23/min. On physical examination, her pulses are bounding and irregular, complexion is pale, but breath sounds remain clear. On examination, the physician finds diffuse skin pallor and orders a complete blood count. Her laboratory data demonstrate a hematocrit of 27.1%, MCV of 79 fL, and a reticulocyte count of 2.0%. The patient is diagnosed with anemia. Which of the following represents the most likely etiology of her anemia.
What of the following is the right choice? Explain your answer.
(A) Vitamin B12 deficiency
(B) Folate deficiency
(C) Iron deficiency
(D) Infiltrative bone marrow process
(E) Intravascular hemolysis
Solution:
Let's solve this step by step by analyzing the patient's presentation and lab values:

1. Key Patient Information:
- 41-year-old female
- Fatigue and weakness
- Mother with breast cancer (caregiver stress)
- History of preeclampsia and other chronic conditions
- Smoker with daily alcohol use

2. Lab Values Analysis:
- Hematocrit: 27.1% (Low - indicating anemia)
- MCV: 79 fL (Low - indicating microcytic anemia)
- Reticulocyte count: 2.0% (Slightly elevated - indicating bone marrow response)

3. Evaluation of Options:

(C) Iron deficiency is the most likely answer. Here's why:
- The MCV of 79 fL indicates microcytic anemia (normal range 80-100 fL)
- Iron deficiency is the most common cause of microcytic anemia in adults
- The patient has risk factors for iron deficiency:
  * Female of reproductive age
  * History of preeclampsia (which can involve blood loss)
  * The reticulocyte count shows the bone marrow is responding, consistent with iron deficiency

Why the other options are less likely:

(A) Vitamin B12 deficiency
- Causes macrocytic anemia (high MCV), not microcytic
- Would show MCV > 100 fL

(B) Folate deficiency
- Also causes macrocytic anemia
- Would show high MCV, not low

(D) Infiltrative bone marrow process
- Would typically show pancytopenia
- Reticulocyte count would be low, not elevated
- No other symptoms suggesting malignancy

(E) Intravascular hemolysis
- Would show higher reticulocyte count
- Would expect other signs like jaundice or dark urine
- MCV would typically be normal

Therefore, (C) Iron deficiency is the most likely etiology of this patient's anemia given the microcytic picture and her risk factors.
Final Answer: The final answer is (C). I hope it is correct."""

class MEDQAPrompt(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
