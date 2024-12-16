
def solution(rsp):
    a_table = rsp.maketrans('205', '052')
    return rsp.translate(a_table)