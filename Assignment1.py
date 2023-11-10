# importing the required python packages
import pandas as pd
import matplotlib.pyplot as plt

# Reading the data set "Cars93.csv" using pandas and assigning it to car_models
car_models = pd.read_csv("Cars93.csv")

# Specifying the required column names from the csv file "Cars.93"
selected_columns = ["Model", "Type", "Min.Price",
                    "Price", "Max.Price", "MPG.city", "MPG.highway"]
car_models = car_models[selected_columns]

# Selecting the data of the first fifteen car models and printing
first_15_car_models = car_models.head(15)
print(first_15_car_models)

# Filter car models actual price, maximum price, and minimum price
price_of_car = first_15_car_models[first_15_car_models["Price"] > 0]
maximum_price_of_car = first_15_car_models[first_15_car_models["Max.Price"] > 0]
minimum_price_of_car = first_15_car_models[first_15_car_models["Min.Price"] > 0]

# Grouping the Price_of_car DataFrame by the "Model" column and calculating the sum of the "Price" column for each group.
price_of_car_models = price_of_car.groupby("Model")["Price"].sum()

# Grouping the Maximum_Price_of_car DataFrame by the "Model" column and calculating the sum of the "Max.Price" column for each group.
maximum_price_of_car_models = maximum_price_of_car.groupby("Model")["Max.Price"].sum()

# Grouping the Minimum_Price_of_car DataFrame by the "Model" column and calculating the sum of the "Min.Price" column for each group.
minimum_price_of_car_models = minimum_price_of_car.groupby("Model")["Min.Price"].sum()

# Counting the occurrences of each unique value in the 'Type' column of the first_15_car_models DataFrame.
type_of_car_models = first_15_car_models['Type'].value_counts()


# Define a function to plot line graph
def plot_line_graph(price, max_price, min_price):
    """
    Plots a line graph to visualize the fluctuation in prices of different car models.

    Parameters:
    - price: Series or list, representing the actual prices of car models.
    - max_price: Series or list, representing the maximum prices of car models.
    - min_price: Series or list, representing the minimum prices of car models.
    """
    # Plotting actual prices in black coloured line
    plt.plot(price, color='#000000', label='Actual Price')

    # Plotting maximum prices in blue coloured line
    plt.plot(max_price, color='#00008B', label='Maximum Price')

    # Plotting minimum prices in red coloured line
    plt.plot(min_price, color='#FF0000', label='Minimum Price')

    # Adding title to the plot
    plt.title('Fluctuation in Price of Different Car Models')

    # Adding labels to the x and y axes
    plt.xlabel("Car Model", fontsize=14)
    plt.ylabel('Price of the car (in 1000 pounds)', fontsize=14)

    # Adding a legend to distinguish between actual, maximum, and minimum prices
    plt.legend(loc='best')

    # Rotating x-axis labels for better readability
    plt.xticks(rotation=90)

    # Displaying the plot
    plt.show()


# Call the function and passing the parameters to plot the line graph
plot_line_graph(price_of_car_models, maximum_price_of_car_models, minimum_price_of_car_models)

# Define a function to plot pie chart
def plot_pie(model_type):
    """
    Plots a pie chart to visualize the distribution of car types.

    Parameters:
    - model_type: Series, representing the count of each car type.
    """
    # Setting up the figure size
    plt.figure(figsize=(6, 6))

    # Plotting the pie chart with labels, percentage format, and starting angle
    plt.pie(model_type, labels=model_type.index,
            autopct='%1.1f%%', startangle=140)

    # Adding a title to the pie chart
    plt.title('Distribution of Car Types')

    # Displaying the pie chart
    plt.show()


# Calling the plot_pie function with the 'type_of_car_models' Series
plot_pie(type_of_car_models)

# Define a function to plot stacked bar graph
def plot_bar(first_15_car_model):
    """
    Plots a stacked bar chart to compare MPG (Miles per Gallon) for city and highway for the top 15 car models.

    Parameters:
    - first_15_car_model: DataFrame, containing information about the top 15 car models.
    """
    # Setting up the figure size
    plt.figure(figsize=(12, 6))

    # Plotting the bar chart for MPG City
    plt.bar(first_15_car_models['Model'],
            first_15_car_models['MPG.city'], label='MPG City', width=0.5)

    # Plotting the bar chart for MPG Highway, stacked on top of MPG City
    plt.bar(first_15_car_models['Model'], first_15_car_models['MPG.highway'],
            label='MPG Highway', width=0.5, bottom=first_15_car_models['MPG.city'])

    # Adding labels and title to the bar chart
    plt.xlabel('Car Model')
    plt.ylabel('Miles per Gallon (MPG)')
    plt.title('MPG City vs. MPG Highway for Top 15 Car Models')

    # Rotating x-axis labels for better readability
    plt.xticks(rotation=90)

    # Adding a legend to distinguish between MPG City and MPG Highway
    plt.legend()

    # Adjusting layout for better visualization
    plt.tight_layout()

    # Displaying the bar chart
    plt.show()


# Calling the plot_bar function with the 'first_15_car_models' DataFrame
plot_bar(first_15_car_models)
