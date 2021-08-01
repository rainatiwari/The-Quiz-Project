from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank =[]

# for i in range(len(question_data)):
#   question= Question(question_data[i]["text"],question_data[i]["answer"])
#   question_bank.append(question)
#   print(question_bank[i].question)

for question in question_data:
  question_text = question["text"]
  #print(question_text)
  question_answer = question["answer"]
  new_question = Question(question_text,question_answer)
  question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
  quiz.next_question()

print(f"You have completed the quiz !!!! .\nYour final score is: {quiz.score}/{quiz.question_number}")





