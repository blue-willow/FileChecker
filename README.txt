=====================================================================================================
Please run the program with the following command:

python3 main.py [input_file_path]
=====================================================================================================
Clarification:

1. Currently support c, c++, java, python files with extension "c", "cc", "cpp", "h", "java", or "py"
=====================================================================================================
Assumptions: 

1. This program assumes the input file has no syntax error
2. For c, c++ and Java file:
   * This program counts all comments within "/* */" as block line comments
   * This program counts all comments after "//" as single line comments
3. For python file:
   * This program ignores comments with unoffical format (i.e. '''...''')
=====================================================================================================
