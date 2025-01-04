int missingNumber(int* nums, int numsSize) {
    int res = 0;
    for (int i = 0; i < numsSize + 1; i++){

        if(i == numsSize){
            res ^= i;
            break;
        }

        res ^= nums[i]; 
        res ^= i;
    }

    return res;   
}