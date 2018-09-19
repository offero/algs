#!/usr/bin/env python3

'''
Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
'''

def find_nth(string, char, n):
    idx = -1
    ct = 0
    for i, c in enumerate(string):
        if c == char:
            ct += 1
        if ct >= n:
            idx = i
            break
    return idx


def deepest_filepath(dirstr):
    maxpath = ''
    i = dirstr.find('\n')
    path = dirstr[:i]
    i += 1
    path_depth = 0
    while i <= len(dirstr):
        # consume all /t chars
        seg_depth = 0
        while True:
            if dirstr[i] != '\t':
                break
            seg_depth += 1
            i += 1

        j = dirstr.find('\n', i)
        if j == -1:
            j = len(dirstr)

        if seg_depth <= path_depth:
            n = find_nth(path, '/', seg_depth)
            path = path[:n]

        # consume till the next n
        path = path + '/' + dirstr[i:j+1]
        path_depth = seg_depth + 1

        i = j + 1  # consume the \n

        if path.rfind('.') > -1 and len(path) > len(maxpath):
            maxpath = path

    return maxpath


def main():
    dirstr = input()

def test():
    dirstr1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    dirstr2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    assert deepest_filepath(dirstr1) == 'dir/subdir2/file.ext'
    assert deepest_filepath(dirstr2) == 'dir/subdir2/subsubdir2/file2.ext'

if __name__ == "__main__":
    main()
