function minPatches(nums: number[], n: number): number {
    const length: number = nums.length;
    let missing: number = 1;
    let i: number = 0;
    let count: number = 0;

    while (missing <= n) {
        if (i < length && nums[i] <= missing) {
            missing += nums[i];
            i++;
        } else {
            missing += missing;
            count++;
        }
    }
    return count;
}

const dummy: number[] = [1, 2, 5, 20];
const n_dummy: number = 46;

const result = minPatches(dummy, n_dummy);

console.log(result);
