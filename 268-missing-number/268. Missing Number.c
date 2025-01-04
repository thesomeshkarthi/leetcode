int missingNumber(int* nums, int numsSize) {
    int numberArr[numsSize + 1];
    int res = 0;
    for (int i = 0; i < numsSize + 1; i++){
        numberArr[i] = i;

        if(i == numsSize){
            res ^= numberArr[i];
            break;
        }

        res ^= nums[i]; 
        res ^= numberArr[i];
    }

    return res;   
}