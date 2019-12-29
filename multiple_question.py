from cla_question import *

question_prompts = [
    'What is the best brower? \n(a)Google\n(b)Firefox\n(c)360brower\n(d)Internet explorer\n\n',
    'What is the best search engine?\n(a)Baidu\n(b)Google\n(c)Bing\n\n',
    'What is the most useful tool for people in China mainland to explore the Internet with science?\n(a)Ghelper\n(b)GAH\n\n'
]

questions = [
    Questions(question_prompts[0], 'a'),
    Questions(question_prompts[1], 'b'),
    Questions(question_prompts[2], 'a')
]


def run_test():
    for question in questions:
        while True:
            answer = input(question.prompt)
            if answer == question.answer:
                if question==questions[len(questions)-1]:
                    print('get all right! Congratulations!')
                else:
                    print('get right,enter next question!')
                break
            else:
                print('get wrong,please try again!')


run_test()
