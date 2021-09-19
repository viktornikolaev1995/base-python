L = [3,1,2,5,6,1,3,6]
for elem1 in L:
  for elem2 in L[L.index(elem1) + 1:]:
    if elem1 == elem2:
        print(elem1, "==", elem2, True)
    else:
        print(elem1, "==", elem2, False)