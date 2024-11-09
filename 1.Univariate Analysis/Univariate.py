class univariate():
    
    def QuanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=='O'):
                #print("qual")
                qual.append(columnName)
            else:
                #print("quan")
                quan.append(columnName)
        return quan,qual
    
    def UnivaraiteDescriptive (dataset,quan):
        import pandas as pd
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%",
                               "IQR","1.5rule","Lesser","Greater","Min","Max"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["Mean"]=dataset[columnName].mean()
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5rule"]=1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25%"]-1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Min"]=dataset[columnName].min()
            descriptive[columnName]["Max"]=dataset[columnName].max()
            descriptive[columnName]["Skewness"]=dataset[columnName].skew()
            descriptive[columnName]["Kurtosis"]=dataset[columnName].kurtosis()
            descriptive[columnName]["Variace"]=dataset[columnName].var()
            descriptive[columnName]["Standard Deviation"]=dataset[columnName].std()
        return descriptive
    
    def ReplacingOutliers(descriptive):
        LesserOutColumns=[]
        GreaterOutColumns=[]
        for columnName in descriptive.columns:
            if (descriptive[columnName]["Min"]<descriptive[columnName]["Lesser"]):
                LesserOutColumns.append(columnName)
            if (descriptive[columnName]["Max"]>descriptive[columnName]["Greater"]):
                GreaterOutColumns.append(columnName)
        return LesserOutColumns,GreaterOutColumns
    
    def FrequencyTable(dataset,columName):
        FreqTable=pd.DataFrame(columns=["Unique_Value","Frequency","Relative_Frequency","Cumulative_Relative_Frequency(CumSum)"])
        FreqTable["Unique_Value"]=dataset[columName].value_counts().index
        FreqTable["Frequency"]=dataset[columName].value_counts().values
        FreqTable["Relative_Frequency"]=dataset[columName].value_counts().values/sum(dataset[columName].value_counts())
        FreqTable["Cumulative_Relative_Frequency(CumSum)"]=FreqTable["Relative_Frequency"].cumsum()
        return FreqTable