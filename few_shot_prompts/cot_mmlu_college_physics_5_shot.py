from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
A refracting telescope consists of two converging lenses separated by 100 cm. The eye-piece lens has a focal length of 20 cm. The angular magnification of the telescope is
What of the following is the right choice? Explain your answer.
(A) 4
(B) 5
(C) 6
(D) 20
Solution:
To determine the angular magnification of a refracting telescope, we apply the formula M = f_o/f_e, where f_o and f_e represent the focal lengths of the objective and eyepiece lenses respectively. Given information: the lenses are separated by 100 cm, and the eyepiece focal length is 20 cm. For a telescope adjusted for normal viewing (final image at infinity), the separation equals the sum of the focal lengths (f_o + f_e = 100 cm). Substituting the known eyepiece focal length, we get f_o + 20 = 100, which yields f_o = 80 cm. Computing the angular magnification directly using our formula: M = 80/20 = 4. Therefore, the angular magnification of this telescope is 4 (Option A).
Final Answer: The final answer is (A). I hope it is correct.

Problem:
For which of the following thermodynamic processes is the increase in the internal energy of an ideal gas equal to the heat added to the gas?
What of the following is the right choice? Explain your answer.
(A) Constant temperature
(B) Constant volume
(C) Constant pressure
(D) Adiabatic
Solution:
The first law of thermodynamics (ΔU = Q - W) guides our analysis of which process allows all heat to increase internal energy. In an ideal gas, internal energy depends only on temperature (ΔU = nCvΔT). Examining each process: during isothermal processes (A), temperature remains constant, so ΔU = 0 and heat equals work (Q = W), making this incorrect; in isochoric processes (B), volume remains constant, so no work is done (W = 0), meaning ΔU = Q - 0 = Q, thus all heat increases internal energy; for isobaric processes (C), volume changes produce work, so Q = ΔU + W, meaning not all heat contributes to internal energy; in adiabatic processes (D), no heat transfer occurs (Q = 0), so ΔU = -W, which doesn't satisfy our criterion. Therefore, constant volume (B) is correct as it's the only condition where all heat added directly increases the gas's internal energy.
Final Answer: The final answer is (B). I hope it is correct.

Problem:
One end of a Nichrome wire of length 2L and cross-sectional area A is attached to an end of another Nichrome wire of length L and cross- sectional area 2A. If the free end of the longer wire is at an electric potential of 8.0 volts, and the free end of the shorter wire is at an electric potential of 1.0 volt, the potential at the junction of the two wires is most nearly equal to
What of the following is the right choice? Explain your answer.
(A) 2.4 V
(B) 3.3 V
(C) 4.5 V
(D) 5.7 V
Solution:
To find the potential at the junction of two Nichrome wires in series, we calculate and compare their resistances, determining the voltage division. For the longer wire with length 2L and area A, resistance R₁ = ρ(2L/A), while the shorter wire with length L and area 2A has resistance R₂ = ρ(L/2A), giving a ratio R₁/R₂ = 4. With total resistance R_total = 5R₂ across a 7.0V potential difference (8.0V - 1.0V), the current becomes I = 7.0V/5R₂. The voltage drop across R₁ equals I·R₁ = (7.0V/5R₂)·4R₂ = 5.6V, making the junction potential 8.0V - 5.6V = 2.4V. We can verify this using the voltage divider formula: V_junction = (V_high·R₂ + V_low·R₁)/(R₁ + R₂) = (8.0V·R₂ + 1.0V·4R₂)/5R₂ = 12R₂/5R₂ = 2.4V.
Final Answer: The final answer is (A). I hope it is correct.

Problem:
A refracting telescope consists of two converging lenses separated by 100 cm. The eye-piece lens has a focal length of 20 cm. The angular magnification of the telescope is
What of the following is the right choice? Explain your answer.
(A) 4
(B) 5
(C) 6
(D) 20
Solution:
To determine the angular magnification of a refracting telescope, I'll use the formula M = f_o/f_e where f_o and f_e are the focal lengths of the objective and eyepiece lenses respectively. Given that the lenses are separated by 100 cm and the eyepiece focal length is 20 cm, I can calculate that the objective lens focal length must be f_o = 100 - 20 = 80 cm (since in an ideal telescope, the separation equals the sum of focal lengths). Applying the magnification formula yields M = 80/20 = 4, making the correct answer (A) 4.
Final Answer: The final answer is (A). I hope it is correct.

Problem:
The muon decays with a characteristic lifetime of about 10^-6 second into an electron, a muon neutrino, and an electron antineutrino. The muon is forbidden from decaying into an electron and just a single neutrino by the law of conservation of
What of the following is the right choice? Explain your answer.
(A) charge
(B) mass
(C) energy and momentum
(D) lepton number
Solution:
The muon decay process must follow lepton number conservation, which requires preservation of both total lepton count and individual lepton family numbers. A hypothetical decay of μ⁻ → e⁻ + ν would violate this principle since the initial state contains a muon (muon family lepton number +1) while the final state includes an electron (electron family lepton number +1), leaving no viable configuration for a single neutrino that could simultaneously balance both family numbers. The correct decay pattern must include an electron antineutrino (ν̄ₑ, electron family lepton number -1) and a muon neutrino (νμ, muon family lepton number +1), yielding μ⁻ → e⁻ + ν̄ₑ + νμ, which preserves both total lepton number and respective family numbers. Alternative explanations based on charge conservation (option A), mass conservation (option B), or energy/momentum conservation (option C) are insufficient constraints, as these principles could theoretically be satisfied by simpler decay patterns; only lepton number conservation (option D) mandates the three-particle outcome observed in nature.
Final Answer: The final answer is (D). I hope it is correct."""

class MMLUCollegePhysics(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
