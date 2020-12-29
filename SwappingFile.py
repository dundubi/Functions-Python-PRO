def swap_files():
    file1 = input("Enter file name 1 ")
    file2 = input("Enter file name 2 ")
    """    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    data_a = f1.read()
    data_b = f2.read()
    f1 = open(file1, 'w')
    f2 = open(file2, 'w')
    f2.write(data_a)
    f1.write(data_b)"""
    with open(file1, 'r') as f1:
        data_a = f1.read()
    with open(file2, 'r') as f2:
        data_b = f2.read()
    with open(file1, 'w') as f1:
        f1.write(data_b)
    with open(file2, 'w') as f2:
        f2.write(data_a)
swap_files()
    