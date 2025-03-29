func findMaxLength(nums []int) int {
    seen := make(map[int]int) // maps the seen sum with its index
    seen[0] = -1
    var curr int
    var out int
    for i , num := range nums{
        if num == 1{
            curr += 1
        }else{
            curr -= 1
        }
        val , ok := seen[curr]
        if ok {
            out = max(out, i - val)
        }else{
            seen[curr] = i
        }
    }
    return out
}