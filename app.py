import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
date = st.date_input(
    "Pickup Date",
    datetime.datetime.now())
st.write('Pickup Date is:', date)

time = st.time_input('Pickup Time', datetime.datetime.now())
st.write('Pickup Time', time)

pickup_latitude = st.number_input('Pickup Latitude', value = 41)
st.write('Pickup Latitude', pickup_latitude)

pickup_longitude = st.number_input('Pickup longitude', value = -74)
st.write('Pickup longitude', pickup_longitude)

dropoff_latitude = st.number_input('Dropoff Latitude', value = 40)
st.write('Dropoff Latitude', dropoff_latitude)

dropoff_longitude = st.number_input('Dropoff longitude', value = -73)
st.write('Dropoff longitude', dropoff_longitude)

passenger_count = st.number_input('Number of Passengers', step = 1, value = 1, min_value = 1, max_value= 6)
st.write('Number of Passengers', passenger_count)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''
2. Let's build a dictionary containing the parameters for our API...
3. Let's call our API using the `requests` package...
4. Let's retrieve the prediction from the **JSON** returned by the API...
## Finally, we can display the prediction to the user
'''

# formatted_date = f"{date[:4]}-{date[4:6]}-{date[6:]}"
# formatted_time = f"{time[:2]}:{time[2:4]}:{time[4:]}"

datetime_format = "YYYY-MM-DD HH:MM:SS"
pickup_datetime = f"{date} {time}"



if st.button("Get Fare Prediction"):
    # Prepare API Parameters
    API_parameters = {
        'pickup_datetime': pickup_datetime,
        'pickup_latitude': pickup_latitude,
        'pickup_longitude': pickup_longitude,
        'dropoff_latitude': dropoff_latitude,
        'dropoff_longitude': dropoff_longitude,
        'passenger_count': passenger_count
    }

    response = requests.get(url, params=API_parameters)

    if response.status_code == 200:
        # Parse JSON Response
        fare_prediction = response.json().get("fare", "No fare returned")
        st.metric("Estimated Taxi Fare", f"${fare_prediction:.2f}")
    else:
        st.error(f"API call failed. Status code: {response.status_code}")
        st.write(response.text)

# API_parameters={'pickup_datetime' : pickup_datetime,
#                 'pickup_latitude' :pickup_latitude,
#                 'pickup_longitude' :pickup_longitude,
#                 'dropoff_latitude' :dropoff_latitude,
#                 'dropoff_longitude' :dropoff_longitude,
#                 'passeger_count' :passeger_count
# }

# request = requests.get(url, params=API_parameters)
# if request.status_code == 200:
#     print("Response data:", request.json())  # Parse JSON response
# else:
#     print("Failed to fetch data. Status code:", response.status_code)
#     print("Error message:", request.text)

# # json = {'fare' : ' '}
# # response = requests.post(url, json=json)
# # if response.status_code == 201:  # 201 is typical for resource creation
# #     print("Resource created:", response.json())
# # else:
# #     print("Failed to create resource. Status code:", response.status_code)
# #     print("Error message:", response.text)

# col1 = st.columns(1)
# col1.metric("Your Taxi fare estimation", response)
