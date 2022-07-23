import sys
from DL_module.utils import trans_test
import utils
import argparse
from datetime import timedelta
import time

from utils import read_SQL, save_SQL, preprocessing, trans_timeseries
from keras.models import load_model

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-sd", "--start", default='YYYYMMDD', type=timedelta)
    parser.add_argument("-ed", "--end", default='YYYYMMDD', type=timedelta)
    #  YYYYMMDD는 시작날짜와 끝날짜로 데이터 범위 확인후 지정
    parser.add_argument("-m", "--modelname", default='model_YYYYMMDD_YYYYMMDD_1.h5', type=int)
    parser.add_argument("-s", "--sql", action="store_true")
    parser.add_argument("-c", "--csv", action="store_trhe")

    args = parser.parse_args()
    start = args.start
    end = args.end
    modelname = args.modelname
    sql = args.sql
    csv = args.csv

    model_path = "models/" + modelname
    output_path = "data/result/"

    start_time = time.time()

    ### 입력할 데이터 변환 과정

    df = read_SQL(start, end)
    time_step = int(modelname.split('_')[3].split('.')[0])
    if len(df.index) < time_step:
        sys.exit("ERROR! : forecast period should be larger than time_step.")
    feature_np = trans_test(feature_df=df, time_step=time_step)


    ### 예측과정
    model = load_model(model_path)
    predict = model.predict(feature_np)
    

    ### 결과물 도출
    if sql:
        save_SQL(predict)

    if csv:
        save_CSV(predict)