# The program iterates over a list and splits the information into smaller 
# pieces. Then it prints out the information in a more clear manner.

products = [
    "PHILIPS_Kettle_HD4646_2020_09_21_C_1",
    "KENWOOD_FoodProcessor_KVL8300S_2015_09_22_C_3",
    "BOSCH_Blendermixer_MMB65G5M_2016_05_07_C_3",
    "WHIRLPOOL_Microwave_MCP345WH_2019_01_15_C_1",
    "ROSENLEW_Freezer_RPP2330_2017_01_29_C_2",
    "ELECTROLUX_Refrigerator_ERF4114AOW_2017_11_07_C_2",
    "DYSON_VacuumCleaner_BHJG567_2025_01_27_C_0"   
]

# 1 = Small Appliances
# 2 = Refrigeration Equipment
# 3 = Mixers

categories = ["Other", "Small Appliances", "Refrigeration Equipment", "Mixers"]

for row in products:
    info = row.split("_")
    manufacturer = info[0]
    name_and_model = info[1]
    model = info[2]
    year = info[3]
    month = info[4]
    day = info[5]
    category_code = int(info[7])

    # Check if the category is valid
    if 1 <= category_code <= len(categories) - 1:
        category_name = categories[category_code]
    else:
        category_name = categories[0] 

    print(f"Manufacturer: {manufacturer}\n"
          f"Name and Model: {name_and_model} ({model})\n"
          f"Category: {category_name}\n"
          f"Addition Date: {day}.{month}.{year}")
    print()
