from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('sales_random_forest.pkl','rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        Outlet_Establishment_Year= int(request.form['Outlet_Establishment_Year'])
        No_of_Years = 2022 - Outlet_Establishment_Year
        Item_Weight=float(request.form['Item_Weight'])
        Item_Fat_Content=str(request.form['Item_Fat_Content'])
        if (Item_Fat_Content == 'Low Fat'):
            Item_Fat_Content = 1
        else:
            Item_Fat_Content = 0
        Item_Visibility=float(request.form['Item_Visibility'])
        Item_MRP=float(request.form['Item_MRP'])
        Outlet_Size=str(request.form['Outlet_Size'])
        if(Outlet_Size=='Small'):
            Outlet_Size=0
        elif(Outlet_Size=='Medium'):
            Outlet_Size = 1
        else:
            Outlet_Size = 2
        Outlet_Location_Type = str(request.form['Outlet_Location_Type'])
        if(Outlet_Location_Type =='Tier 1'):
            Outlet_Location_Type=0
        elif(Outlet_Location_Type == 'Tier 2'):
            Outlet_Location_Type=1
        else:
            Outlet_Location_Type=2
        Outlet_Type=str(request.form['Outlet_Type'])
        if(Outlet_Type=='Grocery Store'):
            Outlet_Type=0
        elif(Outlet_Type=='Supermarket Type1'):
            Outlet_Type=1
        elif(Outlet_Type=='Supermarket Type2'):
            Outlet_Type=2
        else:
            Outlet_Type=3
        Item_Type_Baking_Goods=(request.form['Item_Type_Baking_Goods'])
        if(Item_Type_Baking_Goods=='Baking Goods'):
            Item_Type_Baking_Goods=1
            Item_Type_Breads=0
            Item_Type_Breakfast=0
            Item_Type_Canned=0
            Item_Type_Dairy=0
            Item_Type_Frozen_Foods=0
            Item_Type_Fruits_and_Vegetables=0
            Item_Type_Hard_Drinks=0
            Item_Type_Health_and_Hygiene=0
            Item_Type_Household=0
            Item_Type_Meat=0
            Item_Type_Others=0
            Item_Type_Seafood=0
            Item_Type_Snack_Foods=0
            Item_Type_Soft_Drinks=0
            Item_Type_Starchy_Foods=0
        elif(Item_Type_Baking_Goods=='Breads'):
            Item_Type_Baking_Goods = 0
            Item_Type_Breads = 1
            Item_Type_Breakfast = 0
            Item_Type_Canned = 0
            Item_Type_Dairy = 0
            Item_Type_Frozen_Foods = 0
            Item_Type_Fruits_and_Vegetables = 0
            Item_Type_Hard_Drinks = 0
            Item_Type_Health_and_Hygiene = 0
            Item_Type_Household = 0
            Item_Type_Meat = 0
            Item_Type_Others = 0
            Item_Type_Seafood = 0
            Item_Type_Snack_Foods = 0
            Item_Type_Soft_Drinks = 0
            Item_Type_Starchy_Foods = 0
        elif(Item_Type_Baking_Goods=='Breakfast'):
            Item_Type_Baking_Goods = 0
            Item_Type_Breads = 0
            Item_Type_Breakfast = 1
            Item_Type_Canned = 0
            Item_Type_Dairy = 0
            Item_Type_Frozen_Foods = 0
            Item_Type_Fruits_and_Vegetables = 0
            Item_Type_Hard_Drinks = 0
            Item_Type_Health_and_Hygiene = 0
            Item_Type_Household = 0
            Item_Type_Meat = 0
            Item_Type_Others = 0
            Item_Type_Seafood = 0
            Item_Type_Snack_Foods = 0
            Item_Type_Soft_Drinks = 0
            Item_Type_Starchy_Foods = 0
        elif(Item_Type_Baking_Goods == 'Canned'):
            Item_Type_Baking_Goods = 0
            Item_Type_Breads = 0
            Item_Type_Breakfast = 0
            Item_Type_Canned = 1
            Item_Type_Dairy = 0
            Item_Type_Frozen_Foods = 0
            Item_Type_Fruits_and_Vegetables = 0
            Item_Type_Hard_Drinks = 0
            Item_Type_Health_and_Hygiene = 0
            Item_Type_Household = 0
            Item_Type_Meat = 0
            Item_Type_Others = 0
            Item_Type_Seafood = 0
            Item_Type_Snack_Foods = 0
            Item_Type_Soft_Drinks = 0
            Item_Type_Starchy_Foods = 0
        elif(Item_Type_Baking_Goods == 'Dairy'):
            Item_Type_Baking_Goods = 0
            Item_Type_Breads = 0
            Item_Type_Breakfast = 0
            Item_Type_Canned = 0
            Item_Type_Dairy = 1
            Item_Type_Frozen_Foods = 0
            Item_Type_Fruits_and_Vegetables = 0
            Item_Type_Hard_Drinks = 0
            Item_Type_Health_and_Hygiene = 0
            Item_Type_Household = 0
            Item_Type_Meat = 0
            Item_Type_Others = 0
            Item_Type_Seafood = 0
            Item_Type_Snack_Foods = 0
            Item_Type_Soft_Drinks = 0
            Item_Type_Starchy_Foods = 0
        elif(Item_Type_Baking_Goods == 'Frozen Foods'):
            Item_Type_Baking_Goods = 0
            Item_Type_Breads = 0
            Item_Type_Breakfast = 0
            Item_Type_Canned = 0
            Item_Type_Dairy = 0
            Item_Type_Frozen_Foods = 1
            Item_Type_Fruits_and_Vegetables = 0
            Item_Type_Hard_Drinks = 0
            Item_Type_Health_and_Hygiene = 0
            Item_Type_Household = 0
            Item_Type_Meat = 0
            Item_Type_Others = 0
            Item_Type_Seafood = 0
            Item_Type_Snack_Foods = 0
            Item_Type_Soft_Drinks = 0
            Item_Type_Starchy_Foods = 0
        elif(Item_Type_Baking_Goods == 'Fruits and Vegetables'):
            Item_Type_Baking_Goods = 0
            Item_Type_Breads = 0
            Item_Type_Breakfast = 0
            Item_Type_Canned = 0
            Item_Type_Dairy = 0
            Item_Type_Frozen_Foods = 0
            Item_Type_Fruits_and_Vegetables = 1
            Item_Type_Hard_Drinks = 0
            Item_Type_Health_and_Hygiene = 0
            Item_Type_Household = 0
            Item_Type_Meat = 0
            Item_Type_Others = 0
            Item_Type_Seafood = 0
            Item_Type_Snack_Foods = 0
            Item_Type_Soft_Drinks = 0
            Item_Type_Starchy_Foods = 0
        elif (Item_Type_Baking_Goods == 'Hard Drinks'):
            Item_Type_Baking_Goods = 0
            Item_Type_Breads = 0
            Item_Type_Breakfast = 0
            Item_Type_Canned = 0
            Item_Type_Dairy = 0
            Item_Type_Frozen_Foods = 0
            Item_Type_Fruits_and_Vegetables = 0
            Item_Type_Hard_Drinks = 1
            Item_Type_Health_and_Hygiene = 0
            Item_Type_Household = 0
            Item_Type_Meat = 0
            Item_Type_Others = 0
            Item_Type_Seafood = 0
            Item_Type_Snack_Foods = 0
            Item_Type_Soft_Drinks = 0
            Item_Type_Starchy_Foods = 0
        elif(Item_Type_Baking_Goods == 'Health and Hygiene'):
            Item_Type_Baking_Goods = 0
            Item_Type_Breads = 0
            Item_Type_Breakfast = 0
            Item_Type_Canned = 0
            Item_Type_Dairy = 0
            Item_Type_Frozen_Foods = 0
            Item_Type_Fruits_and_Vegetables = 0
            Item_Type_Hard_Drinks = 0
            Item_Type_Health_and_Hygiene = 1
            Item_Type_Household = 0
            Item_Type_Meat = 0
            Item_Type_Others = 0
            Item_Type_Seafood = 0
            Item_Type_Snack_Foods = 0
            Item_Type_Soft_Drinks = 0
            Item_Type_Starchy_Foods = 0
        elif(Item_Type_Baking_Goods == 'Household'):
            Item_Type_Baking_Goods = 0
            Item_Type_Breads = 0
            Item_Type_Breakfast = 0
            Item_Type_Canned = 0
            Item_Type_Dairy = 0
            Item_Type_Frozen_Foods = 0
            Item_Type_Fruits_and_Vegetables = 0
            Item_Type_Hard_Drinks = 0
            Item_Type_Health_and_Hygiene = 0
            Item_Type_Household = 1
            Item_Type_Meat = 0
            Item_Type_Others = 0
            Item_Type_Seafood = 0
            Item_Type_Snack_Foods = 0
            Item_Type_Soft_Drinks = 0
            Item_Type_Starchy_Foods = 0
        elif(Item_Type_Baking_Goods == 'Meat'):
            Item_Type_Baking_Goods = 0
            Item_Type_Breads = 0
            Item_Type_Breakfast = 0
            Item_Type_Canned = 0
            Item_Type_Dairy = 0
            Item_Type_Frozen_Foods = 0
            Item_Type_Fruits_and_Vegetables = 0
            Item_Type_Hard_Drinks = 0
            Item_Type_Health_and_Hygiene = 0
            Item_Type_Household = 0
            Item_Type_Meat = 1
            Item_Type_Others = 0
            Item_Type_Seafood = 0
            Item_Type_Snack_Foods = 0
            Item_Type_Soft_Drinks = 0
            Item_Type_Starchy_Foods = 0
        elif(Item_Type_Baking_Goods == 'Others'):
            Item_Type_Baking_Goods = 0
            Item_Type_Breads = 0
            Item_Type_Breakfast = 0
            Item_Type_Canned = 0
            Item_Type_Dairy = 0
            Item_Type_Frozen_Foods = 0
            Item_Type_Fruits_and_Vegetables = 0
            Item_Type_Hard_Drinks = 0
            Item_Type_Health_and_Hygiene = 0
            Item_Type_Household = 0
            Item_Type_Meat = 0
            Item_Type_Others = 1
            Item_Type_Seafood = 0
            Item_Type_Snack_Foods = 0
            Item_Type_Soft_Drinks = 0
            Item_Type_Starchy_Foods = 0
        elif(Item_Type_Baking_Goods == 'Seafood'):
            Item_Type_Baking_Goods = 0
            Item_Type_Breads = 0
            Item_Type_Breakfast = 0
            Item_Type_Canned = 0
            Item_Type_Dairy = 0
            Item_Type_Frozen_Foods = 0
            Item_Type_Fruits_and_Vegetables = 0
            Item_Type_Hard_Drinks = 0
            Item_Type_Health_and_Hygiene = 0
            Item_Type_Household = 0
            Item_Type_Meat = 0
            Item_Type_Others = 0
            Item_Type_Seafood = 1
            Item_Type_Snack_Foods = 0
            Item_Type_Soft_Drinks = 0
            Item_Type_Starchy_Foods = 0
        elif(Item_Type_Baking_Goods == 'Snack Foods'):
            Item_Type_Baking_Goods = 0
            Item_Type_Breads = 0
            Item_Type_Breakfast = 0
            Item_Type_Canned = 0
            Item_Type_Dairy = 0
            Item_Type_Frozen_Foods = 0
            Item_Type_Fruits_and_Vegetables = 0
            Item_Type_Hard_Drinks = 0
            Item_Type_Health_and_Hygiene = 0
            Item_Type_Household = 0
            Item_Type_Meat = 0
            Item_Type_Others = 0
            Item_Type_Seafood = 0
            Item_Type_Snack_Foods = 1
            Item_Type_Soft_Drinks = 0
            Item_Type_Starchy_Foods = 0
        elif(Item_Type_Baking_Goods == 'Soft Drinks'):
            Item_Type_Baking_Goods = 0
            Item_Type_Breads = 0
            Item_Type_Breakfast = 0
            Item_Type_Canned = 0
            Item_Type_Dairy = 0
            Item_Type_Frozen_Foods = 0
            Item_Type_Fruits_and_Vegetables = 0
            Item_Type_Hard_Drinks = 0
            Item_Type_Health_and_Hygiene = 0
            Item_Type_Household = 0
            Item_Type_Meat = 0
            Item_Type_Others = 0
            Item_Type_Seafood = 0
            Item_Type_Snack_Foods = 0
            Item_Type_Soft_Drinks = 1
            Item_Type_Starchy_Foods = 0
        else:
            Item_Type_Baking_Goods = 0
            Item_Type_Breads = 0
            Item_Type_Breakfast = 0
            Item_Type_Canned = 0
            Item_Type_Dairy = 0
            Item_Type_Frozen_Foods = 0
            Item_Type_Fruits_and_Vegetables = 0
            Item_Type_Hard_Drinks = 0
            Item_Type_Health_and_Hygiene = 0
            Item_Type_Household = 0
            Item_Type_Meat = 0
            Item_Type_Others = 0
            Item_Type_Seafood = 0
            Item_Type_Snack_Foods = 0
            Item_Type_Soft_Drinks = 0
            Item_Type_Starchy_Foods = 1



        prediction=model.predict([[Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP,Outlet_Size, Outlet_Location_Type, Outlet_Type,Item_Type_Baking_Goods, Item_Type_Breads, Item_Type_Breakfast,Item_Type_Canned, Item_Type_Dairy, Item_Type_Frozen_Foods,Item_Type_Fruits_and_Vegetables, Item_Type_Hard_Drinks,
       Item_Type_Health_and_Hygiene, Item_Type_Household, Item_Type_Meat,
       Item_Type_Others, Item_Type_Seafood, Item_Type_Snack_Foods,
       Item_Type_Soft_Drinks, Item_Type_Starchy_Foods, No_of_Years]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="This is unacceptable")
        else:
            return render_template('index.html',prediction_text="Sales are {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080)