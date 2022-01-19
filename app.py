import pandas as pd 
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random

df=pd.read_csv("data.csv")
data=df["reading_time"].tolist()
df_new=pd.read_csv("data.csv")
data_new=df_new["Math_score"].tolist()

population_mean=statistics.mean(data_new)

def sample_data_points(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,(len(data)-1))
        value=data[random_index]    
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def setup():
    mean_list=[]
    for i in range(1000):
        mean_of_samples=sample_data_points(100)
        mean_list.append(mean_of_samples)

    sampling_mean=statistics.mean(mean_list)
    sampling_stdev=statistics.stdev(mean_list)

    zscore= (population_mean-sampling_mean)/sampling_stdev
    print( "The zscore fro School1 is : ", zscore)
    first_std_dev_start, first_std_dev_end= sampling_mean-sampling_stdev,sampling_mean+sampling_stdev
    second_std_dev_start, second_std_dev_end= sampling_mean-(2*sampling_stdev), sampling_mean+(2*sampling_stdev)
    third_std_dev_start, third_std_dev_end= sampling_mean-(3*sampling_stdev), sampling_mean+(3*sampling_stdev)

    fig= ff.create_distplot([mean_list], ["Reading time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[sampling_mean, sampling_mean], y= [0,0.15], mode="lines", name= "Mean"))
    fig.add_trace(go.Scatter(x=[population_mean, population_mean], y=[0,0.15], mode=("lines"), name="Mean after internention"))
    fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[0,0.15], mode="lines", name="First std dev Start"))
    fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0,0.15], mode="lines", name="First std dev end"))
    fig.show()

setup()