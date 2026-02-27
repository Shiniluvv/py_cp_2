def create_phone_number(lst: list) -> str:
    digits = ''.join(str(d) for d in lst)
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

def duplicate_encode(text: str) -> str:
    text_lower = text.lower()
    result = []
    for ch in text_lower:
        if text_lower.count(ch) == 1:
            result.append('(')
        else:
            result.append(')')
    return ''.join(result)

def is_valid_walk(walk: list) -> bool:
    if len(walk) != 10:
        return False
    ns = walk.count('n') - walk.count('s')
    ew = walk.count('e') - walk.count('w')
    return ns == 0 and ew == 0

def move_zeros(lst: list) -> list:
    non_zeros = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros

def find_uniq(lst: list):
    if lst[0] != lst[1] and lst[0] != lst[2]:
        return lst[0]
    if lst[1] != lst[0] and lst[1] != lst[2]:
        return lst[1]
    common = lst[0]
    for num in lst:
        if num != common:
            return num
    return None
