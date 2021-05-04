import matplotlib.pyplot as plt

# Helper class for plotting the obtained data.
class DataPlotter():
    maxOutArr=None
    inCounts=None
    outCounts=None
    inDelays=None

    def __init__(self,vhCntIn,vhCntOut,vhDelays,maxOutDuration):
        self.maxOutArr=maxOutDuration
        self.inCounts=vhCntIn
        self.outCounts=vhCntOut
        self.inDelays=vhDelays

    # Plots the max out values obtained in the simulation across time
    def plotMaxOut(self):
        fig=plt.figure(figsize=(20,20))
        tstamps=[x[0] for x in self.maxOutArr]
        maxouts=[x[1] for x in self.maxOutArr]
        plt.plot(tstamps,maxouts)
        fig.savefig("drlPlotMaxout.jpg")
    
    # Plots the incoming vehicle queue counts across time
    def plotQueueLength(self):
        fig=plt.figure(figsize=(20,20))
        tstamps=[x[0] for x in self.inCounts]
        queueL=[max(0,x[1]-10) for x in self.inCounts]
        plt.plot(tstamps,queueL)
        fig.savefig("drlPlotQueueLength.jpg")

