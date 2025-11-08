def get_data():

    with open('list.txt') as file:
        data=file.read()
        data=data.split()
        return data
    