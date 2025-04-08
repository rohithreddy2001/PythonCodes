# Function to find the maximum contiguous subarray in DP approach
# Formula: DP[i] = max(DP[i-1] + arr[i] , arr[i] )
def max_sub_array_sum(a, size):
	dp = [0] * size
	dp[0] = a[0]
	ans = dp[0]
	for i in range(1, size):
		dp[i] = max(a[i], a[i] + dp[i - 1])
		ans = max(ans, dp[i])
	print(ans)

if __name__ == "__main__":
	a = [-2, -3, 4, -1, -2, 1, 5, -3]
	n = len(a)
	max_sub_array_sum(a, n)