from collections import defaultdict

class Solution:
    def list2dict(self, l):
        return {value: index for index, value in enumerate(l)}

    def findRestaurant(self, list1, list2):
        dict2 = self.list2dict(list2)
        hash_index_sum = defaultdict(list)
        min_index = float('inf')

        for index1 in range(len(list1)):
            place = list1[index1]
            if place not in dict2:
                continue
            index2 = dict2[place]
            index_comb = index1 + index2
            hash_index_sum[index_comb].append(place)
            if index_comb < min_index:
                min_index = index_comb

        
        return hash_index_sum[min_index]

def main():

    assert_cases = [
        [["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"],["Shogun"]],
        [["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Shogun","Burger King"],["Shogun"]],
        [["happy","sad","good"],["sad","happy","good"],["sad","happy"]],
    ]

    solution = Solution()
    for var1, var2, expected in assert_cases:
        result = solution.findRestaurant(var1, var2)
        print("var1={}, var2={}, expected={}, result={}"
              .format(var1, var2, expected, result))
        if result != expected:
            print("ERROR")

if __name__ == "__main__":
    main()