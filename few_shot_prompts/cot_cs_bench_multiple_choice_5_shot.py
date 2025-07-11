from .few_shot_prompting import FewShotPrompting

# dev set
few_shot_prompt = """Problem:
Given a one-dimensional array with n elements, the minimum time complexity to create a sorted singly linked list is ( ).
What of the following is the right choice? Explain your answer.
(A) O(1)
(B) O(n)
(C) O(n^2)
(D) O(nlog₂n)
Solution:
If a linked list is created first and then elements are inserted sequentially to establish an ordered list, each insertion requires traversing the linked list to find the insertion position, which is essentially straight insertion sort with a time complexity of O(n). If the array is sorted first and then the linked list is created, the time complexity of creating the linked list is O(n), and the best time complexity for array sorting is O(nlog2n), resulting in a total time complexity of O(nlog2n). Therefore, option D is selected.
Final Answer: The final answer is (D). I hope it is correct.

Problem:
In a doubly linked list storage structure, when deleting the node pointed to by P, it is necessary to modify the pointers ().
What of the following is the right choice? Explain your answer.
(A) p->llink->rlink = p->rlink; p->rlink->llink = p->llink;
(B) p->link = p->llink->1link; p->llink->rlink = p;
(C) p->rlink->llink = p; p->rlink = p->rlink->rlink;
(D) p->rlink = p->llink->llink; p->llink = p->rlink->rlink;
Solution:
This task simply involves deleting a node, ensuring to link the previous and next nodes of P together. The key is to maintain the integrity of the chain during the modification of the node pointers!
Final Answer: The final answer is (A). I hope it is correct.

Problem:
The \"first in, first out\" characteristic of a queue refers to ().\nⅠ. The last element inserted into the queue is always the last to be deleted\nⅡ. When insertion and deletion operations occur simultaneously, the insertion operation always takes precedence\nⅢ. Whenever there is a deletion operation, an insertion operation must be performed first\nⅣ. The element deleted from the queue is always the one that was inserted earliest
What of the following is the right choice? Explain your answer.
(A) Ⅰ
(B) Ⅰ and Ⅳ
(C) Ⅱ and Ⅲ
(D) Ⅳ
Solution:
The characteristic of a queue being \"first in, first out\" is reflected in the fact that elements that enter the queue first will leave the queue first, while elements that enter the queue later will leave the queue later. Entering the queue corresponds to an insertion operation, and leaving the queue corresponds to a deletion operation. Both Ⅰ and Ⅳ are correct.
Final Answer: The final answer is (B). I hope it is correct.

Problem:
In a linked queue, assuming the front pointer is 'front' and the rear pointer is 'rear', the operation required to enqueue the element pointed to by x is ().
What of the following is the right choice? Explain your answer.
(A) front=x, front->next
(B) x->next = front->next; front = x
(C) rear->next = x; rear = x;
(D) rear->next = x, x->next = null, rear = x
Solution:
During the insertion operation, first insert node x at the end of the linked list, and then make rear point to this node x. The approach in C is not rigorous enough, because it is the end of the queue, so the tail x->next must be set to NULL.
Final Answer: The final answer is (D). I hope it is correct.

Problem:
Assuming the base of the floating-point number is 4 and the mantissa is represented in true form, then the following ( ) is a normalized number.
What of the following is the right choice? Explain your answer.
(A) 1.001101
(B) 0.001101
(C) 1.011011
(D) 0.00001
Solution:
The normalized fraction represented in true form has two digits after the decimal point (with a base of 4, using two digits to represent a non-zero fraction).
Final Answer: The final answer is (A). I hope it is correct."""

class CSBenchMultipleChoice(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\nProblem:\n{task_input}\nSolution:\n{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\nProblem:"]
