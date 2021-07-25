def insertShiftArray(array,num):
   if len(array)%2==0:
      array.insert(int(len(array)/2),num)
<<<<<<< HEAD
      
=======
>>>>>>> 82c4a39ec20e4c5c83290074d8af81992c468636
   else:
      array.insert((int(len(array)/2)+1),num)

   return array   

      


print(insertShiftArray([1,2,3,4],5))  # 5 should be in second index
print(insertShiftArray([1,2,3,4,5],5))  # 5 should be in third index       





