#include <iostream>
#include <set>
#include <vector>

#include "solution1.h"

// neetcode's Solution class is unqualified, so keep it in its own namespace.
namespace neetcode_contains_duplicate {
#include "contains_duplicate.h"
}

int main() {
  std::vector<int> nums = {2, 7, 11, 15};
  auto result = Solution1().twoSum(nums, 9);
  std::cout << "[" << result[0] << ", " << result[1] << "]" << std::endl;

  std::vector<int> dupes = {1, 2, 3, 3};
  std::cout << std::boolalpha
            << neetcode_contains_duplicate::Solution().hasDuplicate(dupes)
            << std::endl;
}
