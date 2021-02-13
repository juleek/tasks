class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard_dic: Dict[str, int] = dict()
        for i in range(len(keyboard)):
            keyboard_dic[keyboard[i]] = i
            
        result: int = 0
        current_pos: int = 0
        for letter in word:
            next_pos: int = keyboard_dic[letter]
            time_taken: int = current_pos - next_pos
            result += abs(time_taken)
            current_pos = next_pos
        return result
