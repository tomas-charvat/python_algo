
from backtesting.lib import crossover
from backtesting.test import SMA
import pandas as pd

from backtesting import Strategy, Backtest



class Gold_5min_Strategy(Strategy):
    SMA1=20
    SMA2=50
    SMA3=200
    tp_price=2.0
    sl_price=2.0


    def init(self):
        self.tp_price=self.tp_price
        self.sl_price=self.sl_price
        self.SMA1 = self.I(SMA,self.data.Close,self.SMA1)
        self.SMA2 = self.I(SMA,self.data.Close,self.SMA2)
        self.SMA3 = self.I(SMA,self.data.Close,self.SMA3)


    def next(self):

        current_price = float(self.data.Close[-1])

        if crossover(self.SMA1,self.SMA2):
            if current_price > self.SMA3:
                if self.position.is_short:
                    self.position.close()


                tp_price = current_price+self.tp_price
                sl_price = current_price-self.sl_price
                self.buy(sl=sl_price,tp=tp_price,size=0.2)



        elif crossover(self.SMA2,self.SMA1):
            if current_price < self.SMA3:
                if self.position.is_long:
                    self.position.close()




            tp_price = current_price-self.tp_price
            sl_price = current_price+self.sl_price

            self.sell(sl=sl_price,tp=tp_price,size=0.2)



if __name__ == '__main__':

    gold_data=pd.read_csv('gold_5m_data2.csv')


    #gold_data.columns=['Close','High','Low','Open','Volume']
    gold_data.reset_index(drop=True, inplace=True)
    gold_data['Datetime']=pd.to_datetime(gold_data['Datetime'])
    gold_data.set_index('Datetime',inplace=True)
    print(gold_data.head())
    print(gold_data.info())

    bt=Backtest(gold_data[0:10000],Gold_5min_Strategy,cash=10_000,commission=0.001)


    def constraints(params: dict) -> bool:
        return params['SMA1']<params['SMA2']<params['SMA3']


    stats=bt.optimize(
        tp_price=range(1,5,1),
        sl_price=range(1,5,1),
        SMA1=range(5,50,5),
        SMA2=range(20,100,10),
        SMA3=range(50,300,20),
        maximize= 'Sharpe Ratio',
        constraint= constraints,
         max_tries=1000
    )

    print(stats)
    bt.plot()




