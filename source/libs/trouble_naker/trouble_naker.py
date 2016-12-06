import random
from operator import attrgetter

class QuestionState:
    def __init__(self, label: str, states: list, answer: str, state_value: float):
        self.label = label
        self.states = states
        self.answer = answer
        self.state_value = state_value

    def check_state(self, check_states: list):
        return self.states == check_states


class TroubleNaker:
    questions_master_table = ["あなたは男ですか", "イケメンですか", "年収700万以上ありますか", "夢はありますか", "好きな人はいますか"]
    choices_master_table = [True, False]
    answers_master_table = ["結婚できない", "年収が低い", "女が嫌い"]

    def __init__(self):
        self.user_answers = []

    def game_start(self):
        while True:
            q_a = {"question": '', "answer": ''}
            q_a["question"] = TroubleNaker.Questions[random.randint(0, len(TroubleNaker.Questions))] if len(self.user_answers) == 0 else "次の質問です"
            print(q_a["question"])

            user_input = input()
            q_a["answer"] = True if user_input == 'y' else False







if __name__ == '__main__':


    # values["state1"] = QuestionState(label="state1", states=state1, answer="モテない", state_value=0.90)
    # values["state2"] = QuestionState(label="state2", states=state2, answer="早く子供欲しい", state_value=0.891)
    # values["state3"] = QuestionState(label="state3", states=state3, answer="早く作曲したい", state_value=0.512)
    # values["state4"] = QuestionState(label="state4", states=state4, answer="早く子供欲しい", state_value=0.2)
    #
    # for (key, value) in values.items():
    #     print(value)
    #     print(key)
    #
    # maybe = [value for (key, value) in values.items() if value.check_state(user)]
    #
    # maybe = max(maybe, key=attrgetter("state_value"))
    #
    # print(maybe.label)
    #
    # if maybe.state_value >= 0.90:
    #     #別の質問をする => 同じ質問+回答セットを「含み」、1-deltaの確率で最もvalueの高いもの、deltaの確率でランダムに選択する
    #     #将来的にはベイズ推定を用いる
    #     print("別の質問")
    # else:
    #     #回答を表示する
    #     print(maybe.label)
    #
    #
    #
    #
    #


