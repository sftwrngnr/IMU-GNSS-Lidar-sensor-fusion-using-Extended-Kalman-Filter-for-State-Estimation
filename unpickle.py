import pickle as pkl
import pandas as pd

df1 = pd.read_pickle('data/pt1_data.pkl') #to load 123.pkl back to thpt1_e dataframe df
with open("data/pt1_data.pkl", "rb") as f:
    data = pkl.load(f)

    gt = data['gt']
    imu_f = data['imu_f']
    imu_w = data['imu_w']
    gnss = data['gnss']
    lidar = data['lidar']

    # print imu data
    print("gt vars")
    print(vars(gt))
    print("imu_f vars")
    print(vars(imu_f))
    print("imu_w vars")
    print(vars(imu_w))
    print("gnss vars")
    print(vars(gnss))
    #for t in imu_f.t:
    #    print(t)
    #for k in imu_f.data:
    #    print(k)
