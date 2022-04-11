"""This program uses data from a DataFrame to predict a result from other data
using a decision tree. It also lets the user to add data themselves.

Author: Simon Johansson
Estimated time: 10 hours
Actual time: 11 hours"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def menu():
    """Lets the user select an option and returns a number based on what option
    the user choses"""
    correct_input = False
    while correct_input == False:
        number_is_int = True
        print(f"1 Read CSV file\n2 Print current data\n3 Add manual data" +
        "\n4 Build decision tree\n5 Add new observation" +
        "\n6 Classify test data\n7 Exit program")
        try_user_choice = input("\nYour choice: ")
        try:
            int(try_user_choice)
        except ValueError:
            print("Input should be between 1 and 7")
            number_is_int = False

        if number_is_int:
            user_choice = int(try_user_choice)
            if 1 <= user_choice <= 7:
                return user_choice



def load_csv_file(search_file_name):
    """Loads a csv file from user input"""
    try:
        load_data_frame = pd.read_csv(search_file_name, dtype="category", sep=",")
    except:
        print("Error when reading file: File '" + search_file_name + "' does not exist")
        load_data_frame = pd.DataFrame()
        return load_data_frame

    load_data_frame = pd.read_csv(search_file_name, dtype="category", sep=",")

    return load_data_frame

def print_data_frame(data_frame_to_print):
    """Prints a DataFrame"""
    print(data_frame_to_print)

def add_data(data_frame_to_add):
    """Lets the user add data to a DataFrame"""
    new_data_list = []
    if len(data_frame_to_add) == 0:
        print("No data in the frame to add to")
        return data_frame_to_add
    else:
        identifier = input("Input the identifier: ")
        new_data_list.append(identifier)
        for catname in data_frame_to_add.columns[1:]:
            temp_list = []
            print(catname)
            for value in data_frame_to_add[catname]:
                temp_list.append(value)
            print("Possible values: " + str(temp_list))
            new_data = new_column_data(temp_list)
            new_data_list.append(new_data)
        new_series = pd.Series(new_data_list,index=data_frame_to_add.columns)
        data_frame_to_add = data_frame_to_add.append(new_series, ignore_index = True)
        return data_frame_to_add
     
def new_column_data(temp_list):
    """Checks if the Data the user choses is allowed"""
    new_data = input("Input value: ")
    if new_data in temp_list:
        return new_data
    else:
        new_column_data(temp_list)
        return new_data

def build_decision_tree(data_frame_to_tree):
    """Builds a decision tree"""
    if len(data_frame_to_tree) == 0:
        print("Error no data to create tree from")
        return None
    df_coded = pd.DataFrame()
    for catindex, catname in enumerate( data_frame_to_tree.columns ):
        df_coded[catname] = data_frame_to_tree[catname].astype("category").cat.codes

    data_elements = df_coded.iloc[:,1:-1]
    data_results = df_coded.iloc[:,-1]

    new_dtree = DecisionTreeClassifier(criterion='entropy', random_state=0)
    new_dtree.fit(data_elements,data_results)
    return new_dtree

def add_observation(data_frame_to_add_ob, new_test_data):
    """Adds an observation to a data_frame"""
    test_data_lst = []
    if len(data_frame_to_add_ob) == 0:
        print("No loaded data to create test data for")
        return new_test_data

    for catindex, catname in enumerate (data_frame_to_add_ob.columns):
        if 1 <= catindex < len(data_frame_to_add_ob.columns) - 1:
            row_list = []
            for value in data_frame_to_add_ob[catname]:
                row_list.append(value)

            print(data_frame_to_add_ob.columns[catindex])
            print(row_list)

            correct_input = False
            while not correct_input:
                try:
                    value = int(input("Choose the index of the desired option 0-" + str(len(row_list) - 1) + ": "))

                    if value < 0 or value > len(row_list) - 1:
                        raise ValueError

                    test_data_lst.append(int(value))
                    correct_input = True
                except ValueError:
                    print("Wrong value input.")

    df_length = len(test_data)
    new_test_data.loc[df_length] = test_data_lst

    return test_data

def classify(data_frame_to_classify, test_data_to_classify, dtree_to_classify):
    """Predicts the result from a DataFrame"""
    new_prediction_results = []

    if len(data_frame_to_classify) == 0:
        print("No loaded data to test against was found")
        return None
    elif len(test_data_to_classify) == 0:
        print("No loaded data to test against was found")
        return None
    elif dtree_to_classify == None:
        print("No loaded data to test against was found")
        return None

    test_prediction = dtree_to_classify.predict(test_data_to_classify)
    for i in test_prediction:
        new_prediction_results.append(data_frame_to_classify[data_frame_to_classify.columns[-1]].cat.categories.tolist()[i])

    return new_prediction_results


if __name__ == "__main__":
    program_is_running = True
    data_frame = pd.DataFrame()
    test_data = pd.DataFrame()
    dtree = None

    while program_is_running == True:
        user_choice = menu()
        if user_choice == 1:
            file_name = input("What is the name of the file you wish to load?: ")
            data_frame = load_csv_file(file_name)
            test_data = pd.DataFrame(columns=data_frame.columns[1:len(data_frame.columns)-1])
        elif user_choice == 2:
            print_data_frame(data_frame)
        elif user_choice == 3:
            data_frame = add_data(data_frame)
        elif user_choice == 4:
            dtree = build_decision_tree(data_frame)
        elif user_choice == 5:
            test_data = add_observation(data_frame, test_data)
        elif user_choice == 6:
            prediction_results = classify(data_frame, test_data, dtree)
            if prediction_results is not None:
                for results in prediction_results:
                    print(results)
        elif user_choice == 7:
            program_is_running = False
        else:
            print("Wrong value, try again")
