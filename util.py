def ReadFile(file_name):
    lines = []
    with open(file_name, 'r') as f:
        for line in f:
            lines.append(line)
    return lines               
    
def FindNextString(line, begin_index):
    single_string_start = line.find("'", begin_index)
    double_string_start = line.find('"', begin_index)
    if double_string_start == -1 and single_string_start != -1:
        return single_string_start
    elif double_string_start != -1 and single_string_start == -1:
        return double_string_start
    elif double_string_start < single_string_start:
        return double_string_start
    elif double_string_start > single_string_start:
        return single_string_start
    else:
        return -1
                
def FindNextComment(line, begin_index):
    block_comment_start = line.find('/*', begin_index)
    single_comment_start = line.find('//', begin_index)
    if block_comment_start == -1 and single_comment_start != -1:
        return single_comment_start
    elif block_comment_start != -1 and single_comment_start == -1:
        return block_comment_start
    elif block_comment_start < single_comment_start:
        return block_comment_start
    elif block_comment_start > single_comment_start:
        return single_comment_start
    else:
        return -1
    
def FindFirstNonSpaceChar(string):
    for i in range(0, len(string)):
        if string[i] != ' ':
            return i
    return -1