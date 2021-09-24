import pandas as pd
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random
df = pd.read_csv("medium_data.csv")
population_mean = df["id"].tolist()
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
    for i in range(0, 30):
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

    figure1 = ff.create_distplot([df1], ["id"], show_hist=False)
    figure1.add_trace(go.Scatter(x = [meanofsamplingdistribution, meanofsamplingdistribution], y = [0, 0.17], mode = "lines", name = "mean"))
    figure1.add_trace(go.Scatter(x = [firststandarddeviationstart, firststandarddeviationstart], y = [0, 0.17], mode = "lines", name = "standard deviation 1 start"))
    figure1.add_trace(go.Scatter(x = [firststandarddeviationend, firststandarddeviationend], y = [0, 0.17], mode = "lines", name = "standard deviation 1 end"))
    figure1.add_trace(go.Scatter(x = [secondstandarddeviationstart, secondstandarddeviationstart], y = [0, 0.17], mode = "lines", name = "standard deviation 2 start"))
    figure1.add_trace(go.Scatter(x = [secondstandarddeviationend, secondstandarddeviationend], y = [0, 0.17], mode = "lines", name = "standard deviation 2 end"))

    df2 = pd.read_csv("medium_data.csv")
    population_mean2 = df2["id"].tolist()
    meanofid = statistics.mean(population_mean2)
    print("population with id:", meanofid)
    figure1.add_trace(go.Scatter(x = [meanofid, meanofid], y = [0, 0.17], mode = "lines", name = "mean of id"))
    zscore = (meanofsamplingdistribution - meanofid)/standarddeviationofsamplingdistribution
    print(zscore, "zscoreofid")


    df3 = pd.read_csv("median_data.csv")
    population_mean3 = df3["url"].tolist()
    meanofurl = statistics.mean(population_mean3)
    print("population with url:", meanofurl)
    figure1.add_trace(go.Scatter(x = [meanofurl, meanofurl], y = [0, 0.17], mode = "lines", name = "mean of url"))
    zscore = (meanofsamplingdistribution - meanofurl)/standarddeviationofsamplingdistribution
    print(zscore, "zscoreofextraclasses")


    df4 = pd.read_csv("median_data.csv")
    population_mean4 = df4["title"].tolist()
    meanoftitle = statistics.mean(population_mean4)
    print("students who use fun sheets:", meanoftitle)
    figure1.add_trace(go.Scatter(x = [meanoftitle, meanoftitle], y = [0, 0.17], mode = "lines", name = "mean of title"))
    zscore = (meanofsamplingdistribution - meanoftitle)/standarddeviationofsamplingdistribution
    print(zscore)
    figure1.show()

    df5 = pd.read_csv("median_data.csv")
    population_mean5 = df5["subtitle"].tolist()
    meanofsubtitle = statistics.mean(population_mean5)
    print("students who use fun sheets:", meanofsubtitle)
    figure1.add_trace(go.Scatter(x = [meanofsubtitle, meanofsubtitle], y = [0, 0.17], mode = "lines", name = "mean of subtitle"))
    zscore = (meanofsamplingdistribution - meanofsubtitle)/standarddeviationofsamplingdistribution
    print(zscore)
    figure1.show()

    df6 = pd.read_csv("median_data.csv")
    population_mean6 = df6["image"].tolist()
    meanofimage = statistics.mean(population_mean6)
    print("students who use fun sheets:", meanofimage)
    figure1.add_trace(go.Scatter(x = [meanofimage, meanofimage], y = [0, 0.17], mode = "lines", name = "mean of image"))
    zscore = (meanofsamplingdistribution - meanofimage)/standarddeviationofsamplingdistribution
    print(zscore)
    figure1.show()

    df7 = pd.read_csv("median_data.csv")
    population_mean7 = df7["claps"].tolist()
    meanofclaps = statistics.mean(population_mean7)
    print("students who use fun sheets:", meanofclaps)
    figure1.add_trace(go.Scatter(x = [meanofclaps, meanofclaps], y = [0, 0.17], mode = "lines", name = "mean of claps"))
    zscore = (meanofsamplingdistribution - meanofclaps)/standarddeviationofsamplingdistribution
    print(zscore)
    figure1.show()

    df8 = pd.read_csv("median_data.csv")
    population_mean8 = df8["responses"].tolist()
    meanofresponses = statistics.mean(population_mean8)
    print("students who use fun sheets:", meanofresponses)
    figure1.add_trace(go.Scatter(x = [meanofresponses, meanofresponses], y = [0, 0.17], mode = "lines", name = "mean of responses"))
    zscore = (meanofsamplingdistribution - meanofresponses)/standarddeviationofsamplingdistribution
    print(zscore)
    figure1.show()

    df9 = pd.read_csv("median_data.csv")
    population_mean9 = df9["reading_time"].tolist()
    meanofreadingtime = statistics.mean(population_mean9)
    print("students who use fun sheets:", meanofreadingtime)
    figure1.add_trace(go.Scatter(x = [meanofreadingtime, meanofreadingtime], y = [0, 0.17], mode = "lines", name = "mean of reading time"))
    zscore = (meanofsamplingdistribution - meanofreadingtime)/standarddeviationofsamplingdistribution
    print(zscore)
    figure1.show()

    df10 = pd.read_csv("median_data.csv")
    population_mean10 = df10["publication"].tolist()
    meanofpublication = statistics.mean(population_mean10)
    print("students who use fun sheets:", meanofpublication)
    figure1.add_trace(go.Scatter(x = [meanofpublication, meanofpublication], y = [0, 0.17], mode = "lines", name = "mean of publication"))
    zscore = (meanofsamplingdistribution - meanofpublication)/standarddeviationofsamplingdistribution
    print(zscore)
    figure1.show()

    df11 = pd.read_csv("median_data.csv")
    population_mean11 = df11["date"].tolist()
    meanofdate = statistics.mean(population_mean11)
    print("students who use fun sheets:", meanofdate)
    figure1.add_trace(go.Scatter(x = [meanofdate, meanofdate], y = [0, 0.17], mode = "lines", name = "mean of date"))
    zscore = (meanofsamplingdistribution - meanofdate)/standarddeviationofsamplingdistribution
    print(zscore)
    figure1.show()

def setup():
    meanlist = []
    for i in range(0, 1000):
        setofmeans = randomsetofmeans(100)
        meanlist.append(setofmeans)
    showfigure(meanlist)

setup()