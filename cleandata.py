import os

#run this file to erase the data for testing

def cleandata():
    data_file = "medidata.csv"
    try:
        if os.path.exists(data_file):
            os.remove(data_file)
            print(f"{data_file} has been deleted successfully.")
        else:
            print(f"{data_file} does not exist, nothing to delete.")
    except Exception as e:
        print(f"Error occurred while deleting {data_file}: {e}")

if __name__ == "__main__":
    cleandata()
