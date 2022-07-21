from DL_module.utils import trans_timeseries
import model
from utils import read_SQL, preprocessing

class Make_model:
    def __init__(
        self, start, end,learning_rate, time_step, channel, epoch, batch 
    ):
        self.start = start,
        self.end = end,
        self.learning_rate = learning_rate,
        self.time_step = time_step,
        self.channel = channel,
        self.epoch = epoch,
        self.batch = batch

    def prepare_data(self):
        start = self.start
        end = self.end

        df = read_SQL(start, end)
        feature_df, label_df = preprocessing(df)
        feature_np, label_np = trans_timeseries(feature_df=feature_df, label_df=label_df, time_step=self.time_step)

        return feature_np, label_np
    

    def train(self):
        

