import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
from DataCleaning import open_and_manage
 
def clean_select_quant(csv_file):
    """ clean data using open_and_manage fucntion
        select the quantitaive data
    """
    df=open_and_manage(csv_file)
    df1=df[['price','constructionYear','room_number','nbr_parking_indoor','nbr_parking_outdoor','square_metres']]
    """
    number of rows and columns in the data matrix
    """
    a=df.shape
    """
    number of rows and columns in the quantitative data matrix
    """
    b=df1.shape
    print('\n number of rows and columns in the data matrix')
    print(a)
    print('\n number of rows and columns in the quantitative data matrix')
    print(b)
    return df1
    
#df1=clean_select_quant('~/challenge-data-analysis/quick_clean.csv')
#print(a)

def corr_var_target (df1):
    """correlation between the variables and the target variables
    """
    data1=df1.drop("square_metres", axis=1).apply(lambda x: x.corr(df1.square_metres))
    corrMatrix1=pd.DataFrame(data1)
    ax=plt.axes()
    graph=sn.heatmap(corrMatrix1, annot=True,cmap = 'coolwarm')
    ax.set_title('Correlation between variables and the Price')
    plt.show()
    """
    variables with the greatest influence on the target
    """
    big=corrMatrix1.nlargest(3, 0)
    """
    variables with the least influence on the target
    """
    small=corrMatrix1.nsmallest(2, 0)
    plt.show()
    print('\n\tthe variables with the greatest influence on the target variable:')
    print(big)
    print('\n\t the variables with the least influence on the target variable :')
    print(small)

#corr_var_target(df1)

def corr_matrix (df1):
    corrMatrix2 = df1.corr()
    mask = np.zeros(corrMatrix2.shape, dtype=bool)
    mask[np.triu_indices(len(mask))] = True
    ax=plt.axes()
    sn.heatmap(corrMatrix2, ax=ax, vmin = -1, vmax = 1, center = 0, cmap = 'coolwarm', annot = True, mask = mask)
    ax.set_title('Correlation Matrix')
    plt.show()

#corr_matrix(df1)

def miss_val_quant (df1):
    """
    Percentage of missing values per column in the quantitave variables
    """
    miss_val = df1.isna() #transform in bool
    miss_val_num = miss_val.sum()   #from bool to numerical
    miss= miss_val_num / len(df1)
    print('\nthe Percentage of missing values per column in the quantitave variables :')
    print(miss)

#miss_val_quant(df1)

def abdellah(csv_file):
    """
    quantitative data selection and Data Analysis
    """
    df1=clean_select_quant(csv_file)
    corr_var_target (df1)
    corr_matrix(df1)
    miss_val_quant(df1)

#abdellah('~/challenge-data-analysis/quick_clean.csv')





