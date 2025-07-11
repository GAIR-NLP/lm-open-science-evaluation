from .few_shot_prompting import FewShotPrompting

# training set the first 5 data
few_shot_prompt = """Problem:
Chronic urethral obstruction due to benign prismatic hyperplasia can lead to the following change in kidney parenchyma
What of the following is the right choice? Explain your answer.
(A) Hyperplasia
(B) Hyperophy
(C) Atrophy
(D) Dyplasia
Solution:
Chronic urethral obstruction because of urinary calculi, prostatic hyperophy, tumors, normal pregnancy, tumors, uterine prolapse or functional disorders cause hydronephrosis which by definition is used to describe dilatation of renal pelvis and calculus associated with progressive atrophy of the kidney due to obstruction to the outflow of urine Refer Robbins 7yh/9,1012,9/e. P950
Final Answer: The final answer is (C). I hope it is correct.

Problem:
Which vitamin is supplied from only animal source:
What of the following is the right choice? Explain your answer.
(A) Vitamin C
(B) Vitamin B7
(C) Vitamin B12
(D) Vitamin D
Solution:
Ans. (c) Vitamin B12 Ref: Harrison's 19th ed. P 640* Vitamin B12 (Cobalamin) is synthesized solely by microorganisms.* In humans, the only source for humans is food of animal origin, e.g., meat, fish, and dairy products.* Vegetables, fruits, and other foods of nonanimal origin doesn't contain Vitamin B12 .* Daily requirements of vitamin Bp is about 1-3 pg. Body stores are of the order of 2-3 mg, sufficient for 3-4 years if supplies are completely cut off.
Final Answer: The final answer is (C). I hope it is correct.

Problem:
All of the following are surgical options for morbid obesity except -
What of the following is the right choice? Explain your answer.
(A) Adjustable gastric banding
(B) Biliopancreatic diversion
(C) Duodenal Switch
(D) Roux en Y Duodenal By pass
Solution:
Ans. is 'd' i.e., Roux en Y Duodenal Bypass Bariatric surgical procedures include:a. Vertical banded gastroplastyb. Adjustable gastric bandingc. Roux-en Y gastric bypass (Not - Roux-en Y Duodenal Bypass)d. Biliopancreatic diversione. Duodenal switcho The surgical treatment of morbid obesity is known as bariatric surgery.o Morbid obesity is defined as body mass index of 35 kg/m2 or more with obesity related comorbidity, or BMI of 40 kg/m2 or greater without comorbidity.o Bariatric operations produce weight loss as a result of 2 factors. One is restriction of oralintake. The other is malabsorbtion of ingested food.o Gastric restrictive procedures include Vertical banded gastroplasty & Adjustable gastric bandingo Malabsorbtive procedures include Biliopancreatic diversion, and Duodenal switcho Roux-en Y gastric bypass has features of both restriction and malabsorptionBariatric Operations: Mechanism of ActionRestrictiveVertical banded gastroplastyLaparoscopic adjustable gastric bandingLargely Restrictive/Mildly MalabsorptiveRoux-en-Y gastric bypassLargely Malabsorptive/Mildly RestrictiveBiliopancreatic diversionDuodenal switch
Final Answer: The final answer is (D). I hope it is correct.

Problem:
Following endaerectomy on the right common carotid, a patient is found to be blind in the right eye. It is appears that a small thrombus embolized during surgery and lodged in the aery supplying the optic nerve. Which aery would be blocked?
What of the following is the right choice? Explain your answer.
(A) Central aery of the retina
(B) Infraorbital aery
(C) Lacrimal aery
(D) Nasociliary aretry
Solution:
The central aery of the retina is a branch of the ophthalmic aery. It is the sole blood supply to the retina; it has no significant collateral circulation and blockage of this vessel leads to blindness. The branches of this aery are what you view during a fundoscopic exam. Note: The infraorbital aery is a branch of the maxillary aery. It comes through the infraorbital foramen, inferior to the eye. It supplies the maxillary sinus, the maxillary incisors, canine and premolar teeth, and the skin of the cheek below the orbit. The supraorbital aery is another branch of the maxillary aery. It comes through the supraorbital foramen and supplies blood to the muscles, skin and fascia of the forehead. The lacrimal aery is a branch of the ophthalmic aery that supplies the lacrimal gland. The nasociliary aery doesn't exist, but there is a nasociliary nerve that travels with the ophthalmic aery. Ref: Moon D.A., Foreman K.B., Albeine K.H. (2011). Chapter 18. Orbit. In D.A. Moon, K.B. Foreman, K.H. Albeine (Eds), The Big Picture: Gross Anatomy.
Final Answer: The final answer is (A). I hope it is correct.

Problem:
Growth hormone has its effect on growth through?
What of the following is the right choice? Explain your answer.
(A) Directly
(B) IG1-1
(C) Thyroxine
(D) Intranuclear receptors
Solution:
Ans. is 'b' i.e., IGI-1GH has two major functions :-i) Growth of skeletal system :- The growth is mediated by somatomedins (IGF). Increased deposition of cailage (including chondroitin sulfate) and bone with increased proliferation of chondrocytes and osteocytes.ii) Metabolic effects :- Most of the metabolic effects are due to direct action of GH. These include gluconeogenesis, decreased peripheral utilization of glucose (decreased uptake), lipolysis and anabolic effect on proteins.
Final Answer: The final answer is (B). I hope it is correct."""

class MEDMCQAPrompt(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
