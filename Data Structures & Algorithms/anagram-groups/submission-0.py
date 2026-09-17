class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for word in strs:
            key = "".join(sorted(word))

            # 이 key가 dictionary에 있으면
            # 그 리스트에 word 추가
            if key in dictionary:
                dictionary[key].append(word)

            # 없으면
            # 새 리스트를 만들고 word 넣기
            else:
                dictionary[key] = [word]

        return list(dictionary.values())