#!/usr/bin/python3
def calc_weight(list_=[]):
	if not list_:
		return None

	calc_weight =  [x for tup in list_ for x in tup] 
	if calc_weight:
		return sum(calc_weight) / len(calc_weight)
	else:
		return 0


if __name__=="__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
