var binarySearch = function(aList, item){
    var low = 0;
    var high = aList.length - 1;
    var mid;
    
    while(low <= high){
        mid = low + Math.floor((high-low)/2);
        if(item < aList[mid]){
            high = mid - 1;
        }else if(item > aList[mid]){
            low = mid + 1;
        }else {
            return mid;
        }

    }
    return -1;

};


//Examples
var test = [1,3,7,9,13,56,78,200,2001,2003,3000,9485];

console.log(binarySearch(test, 7));
console.log(binarySearch(test, 10));
console.log(binarySearch(test, 999999));
console.log(binarySearch(test, -3));
console.log(binarySearch(test, 0));
console.log(binarySearch(test, 1));