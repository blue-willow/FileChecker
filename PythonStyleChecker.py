from util import ReadFile, FindNextString, FindFirstNonSpaceChar

# Return a list of all lines containing comments
def GetCommentLines(lines):
    comment_lines = []
    is_in_string_double = False
    is_in_string_single = False
    for line in lines:
        begin_index = 0
        while True:
            if is_in_string_double:
                if line.find('"', begin_index) != -1:
                    is_in_string_double = False
                    begin_index = line.find('"', begin_index)+1
                else:
                    break
            elif is_in_string_single:
                if line.find("'", begin_index) != -1:
                    is_in_string_single = False
                    begin_index = line.find("'", begin_index)+1
                else:
                    break
            else:
                comment_start = line.find('#', begin_index)
                string_start = FindNextString(line, begin_index)
                if comment_start != -1 and string_start == -1:
                    comment_lines.append(line)
                    break                      
                elif comment_start == -1 and string_start != -1:
                    if line[string_start] == '"':
                        is_in_string_double = True
                    else:
                        is_in_string_single = True
                    begin_index = string_start+1
                elif comment_start == -1 and string_start == -1:
                    break
                else:
                    if comment_start < string_start:
                        comment_lines.append(line)
                        break
                    else:
                        if line[string_start] == '"':
                            is_in_string_double = True
                        else:
                            is_in_string_single = True
                        begin_index = string_start+1             
    return comment_lines

# Return the list of all lines containing single-line comments
def GetSingleLineComments(lines):
    single_line_comments = GetCommentLines(lines)
    block_comment_lines = GetBlockCommentLines(lines)
    for line in block_comment_lines:
        single_line_comments.remove(line)
    return single_line_comments

# Return the list of all lines containing block comments
def GetBlockCommentLines(lines):
    block_comment_lines = []
    block_line_count = 0
    is_in_string_double = False
    is_in_string_single = False
    for i in range(0, len(lines)):
        line = lines[i]
        index = FindFirstNonSpaceChar(line)
        if index != -1 and line[index] == "#":
            if block_line_count == 1:
                block_comment_lines.append(lines[i-1])
                block_comment_lines.append(lines[i])
                block_line_count += 1
            elif block_line_count > 1:
                block_comment_lines.append(lines[i])
                block_line_count += 1
            elif not is_in_string_double and not is_in_string_single:
                block_line_count += 1
            else:
                block_line_count = 0 
        else:
            block_line_count = 0             
        # This while loop is for checking if next line is in a string
        begin_index = 0
        while True:
            if is_in_string_double:
                if line.find('"', begin_index) != -1:
                    is_in_string_double = False
                    begin_index = line.find('"', begin_index)+1
                else:
                    break
            elif is_in_string_single:
                if line.find("'", begin_index) != -1:
                    is_in_string_single = False
                    begin_index = line.find("'", begin_index)+1
                else:
                    break
            else:
                comment_start = line.find('#', begin_index)
                string_start = FindNextString(line, begin_index)
                if comment_start != -1 and string_start == -1:
                    break                      
                elif comment_start == -1 and string_start != -1:
                    if line[string_start] == '"':
                        is_in_string_double = True
                    else:
                        is_in_string_single = True
                    begin_index = string_start+1
                elif comment_start == -1 and string_start == -1:
                    break
                else:
                    if comment_start < string_start:
                        break
                    else:
                        if line[string_start] == '"':
                            is_in_string_double = True
                        else:
                            is_in_string_single = True
                        begin_index = string_start+1              
    return block_comment_lines

# Return the number of block comments
def CountBlockComments(lines):
    block_count = 0
    block_line_count = 0
    is_in_string_double = False
    is_in_string_single = False
    for i in range(0, len(lines)):
        line = lines[i]
        index = FindFirstNonSpaceChar(line)
        if index != -1 and line[index] == "#":
            if block_line_count == 1:
                block_count += 1
                block_line_count += 1
            elif block_line_count > 1:
                block_line_count += 1
            elif not is_in_string_double and not is_in_string_single:
                block_line_count += 1
            else:
                block_line_count = 0 
        else:
            block_line_count = 0             
        # This while loop checks if next line is in a string
        begin_index = 0
        while True:
            if is_in_string_double:
                if line.find('"', begin_index) != -1:
                    is_in_string_double = False
                    begin_index = line.find('"', begin_index)+1
                else:
                    break
            elif is_in_string_single:
                if line.find("'", begin_index) != -1:
                    is_in_string_single = False
                    begin_index = line.find("'", begin_index)+1
                else:
                    break
            else:
                comment_start = line.find('#', begin_index)
                string_start = FindNextString(line, begin_index)
                if comment_start != -1 and string_start == -1:
                    break                      
                elif comment_start == -1 and string_start != -1:
                    if line[string_start] == '"':
                        is_in_string_double = True
                    else:
                        is_in_string_single = True
                    begin_index = string_start+1
                elif comment_start == -1 and string_start == -1:
                    break
                else:
                    if comment_start < string_start:
                        break
                    else:
                        if line[string_start] == '"':
                            is_in_string_double = True
                        else:
                            is_in_string_single = True
                        begin_index = string_start+1              
    return block_count

# Return the number of TODOs in comments
def CountTODOs(lines):
    count = 0
    is_in_string_double = False
    is_in_string_single = False
    for line in lines:
        begin_index = 0
        while True:
            if is_in_string_double:
                if line.find('"', begin_index) != -1:
                    is_in_string_double = False
                    begin_index = line.find('"', begin_index)+1
                else:
                    break
            elif is_in_string_single:
                if line.find("'", begin_index) != -1:
                    is_in_string_single = False
                    begin_index = line.find("'", begin_index)+1
                else:
                    break
            else:
                comment_start = line.find('#', begin_index)
                string_start = FindNextString(line, begin_index)
                if comment_start != -1 and string_start == -1:
                    count += line.count("TODO", comment_start)
                    break                      
                elif comment_start == -1 and string_start != -1:
                    if line[string_start] == '"':
                        is_in_string_double = True
                    else:
                        is_in_string_single = True
                    begin_index = string_start+1
                elif comment_start == -1 and string_start == -1:
                    break
                else:
                    if comment_start < string_start:
                        count += line.count("TODO", comment_start)
                        break
                    else:
                        if line[string_start] == '"':
                            is_in_string_double = True
                        else:
                            is_in_string_single = True
                        begin_index = string_start+1    
    return count
