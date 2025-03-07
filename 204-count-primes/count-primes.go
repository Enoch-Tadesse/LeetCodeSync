func countPrimes(n int) int {
    var counter int
    primes := make([]bool, n + 2, n+ 2)
    primes[0] , primes[1] = true, true
    for i:=2; i < n; i++ {
        if (!primes[i]) {
            counter ++
            for j := i + i; j < n; j += i{
                primes[j] = true
            }
        }
    }
    return counter

}