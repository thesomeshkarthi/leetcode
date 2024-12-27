int hammingWeight(int n) {

    int res;
    int count = 0;
    while(n){
        res = n & 1;
        if(res){
            count++;
        }
        n = n >> 1;
    }
    return count;
}