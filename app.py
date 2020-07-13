from flask import Flask, render_template, redirect, url_for, flash, session, send_file
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os
import json
import pandas as pd
import os.path
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
# import statsmodels.api as sm
from statsmodels import api as sm
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
import pickle
import sklearn.metrics as metrics
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db_path = os.path.join(os.path.dirname(__file__), 'database.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri


Bootstrap(app)


db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField('username', validators=[
                           InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[
                             InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(
        message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[
                           InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[
                             InputRequired(), Length(min=8, max=80)])


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('index'))
    return wrap


@app.route('/', methods=['GET', 'POST'])
def index():
    form2 = RegisterForm()
    if request.method == "POST":
        if request.form["login"] == "Login":
            form = LoginForm()
            form2 = RegisterForm()
            if form.validate_on_submit():
                user = User.query.filter_by(
                    username=form.username.data).first()
                if user:
                    login_user(user, remember=form.remember.data)
                    if check_password_hash(user.password, form.password.data):
                        return redirect(url_for('welcome'))
                flash('Invalid username or password')
            return render_template('index.html', form=form2)
        else:
            form2 = RegisterForm()
            if form2.validate_on_submit():
                hashed_password = generate_password_hash(
                    form2.password.data, method='sha256')
                print(form2.username.data)
                if User.query.filter_by(username=form2.username.data).first():
                    flash("Username already exists!")
                elif User.query.filter_by(email=form2.email.data).first():
                    flash("Email already exists!")
                else:
                    new_user = User(username=form2.username.data,
                                    email=form2.email.data, password=hashed_password)
                    db.session.add(new_user)
                    db.session.commit()
                    # return redirect(url_for('index'))
            # return render_template('index.html', form=form2)
        return render_template('index.html', form=form2)
    elif current_user.is_authenticated:
        return render_template('upload.html')
    else:
        return render_template('index.html', form=form2)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user:
#             login_user(user, remember=form.remember.data)
#             if check_password_hash(user.password, form.password.data):
#                 return redirect(url_for('welcome'))

#         return "<h1>" + "Invalid Username or password" + "</h1>"
#         # flash("Invalid Username or Password")

#     return render_template('login.html', form=form)


# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     form = RegisterForm()

#     if form.validate_on_submit():
#         hashed_password = generate_password_hash(
#             form.password.data, method='sha256')
#         # if User.query.filter_by(username=form.username.data).first() == form.username.data:
#         #    flash("Username already exits!")
#         # else:
#         new_user = User(username=form.username.data,
#                         email=form.email.data, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()

#         return '<h1>New user has been created!</h1>'
#         # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

#     return render_template('signup.html', form=form)


@app.route('/welcome')
@login_required
def welcome():
    return render_template('upload.html')


@app.route('/logout', methods=['GET', 'POST'])
# @login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
    # return render_template('login.html')
# copied


@app.route('/transform2', methods=['POST', 'GET'])
def transform_view2():
    df = pd.read_csv(r'C:\Users\Admin\Downloads\export.csv')
    # df = pd.read_csv(request.files.get('data_file'))
    # resp = transform_view()
    # print(resp)
    # resp = resp.response
    # resp2 = pd.DataFrame(resp)
    # final1 = pd.read_csv(final)
    # print(final1.columns)
    # print(resp)
    # df1 = df[['Converted', 'Converted_prob', 'final_predicted']]
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template("graphtest.html", data=data)


@app.route('/graph_visualization/')
def graph_visualization():
    fig, ax = plt.subplots(nrows=1, ncols=2)
    df = pd.read_csv(r'C:\Users\Admin\Downloads\export.csv')
    for row in ax:
        sns.barplot(x="Lead Origin",
                    y="Converted", data=df, ax=ax[0])
        sns.barplot(x="Lead Source",
                    y="Converted", data=df, ax=ax[1])
        plt.setp(row.get_xticklabels(), rotation=30,
                 horizontalalignment='right')
    # # sns.countplot(x="Last Activity",
    # #               data=df, ax=ax[1, 0])
    # sns.barplot(x="Last Activity", y="Converted", data=df, ax=ax[1, 0])
    # sns.barplot(x="Specialization",
    #               y="Converted", data=df, ax=ax[1, 1])
    plt.setp(row.get_xticklabels(), rotation=30,
             horizontalalignment='right')
    plt.tight_layout()
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.set_size_inches(18.5, 10.5, forward=True)
    fig.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png', cache_timeout=-1)


@app.route('/graph_visualization2/')
def graph_visualization2():
    fig, ax = plt.subplots(nrows=1, ncols=2)
    df = pd.read_csv(r'C:\Users\Admin\Downloads\export.csv')
    for row in ax:
        sns.countplot(x="Last Activity", hue="Converted", data=df, ax=ax[0])
        # sns.barplot(x="Specialization",
        #             y="Converted", data=df, ax=ax[1])
        sns.countplot(x="Lead Origin", hue="Converted", data=df, ax=ax[1])
        plt.setp(row.get_xticklabels(), rotation=30,
                 horizontalalignment='right')
    plt.tight_layout()
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.set_size_inches(18.5, 10.5, forward=True)
    fig.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png', cache_timeout=-1)


# @app.route('/graph_visualization3/')
# def graph_visualization3():
#     fig2, ax2 = plt.subplots()
#     df = pd.read_csv(r'C:\Users\Admin\Downloads\export.csv')
#     # sns.countplot(x="City", hue="Converted", data=df)
#     sns.barplot(x="Last Activity", y="Converted", data=df)
#     xticks(rotation=90)
#     plt.tight_layout()
#     plt.ylabel('Converted')
#     plt.xlabel('Last Activity')
#     canvas = FigureCanvas(fig2)
#     img2 = BytesIO()
#     fig2.savefig(img2, format='png')
#     img2.seek(0)

#     return send_file(img2, mimetype='image/png', cache_timeout=-1)


@app.route('/transform', methods=['POST'])
def transform_view():

    warnings.filterwarnings('ignore')

    # Importing libraries

    # visulaisation

    # get_ipython().run_line_magic('matplotlib', 'inline')

    # Data display coustomization

    pd.set_option('display.max_rows', 100)
    pd.set_option('display.max_columns', 100)

    # In[3]:

    # data = pd.DataFrame(pd.read_csv('static/leads_cleaned.csv'))
    data1 = pd.read_csv(request.files.get('data_file'))
    data = data1
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

    # data.head()

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
    # dummy1.head()

    # In[13]:

    # Adding the results to the master dataframe

    data = pd.concat([data, dummy1], axis=1)
    # data.head()

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

    X = data.drop(['Prospect ID', 'Converted', 'row_number'], axis=1)

    # In[17]:

    # Putting response variable to y

    y = data['Converted']

    # y.head()

    # In[27]:

    # Runnning your first model

    logreg = LogisticRegression()

    rfe = RFE(logreg, 15)  # running RFE with 15 variables as output
    rfe = rfe.fit(X, y)
    col = X.columns[rfe.support_]
    col1 = col.drop('Tags_invalid number', 1)
    col2 = col1.drop('Tags_wrong number given', 1)
    X_train = sm.add_constant(X[col2])
    # X_train.info()

    # In[34]:

    res = pickle.load(open('model.pkl', 'rb'))
    y_train_pred = res.predict(X_train)
    y_train_pred = pd.DataFrame(y_train_pred)

    final = pd.concat([X_train, y_train_pred, y], axis=1)

    final = final.rename(columns={0: 'Converted_prob'})
    # final
    final['final_predicted'] = final.Converted_prob.map(lambda x:
                                                        (1 if x > 0.5 else 0))
    data1['final_score'] = final.Converted_prob.map(lambda x: x*100)
    metrics.accuracy_score(final.Converted, final.final_predicted)
    resp = make_response(data1.to_csv())
    resp.headers['Content-Disposition'] = \
        'attachment; filename= export.csv'
    resp.headers['Content-Type'] = 'text/csv'
    return resp


if __name__ == '__main__':
    app.run(debug=True)
