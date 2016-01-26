class Rect:
    def __init__(self, x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

def x_overlap(rect1, rect2):
    highest_start = max(rect1.x, rect2.x)
    lowest_end = max(rect1.x + rect1.w, rect2.x + rect2.w)

    #no overlap
    if highest_start > lowest_end:
        return None
    else:
        return highest_start,lowest_end

def y_overlap(rect1, rect2):
    highest_start = max(rect1.y, rect2.y)
    lowest_end = max(rect1.y + rect1.h, rect2.y + rect2.h)

    if highest_start > lowest_end:
        return None

    else:
        return highest_start,lowest_end

def find_intersection(rect1, rect2):

    x1,x2 = x_overlap(rect1, rect2)
    y1,y2 = y_overlap(rect1, rect2)
    return x1,y1,x2-x1,y2-y1

if __name__ == "__main__":

    r1 = Rect(0,0,4,4)
    r2 = Rect(1,1,5,5)
    print(find_intersection(r1,r2))

    
