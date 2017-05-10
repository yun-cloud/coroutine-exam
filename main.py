def start_exam(fname):
    pass

if __name__ == '__main__':
    fname = 'exam.txt'
    exam = start_exam(fname)
    question = exam.send(None)
    #print(question)
    while question != '---end-of-exam---\n':
        answer = eval(question[:question.find('=')])
        question = exam.send(answer)
        #print(question)
