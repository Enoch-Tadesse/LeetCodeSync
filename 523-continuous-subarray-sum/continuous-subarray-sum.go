func checkSubarraySum(nums []int, k int) bool {
    mods := make(map[int]int)
    mods[0] = -1 // Important for cases where the sum itself is a multiple of k

    var curr int
    for i, num := range nums {
        curr += num
        mod := curr % k
        if val, ok := mods[mod]; ok {
            if i - val >= 2 {
                return true
            }
        } else {
            mods[mod] = i
        }
    }
    return false
}
