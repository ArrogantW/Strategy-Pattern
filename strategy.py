# -*- coding:utf-8 -*-


# 策略类
class Strategy(object):
    def get_cash(self, cash):
        pass


# 具体策略类之85折子类
class Charge(Strategy):
    def __init__(self, discount=0.85):
        self.discount = discount

    def get_cash(self, cash):
        return cash * self.discount


# 具体策略类之满减子类一
class Reduction1(Strategy):
    def __init__(self, cash_accepted=300, reduction=50):
        self.cash_accepted = cash_accepted
        self.reduction = reduction

    def get_cash(self, cash):
        if cash >= self.cash_accepted:
            return cash - self.reduction
        else:
            print("您不满足该条件")
            return cash


# 具体策略类之满减子类二
class Reduction2(Strategy):
    def __init__(self, cash_accepted=500, reduction=100):
        self.cash_accepted = cash_accepted
        self.reduction = reduction

    def get_cash(self, cash):
        if cash >= self.cash_accepted:
            return cash - self.reduction
        else:
            print("您不满足该条件")
            return cash


# 上下文管理类
class Accept(object):
    def __init__(self, cash_):
        self.cash_ = cash_

    def get_result(self, cash):
        return self.cash_.get_cash(cash)


if __name__ == '__main__':
    command = ''
    while command != 'exit':
        cashes = eval(input("原价: "))
        types = {'85折': Accept(Charge()),
                 '满300减50': Accept(Reduction1()),
                 '满500减100': Accept(Reduction2()),}
        model = input("选择折扣方式: 85折、满300减50、满500减100: ")
        if model in types:
            money = types[model]
            print("需要支付: ", money.get_result(cashes))
        else:
            print("不存在的折扣方式")
        command = input("按下回车键继续或输入exit退出：")