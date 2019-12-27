num_boxes, capacity = list(map(int, input().split()))
stack = []
num_cars = 0
stack.append(num_boxes)
while len(stack) > 0:
    candidate_boxes = stack.pop()
    if candidate_boxes <= capacity:
        num_cars += 1
        continue
    else:
        if candidate_boxes%2 == 0:
            stack.append(int(candidate_boxes/2))
            stack.append(int(candidate_boxes/2))
        else:
            stack.append(int(candidate_boxes/2))
            stack.append(int(candidate_boxes/2 + 1))

print(num_cars)   