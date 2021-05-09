
def is_float(x):
    try:
        float(x)
    except :
        return False
    return True

def convert_range_to_num(x):
    n = x.split('-')
    if len(n)==2:
        return (float(n[0])+float(n[1]))/2
    try :
        return float(x)
    except:
        return None