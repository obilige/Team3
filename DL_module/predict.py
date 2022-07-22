import utils
import argparse
from datetime import timedelta
import time

from utils import save_SQL, preprocessing, trans_timeseries
from keras.models import load_model

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-sd", "--start", default='YYYYMMDD', type=timedelta)
    parser.add_argument("-ed", "--end", default='YYYYMMDD', type=timedelta)
    parser.add_argument("-t", "--time_step", default=1, type=int)
    #  YYYYMMDD는 시작날짜와 끝날짜로 데이터 범위 확인후 지정
    parser.add_argument("-m", "--modelname", default='model_YYYYMMDD_YYYYMMDD_1.h5', type=int)
    parser.add_argument("-s", "--sql", action="store_true")
    parser.add_argument("-c", "--csv", action="store_trhe")

    args = parser.parse_args()
    start = args.start
    end = args.end
    time_step =args.time_step
    modelname = args.modelname
    sql = args.sql
    csv = args.csv

    model_path = "models/" + modelname
    output_path = "data/result/"

    start_time = time.time()

    ### 입력할 데이터 변환 과정


    #############################

    ### 예측과정
    model = load_model(model_path)
    predict = model.predict()
    training.train()