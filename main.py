#
# Clarification:
# 1. Currently support c, c++, java, python files with extension "c", "cc", "cpp", "h", "java", or "py"
#
# Assumptions: 
# 1. This program assumes the input file has no syntax error
# 2. For c, c++ and Java file:
#    * This program counts all comments within "/* */" as block line comments
#    * This program counts all comments after "//" as single line comments
# 3. For python file:
#    * This program ignores comments with unoffical format (i.e. '''...''')

import sys
import os
import JavaStyleChecker
import PythonStyleChecker
from util import ReadFile

def Print(lines):
    for i in range(0, len(lines)):
        print("{}:  ".format(i)+lines[i])

def CheckInFile(file_name, Checker):
    lines = ReadFile(file_name)
    comment_lines = Checker.GetCommentLines(lines)
    single_line_comments = Checker.GetSingleLineComments(lines)
    block_comment_lines = Checker.GetBlockCommentLines(lines)
    total_block_comments = Checker.CountBlockComments(lines)
    total_TODOs = Checker.CountTODOs(lines)
    print("Total # of lines: ", len(lines))
    print("Total # of comment lines: ", len(comment_lines))
    print("Total # of single line comments: ", len(single_line_comments))
    print("Total # of comment lines within block comments: ", len(block_comment_lines))
    print("Total # of block line comments: ", total_block_comments)
    print("Total # of TODO's: ", total_TODOs)

if __name__ == "__main__":    
    java_style_extensions = ["c", "cc", "cpp", "h", "java"]
    python_style_extensions = ["py"]
    file_name = sys.argv[1]
    file_extension = file_name.split(".")[-1]    
    if not os.path.exists(file_name):
        print("Err: Invalid file path. File " + file_name + " does not exit")
    elif file_extension in java_style_extensions:
        CheckInFile(file_name, JavaStyleChecker)
    elif file_extension in python_style_extensions:
        CheckInFile(file_name, PythonStyleChecker)
    else:
        print("Err: Invalid file type. Please provide a file with following extensions: ")
        print(java_style_extensions, " or ", python_style_extensions)        
            
