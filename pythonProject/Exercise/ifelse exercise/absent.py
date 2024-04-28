marks=[2,5,8,4,9,-1,6,-1]
print(marks)
absent=marks.count(-1)
#marks.remove(-1)
print('')
count=len(marks)-absent
total=sum(marks)+absent
print('total student who sit for exam= ',count)
print('total marks= ',total)
#marks.pop()
avg=total/len(marks)-absent
print('avg= ',avg)
print('max= ',max(marks))
