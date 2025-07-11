from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
Which of the following conditions will ensure that angular momentum is conserved? I. Conservation of linear momentum II. Zero net external force III. Zero net external torque
What of the following is the right choice? Explain your answer.
(A) I and II only
(B) I and III only
(C) II and III only
(D) III only
Solution:
To determine which condition(s) ensure angular momentum conservation, we must examine the fundamental principle that angular momentum L is conserved when no net external torque acts on a system (expressed mathematically as dL/dt = τₑₓₜ, where conservation occurs if τₑₓₜ = 0). Analyzing each condition: Conservation of Linear Momentum (I) does not guarantee angular momentum conservation since these quantities are independent—external forces could still generate torques even if they sum to zero; Zero Net External Force (II) similarly ensures only linear momentum conservation but doesn't prevent torques created by forces acting at different points; Zero Net External Torque (III) directly satisfies our conservation criterion by definition. Therefore, only condition III guarantees angular momentum conservation, making the answer (D) III only.
Final Answer: The final answer is (D). I hope it is correct.

Problem:
A pipe full of air is closed at one end. A standing wave is produced in the pipe, causing the pipe to sound a note. Which of the following is a correct statement about the wave’s properties at the closed end of the pipe?
What of the following is the right choice? Explain your answer.
(A) The pressure is at a node, but the particle displacement is at an antinode.
(B) The pressure is at an antinode, but the particle displacement is at a node.
(C) The pressure and the particle displacement are both at nodes.
(D) The pressure and the particle displacement are both at antinodes.
Solution:
A standing wave in a one-end-closed pipe creates specific boundary conditions where particle displacement and pressure variation are complementary. At the closed end, air particles cannot move (displacement node) but pressure can fluctuate maximally (pressure antinode), while at the open end, air moves freely (displacement antinode) but pressure remains constant at atmospheric level (pressure node). This inverse relationship means that at the closed end specifically, pressure variation reaches its maximum (antinode) while particle displacement is zero (node), confirming option (B) as correct.
Final Answer: The final answer is (B). I hope it is correct.

Problem:
A photocell of work function ϕ = 2eV is connected to a resistor in series. Light of frequency f = 1 × 10^15 Hz hits a metal plate of the photocell. If the power of the light is P = 100 W, what is the current through the resistor?
What of the following is the right choice? Explain your answer.
(A) 2:00 AM
(B) 6:00 AM
(C) 12:00 AM
(D) 24 A
Solution:
To find the current through the resistor, I first calculated the energy of a single photon using E = hf, where h = 6.626 × 10^-34 J·s and f = 1 × 10^15 Hz, yielding E = 6.626 × 10^-19 J or 4.14 eV. Next, I determined the maximum kinetic energy of emitted electrons using the photoelectric equation Kₘₐₓ = E - φ, where φ = 2 eV is the work function, giving Kₘₐₓ = 2.14 eV. Then, I found the number of emitted electrons per second by dividing the power P = 100 W by the photon energy, N = P/E = 1.51 × 10^20 electrons per second. Finally, I calculated the current using I = Ne, where e = 1.6 × 10^-19 C is the electron charge, resulting in I = 24.16 A ≈ 24 A.
Final Answer: The final answer is (D). I hope it is correct.

Problem:
A microwave oven is connected to an outlet, 120 V, and draws a current of 2 amps. At what rate is energy being used by the microwave oven?
What of the following is the right choice? Explain your answer.
(A) 10 W
(B) 30 W
(C) 60 W
(D) 240 W
Solution:
To determine the microwave's energy usage, we start with the power formula P = V × I, where P is power in watts, V is voltage in volts, and I is current in amperes. Given values of V = 120V and I = 2A, we simply multiply these quantities: P = 120V × 2A = 240W. Therefore, the microwave uses energy at a rate of 240 watts, corresponding to answer choice (D).
Final Answer: The final answer is (D). I hope it is correct.

Problem:
A point charge, Q = +1 mC, is fixed at the origin. How much work is required to move a charge, Q = +8 µC, from the point (0, 4 meters) to the point (3 meters, 0)?
What of the following is the right choice? Explain your answer.
(A) 3.5 J
(B) 6.0 J
(C) 22.5 J
(D) 40 J
Solution:
To determine the work required to move a charge q = +8 μC from point A(0, 4 m) to point B(3, 0) in the electric field of a source charge Q = +1 mC at the origin, we apply the formula W = q(VB - VA), where V represents electric potential. First, we calculate the potentials at both points using V = kQ/r: at point A, with rA = 4 m, VA = (9.0×10⁹)(1.0×10⁻³)/4 = 2.25×10⁶ V; at point B, with rB = 3 m, VB = (9.0×10⁹)(1.0×10⁻³)/3 = 3.0×10⁶ V. We then find the potential difference ΔV = VB - VA = 0.75×10⁶ V. Finally, multiplying this by the charge q = 8.0×10⁻⁶ C yields W = (8.0×10⁻⁶)(0.75×10⁶) = 6.0 J, so the answer is (B) 6.0 J.
Final Answer: The final answer is (B). I hope it is correct."""

class MMLUHighSchoolPhysics(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
