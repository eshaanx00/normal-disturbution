import pandas as pd
import plotly.figure_factory as px
import statistics
import plotly.graph_objects as gx

list = pd.read_csv("StudentsPerformance.csv")
score = list["reading score"].tolist()

score_mean = statistics.mean(score)
score_mode = statistics.mode(score)
score_median = statistics.median(score)
score_dev = statistics.stdev(score)

score_first_sd_start,score_first_sd_end = score_mean-score_dev,score_dev+score_mean
score_second_sd_start,score_second_sd_end = score_mean-(score_dev*2),(score_dev*2)+score_mean
score_third_sd_start,score_third_sd_end = score_mean-(score_dev*3),(score_dev*3)+score_mean

score_list_first_sd = [result for result in score if result > score_first_sd_start and result < score_first_sd_end]
score_list_second_sd = [result for result in score if result > score_second_sd_start and result < score_second_sd_end]
score_list_third_sd = [result for result in score if result > score_third_sd_start and result < score_third_sd_end]

score_percentage_for_first_sd = len(score_list_first_sd)*100/len(score)
score_percentage_for_second_sd = len(score_list_second_sd)*100/len(score)
score_percentage_for_third_sd = len(score_list_third_sd)*100/len(score)

print("Mean:",score_mean,"\nmedian:",score_median,"\nmode:",score_mode,"\ndeviation:",score_dev,"\n",score_percentage_for_first_sd,"%","lies in 1st std","\n",score_percentage_for_second_sd,"%","lies in 2nd std","\n",score_percentage_for_third_sd,"%","lies in 3rd std")

fig = px.create_distplot([score],["result"],show_hist=False)
fig.add_trace(gx.Scatter(x=[score_mean,score_mean],y=[0,0.17],mode='lines',name='mean'))
fig.add_trace(gx.Scatter(x=[score_first_sd_start,score_first_sd_start],y=[0,0.17],mode='lines',name='sd1'))
fig.add_trace(gx.Scatter(x=[score_first_sd_end,score_first_sd_end],y=[0,0.17],mode='lines',name='sd1'))

fig.add_trace(gx.Scatter(x=[score_second_sd_start,score_second_sd_start],y=[0,0.17],mode='lines',name='sd2'))
fig.add_trace(gx.Scatter(x=[score_second_sd_end,score_second_sd_end],y=[0,0.17],mode='lines',name='sd2'))

fig.add_trace(gx.Scatter(x=[score_third_sd_start,score_third_sd_start],y=[0,0.17],mode='lines',name='sd3'))
fig.add_trace(gx.Scatter(x=[score_third_sd_end,score_third_sd_end],y=[0,0.17],mode='lines',name='sd3'))

fig.show()