# project.py

import module as mod

def main():
    mod.dashboard()

    while True:
        print("Select the type of plot:")
        print("1. Foreign Tourist Arrivals (FTAs) and NRIs Year-Wise")
        print("2. Distribution of ITA")
        print("3. Foreign exchange earnings (FEEs) from tourism vs FTA")
        print("4. Arrivals by Mode of Travel (Year-wise)")
        print("5. Statistics of ITAs to India based on Counts and Purpose")
        print("6. Countrywise contributions to the Indian tourism market.")
        print("7. Average Duration of Stay by Region and Country of Nationality.")
        print("8. Indian Tourism Statewise Statistics(foreign and domestic travellers) and Top 10 Tourism Destinations")
        print("9. Position of Indian Tourism in the world [2001 - 2021]")
        print("Enter 'q' to quit")

        
        choice = input("Enter your choice: ")
        
        if choice.lower() == 'q':
            break

        if choice=='1':
            file_path = "data\India-Tourism-Statistics-2001-2020-fta_nri_ita.csv"
            df = mod.load_csv(file_path)

            # Preprocess data
            df = mod.preprocess_data(df)

            # Plot FTAs and NRIs
            mod.plot_ftas_nris(df)
            mod.box_plot(df,'FTAs in India (in million)')
            mod.plot_itas_world(df)
            mod.box_plot(df,"World_ITA")

        elif choice == '2':
            #Path for total arrivals
            file_path = "data\India-Tourism-Statistics-1981-2020-fta_nri_ita.csv"
            df_total = mod.load_csv(file_path)
            df_total=mod.preprocess_data(df_total)
            mod.plot_total_arrivals(df_total)
        
        elif choice == '3':
            file_path = "data\India-Tourism-Statistics-1981-2020-fta_nri_ita.csv"
            df = mod.load_csv(file_path)
            import numpy as np
            #FEEs data from ministry of Tourism
            fee_data = np.array([
                3.2, 3.1, 4.46, 6.17, 7.48, 8.63, 10.73, 11.83, 11.39,
                14.19, 16.56, 17.74, 18.39, 19.7, 21.1, 23.15, 27.69, 28.59, 30.06, 6.96, 8.8, 16.93
                ])
            mod.plot_scatter_ftas_earnings(df, fee_data)

        elif choice== '4':
            #plot for modes of travel used by tourists and Arrival by Port
            path="data\\airport_arrival"
            mod.plot_of_mode(path)
        
        elif choice=='5':
            #Statistics of ITAs to India based on purpose 2019
            #Tourists to India from Top 5 countries - 2019
            path="data\\India-Tourism-Statistics-2019_region-and-reason.csv"
            # plot for:
            # Top Arrivals by Country of Nationality in 2019
            # Top 10 Arrivals by Country of Nationality in 2022
            # Tourists to India from Top 5 countries (2019) with purpose"
            mod.top_source_countries_and_purpose(path)

        elif choice=='6':
            #Countrywise contributions to the Indian tourism market from 2017 to 2019.
            path="data\\India-Tourism-Statistics-region-2017-2019.csv"
            mod.Contribution_tourism(path)
        
        elif choice=='7':
            #Average Duration of Stay by Region and Country of Nationality
            path="data\\India-Tourism-Statistics-2022-Table-2.9.1.csv"
            mod.avg_duration_stay(path)

        elif choice=='8':
            #Indian Tourism Statewise Statistics and Top 10 Tourism Destinations 
            path1="data\\India-Tourism-Statistics-statewise_2019-2020_domestic_foreign.csv"
            path2='data\\India-Tourism-Statistics-2021-monuments.csv'
            mod.statewise_stat(path1, path2)
        
        elif choice=='9':
            #Position of Indian Tourism in the world [2001 - 2021]
            path='data\\India-Tourism-Statistics-2001-2019-worldvsindia.csv'
            mod.worldranking(path)

            
        else:
            print("Invalid choice. Please enter a value between 1 to 9 or 'q' to quit.")

if __name__ == "__main__":
    main()
