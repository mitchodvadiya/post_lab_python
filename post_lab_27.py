# post lab 27
# ------------------------------------------------------------------------------------------------------

# code : 1
import numpy as np
import seaborn as sns
sns.set(style="white")
# Generate a random univariate dataset
rs = np.random.RandomState(10)
d = rs.normal(size=100)
# Plot a simple histogram and kde
sns.histplot(d, kde=True, color="m")

# code : 2
import seaborn as sns
sns.set(style="dark")
fmri = sns.load_dataset("fmri")
# Plot the responses for different\
# events and regions
sns.lineplot(x="timepoint",
             y="signal",
             hue="region",
             style="event",
             data=fmri)

# code : 3
import seaborn as sns
sns.set(style="ticks")
# Loading the dataset
df = sns.load_dataset("anscombe")
# Show the results of a linear regression
sns.lmplot(x="x", y="y", data=df)

# code : 4
import pandas as pd
import seaborn as sns
 
# initialise data of lists
data = {'Name':[ 'Mohe' , 'Karnal' , 'Yrik' , 'jack' ],
        'Age':[ 30 , 21 , 29 , 28 ]}
df = pd.DataFrame( data )
sns.boxplot( data['Age'] )

# code : 5
import pandas as pd
import seaborn as sns
# initialise data of lists
data = {'Name':[ 'Mohe' , 'Karnal' , 'Yrik' , 'jack' ],
        'Age':[ 30 , 21 , 29 , 28 ]}
df = pd.DataFrame( data )
sns.violinplot(data['Age'])


