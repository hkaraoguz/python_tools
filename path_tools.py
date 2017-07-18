#!/usr/bin/env python
import os


def get_sorted_filenames(path,file_endings=[]):
    """
    Get sorted filenames in a directory.
    File endings can be specified with file_endings argument
    """

    sorted_filenames = []
    filenames = os.listdir(path)
    filenames.sort()

    if file_endings:
        for filename in filenames:
            for file_ending in file_endings:
                if filename.endswith(file_ending):
                    sorted_filenames.append(filename)
                    break
    else:
        return filenames

    return sorted_filenames

def get_absolute_paths(relative_path,filenames):
    """
    Get the absolute paths for files in the relative path
    """

    absolute_paths = []

    for filename in filenames:
        relative_full_path = os.path.join(relative_path,filename)
        absolute_paths.append(os.path.abspath(relative_full_path))

    return absolute_paths
