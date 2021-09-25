import pandas as pd
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random
df = pd.read_csv("medium_data.csv")
population_mean = df["reading_time"].tolist()
mean = statistics.mean(population_mean)
median = statistics.median(population_mean)
mode = statistics.mode(population_mean)
standarddeviation = statistics.stdev(population_mean)
print("populationstandarddeviation", standarddeviation)
print("populationmean", mean)
print("populationmedian", median)
print("populationmode", mode)
figure = ff.create_distplot([population_mean], ["Population Mean"], show_hist=False)
figure.show()
def randomsetofmeans(counter):
    population_meanset = []
    for i in range(0, counter):
        randomindex = random.randint(0, len(population_mean)-1)
        value = population_mean[randomindex]
        population_meanset.append(value)
    mean1 = statistics.mean(population_meanset)
    return mean1 
def showfigure(meanlist):
    df1 = meanlist
    meanofsamplingdistribution = statistics.mean(meanlist)
    standarddeviationofsamplingdistribution = statistics.stdev(meanlist)
    print("standarddeviationofsamplingdistribution", standarddeviationofsamplingdistribution)
    medianofsamplingdistribution = statistics.median(meanlist)
    modeofsamplingdistribution = statistics.mode(meanlist)
    print("meanofsamplingdistribution", meanofsamplingdistribution)
    print("medianofsamplingdistribution", medianofsamplingdistribution)
    print("modeofsamplingdistribution", modeofsamplingdistribution)
    firststandarddeviationstart, firststandarddeviationend = meanofsamplingdistribution - standarddeviationofsamplingdistribution, meanofsamplingdistribution + standarddeviationofsamplingdistribution
    secondstandarddeviationstart, secondstandarddeviationend = meanofsamplingdistribution - (2*standarddeviationofsamplingdistribution), meanofsamplingdistribution + (2*standarddeviationofsamplingdistribution)
    thirdstandarddeviationstart, thirdstandarddeviationend = meanofsamplingdistribution - (3*standarddeviationofsamplingdistribution), meanofsamplingdistribution + (3*standarddeviationofsamplingdistribution)

    figure1 = ff.create_distplot([df1], ["reading_time"], show_hist=False)
    figure1.add_trace(go.Scatter(x = [meanofsamplingdistribution, meanofsamplingdistribution], y = [0, 0.17], mode = "lines", name = "mean"))
    figure1.add_trace(go.Scatter(x = [firststandarddeviationstart, firststandarddeviationstart], y = [0, 0.17], mode = "lines", name = "standard deviation 1 start"))
    figure1.add_trace(go.Scatter(x = [firststandarddeviationend, firststandarddeviationend], y = [0, 0.17], mode = "lines", name = "standard deviation 1 end"))
    figure1.add_trace(go.Scatter(x = [secondstandarddeviationstart, secondstandarddeviationstart], y = [0, 0.17], mode = "lines", name = "standard deviation 2 start"))
    figure1.add_trace(go.Scatter(x = [secondstandarddeviationend, secondstandarddeviationend], y = [0, 0.17], mode = "lines", name = "standard deviation 2 end"))

    df2 = pd.read_csv("medium_data.csv")
    population_mean2 = df2["reading_time"].tolist()
    meanofid = statistics.mean(population_mean2)
    print("population with id:", meanofid)
    figure1.add_trace(go.Scatter(x = [meanofid, meanofid], y = [0, 0.17], mode = "lines", name = "mean of id"))
    zscore = (meanofsamplingdistribution - meanofid)/standarddeviationofsamplingdistribution
    print(zscore, "zscoreofid")

    figure1.show()

def setup():
    meanlist = []
    for i in range(0, 1000):
        setofmeans = randomsetofmeans(100)
        meanlist.append(setofmeans)
    showfigure(meanlist)

setup()