from flask import Flask, request
import pandas as pd
import pickle
import json


app = Flask(__name__)

# ------------------------Quize predict Senesh----------------------
@app.route('/foodcheck', methods=['GET', 'POST'])
def quzesselect():

    v1 = int(request.args.get('v1'))
    v2 = int(request.args.get('v2'))
    v3 = int(request.args.get('v3'))
    v4 = int(request.args.get('v4'))
    v5 = int(request.args.get('v5'))
    v6 = int(request.args.get('v6'))
    v7 = int(request.args.get('v7'))
    v8 = int(request.args.get('v8'))
    v9 = int(request.args.get('v9'))
    v10 = int(request.args.get('v10'))
    v11 = int(request.args.get('v11'))
  	

    df = pd.read_csv("fooddataset2.csv")
    df.head()

    inputs = df.drop('Suitability',axis='columns')
    target = df['Suitability']

    from sklearn.preprocessing import LabelEncoder

    # le_Height = LabelEncoder()
    # le_Weight = LabelEncoder()
    # le_Age = LabelEncoder()
    le_Diet = LabelEncoder()
    le_Allergies = LabelEncoder()
    le_Health = LabelEncoder()
    # le_FunctionTime = LabelEncoder()

    # inputs['Height_n'] = le_Height.fit_transform(inputs['Height'])
    # inputs['Weight_n'] = le_Weight.fit_transform(inputs['Weight'])
    # inputs['Age_n'] = le_Age.fit_transform(inputs['Age'])
    inputs['Gender_n'] = le_Diet.fit_transform(inputs['Diet'])
    inputs['FavoriteColor_n'] = le_Allergies.fit_transform(inputs['Allergies'])
    inputs['FunctionType_n'] = le_Health.fit_transform(inputs['Health'])
    # inputs['FunctionTime_n'] = le_FunctionTime.fit_transform(inputs['FunctionTime'])
    inputs.head()

    inputs_n = inputs.drop(['Diet','Allergies','Health'],axis='columns')
    # inputs_n

    from sklearn import tree

    model = tree.DecisionTreeClassifier()

    model.fit(inputs_n,target)

    model.score(inputs_n, target)

    output = model.predict([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11]])
    # output = "test"
    # result = {"prediction": output.tolist()}
    # json_data = json.dumps(result)
    # return output
    # return 'Player Status: {}'.format(output)
    return (format(output))
    # return json_data
    # print(output)

    # ------------------------Quize predict Senesh----------------------
    
if __name__ == '__main__':

  app.run()