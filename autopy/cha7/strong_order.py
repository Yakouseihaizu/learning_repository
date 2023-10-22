import re
def check_order(order):
    up_regex = re.compile(r'[A-Z]')
    low_regex = re.compile(r'[a-z]')
    num_regex = re.compile(r'\d')

    # order = ''
    mo1 = up_regex.search(order)
    mo2 = low_regex.search(order)
    mo3 = num_regex.search(order)
    print(mo1 and mo2 and mo3 and len(order)>=8)

check_order('makeasfa')
check_order('244Usnlcaf')
check_order('Unco8ckKjnvksksnsfdnovds58f95vgds9')
check_order('CKJBBKJVDSJLS3436436N')
check_order('1294710013352')
check_order('U8y')