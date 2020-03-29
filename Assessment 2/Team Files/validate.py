import os


def verify_file(file_path):
    """ Verifying file contents."""
    # Check if file exist and it is empty
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0
 
 
def read_file(file_name):
    """ Verifying file contents by reading the first letter."""
    # open ile in read mode
    with open(file_name, 'r') as read_obj:
        # read first character
        one_char = read_obj.read(1)
        # if not fetched then file is empty
        if not one_char:
            return True
    return False
 
 
def main():
 
    print('Check if the file is empty or not.')
 
    file_path = 'classes_result.dot'
 
    # check if size of file is 0
    if os.stat(file_path).st_size == 0:
        print('File is empty')
    else:
        print('File is not empty')
 
    print('Check if file exists and is empty or not.')
 
    file_path = 'classes_result.dot'
    # check if file exist and it is empty
    is_empty = verify_file(file_path)
 
    if is_empty:
        print('File is empty')
    else:
        print('File is not empty')
 
    print('Check if file is empty by opening and it and reading its first character in Python.')
 
    file_path = 'classes_result.dot'
 
    # check if file is empty
    is_empty = read_file(file_path)
 
    print(is_empty)
 
 
if __name__ == '__main__':
    main()
