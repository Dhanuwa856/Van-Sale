from bs4 import BeautifulSoup
import requests
import pandas as pd


base_url = "https://www.autolanka.com/cars/index{}.html"

# Number of pages to scrape
num_pages = 6

# Initialize lists to store data
titles = []
prices = []
fieldss = []
transmissions = []
engine_cylinderss = []
fuels = []
mileages = []
infos = []


# Iterate over each page
for page_num in range(1, num_pages + 1):
  # Construct the URL for the current page
  url = base_url.format(page_num)
  
  # Send a GET request to the page URL
  response = requests.get(url)
  soup = BeautifulSoup(response.text,'html.parser')
  
  
    # Find all car listing items
  car_list = soup.find_all("article",class_="item two-inline col-sm-4")
  for car_info in car_list:
    
    # Title
    title = car_info.find_all("li",class_="title")
    if title == []:
      title_available = "Title Not Available"
    else:
      title_available = "Title Available"
    # print(title_available)  
    
    for title_list in title:
      main_title = title_list.text.strip()
      
    if title_available == "Title Not Available":
      title_set = "Title Not Available"
    elif title_available == "Title Available":
      title_set = main_title
    # print("Title :",title_set)   
    titles.append(title_set)
   
    # Price
    price = car_info.find_all("span",class_="price-tag") 
    if price == []:
      price_available = "Price Not Available"
    else:
      price_available = "Price Available"
    # print(price_available)    
    
    for price_list in price:
      main_price = price_list.text.strip()
      
    if price_available == "Price Not Available":
      price_set = "Price Not Available"
    elif price_available == "Price Available":
      price_set = main_price
    # print("Price :",price_set)  
    prices.append(price_set)
    
    # fields
    
    fields = car_info.find_all("li",class_="fields")
    # print(fields)
    
    if fields == []:
     fields_available = "Fields Not Available"
    else :
      fields_available = "Fields Available"
    
    for fields_list in fields:
      span = fields_list.find_all("span")
      field_year = span[0].text
      body_style = span[1].text
      main_fields = field_year+","+body_style.strip()
    # print(main_fields)
    
    
    if fields_available == "Fields Not Available":
      fields_set = "Fields Not Available"
    elif fields_available == "Fields Available":
      fields_set = main_fields
    # print("Fields :",fields_set)  
    fieldss.append(fields_set)
    
    # vehicle url 
    
    vehicle_url = car_info.find_all("div",class_="main-column clearfix")
    for vehicle_url_list in vehicle_url:
      a_tag = vehicle_url_list.find("a")["href"]
  
   
      
    # print("Url :",a_tag)

    # description page scrape 
    description_response = requests.get(a_tag)
    description_soup = BeautifulSoup(description_response.text,"html.parser")
    
    # Transmission
    transmission = description_soup.find_all("div",class_="table-cell clearfix",id="df_field_transmission")
    
    if transmission == []:
     transmission_available = "Transmission Not Available"
    else:
      transmission_available = "Transission Available"
    
    for transmission_list in transmission:
      transmission_value = transmission_list.find("div",class_="value")
      transmission_value_set = transmission_value.text.strip()
    
    if transmission_available == "Transmission Not Available":
      main_transmission_value = "Transmisson Not Available"
    elif transmission_available == "Transission Available":
      main_transmission_value = transmission_value_set
    # print("Transmission :",main_transmission_value) 
    transmissions.append(main_transmission_value)
    
     
    # engine cylinders
    engine_cylinders = description_soup.find_all("div",class_="table-cell clearfix",id="df_field_engine_cylinders")
    
    if engine_cylinders == []:
     engine_cylinders_available = "engine cylinders Not Available"
    else:
      engine_cylinders_available = "engine cylinders Available"
    
    
    for engine_cylinders_list in engine_cylinders:
      engine_cylinders_value = engine_cylinders_list.find("div",class_="value")
      engine_cylinders_value_set = engine_cylinders_value.text.strip()
    
    if engine_cylinders_available == "engine cylinders Not Available":
      main_engine_cylinder_value = "Engine Cylinders Not Available"
    elif transmission_available == "Transission Available":
     main_engine_cylinder_value = engine_cylinders_value_set
    # print("Engine Cylinders :",main_engine_cylinder_value)  
    engine_cylinderss.append(main_engine_cylinder_value)
    
    
    # fuel
    fuel = description_soup.find_all("div",class_="table-cell clearfix",id="df_field_fuel")
    
    if fuel == []:
     fuel_available = "Fuel Not Available"
    else:
     fuel_available = "Fuel Available"
    
    for fuel_list in fuel:
      fuel_value = fuel_list.find("div",class_="value")
      fuel_value_set = fuel_value.text.strip()
    
    if fuel_available  == "Fuel Not Available":
      main_fuel_value = "Fuel Not Available"
    elif fuel_available == "Fuel Available":
      main_fuel_value = fuel_value_set
    # print("Fuel :",main_fuel_value)  
    fuels.append(main_fuel_value)
    
    
    # mileage
    mileage = description_soup.find_all("div",class_="table-cell clearfix",id="df_field_mileage")
    
    if mileage == []:
     mileage_available = "Mileage Not Available"
    else:
     mileage_available = "Mileage Available"
    
    for mileage_list in mileage:
      mileage_value = mileage_list.find("div",class_="value")
      mileage_value_set = mileage_value.text.strip()
    
    if mileage_available  == "Mileage Not Available":
      main_mileage_value = "Mileage Not Available"
    elif mileage_available == "Mileage Available":
      main_mileage_value = mileage_value_set
      
    # print("Mileage :",main_mileage_value)  
    mileages.append(main_mileage_value)
    
    # Additional Information
    
    info = description_soup.find_all("div",class_="table-cell clearfix wide-field textarea",id="df_field_additional_information")
    
    if info == []:
      info_available = "Info Not Available"
    else:
      info_available = "Info Available"
    
    for info_list in info:
      info_value = info_list.find("div",class_="value")
      info_value_set = info_value.text.strip()
      
    if info_available == "Info Not Available":
      main_info_value = "Info Value Not Available"
    elif info_available == "Info Available":
      main_info_value = info_value_set
      
    # print("Additional Information :",main_info_value)
    infos.append(main_info_value)
    
# Print lengths of lists before creating DataFrame
# print("Length of titles:", len(titles))
# print("Length of prices:", len(prices))
# print("Length of fields:", len(fieldss))
# print("Length of transmissions:", len(transmissions))
# print("Length of engine cylinders:", len(engine_cylinderss))
# print("Length of fuel:", len(fuels))    
# print("Length of mileages:", len(mileages))    
# print("Length of info:", len(infos))    
      
# Create a DataFrame from the collected data
data = {"Title":titles,"Price":prices,"Fields":fieldss,"Transmission":transmissions,"Engine Cylinders":engine_cylinderss,"Fuel":fuels,"Mileage":mileages,"Additional Information":infos}

df = pd.DataFrame(data)    

# Write the DataFrame to an Excel file
df.to_excel("Car_sale.xlsx",index=False)
print("Data successfully exported to Car_sale.xlsx")
    
    
    
