var sieve = function(limit){
	primesBoolList = [];
	primes = [];
	for(var i = 0; i <= limit; i++){
		primesBoolList.push(0);
	}
	len = primesBoolList.length
	for(var i = 2; i < len; i++){
		if(primesBoolList[i] !== 1){
			primes.push(i);
			primesBoolList[i] = 1;
			for(var j = i*i; j < limit + 1; j += i){
				primesBoolList[j] = 1;
			}
		}
	}

	return primes;
};


