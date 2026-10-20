def view_info_storaged(data_list): 
    try:
        if not data_list: 
            print("No student data available. Please enter students first")
        else:
            print(data_list)
    except Exception as error:
        print(f"Error due to {error}")
    return data_list
