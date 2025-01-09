def load_data(data):
    data1=[]
    with open(file_name,"r") as file:
        file.readline()
        data=file.readlines()
    for row in data:
        Date,Crop,Region,Production,Price=row.strip().split(",")
        data1.append((Date,Crop,Region,float(Production),float(Price)))
    print(data1)
    return(data1)

#1 Total yield of crop
def total_yield_by_crop(data):
    yield_by_crop={}
    for row in data:
        crop=row[1]
        if crop not in yield_by_crop:
            yield_by_crop[crop]=0
        yield_by_crop[crop]+=row[3]
    return yield_by_crop

#2 Average price by crop
def average_price_by_crop(data):
    price_sum={}
    count={}
    for row in data:
        crop=row[1]
        if crop not in price_sum:
            price_sum[crop]=0
            count[crop]=0
        price_sum[crop]+=row[4]
        count[crop]+=1
    average_price={}
    for crop in price_sum:
        average_price=price_sum[crop]/count[crop]
    return average_price

#3 Identify high yield
def high_yield_crop_by_region(data):
    yield_by_region={}
    for row in data:
        region=row[2]
        crop=row[1]
        if region not in yield_by_region:
            yield_by_region[region]={}
        if crop not in yield_by_region[region]:
            yield_by_region[region][crop]=0
        yield_by_region[region][crop]+=row[3]
    #print(yield_by_region)
    high_yield_crops={}
    for region in yield_by_region:
        max_crop=None
        max_yield=0
        for crop,yield_value in yield_by_region[region].items():
            if yield_value>max_yield:
                max_crop=crop
                max_yield=yield_value
        high_yield_crops[region]=(max_crop,max_yield)
    return high_yield_crops

#4 Total Revenue by region
def total_revenue_by_region(data):
    revenue_by_region={}
    for row in data:
        region=row[2]
        revenue=row[3]*row[4]
        if region not in revenue_by_region:
            revenue_by_region[region]=0
        revenue_by_region[region]+=revenue
    return revenue_by_region
        
#5 Most profitable crop in each region
def most_profitable_crop(data):
    profit_by_region={}
    for row in data:
        region=row[2]
        crop=row[1]
        revenue=row[3]*row[4]
        if region not in profit_by_region:
            profit_by_region[region]={}
        if crop not in profit_by_region[region]:
            profit_by_region[region][crop]=0
        profit_by_region[region][crop]+=revenue
    most_profitable={}
    for region in profit_by_region:
        max_crop=None
        max_profit=0
        for crop, profit_value in profit_by_region[region].items():
            if profit_value>max_profit:
                max_profit=profit_value
                max_crop=crop
        most_profitable[region]=(max_crop,max_profit)
    return most_profitable

#6 Region with highest total yield
def region_with_highest_yield(data):
    yield_by_region = {}
    for row in data:
        region = row[2]
        if region not in yield_by_region:
            yield_by_region[region] = 0
        yield_by_region[region] += row[3]
    max_region = max(yield_by_region, key=yield_by_region.get)
    return max_region, yield_by_region[max_region]

#7 Summarized yearly production for a specific crop
def yearly_production_summary(data, crop_name):
    yearly_production = {}
    for row in data:
        date, crop = row[0], row[1]
        year = date.split("-")[-1]
        if crop == crop_name:
            if year not in yearly_production:
                yearly_production[year] = 0
            yearly_production[year] += row[3]
    return yearly_production

#8 Sort regions by average price
def sort_regions_by_average_price(data):
    region_price_sum = {}
    count = {}
    for row in data:
        region = row[2]
        if region not in region_price_sum:
            region_price_sum[region] = 0
            count[region] = 0
        region_price_sum[region] += row[4]
        count[region] += 1
    average_price_by_region = {region: region_price_sum[region] / count[region] for region in region_price_sum}
    sorted_regions = sorted(average_price_by_region.items(), key=lambda x: x[1], reverse=True)
    return sorted_regions

#9 Add new crop data
def add_new_crop(data, date, crop, region, production, price):
    data.append((date, crop, region, production, price))

file_name="agri.txt"
agriculture_data=load_data(file_name)

while True:
    print("Menu")
    print("""    1. Total Yield by Crop Type
    2. Average Price by Crop Type
    3. Identify High-Yield Crops by Region
    4. Calculate Total Revenue by Region
    5. Most Profitable Crop in Each Region
    6. Region with Highest Total Yield
    7. Summarize Yearly Production for a Crop.
    8. Sort Regions by Average Price.
    9. Add New Crop Data..
    0. Exit
    """)
    choice=input("Enter your choice(0-9): ")
    if choice=='1':
        print("Total yield by crop: ",total_yield_by_crop(agriculture_data))
    if choice=='2':
        print("Average Price: ",average_price_by_crop(agriculture_data))
    if choice=='3':
        print("Yield by region: ",high_yield_crop_by_region(agriculture_data))
    if choice=='4':
        print("Total revenue by region: ",total_revenue_by_region(agriculture_data))
    if choice=='5':
        print("Most Profitable: ",most_profitable_crop(agriculture_data))
    if choice=='6':
        print("Region with highest total yield:", region_with_highest_yield(agriculture_data))
    if choice=='7':
        crop_name = input("Enter crop name for yearly production summary: ")
        print("Yearly production for", crop_name, ":", yearly_production_summary(agriculture_data, crop_name))
    if choice=='8':
         print("Regions sorted by average price:", sort_regions_by_average_price(agriculture_data))
    if choice=='9':
        date = input("Enter date (dd-mm-yyyy): ")
        crop = input("Enter crop name: ")
        region = input("Enter region: ")
        production = float(input("Enter production: "))
        price = float(input("Enter price: "))
        add_new_crop(agriculture_data, date, crop, region, production, price)
        print("New crop data added successfully.")
    if choice=='0':
        print("Exiting...")
        break
