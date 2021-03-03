from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        broken_logs = self.__break_logs(logs)

        digit_logs, alpha_logs = self.__split_logs(broken_logs)

        alpha_logs = self.__sort_alpha_logs(alpha_logs)

        return self.__join_parts(alpha_logs) + self.__join_parts(digit_logs)

    def __break_logs(self, logs: List[str]):
        res = []

        for log in logs:
            parts = log.split(' ')
            res.append((parts[0], ' '.join(parts[1:])))

        return res

    def __join_parts(self, log_parts):
        res = []

        for parts in log_parts:
            res.append(f"{parts[0]} {parts[1]}")

        return res

    def __split_logs(self, logs):
        dig, alp = [], []

        for log_parts in logs:
            joined = ''.join(log_parts[1].split( ))

            if joined.isnumeric():
                dig.append(log_parts)
            else:
                alp.append(log_parts)

        return dig, alp

    def __sort_alpha_logs(self, alpha_logs):
        sort_key = lambda parts: (''.join(parts[1]), parts[0])

        return sorted(alpha_logs, key=sort_key)


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    res = Solution().reorderLogFiles(logs)

    print(res)