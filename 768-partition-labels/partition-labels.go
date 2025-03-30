func partitionLabels(s string) []int {
    seen := make([]int, 26 , 26)
    var offset rune = rune('a')
    for i, c := range(s){
        seen[c - offset] = i
    }
    l := 0
    furthest := 0
    out := make([]int,0)
    for r , c := range(s){
        furthest = max(furthest, seen[c - offset])
        if furthest == r {
            out = append(out, r - l + 1)
            l = r + 1
        }
    }
    return out
}