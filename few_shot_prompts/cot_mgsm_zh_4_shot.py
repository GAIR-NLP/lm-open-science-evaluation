from .few_shot_prompting import FewShotPrompting


few_shot_prompt = """
问题：罗杰有5个网球。他又买了2罐网球。每罐有3个网球。他现在有多少个网球？
答案：罗杰一开始有5个球。2罐各3个网球就是6个网球。5+6=11。所以答案是：11。


问题：服务器机房里有九台电脑。从周一到周四，每天又安装了五台电脑。服务器机房里现在有多少台电脑？
答案：从周一到周四有4天。每天增加5台电脑。这意味着一共增加了4×5=20台电脑。一开始有9台电脑，所以现在有9+20=29台电脑。所以答案是：29。


问题：利亚有32块巧克力，她妹妹有42块。如果她们吃了35块，她们一共还剩下多少块？
答案：利亚有32块巧克力，利亚的妹妹有42块。这意味着原来有32+42=74块巧克力。35块被吃掉了。所以她们一共还剩74-35=39块巧克力。所以答案是：39。


问题：肖恩有五个玩具。圣诞节他从他爸爸妈妈那里各得到了两个玩具。他现在有多少个玩具？
答案：他有5个玩具。他从妈妈那里得到了2个，所以之后他有5+2=7个玩具。然后他又从爸爸那里得到了2个，所以他一共拥有7+2=9个玩具。所以答案是：9。
""".strip()


class CoTMGSMZHPrompt4Shot(FewShotPrompting):
    def __init__(self):
        super().__init__()

    def format_prompt(self, task_input, task_output):
        prompt = f"{few_shot_prompt}\n\n\n问题：{task_input}\n答案：{task_output}"
        return prompt.rstrip()

    def stop_words(self):
        return ["\n问题："]
