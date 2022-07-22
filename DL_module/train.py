import argparse
from datetime import timedelta
import matplotlib.pyplot as plt
import model
from utils import read_SQL, preprocessing, split_timeseries, trans_timeseries
from keras.callbacks import EarlyStopping, ModelCheckpoint

class Make_model:
    def __init__(
        self, start, end, ratio, learning_rate, time_step, channel, epoch, batch 
    ):
        self.start = start,
        self.end = end,
        self.ratio = ratio,
        self.learning_rate = learning_rate,
        self.time_step = time_step,
        self.channel = channel,
        self.epoch = epoch,
        self.batch = batch

    def prepare_data(self):
        start = self.start
        end = self.end
        ratio = self.ratio

        if ratio >= 1 or ratio < 0:
            print('ERROR! : Ratio range is 0 - 1 /// 10% = 0.1')

        df = read_SQL(start, end)
        feature_df, label_df = preprocessing(df)
        feature_np, label_np = trans_timeseries(feature_df=feature_df, label_df=label_df, time_step=self.time_step)
        self.feature_train, self.label_train, self.feature_validation, self.label_validation = split_timeseries(feature_np, label_np, ratio)
    

    def train(self):
        self.model = model.LSTM(maxchannel=self.channel, col_num=len(self.feature_train[1]), learning_rate=self.learning_rate)

        check_point = ModelCheckpoint(
            f"models/model_{self.start}_{self.end}_{self.time_step}.h5",
            verbose = 1
            save_best_only = True
        )

        stop = EarlyStopping(monitor='val_mape', verbose = 1, patience = 40)

        self.training = self.model.fit(self.feature_train, self.label_train,
                        epochs=self.epoch,
                        callbacks=[check_point, stop],
                        validation_data=(self.feature_validation, self.label_validation))

    def validation(self):
        pred = self.model.predict(self.feature_validation)

        fig = plt.figure(facecolor='white', figsize=(20, 10))
        ax = fig.add_subplot(111)
        ax.plot(self.label_validation, label='True')
        ax.plot(pred, label='Prediction')
        ax.legend()
        # 2022-07-22, jaehoon : matplotlib 저장방법 구글링 후 적용해야
        ax.save('report/val.png')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-sd", "--start", default='YYYYMMDD', type=timedelta)
    parser.add_argument("-ed", "--end", default='YYYYMMDD', type=timedelta)
    parser.add_argument("-r", "--ratio", default=0.1, type=float)
    parser.add_argument("-lr", "--learning_rate", default=0.01, type=float)
    parser.add_argument("-t", "--time_step", default=1, type=int)
    parser.add_argument("-c", "--channel", default=1024, type=int)
    parser.add_argument("-e", "--epoch", default=100, type=int)
    parser.add_argument("-b", "--batch", default=200, type=int)

    args = parser.parse_args()
    start = args.start
    end = args.end
    ratio = args.ratio
    learning_rate = args.learning_rate
    time_step = args.time_step
    channel = args.channel
    epoch = args.epoch
    batch = args.batch

    training = Make_model(
        start, end, ratio, learning_rate, time_step, channel, epoch, batch
    )
    training.prepare_data()
    training.train()