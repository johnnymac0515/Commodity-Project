""""Module is responsible for plotting relevant data passed to it as a dataframe"""

import matplotlib.pyplot as plt

#TODO running average

IR_BEGIN = 1760
IR_END = 1840

def running_average(data):
    """returns the running average of the passed dataset"""
    pass

def plotter(dataframe, location, commodity):
    
    title = "Value of {} in {} from {} to {}".format(commodity, location, 
            dataframe['Item Year'].min(), dataframe['Item Year'].max())

    a_x = dataframe.plot(x='Item Year', y=['Original Value','Standard Value'], title=title)
    a_x.axvspan(xmin=IR_BEGIN, xmax=IR_END, ymin=0, ymax=1, alpha=0.3, color='r')
    plt.show(block=False)
    return