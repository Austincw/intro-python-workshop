
#
# def words(params):
#     return params.split()
#
# test =  words("Hello world how are you")
# print test


# def student(age = 20, major="Comp Sci"):
#     print age, major
#
#
# student(major="computer engineering")
# student()


# for row in open("us_stores.csv", "r"):
#     row = row.rstrip()
#     data = row.split(',')
#     print "{0}: {1} ({2})".format(data[0], data[1], data[2].lstrip())
#     # formatData(data)
#     # print row


colors = ['yellow', 'blue', 'green', 'red', 'amber', 'mauve']

# print sorted(colors, reverse=True)


def sort_by_second_letter(text):
    print "{}: the second letter is {}".format(text, text[1])
    return text[1]

result = sorted(colors, key = sort_by_second_letter)
print result
