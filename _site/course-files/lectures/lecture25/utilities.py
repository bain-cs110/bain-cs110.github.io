def get_file_path(file_name, subdirectory=None):
    import os
    import sys
    dir_path = os.path.dirname(sys.argv[0])
    if subdirectory:
        return os.path.join(dir_path, subdirectory, file_name)
    else:
        return os.path.join(dir_path, file_name)

def sort_dictionary(d:dict, reverse=True):
    import collections
    sorted_keys = sorted(d, key=d.get, reverse=reverse)
    new_dictionary = collections.OrderedDict()
    for key in sorted_keys:
        new_dictionary[key] = d[key]
    return new_dictionary
