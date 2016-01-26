class Meet(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def merge_meeting(meet_arr):
    new_meet_arr = sorted(meet_arr, key = lambda x: x.start)
    merged_arr = []

    prev = new_meet_arr[0]
    for i in new_meet_arr[1:]:
        if i.start <= prev.end:
            prev.end = max(prev.end, i.end)
        else:
            merged_arr.append(Meet(prev.start, prev.end))
            prev = i

    merged_arr.append(Meet(prev.start, prev.end))
    return merged_arr

if __name__ == "__main__":

    m_arr = []
    m_arr.append(Meet(0,1))
    m_arr.append(Meet(3,5))
    m_arr.append(Meet(4,8))
    m_arr.append(Meet(10,12))
    m_arr.append(Meet(9,10))

    new_arr = merge_meeting(m_arr)

    for i in new_arr:
    	print(i.start,"->",i.end)

        
