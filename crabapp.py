import streamlit as st
import pickle

model = pickle.load(open('crab.pkl', 'rb'), encoding='latin1')

def run():
    st.title("Crab Age Prediction using Machine Learning")

     ## Length
    st.caption('Length of the Crab (in Feet; 1 foot = 30.48 cms)')
    length = st.number_input('Enter Length of the Crab') 

    ## Diameter
    st.caption('Diamenter of the Crab (in Feet; 1 foot = 30.48 cms)')
    diameter = st.number_input('Enter Diameter of the Crab')

    ## Height
    st.caption('Height of the Crab (in Feet; 1 foot = 30.48 cms)')
    height = st.number_input('Enter Height of the Crab')

    ##Weight
    st.caption('Weight of the Crab (in ounces; 1 Pound = 16 ounces)')
    weight = st.number_input('Enter Weight of the Crab')
     
    ##Shucked Weight
    st.caption('Weight without the shell (in ounces; 1 Pound = 16 ounces)')
    shuweight = st.number_input('Enter Shucked Weight of the Crab')

    ##Viscera Weight
    st.caption('Is Weight that wraps around your abdominal organs deep inside body (in ounces; 1 Pound = 16 ounces)')
    vweight = st.number_input('Enter Viscera Weight of the Crab')

    ##Shell Weight
    st.caption('Weight of the Shell (in ounces; 1 Pound = 16 ounces)')
    shellweight = st.number_input('Enter Shell Weight of the Crab')


    if st.button("Submit"):
        features = [[length, diameter,height,weight,shuweight,vweight,shellweight]]
        print(features)
        prediction = model.predict(features)
        weight = [str(i) for i in prediction]
        ans = ', '.join(weight)
        if ans==0:
            st.error("Error in the Inputs: Please Try Again")

        else:
            st.success("The Age of the crab in months predicted is:"+" "+ans)


            

run()