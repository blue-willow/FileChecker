from util import ReadFile, FindNextString, FindNextComment

# Return the list of all lines containing comments
def GetCommentLines(lines):
    comment_lines = []
    is_in_block_comment = False
    is_in_string_double = False
    is_in_string_single = False
    appended = False
    for line in lines:
        appended = False
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
            elif is_in_block_comment:
                if not appended:
                    comment_lines.append(line)
                    appended = True
                end_index = line.find("*/", begin_index)
                if end_index != -1:
                    is_in_block_comment = False
                    begin_index = end_index+2
                else:
                    break
            else:
                comment_start = FindNextComment(line, begin_index)
                string_start = FindNextString(line, begin_index)
                if comment_start != -1 and string_start == -1:
                    if not appended:
                        comment_lines.append(line)
                        appended = True
                    if line[comment_start+1] == "*":
                        is_in_block_comment = True
                        begin_index = comment_start+2
                    else:
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
                        if not appended:
                            comment_lines.append(line)
                            appended = True
                        if line[comment_start+1] == "*":
                            is_in_block_comment = True
                            begin_index = comment_start+2
                        else:
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
    single_line_comments = []
    is_in_block_comment = False
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
            elif is_in_block_comment:
                end_index = line.find("*/", begin_index)
                if end_index != -1:
                    is_in_block_comment = False
                    begin_index = end_index+2
                else:
                    break
            else:
                comment_start = FindNextComment(line, begin_index)
                string_start = FindNextString(line, begin_index)
                if comment_start != -1 and string_start == -1:
                    if line[comment_start+1] == "*":
                        is_in_block_comment = True
                        begin_index = comment_start+2
                    else:
                        single_line_comments.append(line)
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
                        if line[comment_start+1] == "*":
                            is_in_block_comment = True
                            begin_index = comment_start+2
                        else:
                            single_line_comments.append(line)
                            break
                    else:
                        if line[string_start] == '"':
                            is_in_string_double = True
                        else:
                            is_in_string_single = True
                        begin_index = string_start+1             
    return single_line_comments

# Return the list of all lines containing block comments
def GetBlockCommentLines(lines):
    block_comment_lines = []
    is_in_block_comment = False
    is_in_string_double = False
    is_in_string_single = False
    appended = False
    for line in lines:
        appended = False
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
            elif is_in_block_comment:
                if not appended:
                    block_comment_lines.append(line)
                    appended = True
                end_index = line.find("*/", begin_index)
                if end_index != -1:
                    is_in_block_comment = False
                    begin_index = end_index+2
                else:
                    break
            else:
                comment_start = FindNextComment(line, begin_index)
                string_start = FindNextString(line, begin_index)
                if comment_start != -1 and string_start == -1:
                    if line[comment_start+1] == "*":
                        if not appended:
                            block_comment_lines.append(line)
                            appended = True
                        is_in_block_comment = True
                        begin_index = comment_start+2
                    else:
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
                        if line[comment_start+1] == "*":
                            if not appended:
                                block_comment_lines.append(line)
                                appended = True
                            is_in_block_comment = True
                            begin_index = comment_start+2
                        else:
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
    block_comment_lines = []
    is_in_block_comment = False
    is_in_string_double = False
    is_in_string_single = False
    counted = False
    count = 0
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
            elif is_in_block_comment:
                if not counted:
                    count += 1
                    counted = True
                end_index = line.find("*/", begin_index)
                if end_index != -1:
                    is_in_block_comment = False
                    counted = False
                    begin_index = end_index+2
                else:
                    break
            else:
                comment_start = FindNextComment(line, begin_index)
                string_start = FindNextString(line, begin_index)
                if comment_start != -1 and string_start == -1:
                    if line[comment_start+1] == "*":
                        count += 1
                        counted = True
                        is_in_block_comment = True
                        begin_index = comment_start+2
                    else:
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
                        if line[comment_start+1] == "*":
                            count += 1
                            counted = True
                            is_in_block_comment = True
                            begin_index = comment_start+2
                        else:
                            break
                    else:
                        if line[string_start] == '"':
                            is_in_string_double = True
                        else:
                            is_in_string_single = True
                        begin_index = string_start+1             
    return count

# Return the number of TODOs in comments
def CountTODOs(lines):
    count = 0
    is_in_block_comment = False
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
            elif is_in_block_comment:
                end_index = line.find("*/", begin_index)
                if end_index != -1:
                    count += line.count("TODO", begin_index, end_index)
                    is_in_block_comment = False
                    begin_index = end_index+2
                else:
                    count += line.count("TODO", begin_index)
                    break
            else:
                comment_start = FindNextComment(line, begin_index)
                string_start = FindNextString(line, begin_index)
                if comment_start != -1 and string_start == -1:
                    if line[comment_start+1] == "*":
                        is_in_block_comment = True
                        begin_index = comment_start+2
                    else:
                        count += line.count("TODO", begin_index)
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
                        if line[comment_start+1] == "*":
                            is_in_block_comment = True
                            begin_index = comment_start+2
                        else:
                            count += line.count("TODO", begin_index)
                            break
                    else:
                        if line[string_start] == '"':
                            is_in_string_double = True
                        else:
                            is_in_string_single = True
                        begin_index = string_start+1             
    return count