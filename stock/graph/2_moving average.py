# -*- coding: utf-8 -*-
"""
이동 평균선
5, 20, 60, 120 동안의 수정 종가의 주가의 이동 평균치
각각의 5, 20, 60, 120일의 그래프가 교차하는 부분을 크로스라 한다. (매매시점)
"""
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt


class Stock:
    def get_stock_from_yahoo(self, start, end, code):
        return web.DataReader(code, 'yahoo', start, end)

    def moving_average(self, gs, date=5):
        return gs['Close'].rolling(window=date).mean()

    def stock_close_graph(self, gs):
        """
        종가 그래프
        :return:
        """

        plt.plot(gs.index, gs['Close'], label="Close")
        plt.plot(gs.index, gs['MA5'], label="MA5")
        plt.plot(gs.index, gs['MA20'], label="MA20")
        plt.plot(gs.index, gs['MA60'], label="MA60")
        plt.plot(gs.index, gs['MA120'], label="MA120")
        plt.legend(loc='best')
        plt.grid()
        plt.show()


if __name__ == '__main__':
    s = Stock()

    start = datetime.datetime(2014, 1, 1)
    end = datetime.datetime(2016, 3, 6)
    gs = s.get_stock_from_yahoo(start, end, "078930.KS")

    ma5 = s.moving_average(gs, 5)
    ma20 = s.moving_average(gs, 20)
    ma60 = s.moving_average(gs, 60)
    ma120 = s.moving_average(gs, 120)

    #print(ma5.tail(10))

    # 칼럼 추가 이동평균치 5 ~ 120
    gs['MA5'] = ma5
    gs['MA20'] = ma20
    gs['MA60'] = ma60
    gs['MA120'] = ma120

    print(gs.tail())


    s.stock_close_graph(gs)




