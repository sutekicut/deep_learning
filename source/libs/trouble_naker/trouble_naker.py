import random

class TroubleNaker:
    Questions = ['あなたは男ですか?', 'イケメンですか', '年収700万以上ありますか', '夢はありますか']
    Troubles = ['モテない', '早く子供欲しい', '早く作曲したい']
    Answers = ['はい', 'どちらでもない', 'いいえ']

    def __init__(self):
        self.user_answers = []
