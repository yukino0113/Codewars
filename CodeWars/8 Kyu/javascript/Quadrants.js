// https://www.codewars.com/kata/643af0fa9fa6c406b47c5399/train/python

function quadrant(x, y) {
  switch(x>0){
      case true:
        if (y>0){
          return 1
        }else{
          return 4
        }
      case false:
        if (y>0){
            return 2
          }else{
            return 3
          }
      }
}