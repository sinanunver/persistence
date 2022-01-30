# import required module
import os
import re

# This is for sorting the files
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)


path = '/Users/sinanunver/Desktop/xy-of-boundary-points-classes_copy'

directory = os.listdir(path)


# This is to rearrange the names in the folder in a nice order and saving that as a list.
sorted_directory = sorted_alphanumeric(directory)

# This is to add the folder name to the above file extensions to be able to access the file.
fullpath_sorted_directory = []

for filename in sorted_directory:
    fullpath_sorted_directory.append('/Users/sinanunver/Desktop/xy-of-boundary-points-classes_copy/'+filename)


# for j in range(len(sorted_directory)):
#     # This is to make the lines in a file a list.
#
#     with open(fullpath_sorted_directory[j]) as f_in:
#         lines = [l for l in f_in]
#
#     # This is to get the annotations in a file
#     ann = []
#
#     for i in range(len(lines)):
#         ann.append(int(lines[i][-2]))
#
#     ann_set = set(ann)
#
#     print(ann_set)


f = open("../../../Library/Application Support/JetBrains/PyCharmCE2021.2/scratches/annotation.txt", "a")


# The following portion saves the information in a file rather than just printing it.


for j in range(len(sorted_directory)):
    # This is to make the lines in a file a list.

    with open(fullpath_sorted_directory[j]) as f_in:
        lines = [l for l in f_in]

    # This is to get the annotations in a file
    ann = []

    for i in range(len(lines)):
        ann.append(int(lines[i][-2]))

    ann_set = set(ann)
    string_set = fullpath_sorted_directory[j]+': '+ str(ann_set)+'\n'
    f.write(string_set)
f.close()


