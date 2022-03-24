asal1=list()
for s in range(1,42):
      for y in range(2,s):
              if s % y == 0 :
                        break

                      if y == s-1:
                              asal1.append(s)
                              print(asal1)

