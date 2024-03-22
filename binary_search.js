
function isSorted(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            return false;
        }
    }
    return true;
}


let arr = [1,2,3,4,5,6]; //1,1,1,12,12,13,14,16,22,41,43,66,89,95,99


if (isSorted(arr) == false) {
    throw new Error("This algorithm only works with sorted list");
}

let mid = Math.floor((arr.length) / 2);
let low = 0; 
let high = arr.length - 1;

console.log(mid); 

const res = 2;

let not_found = true;

while (low <= high) {
    
    mid = Math.floor((low + high) /2);


    if (arr[mid] === res) {
        not_found =false;
        break;
    }


        
    if (arr[mid] > res) {
        high = mid -1 ;
      
    } 
    else if (arr[mid] < res) {
        low = mid +1;
    
    }

    
    
    
    
    
    
    console.log(`Low: ${low}, High: ${high}, Mid: ${mid}`);

    
  
}
if (not_found){
    console.log('Not Found');

} else {
    console.log('Found');

    console.log("Index is " + mid);


}
    
