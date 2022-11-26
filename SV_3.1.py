
import os
import datetime
from pickle import NONE
import sys
import lasio
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import rc
from matplotlib.lines import Line2D
import datetime as dt
from openpyxl import Workbook
from openpyxl.drawing.image import Image as ImageXl
from io import BytesIO
import win32clipboard
from PIL import Image
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import tkinter as tk

#creating the glogal window varaible for the dialogs in the program
win = tk.Tk()
SnSLimits = [100, 150]

def midRPM():
    global SnSLimits
    SnSLimits = [75,125]
    win.destroy()

def highRPM():
    global SnSLimits
    SnSLimits = [50,100]
    win.destroy()

#Set the geometry of Tkinter frame 
#This variable is created up top


win.title("Choose RPM Range")
win.geometry("400x100")

B1 = tk.Button(win, text= "Average Rotation Below 100 RPM",command = win.destroy).pack()
B2 = tk.Button(win, text= "Average Rotation Between 100 and 200 RPM",command = midRPM).pack()
B3 = tk.Button(win, text= "Average Rotation Above 200 RPM",command = highRPM).pack()
win.mainloop()
    


#Tool class will be used in the script. Cointains a dictionary with all the tools and its neumonic, a dictionary with the limits 
#for each tool.

class TOOL:
    allTools = {'TeleScope': 'TELE',
            'PowerDrive': 'PD',
            'arcVISION': 'ARC',
            'EcoScope':'DV6MT',
            'TruLink':'ROS',
            'PeriScope':'PERISCOPE',
            'XEM': 'XEM',
            'adnVISION':'ADN',
            'IMPulse':'IMP',
            'ShortPulse':'SHORT',
            'SonicScope':'SONICSCOPE',
            'SonicVISION':'SONICVISION',
            'geoVISION':'RAB',
            'MicroScope675':'MI6',
            'MicroScope475':'MicroScope',
            'TerraSphere': 'KIA'
            }
            
    telescopeLimits = [{'STICKRATIO': SnSLimits,
                        'SHKRSK': [2, 3],
                        'VIB_LAT': [4, 7],
                        'VIB_X': [4, 7]
                        },
                        {'SHKPK': [75, 125],
                        }]
    xemLimits = [{'STICK': [2, 3],
                  'SHKL_RAD': [2, 3],
                  },
                 {'SHKPK_LAT': [225, 325],
                  'SHKPK_X':[225,325],
                  }]
    trulinkLimits = [{'STICKRATIO': SnSLimits,
                      'SHKRSK': [2, 3],
                      'VIB_LAT': [4, 7],
                      'VIB_X': [4, 7],
                      'VIB_LAT_PMVC': [4, 7],
                      'VIB_X_PMVC': [4, 7],
                      'VIB_AXL': [4, 7],
                       },
                     {'SHKPK_LAT': [75, 125],
                      'SHKPK_AXL': [75, 125],
                      'SHKPK_X': [75, 125],
                       }]
    powerdriveLimits = [{'SHKRSK': [2, 3],
                         'VIB_LAT': [20, 25],
                         'VIB_AXL': [5, 7]
                         },
                        {'SHKPK_LAT': [225,325],
                         'SHKPK_AXL':[225,325]
                         }]
    ecoscopeLimits = [{'SHKL': [2, 3],
                       'VIB_LAT': [5, 10],
                       'VIB_X': [5, 10],
                       'VIB_ROT':[5,10],
                        },
                      {'SHKPK_LAT': [100, 175],
                       'SHKPK_X': [100, 175],
                       'SHKPK_ROT': [100, 175],
                        }]
    lwdLimits = [{'SHKL': [2, 3],
                  'SHKRSK':[2,3]},
                 {}]
    GVRLimits = [{'SHKT': [5, 10],
                  'SHKA':[5, 10],
                  'SHKL':[2,3]},
                 {}]
    impulseLimits = [{'STICKRATIO': SnSLimits,
                      'SHKRSK': [2, 3],
                      },
                      {}]
    terraLimits = [{'SBRSKLV_RT': [2, 3],
                    'SHKRMSRSK_AXL_MX':[2,3],
                    'SHKRMSRSK_LAT_MX':[2,3],
                    'SHKRSK_AXL_MX':[2,3],
                    'SHKRSK_LAT_MX':[2,3],
                    'SHKPK_AXL_MX':[100, 175],
                    'SHKPK_LAT_MX':[100, 175],
                    'SHKRMS_AXL_MX':[6,10],
                    'SHKRMS_LAT_MX':[6,10]},
                   {}]
    
    allToolsLimits = {'TeleScope': telescopeLimits,
            'PowerDrive': powerdriveLimits,
            'arcVISION': lwdLimits,
            'EcoScope':ecoscopeLimits,
            'TruLink':trulinkLimits,
            'PeriScope':lwdLimits,
            'XEM': xemLimits,
            'adnVISION':lwdLimits,
            'IMPulse':impulseLimits,
            'ShortPulse':impulseLimits,
            'SonicVISION':lwdLimits,
            'SonicScope':lwdLimits,
            'geoVISION':GVRLimits,
            'MicroScope675':GVRLimits,
            'MicroScope475':GVRLimits,
            'TerraSphere': terraLimits
            }

    def __init__(self, name, data_raw):
        self.name = name
        self.data_raw = data_raw
        self.channels, self.counters = self.getLimits(name)
        self.channels, self.data_raw =  self.cleaner(self.channels, self.data_raw)
        self.counters, self.data_raw = self.cleaner(self.counters, self.data_raw)

        self.resAcc = NONE
        self.resCons = NONE
        self.resStats = NONE
        self.resCounts = NONE

    def getLimits(self,name):
        channels = self.allToolsLimits[name][0]
        counters = self.allToolsLimits[name][1]

        return channels, counters
    #This function will clean the channels and counters keys, If a key is found to be repeated it will correct labeling to use the first
    #key in the analysis.

    def cleaner(self, toClean, data_df):

        channels = toClean
        keys = list(channels.keys())

        print(self.name)

        sufixes = [':1', ':2',':3']

        for channel in keys:


            try:
                d = data_df[[channel]]

            except:

                for sufix in sufixes:

                    try:
                        d = data_df[[channel+sufix]]
                        data_df = data_df.rename(columns = {channel+sufix : channel})
                        break
                    except:
                        if sufix == sufixes[-1]:
                            print(channel + ' not found!')
                            del channels[channel]

        return channels, data_df






#This function receives a string and tries to find a tool neumonic inside it. It returns the tool it found 
# or none if it didn't find anythin.

def getToolName(descr):

    matchedToolName = 'NoTool'

    toolsNames = TOOL.allTools
    
    for toolName in toolsNames:
        matchedTool = re.search(toolsNames[toolName],descr, flags = re.IGNORECASE)
        if matchedTool:
            matchedToolName =  toolName
            break

    return matchedToolName

#This function translates all abreviations of shock and vibs from a string into their full words. it receives a string and returns the 
#translation

def translate (channelName):

    abreviations = {'STICKRATIO': 'Stick & Slip',
                    'STICK': 'Stick & Slip',
                    'SHKL_RAD': 'Shock Risk',
                    'SHKRSK': 'Shock Risk',
                    'SHKL': 'Shock Level',
                    'SHKT': 'Shock Risk Lateral',
                    'SHKA': 'Shock Risk Axial',
                    'SBRSKLV_RT': 'KAI Shock Level',
                    'SHKRMSRSK_AXL_MX':'Axial RMS Shock Risk',
                    'SHKRMSRSK_LAT_MX':'Lateral RMS Shock Risk',
                    'SHKRSK_AXL_MX': 'Axial Shock Risk',
                    'SHKRSK_LAT_MX': 'Lateral Shock Risk',
                    'SHKPK_AXL_MX': 'Axial Shock Peak',
                    'SHKPK_LAT_MX': 'Lateral Shock Peak',
                    'SHKRMS_AXL_MX': 'Axial RMS Shocks',
                    'SHKRMS_LAT_MX': 'Lateral RMS Shocks',
                    'VIB_LAT': 'Lateral Vibrations',
                    'VIB_X': 'Axial Vibrations',
                    'VIB_AXL': 'Axial Vibrations',
                    'VIB_LAT_PMVC': 'Lateral Vibrations',
                    'VIB_X_PMVC': 'Axial Vibrations',
                    'VIB_ROT':'Rotational Vibrations',
                    'SHKPK':'Lateral Shock Peak',
                    'SHKPK_X':'Axial Shock Peak',
                    'SHKPK_AXL':'Axial Shock Peak',
                    'SHKPK_LAT':'Lateral Shock Peak',
                    'SHKPK_ROT': 'Rotational Shock Peak'}
    try:
        return abreviations[channelName]
    except Exception as e:
        print(e)
        return channelName

#Load channels is a function that recieves the name of a las file, loads the file into a dataframe and returns
#a dataframe with multi-indexed columns and TIME as an index. e.g. 
#Channels            STICKSLIP SHOCKRISK SHOCKLEVEL    VIBLAT      VIBX
#Tool                TeleScope TeleScope  arcVISION TeleScope TeleScope
#TIME                                                                  
#2021-03-09 15:22:26   -999.25      0.00    -999.25   -999.25   -999.25
#2021-03-09 15:22:36   -999.25   -999.25    -999.25   -999.25   -999.25
#2021-03-09 15:22:46   -999.25   -999.25    -999.25   -999.25   -999.25
#2021-03-09 15:22:56   -999.25   -999.25    -999.25   -999.25   -999.25
#2021-03-09 15:23:06   -999.25   -999.25    -999.25   -999.25   -999.25
#The function also converts time into date time. It does not handle a LAS that is not time based.

def processLAS(las):

    df = las.df()

    print(df.dtypes)
    df['TIME'] = pd.to_datetime(df['TIME'], format = "%H:%M:%S/%d-%b-%Y")
    df.reset_index(inplace=True)
    df.drop('TIME_1900',inplace= True,axis =1)
    df.set_index('TIME',inplace=True)

    toolMatch = []

    curvesDict = las.curvesdict

    for neumonic in curvesDict:

        toolName = getToolName(curvesDict[neumonic].descr)
        toolMatch.append(toolName)
    

    df.columns = pd.MultiIndex.from_arrays([toolMatch[2:],df.columns.to_list()], names = ['Channels','Tool'])    


    return df



#This function will ask for the user to choose the file, will return an exception if the file is not a las or if it is not in time.
#This function will return the las file and the las file name.

def getLasFile():

    filePath = askopenfilename()
    fileName,  fileExtension = os.path.splitext(filePath)
    data_df = pd.DataFrame()
    if fileExtension.lower() != '.las':
        messagebox.showwarning(title='Warning', message='That is not a LAS file!')
        raise TypeError('That is not a LAS file!')
    else:

        las = lasio.read(filePath)

        if las.curves[0].mnemonic != 'TIME_1900':
            messagebox.showwarning(title='Warning', message='That is not a TIME LAS file!')
            raise TypeError('That is not a TIME LAS file!')
        else:
            data_df = processLAS(las)
        

    return data_df, filePath

#This function returns the level of the value, in order to avoid double looping. it recieves ths in a list with the las
#limit being infinite.

def  getLevel(value, bins):

    for i, limit in enumerate(bins):
        level = i
        if(value<limit):
            break

    return level

#This function recieves the bins with the last value being np.inf. and return a data frame with the labels for the bins.

def getLabels(bins):
    labels = []
    labels.append('Below '+str(bins[0]))
    for i, limit in enumerate(bins):

        level = i
        nextLvl = bins[i+1]
        if(nextLvl == np.inf):
            nextLvl = ''
            labels.append('Over '+str(limit))
            break
        
        labels.append('From ' + str(limit)+' to '+str(nextLvl))

    return pd.DataFrame(labels, columns = ['Bins'])

#This function recieves channels which is a list of the name of the channelss which is a dictionary with
#the key being the name of the channel and theobject being a list with ths, breakTime which is a time delta object
#with the maximmum amount of time before it stops counting and data_df with the LAS time file. Returns acc df which holds 
#each channel information in a columns, and returns a dictionary with the key being the channel and containing a list of datasets,
#one for each of the bins evaluated, each dataframe contains the start and the timeSpan (in hours as a boolean) of all 
#the periods in each level. Returns also a dict with a list of statistics, 1- avg, 2-max.



def analyze( channels, counters, breakTime, data_df):

    acc = {}
    cons = {}
    stats = {}
    counts = {}

    for channel in counters:

        highLimit = counters[channel][0]
        severeLimit = counters[channel][1]

        target_df = data_df[data_df[channel] >= highLimit]
        highCounts = target_df[channel].count()

        target_df = data_df[data_df[channel] >= severeLimit]
        severeCounts = target_df[channel].count()

        counts[channel] = [highCounts, severeCounts]


    for channel in channels:

        bins = channels[channel]
        bins.append(np.inf)

        target_df = data_df[data_df[channel] != -999.25][[channel]]

        stats[channel] = [target_df[channel].mean(), target_df[channel].max()]
        tempAcc = [0.0] * (len(bins))
        tempCons = [pd.DataFrame(columns = ['start','timeSpan'])] * (len(bins))

        iter = target_df.iterrows()
        prevTime, prevRow = next(iter)
        startSpan = prevTime
        prevLevel = getLevel(prevRow[channel],bins)

        for time, row in iter:
            if(time - prevTime > breakTime):
                if(startSpan != prevTime):
                    span = prevTime - startSpan
                    span = span.total_seconds() / 3600
                    tempAcc[int(prevLevel)] += span
                    tempCons[int(prevLevel)] =  \
                        pd.concat([tempCons[int(prevLevel)], pd.DataFrame({'start': [startSpan],'timeSpan':[span]})],ignore_index=True\
                            )

                prevTime = time
                prevRow = row
                prevLevel = getLevel(prevRow[channel],bins)
                startSpan = time
            else:
                level = getLevel(row[channel],bins)
                if(level != prevLevel):
                    span = prevTime - startSpan + 0.5 *(time - prevTime)
                    span = span.total_seconds() / 3600
                    tempAcc[int(prevLevel)] += span
                    tempCons[int(prevLevel)] =  \
                        pd.concat([tempCons[int(prevLevel)], pd.DataFrame({'start': [startSpan],'timeSpan':[span]})],ignore_index=True\
                            )
                    startSpan = time - 0.5 *(time - prevTime)
                    prevTime = time
                    prevRow = row
                    prevLevel = getLevel(prevRow[channel],bins)

                else:
                    prevTime = time
                    prevRow = row
        
        acc_df = pd.DataFrame(tempAcc, columns = [channel])
        acc_df['Bins'] = getLabels(bins)

        acc[channel] = acc_df
        cons[channel] = tempCons
    
    return acc, cons, stats, counts

#This function re-scales the high level values to have the same limit in the graph as the severe values.
#And returns the actual value in string.It also returns a list of colors for the bars.

def prepareHigh(highLevel, labels, baseColor):

    newValues = []
    newLabels = []
    newColors = []
    newOOSLabel = []

    for i, value in enumerate(highLevel):

        if labels[i] == 'Stick & Slip':
            newValues.append(value*(30/24))
            newLabels.append(('%.1f '+'hrs') % value)

        elif(labels[i][-4:] == 'Peak'):
            newValues.append(value*(30/60))
            newLabels.append(('%.1f '+'Counts') % value)
        else:
            newValues.append(value*(30/2))
            newLabels.append(('%.1f '+'hrs') % value)

        if newValues[i] > 30:
            newColors.append("dimgray")
            newOOSLabel.append('[High Level Out Of Specification] ' + newLabels[i])
        else:
            newColors.append(baseColor)
            newOOSLabel.append('')
    
    return newValues, newLabels, newColors, newOOSLabel

#This function re-scales the severe level values to have the same limit in the graph as the severe values. 
#And returns the actual value in string. It also returns a list of colors for the bars.

def prepareSevere(severeLevel, labels, baseColor):

    newValues = []
    newLabels = []
    newColors = []
    newOOSLabel = []

    for i, value in enumerate(severeLevel):

        if(labels[i][-4:] == 'Peak'):
            newValues.append(value*(30/5))
            newLabels.append(('%.1f '+'Counts') % value)
        else:
            newValues.append(value*60)
            newLabels.append(('%.1f '+'min') % newValues[i])
        

        if newValues[i] > 30:
            newColors.append("dimgray")
            newOOSLabel.append('[Severe Level Out Of Specification] ' + newLabels[i])
        else:
            newColors.append(baseColor)
            newOOSLabel.append('')
    

    
    return newValues, newLabels, newColors, newOOSLabel


#This function should plot what we get from the analyze function. It recieves a dictionary with all the tools


def plotResults(toolsDict, name):
    #setting the font
    rc('font',**{'family':'sans-serif','sans-serif':['Arial']})

    #defining the color map and creating the figure.

    colorbase = ["tab:green", "tab:olive", "tab:orange", "tab:red"]
    nodes = [0.0, 0.6 ,0.7, 1.0]
    cmapSnV = LinearSegmentedColormap.from_list("mycmap", list(zip(nodes,colorbase)))

    #create the figure and the grid spec. It needs to calculate how many channels are in the analysis.

    totalChannels = 0

    for toolName in toolsDict:

        totalChannels += len(toolsDict[toolName].channels)
        totalChannels += len(toolsDict[toolName].counters)



    fig = plt.figure(figsize = (10,1.5*totalChannels), constrained_layout=True)
    spec = fig.add_gridspec(totalChannels, 3, hspace =0.2)

    fig.suptitle('Shocks And Vibrations Analysis \n', fontsize=28, weight = 'bold', linespacing = 0.7, x = 0.025, ha = 'left')
    #Schlumberger Stamp
    pathToLogo = resource_path('schlumberger-blue-small.png')
    im = plt.imread(pathToLogo) # insert local path of the image.
    newax = fig.add_axes([0.8,0.8,0.2,0.2], anchor='NE', zorder=1)
    newax.imshow(im)
    newax.axis('off')

    #setting colors for the bars

    highColor = cmapSnV(0.67)
    severeColor = cmapSnV(0.99)

    severeLimit = 30
    severeXlim = 36



    #This loop will go trhough the tools and create a plot for each tool. W will include a variable that tracks 
    # where the last tool plot ended.
    lastPos = 0


    for i, toolName in enumerate(toolsDict):
        tool = toolsDict[toolName]
        Acc = tool.resAcc
        Counts = tool.resCounts
        labels = []
        highLevel = []
        severeLevel = []

        #This loop will get de data from the tool and organize it into plotable lists

        for channel in Acc:
            Acc_df = Acc[channel]
            labels.append(channel)
            highLevel.append(Acc_df[channel][Acc_df.shape[0]-2])
            severeLevel.append(Acc_df[channel][Acc_df.shape[0]-1])

        #This loop will get the shock peak data from the tool to put it into a plotable list.

        for channel in Counts:
            values_list = Counts[channel]
            labels.append(channel)
            highLevel.append(values_list[0])
            severeLevel.append(values_list[1])


        

        highLevel = np.array(highLevel)
        severeLevel = np.array(severeLevel)

        #tranlating the neumoinics into actual measurements
    
        for j, label in enumerate(labels):
            labels[j] = translate(label)


        highScaled, highLevelLabels, highColors, highOOSLabel = prepareHigh(highLevel,labels, highColor)
        severeScaled, severeLevelLabels, severeColors, severeOOSLabel = prepareSevere(severeLevel,labels, severeColor)
        

        newPos = lastPos + len(labels)


        ax1 = fig.add_subplot(spec[lastPos:newPos,:])
        y_pos = np.arange(len(labels))
        
        lastPos = newPos

        width = 0.35  # the width of the bars

        severeBars = ax1.barh(y_pos + width/2 + 0.01, severeScaled, width, align='center', label = 'Severe',color = severeColors)

        highBars = ax1.barh(y_pos - width/2 - 0.01, highScaled, width, align='center', label = 'High',color = highColors)



        ax1.set_xlim([0,severeXlim])
        
        ax1.axvline(severeLimit, ls='--', color='r',label = 'Limit')
    
        ax1.set_yticks(y_pos, labels=labels)

        if toolName == 'TeleScope' or toolName == 'TruLink':
            ax1.set_title('MWD Shocks & Vibrations', fontsize = 18, fontstyle = 'italic', loc = 'left', pad = 20)
        else:
            ax1.set_title(toolName + ' Shocks & Vibrations', fontsize = 18, fontstyle = 'italic', loc = 'left', pad = 20)
        
        ax1.set_xlabel('Accumulated Shocks')

        #here we will specify the high level color, severe level color and out of spec color, and add this items to the legend.

        legendHandles, legendLabels = ax1.get_legend_handles_labels()
        limitHandle = legendHandles[0]
        highHandle = Line2D([0], [0], color=highColor, lw=6)
        severeHandle = Line2D([0], [0], color=severeColor, lw=6)
        OOSHandle = Line2D([0], [0], color='dimgray', lw=6)

        legendLabels.append('OOS')

        ax1.legend([limitHandle,highHandle,severeHandle,OOSHandle],legendLabels)



        ax1.bar_label(highBars, labels=highLevelLabels, padding=3, fontsize=10)
        ax1.bar_label(severeBars, labels=severeLevelLabels, padding=3, fontsize=10)

        for i, OOSlabel in enumerate(highOOSLabel):
            ax1.text(5,i-width/2 +0.04, OOSlabel, color = 'darkred', weight = 'bold', fontsize = 16)

        for i, OOSlabel in enumerate(severeOOSLabel):
            ax1.text(5,i+width/2 +0.06, OOSlabel, color = 'darkred', weight = 'bold', fontsize = 16)


        ax1.invert_yaxis()  # labels read top-to-bottom
        

        ax1.tick_params(axis='x',          # changes apply to the x-axis
                        which='both',      # both major and minor ticks are affected
                        bottom=False,      # ticks along the bottom edge are off
                        top=False,         # ticks along the top edge are off
                        labelbottom=False) # labels along the bottom edge are off        






    plt.savefig(name[:-4] + '_Shocks and Vibrations.png',bbox_inches = 'tight', pad_inches = 0.2)
#This function will get the path for the SLB Logo

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#This function will deliver all the results, recieves the plot and the 
def send_to_clipboard(clip_type, filepath):
    
    image = Image.open(filepath)

    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()
      
def Run():
    
    try:
        data_df, lasName = getLasFile()
        print('LAS File loaded...')
        bhaTools = {}
        

        foundTools = data_df.columns.droplevel(1).unique().to_list()

        for toolName in foundTools:

            if toolName == 'NoTool':
                continue

            breakTime = dt.timedelta(seconds=400)

            tool = TOOL(toolName, data_df[toolName])

            toolData = tool.data_raw

            channels = tool.channels

            counters = tool.counters

            #this should be handled by the tool class.            

            tool.resAcc, tool.resCons, tool.resStats, tool.resCounts = analyze(channels, counters, breakTime, toolData)
            bhaTools[toolName] = tool



        plotResults(bhaTools, lasName)
        send_to_clipboard(win32clipboard.CF_DIB, lasName[:-4] + '_Shocks and Vibrations.png')

        print('Done')
    except Exception as e:
        print(e)
        print('Try Again!')

try:
    f = open("SnVAnalyzerLog.txt", 'w')
    sys.stdout = f
    print(datetime.datetime.now())
    Run()
    print('')
    f.close()
except Exception as e:
    print(e)
    Run()
