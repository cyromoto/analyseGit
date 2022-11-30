# import basic libraries for DA
import matplotlib.pyplot as plt
import pandas as pd


#import the data file to frame
githubdf=pd.read_csv(".//combined.csv")

#To plot Pie Chart with others
def plotPieWithOthers(dfForLanguage,split,header):
    
    kwargs = dict(
        startangle = 90,
        colormap   = 'Pastel2',
        fontsize   = 13,
        figsize    = (60,8),
        ylabel     ='',
        autopct    = '%1.1f%%',
        title      = header
        )
    
    s = dfForLanguage['language'].value_counts()

    #Split into major languages and minor languages
    dfForLanguageSmall=dfForLanguage[dfForLanguage.isin(s.index[s <= split]).values]
    dfForLanguageLarge=dfForLanguage[dfForLanguage.isin(s.index[s > split]).values]
    
    # Group together the minor languages and append as Other languages
    s = dfForLanguageLarge['language'].value_counts()
    s['Others']=dfForLanguageSmall.groupby(['language'])['language'].count().sum()
    s.plot.pie(**kwargs)
    plt.savefig("output.png")
    plt.show()

#choosing data based on prediction
mergedLanguages=githubdf[githubdf['prediction'] ==0]
rejectedLanguages=githubdf[githubdf['prediction'] ==1]

plotPieWithOthers(mergedLanguages,25000,'Merged Languages')
plotPieWithOthers(rejectedLanguages,500,'Rejected Languages')


majorCoeffLabel= ['review_comments','has_projects','has_wiki','has_discussions','title_size']
majorCoeffValue= [ 3.78903330e-01,-4.43066925e-01,-5.82090870e-01,9.24001782e-01,-2.05548705e-02]
minorCoeffLabel= ['additions', 'deletions', 'open_issues_count', 'watchers_count','forks_count','stargazers_count' ]
minorCoeffValue= [ -2.52929190e-07, -1.54264402e-06,-3.23741228e-05,  2.81550405e-06,2.81550405e-06,2.81550405e-06]

plt.bar(majorCoeffLabel,majorCoeffValue,color ='maroon')
plt.show()
plt.bar(minorCoeffLabel,minorCoeffValue,color ='maroon')
plt.show()