# Vladislavs Boičenko, 16.grupa
# 231RDB387

# 1.uzd
# name=[]
# with open("data.txt", "r") as file:
#     next(file)
#     for line in file:
#         row=line.rstrip().split(",")
#         country = row[4]
#         if country == 'Oman':
#             number_employee = row[6]
#             name.append(int(number_employee))
# print(min(name))


# 2.uzd
# name=[]
# with open("data.txt", "r") as file:
#     next(file)
#     for line in file:
#         row=line.rstrip().split(",")
#         country = row[4]
#         if country == 'Latvia':
#             number_employee = row[8]
#             name.append(int(number_employee))
# print(sum(name))


# 3.uzd
# name=[]
# with open("data.txt", "r") as file:
#     next(file)
#     for line in file:
#         row=line.rstrip().split(",")
#         country = row[4]
#         industry = row[7]
#         if country == 'Latvia' and industry == 'Telecommunications':
#             number_employee = row[8]
#             name.append(int(number_employee))

# print(sum(name))


# 4.uzd
# name=[]
# with open("data.txt", "r") as file:
#     next(file)
#     for line in file:
#         row=line.rstrip().split(",")
#         country = row[4]
#         web = row[3]
#         if country == 'Latvia'and 'https://' in web:
#             name.append(web)

# print(len(name))


# 5.uzd
# name=[]
# with open("data.txt", "r") as file:
#     next(file)
#     for line in file:
#         row=line.rstrip().split(",")
#         country = row[4]
#         web = row[3]
#         if country == 'Latvia' and '.org' in web:
#             name.append(web)

# print(len(name))
