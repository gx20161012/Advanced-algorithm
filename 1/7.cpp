/*
*copyright@nciaebupt 转载请注明出处
*问题：从一列数中筛除尽可能少的数使得从左往右看，这些数是从小到大再从大到小的（网易）。
*比如数列1,4,3,5,6,7,2,0 删除的最少的数的个数为1
*求解思路：双端LIS问题，使用动态规划的思路求解，时间复杂度O(nlog(n))
*/
#include <cstdio>
#include <iostream>
 
using namespace std;
 
int DoubleEndLIS(int *array,int len)
{
    int left,mid,right;
    int max=0;
    int k =0;
 
    //LIS数组中存储的是 递增子序列中最大值最小的子序列的最后一个元素（最大元素）在array中的位置
    int *LIS = new int[len];
    //从左到右LIS中最长子序列中最大值最小的子序列的最后一个元素所在的位置,也就是0~i的数字序列中最长递增子序列的长度-1
    int *B = new int[len];
    //从右到左LIS中最长子序列中最大值最小的子序列的最后一个元素所在的位置,也就是len-1~i的数字序列中最长递增子序列的长度-1
    int *C = new int[len];
    //从左到右
    for(int i = 0;i < len;++i)//LIS数组清零
    {
        B[i] = 0;
        LIS[i] = 0;
    }
    LIS[0] = array[0];
    for(int i = 1;i < len;++i)
    {
        left = 0;
        right = B[k];
        while(left <= right)
        {
            mid = (left + right)/2;
            if(array[i] < LIS[mid])
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }
 
        LIS[left] = array[i];//将array[i]插入到LIS中
        if(left > B[k])
        {
            B[k+1] = B[k] + 1;
            k++;
        }
    }
    for(int i = 0;i < k;++i)
    {
        B[i]++;
    }
    //从右到左
    for(int i = 0;i < len;++i)//LIS数组清零
    {
        C[i] = 0;
        LIS[i] = 0;
    }
    k = 0;
    LIS[0] = array[len-1];
    for(int i = len-2;i >= 0;--i)
    {
        left = 0;
        right = C[k];
        while(left <= right)
        {
            mid = (left + right)/2;
            if(array[i] < LIS[mid])
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }
        LIS[left] = array[i];
        if(left > C[k])
        {
            C[k+1] = C[k] + 1;
            k++;
        }
    }
    for(int i = 0;i <= k;++i)
    {
        C[i]++;
    }
 
    //求max
    for(int i = 0;i < len;++i)
    {
        //cout<<B[i]<<"  "<<C[i]<<endl;
        if(B[i]+C[i]>max)
            max=B[i] + C[i];
    }
 
    return len - max +1;
}
 
int main(int args,char ** argv)
{
    int array[] = {1,4,3,5,6,7,2,0};
    int len = sizeof(array)/sizeof(int);
    int res = DoubleEndLIS(array,len);
    cout<<res<<endl;
    getchar();
    return 0;
}

