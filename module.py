# my_module.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_csv(path):
    df=pd.read_csv(path)
    return df
def load_jason(path):
    df=pd.read_json(path)
    return df
def dashboard():
    
 welcome_message = """

    ***************************************************
    *                                                 *
    *    🌍 Welcome to the Indian Tourism Analysis    *
    *              Dashboard by Tarun Kumar           *
    *                                                 *
    ***************************************************
    
    """
 print(welcome_message)

def preprocess_data(df):
    # Drop NaN values in the 'Year' column and reset index
    df = df.dropna(subset=['Year'])
    df = df.reset_index(drop=True)
    return df

def box_plot(df,col):
    # Create a box plot
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df[col])
    plt.title(f'Box Plot of {col}')
    plt.ylabel('Values')
    plt.show()

##------- Plot for Foreign Tourist Arrival and NRI Arrival over carious Years------##

def plot_ftas_nris(df):
    # Extract necessary columns
    years = df['Year']
    ftas_millions = df['FTAs in India (in million)']
    nris_millions = df['NRIs arrivals in India (in million)']

    # Create a line plot to visualize both FTAs and NRIs arrivals year-wise
    plt.figure(figsize=(14, 7))  # Adjust the figure size as needed
    plt.plot(years, ftas_millions, marker='o', linestyle='-', label='FTAs')
    plt.plot(years, nris_millions, marker='o', linestyle='-', label='NRIs')
    plt.title('Foreign Tourist Arrivals (FTAs) and NRIs Year-Wise')
    plt.xlabel('Year')
    plt.ylabel('Arrivals (Millions)')
    plt.grid(True)
    plt.xticks(years)
    plt.xticks(rotation=45)
    plt.legend()  # Add a legend to differentiate FTAs and NRIs
    plt.show()

#--------Plot for Inbound Tourist arrival in world------#

def plot_itas_world(df):
    years = df['Year']
    # World_ITA = df['World_ITA']
    # # Set the seaborn style
    sns.set(style="whitegrid")

    # Set up the matplotlib figure
    plt.figure(figsize=(14, 7))

    sns.lineplot(data=df, x='Year', y='World_ITA', marker='o')

    # Add labels and title
    plt.title('Foreign Tourist Arrivals (FTAs) in World Year-Wise')
    plt.xlabel('Year')
    plt.ylabel('Arrivals (Millions)')
    plt.xticks(years)
    plt.xticks(rotation=45)
    # plt.legend()  
    # Display the plot
    plt.show()



def preprocess_total_arrivals(df):
    df['NRIs arrivals in India'].fillna(0.73 * df['FTAs in India'], inplace=True)
    df['Total Arrivals'] = df['NRIs arrivals in India'] + df['FTAs in India']
    return df

def plot_total_arrivals(df):
    df['NRIs arrivals in India (in million)'].fillna(0.73*df['FTAs in India (in million)'], inplace=True)
    tot_arrivals = df['NRIs arrivals in India (in million)'] + df['FTAs in India (in million)']
    plt.figure(figsize=(14,7))
    years=df['Year'].astype(int)
    # plotting the bar (column) graph
    plt.figure(figsize=(14,7))

    g = sns.barplot(x=years, y=tot_arrivals, palette='viridis', label="Some Label")

    # Label the bars with values (rounded to two decimal places)
    for bar in g.containers[0]:
        yval = bar.get_height()
        g.text(bar.get_x() + bar.get_width()/2, yval, "{:.2f}".format(yval), ha='center', va='bottom', fontsize=8)

    plt.title("Total Arrivals [2001-2022]", fontsize=18)
    plt.xlabel("Year", fontsize=16)
    plt.ylabel("Arrivals in million", fontsize=16)

    plt.xticks(fontsize=12, rotation=45)

    plt.show()



#---------------Foreign exchange earnings (FEEs) from tourism vs FTA-------------#    

def plot_scatter_ftas_earnings(df,fee_data):
    #preprocessing
    df=preprocess_data(df)
    df['Foreign_Exchange_Earnings'] = fee_data
    # Assuming df has columns 'FTAs in India (in million)' and 'Foreign_Exchange_Earnings'
    ftas = df['FTAs in India (in million)']
    earnings = df['Foreign_Exchange_Earnings']

    # Create a scatterplot
    plt.figure(figsize=(8, 6))
    plt.scatter(ftas, earnings, alpha=0.5, color='b')
    plt.title('Scatterplot of FTAs in India vs. Foreign Exchange Earnings')
    plt.xlabel('FTAs in India (in million)')
    plt.ylabel('Foreign Exchange Earnings (in billion USD)')
    plt.grid(True)
    plt.show()

#-----------Arrivals by Mode of Travel (Year-wise)-----------#

def plot_of_mode(path):
    mode_data = {
    'Year': [ 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Arrivals': [ 6309222, 6577745, 6967601, 7679099, 8027133, 8804411, 10035803, 10557976, 10930355, 2744766, 1527114],
    '% Air': [ 92.0, 91.7, 91.0, 86.1, 84.5, 84.1, 79.6, 79.6, 77.4, 79.2, 87.5],
    '% Sea': [ 0.8, 0.7, 0.5, 0.4, 0.7, 0.9, 0.7, 0.8, 0.9, 1.5, 0.7],
    '% Land': [ 7.2, 7.6, 8.5, 13.5, 14.8, 15.0, 19.7, 19.6, 21.7, 19.3, 11.8]
      }
    
    df = pd.DataFrame(mode_data)
    year=df.Year

    # Plotting year-wise data
    plt.figure(figsize=(12, 6))
    plt.plot(df['Year'], df['% Air'], label='% Air', marker='o')
    plt.plot(df['Year'], df['% Sea'], label='% Sea', marker='o')
    plt.plot(df['Year'], df['% Land'], label='% Land', marker='o')
    plt.title('Arrivals by Mode of Travel (Year-wise)')
    plt.xlabel('Year')
    plt.xticks(year)
    plt.ylabel('Percentage Distribution')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Creating a pie chart for the average distribution
    average_distribution = df[['% Air', '% Sea', '% Land']].mean()
    labels = ['Air', 'Sea', 'Land']
    plt.figure(figsize=(6, 6))
    plt.pie(average_distribution, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Average Distribution of Arrivals by Mode of Travel', pad=20)  # Adjust title position
    plt.axis('equal')
    plt.legend(loc="best")  # Place legend in the best available location
    plt.show()

    #
    try:
        df = pd.read_json(path, orient='split')
    except ValueError as e:
        print(f"Error reading JSON at path: {path}")
        print(e)
        return

    cities = ['% Delhi', '% Mumbai', '% Haridaspur', '% Chennai', '% Bengaluru', '% Kolkata', '% Cochin', '% Hyderabad', '% Others']

    # Select the data for a specific year (2015)
    year_2015 = df.loc[2015, cities]

    # Create a pie chart for the percentage distribution of FTAs for the year 2021
    plt.figure(figsize=(8, 8))
    plt.pie(year_2015, labels=year_2015.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of FTAs by Major Ports in 2015', pad=20)
    plt.axis('equal')
    plt.show()

    # Select the data for a specific year (e.g., 2021)
    year_2021 = df.loc[2021, cities]
    
    # Create a pie chart for the percentage distribution of FTAs for the year 2021
    plt.figure(figsize=(8, 8))
    plt.pie(year_2021, labels=year_2021.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of FTAs by Major Ports in 2021', pad=20)
    plt.axis('equal')
    plt.show()
 

#------------Statistics of ITAs to India based on purpose 2019------------#
    
def top_source_countries_and_purpose(path):
    # fetching data from csv file
    country_and_reason=pd.read_csv(path)
    # Parsing dataframe
    countrywise=country_and_reason[country_and_reason['Country of Nationality'].isin(['Total','Grand Total','Not Classified Elsewhere','OTHERS'])==False].copy()
    # Sorting w.r.t Arrivals in descending order
    countrywise.sort_values(by=["Arrivals (in numbers)"],ascending=False, inplace = True)
    # fetching 10 countries with top arrivals
    countrywise.drop(["Region"],axis=1,inplace=True)

    top10_country=countrywise.iloc[0:10,:]

    #top_10 country data from 2022(ministry of tourism website)
    countries2022 = ['UNITED STATES', 'BANGLADESH', 'UNITED KINGDOM', 'AUSTRALIA', 'CANADA', 'SRI LANKA', 'NEPAL', 'GERMANY', 'SINGAPORE', 'MALAYSIA']
    counts2022 = [1373817, 1255960, 617768, 369023, 277291, 177652, 135347, 124496, 117195, 116523]

    #Arrivals by Country of Nationality in 2019
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Country of Nationality', y='Arrivals (in numbers)', data=top10_country,palette='deep')
    plt.title('Arrivals by Country of Nationality in 2019')
    plt.xlabel('Country of Nationality')
    plt.ylabel('Arrivals (in numbers)')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.show()

    #Arrivals by Country of Nationality in 2022
    sns.set(style="whitegrid")
    sns.set_palette("pastel")
    plt.figure(figsize=(12, 8))
    sns.barplot(x=countries2022, y=counts2022, palette='bright')
    plt.title('Arrivals by Country of Nationality in 2022')
    plt.xlabel('Country of Nationality')
    plt.ylabel('Arrivals (in numbers)')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.show()

  
    # fetching 5 countries with top arrivals and plot for purpose
    countrywise=countrywise.iloc[0:5,:]

    # Renaming columns
    countrywise.rename(columns={
        'Business and Professional(%)':'Business and Professional',
        'Leisure Holiday and Recreation(%)':'Leisure Holiday and Recreation',
        'Medical(%)':'Medical',
        'Indian Diaspora(%)':'Indian Diaspora',
        'Others(%)':'Others'
    },inplace=True)

    # converting %ages to actual values and shifting the decimal places by 3 to the left
    countrywise['Business and Professional']=countrywise['Business and Professional']*countrywise['Arrivals (in numbers)']/100 * 10**-3
    countrywise['Leisure Holiday and Recreation']=countrywise['Leisure Holiday and Recreation']*countrywise['Arrivals (in numbers)']/100 * 10**-3
    countrywise['Medical']=countrywise['Medical']*countrywise['Arrivals (in numbers)']/100* 10**-3
    countrywise['Indian Diaspora']=countrywise['Indian Diaspora']*countrywise['Arrivals (in numbers)']/100* 10**-3
    countrywise['Others']=countrywise['Others']*countrywise['Arrivals (in numbers)']/100* 10**-3
    countrywise["Arrivals (in numbers)"]=countrywise["Arrivals (in numbers)"]/10**3

    # Combining columns w.r.t nationality into a single column 'value' and column 'variable' will distinguish these values 
    df=pd.melt(countrywise,['Country of Nationality']).rename(columns={"variable":"Reason of Visit"})

    # plotting bar (multicolumn) graph
    plt.figure(figsize=(20,8))
    # country v / s reason barplot
    sns.barplot(x ='Country of Nationality',y='value', hue="Reason of Visit",data = df, palette='Paired')

    plt.ylabel("Arrivals (in thousands)",fontsize=18)
    plt.xlabel('Country of Nationality',fontsize=18)
    plt.title("Tourists to India from Top 5 countries (2019)",fontsize=20,fontweight='bold')
    # Show the plot
    plt.show()
    
    #Average Distribution of Tourists to India based on the purpose of visit - 2019

    # fetching the grand total information
    grand_total = country_and_reason[country_and_reason['Country of Nationality'] == 'Grand Total'].copy()

    reason_list = ['Business and Professional(%)', 'Leisure Holiday and Recreation(%)', 'Medical(%)', 'Indian Diaspora(%)', 'Others(%)']
    colors = ['indianred', 'orange', 'deepskyblue', 'turquoise', 'palegreen']  

    # plotting data on pie chart
    plt.figure(figsize=(8, 6))

    pie = plt.pie(grand_total.loc[83, :].values.tolist()[3:], colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 15}, pctdistance=1.15)

    # plt.legend()
    plt.legend(pie[0], reason_list, bbox_to_anchor=(1.5, 0.7), loc="upper right", fontsize=15,
            bbox_transform=plt.gcf().transFigure)

    plt.title("Average distribution of tourists based on purpose of visit - 2019", fontsize=22, fontweight='bold')

    # displaying chart
    plt.show()

    

#------ Countrywise contributions to the Indian tourism market from 2017 to 2019.-------#

def Contribution_tourism(path):
     # Fetching data from csv file
    country_and_share = pd.read_csv(path)

    # List of years
    years = ['2017', '2018', '2019']

    # Plotting subplots (pie charts)
    fig, axes = plt.subplots(1, 3, sharex=True, figsize=(20, 8))
    fig.suptitle('Percentage shares of countries on Indian Tourism [2017, 2018, 2019]', fontsize=25, fontweight='bold')

    colors = ['darkcyan', 'mediumblue', 'darkorchid', 'aqua', 'seagreen', 'maroon', 'gold']

    for i, year in enumerate(years):
        # Obtaining 6 countries with the highest shares for the current year
        highest_countrywise = country_and_share[
            (country_and_share['Country of Nationality'].isin(['Total', 'Grand Total', 'Not Classified elsewhere', 'Others']) == False)
            & (f'Percentage Share - {year}' in country_and_share.columns)
        ].copy()
        highest_countrywise = highest_countrywise[['Country of Nationality', f'Percentage Share - {year}']]
        highest_countrywise.sort_values(by=[f'Percentage Share - {year}'], ascending=False, inplace=True)
        highest_countrywise = highest_countrywise.iloc[0:6, :]

        # %age share values sum of the current year
        perc_sum = highest_countrywise[f'Percentage Share - {year}'].sum()

        # Accumulating the total %age share by the rest of the countries
        highest_countrywise = pd.concat(
            [highest_countrywise, pd.DataFrame.from_records(
                [{'Country of Nationality': 'Others', f'Percentage Share - {year}': (100 - perc_sum)}])],
            ignore_index=True)

        # Plotting pie chart for the current year
        pie = axes[i].pie(highest_countrywise[f'Percentage Share - {year}'], colors=colors, shadow=True, startangle=90)
        percents = highest_countrywise[f'Percentage Share - {year}'] * 100 / highest_countrywise[
            f'Percentage Share - {year}'].sum()

        #providing legend
        axes[i].legend(
            pie[0], [f'{p:.1f}% {l}' for p, l in zip(percents, highest_countrywise['Country of Nationality'])],
            bbox_to_anchor=(0.2 + i * 0.26, 0.5),
            loc="upper right", fontsize=12,
            bbox_transform=plt.gcf().transFigure, framealpha=0.7)
        
        axes[i].set_title(year, fontsize=20, fontweight='bold')


    # Displaying the chart
    plt.show()


#  ------Average Duration of Stay by Region and Country of Nationality-------

def avg_duration_stay(path):
    df=pd.read_csv(path)
    regionwise_stay=df[df['Country of Nationality']=='Total'].copy()
    regionwise_stay.drop(['Country of Nationality'], inplace=True, axis=1)
    regionwise_stay.sort_values(by=["Average duration of stay (in days)"],ascending=False, inplace = True)

    # Plot of Region vs avg_duration_stay
    plt.figure(figsize=(14, 8))
    sns.barplot(x='Region', y='Average duration of stay (in days)', data=regionwise_stay)
    plt.title('Average Duration of Stay by Region', fontsize=16)
    plt.xlabel('Region', fontsize=14)
    plt.ylabel('Average Duration of Stay (in days)', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=12) 
    plt.yticks(fontsize=12)
    sns.despine()
    plt.show()

    countrywise_stay = df[~df['Country of Nationality'].isin(['Total', 'Grand Total', 'Not Classified Elsewhere', 'OTHER', 'Others'])]
    countrywise_stay = countrywise_stay.copy()
    countrywise_stay.drop(['Region'], inplace=True, axis=1)
    countrywise_stay.sort_values(by=["Average duration of stay (in days)"],ascending=False, inplace = True)
    countrywise_stay_15k=countrywise_stay[countrywise_stay['Total (in Number)']>15000]
   

    # Average Duration of Stay by Country of Nationality at least spent 15k days
    plt.figure(figsize=(14, 8))
    sns.barplot(x='Country of Nationality', y='Average duration of stay (in days)', data=countrywise_stay_15k)
    plt.title('Average Duration of Stay by Country of Nationality', fontsize=16)
    plt.xlabel('Country of Nationality', fontsize=14)
    plt.ylabel('Average Duration of Stay (in days)', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=12)  
    plt.yticks(fontsize=12)
    sns.despine()
    plt.show()


#-----Indian Tourism Statewise Statistics-----

def statewise_stat(path1, path2):
    # fetching data from the csv file
    statewise_data=pd.read_csv(path1)
    # Parsing dataframe
    foreign_statewise=statewise_data[['States/UTs','Foreign - 2019','Foreign - 2020']].copy()
    # sorting by Foreign-2019 in descending order
    foreign_statewise.sort_values(by=['Foreign - 2019'], ascending=False, inplace=True)
    #Takin only top 18 states
    foreign_statewise=foreign_statewise.iloc[0:17]
    foreign_statewise=foreign_statewise[foreign_statewise['States/UTs'].isin(['Grand Total'])==False]

    # shifting the decimal places by 5 to the left
    foreign_statewise['Foreign - 2019']=foreign_statewise['Foreign - 2019'] * 10**-5
    foreign_statewise['Foreign - 2020']=foreign_statewise['Foreign - 2020'] * 10**-5

    foreign_statewise.head()
    # Combining columns w.r.t 'States/UTs' into a single column 'value' and column 'variable' will distinguish these values 
    df=pd.melt(foreign_statewise,['States/UTs']).rename(columns={"variable":"Year"})

    # horizontal bar graph
    plt.figure(figsize=(16,50))
    ax = sns.barplot(x="value", y="States/UTs", data=df, hue='Year', palette='GnBu_d')

    for p in ax.patches:
        width = p.get_width()    # get bar length
        ax.text(width + 0.5,       # set the text at 1 unit right of the bar
                p.get_y() + p.get_height() / 2, # get Y coordinate + X coordinate / 2
                '{:1.2f}'.format(width), # set variable to display, 2 decimals
                ha = 'left',   # horizontal alignment
                va = 'center',  # vertical alignment
                fontsize=14)
            
    plt.title("Foreign tourists per State/UTs [2019, 2020]", fontsize=20, fontweight='bold')
    plt.xlabel("Arrivals (in lakhs)", fontsize=18)
    plt.ylabel("States/UTs", fontsize=18)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.legend(bbox_to_anchor=(0.99,0.95), prop={'size': 16})
    plt.show()

    #domestic Travellers

    # Parsing dataframe
    domestic_statewise=statewise_data[['States/UTs','Domestic -2019','Domestic -2020']].copy()
    # sorting by Domestic-2019 in descending order
    domestic_statewise.sort_values(by=['Domestic -2019'], ascending=False, inplace=True)
    domestic_statewise=domestic_statewise[domestic_statewise['States/UTs'].isin(['Grand Total'])==False]
    #taking only top 18 states
    domestic_statewise=domestic_statewise.iloc[0:17]

    # shifting the decimal places by 5 to the left
    domestic_statewise['Domestic -2019']=domestic_statewise['Domestic -2019'] * 10**-5
    domestic_statewise['Domestic -2020']=domestic_statewise['Domestic -2020'] * 10**-5

    # Combining columns w.r.t 'States/UTs' into a single column 'value' and column 'variable' will distinguish these values 
    df=pd.melt(domestic_statewise,['States/UTs']).rename(columns={"variable":"Year"})

    # plotting data on horizontal bar graph
    plt.figure(figsize=(16,50))
    ax = sns.barplot(x="value", y="States/UTs", data=df, hue='Year', palette='flare')

    for p in ax.patches:
        width = p.get_width()    # get bar length
        ax.text(width + 1,       # set the text at 1 unit right of the bar
                p.get_y() + p.get_height() / 2, # get Y coordinate + X coordinate / 2
                '{:1.2f}'.format(width), # set variable to display, 2 decimals
                ha = 'left',   # horizontal alignment
                va = 'center',  # vertical alignment
                fontsize=14)
                
    plt.title("Domestic tourists per State/UTs [2019, 2020]", fontsize=20, fontweight='bold')
    plt.xlabel("Arrivals (in lakhs)", fontsize=18)
    plt.ylabel("States/UTs", fontsize=18)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.legend(bbox_to_anchor=(0.99,0.95), prop={'size': 16})

    # display the chart
    plt.show()

    # parsing the dataframe
    total_statewise=statewise_data[['States/UTs','Domestic -2019','Foreign - 2019','Domestic -2020','Foreign - 2020']].copy()
    # calculating total tourists to States/UTs
    total_statewise['Total Tourists']= total_statewise['Domestic -2019']+ total_statewise['Foreign - 2019']+ total_statewise['Domestic -2020']+ total_statewise['Foreign - 2020']

    total_statewise.drop(['Domestic -2019','Foreign - 2019','Domestic -2020','Foreign - 2020'], axis=1, inplace=True)
    # sorting by Total Tourists in descending order
    total_statewise.sort_values(by=["Total Tourists"], ascending=False, inplace=True)
    total_statewise=total_statewise[total_statewise['States/UTs'].isin(['Grand Total'])==False]
    # shifting the decimal places by 6 to the left
    total_statewise["Total Tourists"]=total_statewise['Total Tourists']* 10**-6

    # fetching the 10 most visited States/UTs
    total_statewise=total_statewise.iloc[0:10]

    total_statewise.head()

    # plotting the bar graph
    plt.figure(figsize=(20,8))

    g=sns.barplot(x=total_statewise['States/UTs'], y=total_statewise['Total Tourists'], palette='YlOrBr_r')

    plt.title("Total Tourists by States/UTs [2019-2020]", fontsize=18)
    plt.xlabel("States/UTs", fontsize=16)
    plt.ylabel("Total Tourists (in million)", fontsize=16)
    plt.xticks(fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    g.bar_label(g.containers[0], fontsize=15) # labelling the bars
    # displaying the chart
    plt.show()


    ########--------------Top 10 Tourism Destinations-------------#######

     # fetching data from the csv file
    monuments=pd.read_csv(path2)
    # parsing the dataframe
    circlewise_tourist=monuments[monuments['Name of the Monument']=='Total'].copy()
    circlewise_tourist.drop(['Name of the Monument'], inplace= True, axis=1)


    sorted_df = circlewise_tourist.sort_values(by='Foreign-2019-20', ascending=False)
    # Take the top 10 rows
    top_10_foreign = sorted_df.head(10)
    # Plotting Circles Visited by Foreign Tourists
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Circle', y='Foreign-2019-20', data=top_10_foreign, palette='viridis')
    plt.title('Top 10 Circles Visited by Foreign Tourists in 2019-20')
    plt.xlabel('Circle')
    plt.ylabel('Foreign Tourists (2019-20)')
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()
    plt.show()

    # Sort the DataFrame based on the 'Domestic-2019-20' column in descending order
    sorted_df = circlewise_tourist.sort_values(by='Domestic-2019-20', ascending=False)
    # Take the top 10 rows
    top_10_domestic = sorted_df.head(10)
    # Plotting with seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Circle', y='Domestic-2019-20', data=top_10_domestic, palette='viridis')
    plt.title('Top 10 Circles Visited by Domestic Tourists in 2019-20')
    plt.xlabel('Circle')
    plt.ylabel('Domestic Tourists (2019-20)')
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()
    plt.show()

    ## Top 10 Monuments visited by foreigners and domestic tourist 2019

    # Parsing the dataframe for top visited place
    monument_visited=monuments[monuments['Name of the Monument'].isin(['Total','Grand Total'])==False].copy()
    sorted_df = monument_visited.sort_values(by='Foreign-2019-20', ascending=False)
    top_10_foreign = sorted_df.head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Name of the Monument', y='Foreign-2019-20', data=top_10_foreign, palette='viridis')
    plt.title('Top 10 Circles Visited by Foreign Tourists in 2019-20')
    plt.xlabel('Circle')
    plt.ylabel('Foreign Tourists (2019-20)')
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()
    plt.show()

    #Top 10 Mounments Visited by Domestic Tourists in 2019-20
    sorted_df = monument_visited.sort_values(by='Domestic-2019-20', ascending=False)
    top_10_domestic = sorted_df.head(10)
    # Plotting with seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Name of the Monument', y='Domestic-2019-20', data=top_10_domestic, palette='viridis')
    plt.title('Top 10 Mounments Visited by Domestic Tourists in 2019-20')
    plt.xlabel('Mounments')
    plt.ylabel('Domestic Tourists (2019-20)')
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()
    # Show the plot
    plt.show()


#-----------Position of Indian Tourism in the world [2001 - 2021]------------#


def worldranking(path):
    # Fetching data from the CSV file
    worldvsindia = pd.read_csv(path)

    # Parsing the dataframe
    worldvsindia_rank = worldvsindia[['Year', 'World - Number (in million)', 'India - Number (in million)', 'Rank of India']].copy()
    worldvsindia_rank.fillna('54th', inplace=True)

    # Displaying data on a line chart
    plt.figure(figsize=(20, 8))

    g = sns.lineplot(x='Year', y='India - Number (in million)', data=worldvsindia_rank, marker='v', markersize=14)
    g.set(xlabel="Year", ylabel="Number of tourists (in million)", title="Indian Tourism rank in the world [2001-2019]")

    plt.xticks(
        range(2001, 2022),
        fontweight='light'
    )

    # Label markers with ranks
    for x, index in zip(g.get_xticks(), worldvsindia_rank.index):
        g.text(x, worldvsindia_rank.at[index, 'India - Number (in million)'] + 0.5, worldvsindia_rank.at[index, 'Rank of India'], size=15)

    plt.grid(True)
    plt.show()



        
        



