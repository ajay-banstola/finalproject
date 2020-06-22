#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm
import warnings
from matplotlib.pyplot import xticks
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from flask import Flask, make_response, request, render_template
import io
import json
import csv
import random
from io import BytesIO
import pandas as pd
import pickle
import sklearn.metrics as metrics
app = Flask(__name__)


@app.route('/')
def form():
    return render_template("upload.html")


@app.route('/transform2', methods=['POST'])
def transform_view2():
    df = pd.read_csv('static/leads_cleaned.csv')
    df1 = df[['row_number', 'TotalVisits', 'Converted']]
    print(df1)
    chart_data = df1.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template("graph.html", data=data)


@app.route('/transform', methods=['POST'])
def transform_view():

    # copied

    # -*- coding: utf-8 -*-

    # In[1]:

    # Supress Warnings

    warnings.filterwarnings('ignore')

    # Importing libraries

    # visulaisation

    #get_ipython().run_line_magic('matplotlib', 'inline')

    # Data display coustomization

    pd.set_option('display.max_rows', 100)
    pd.set_option('display.max_columns', 100)

    # In[3]:

    #data = pd.DataFrame(pd.read_csv('leads_cleaned.csv'))
    data = pd.read_csv(request.files.get('data_file'))
    # data.head(2)

    # In[4]:

    data['Lead Source'] = data['Lead Source'].replace(['google'],
                                                      'Google')
    data['Lead Source'] = data['Lead Source'].replace([
        'Click2call',
        'Live Chat',
        'NC_EDM',
        'Pay per Click Ads',
        'Press_Release',
        'Social Media',
        'WeLearn',
        'bing',
        'blog',
        'testone',
        'welearnblog_Home',
        'youtubechannel',
    ], 'Others')

    # In[5]:

    # Let's keep considerable last activities as such and club all others to "Other_Activity"

    data['Last Activity'] = data['Last Activity'].replace([
        'Had a Phone Conversation',
        'View in browser link Clicked',
        'Visited Booth in Tradeshow',
        'Approached upfront',
        'Resubscribed to emails',
        'Email Received',
        'Email Marked Spam',
    ], 'Other_Activity')

    # In[6]:

    data['Specialization'] = data['Specialization'].replace(['Others'],
                                                            'Other_Specialization')
    data['What is your current occupation'] = \
        data['What is your current occupation'].replace(['Other'],
                                                        'Other_Occupation')

    # In[7]:

    # Let's keep considerable last activities as such and club all others to "Other_Activity"

    data['Tags'] = data['Tags'].replace([
        'In confusion whether part time or DLP',
        'in touch with EINS',
        'Diploma holder (Not Eligible)',
        'Approached upfront',
        'Graduation in progress',
        'number not provided',
        'opp hangup',
        'Still Thinking',
        'Lost to Others',
        'Shall take in the next coming month',
        'Lateral student',
        'Interested in Next batch',
        'Recognition issue (DEC approval)',
        'Want to take admission but has financial problems',
        'University not recognized',
    ], 'Other_Tags')

    # In[8]:

    data = data.drop([
        'Lead Number',
        'What matters most to you in choosing a course',
        'Search',
        'Magazine',
        'Newspaper Article',
        'X Education Forums',
        'Newspaper',
        'Digital Advertisement',
        'Through Recommendations',
        'Receive More Updates About Our Courses',
        'Update me on Supply Chain Content',
        'Get updates on DM Content',
        'I agree to pay the amount through cheque',
        'A free copy of Mastering The Interview',
        'Country',
    ], 1)

    # In[9]:

    data.shape

    # In[10]:

    data.head()

    # In[11]:

    varlist = ['Do Not Email', 'Do Not Call']

    # Defining the map function

    def binary_map(x):
        return x.map({'Yes': 1, 'No': 0})

    # Applying the function to the housing list

    data[varlist] = data[varlist].apply(binary_map)

    # In[12]:

    # Creating a dummy variable for some of the categorical variables and dropping the first one.

    dummy1 = pd.get_dummies(data[[
        'Lead Origin',
        'Lead Source',
        'Last Activity',
        'Specialization',
        'What is your current occupation',
        'Tags',
        'Lead Quality',
        'City',
        'Last Notable Activity',
    ]], drop_first=True)
    dummy1.head()

    # In[13]:

    # Adding the results to the master dataframe

    data = pd.concat([data, dummy1], axis=1)
    data.head()

    # In[14]:

    data = data.drop([
        'Lead Origin',
        'Lead Source',
        'Last Activity',
        'Specialization',
        'What is your current occupation',
        'Tags',
        'Lead Quality',
        'City',
        'Last Notable Activity',
    ], axis=1)

    # In[15]:

    data.head()

    # In[16]:

    # Putting feature variable to X

    X = data.drop(['Prospect ID', 'Converted', 'row_number'], axis=1)

    # In[17]:

    # Putting response variable to y

    y = data['Converted']

    y.head()

    # In[27]:

    # Runnning your first model

    logreg = LogisticRegression()

    rfe = RFE(logreg, 15)  # running RFE with 15 variables as output
    rfe = rfe.fit(X, y)
    col = X.columns[rfe.support_]
    col1 = col.drop('Tags_invalid number', 1)
    col2 = col1.drop('Tags_wrong number given', 1)
    X_train = sm.add_constant(X[col2])
    X_train.info()

    # In[34]:

    res = pickle.load(open('model.pkl', 'rb'))
    y_train_pred = res.predict(X_train)
    y_train_pred = pd.DataFrame(y_train_pred)

    # In[35]:

    y_train_pred

    # In[38]:

    final = pd.concat([X_train, y_train_pred, y], axis=1)

    # In[39]:

    final

    # In[40]:

    # Renaming the column

    final = final.rename(columns={0: 'Converted_prob'})

    # In[41]:

    final

    # In[55]:

    final['final_predicted'] = final.Converted_prob.map(lambda x:
                                                        (1 if x > 0.5 else 0))

    # In[56]:

    final.head()

    # In[57]:

    # Let's check the overall accuracy.

    metrics.accuracy_score(final.Converted, final.final_predicted)

    # In[ ]:

    # copied_finish

    # Send Response

    resp = make_response(final.to_csv())
    resp.headers['Content-Disposition'] = \
        'attachment; filename= export.csv'
    resp.headers['Content-Type'] = 'text/csv'
    return resp


if __name__ == '__main__':
    app.run(debug=True)
