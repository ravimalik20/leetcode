from collections import defaultdict
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain_counts = defaultdict(int)

        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')[:2]
            count = int(count)

            subdomains = self.__generate_subdomains(domain)

            for subdomain in subdomains:
                subdomain_counts[subdomain] += count

        res = []
        for subdomain, count in subdomain_counts.items():
            res.append(f"{count} {subdomain}")

        return res

    def __generate_subdomains(self, domain: str) -> list:
        domain_components = domain.split('.')
        domain_components.reverse()

        prev = None
        subdomains = []

        for comp in domain_components:
            x = f"{comp}.{prev}" if prev is not None else comp

            prev = x
            subdomains.append(x)

        return subdomains
