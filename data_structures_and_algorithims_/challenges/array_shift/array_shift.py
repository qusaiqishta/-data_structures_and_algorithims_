def insertShiftArray(array,num):
   if len(array)%2==0:
      array.insert(int(len(array)/2),num)
      
   else:
      array.insert((int(len(array)/2)+1),num)

   return array   

      


print(insertShiftArray([1,2,3,4],5))  # 5 should be in second index
print(insertShiftArray([1,2,3,4,5],5))  # 5 should be in third index       





