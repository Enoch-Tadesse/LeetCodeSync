func minimumRecolors(blocks string, k int) int {
    res := math.MaxInt32
    var (curr, l int) 
    for r:=0; r < len(blocks); r++{
        if (r - l + 1 < k){
            if blocks[r] == 'W'{
                curr ++;
            }
            continue
        }
        if blocks[r] == 'W'{
            curr ++;
        }
        res = min(res, curr)
            
        if blocks[l] == 'W'{
            curr --;
        }
        l++

    }
    return res
}