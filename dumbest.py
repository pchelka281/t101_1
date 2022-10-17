"""
Лабораторная работа №1
"""

import functools
import time
import generate_and_evaluate as ge

def update_rules(rules):
    """Удаление конфликтных правил и разбиение на классы (or, and, not)
        Args:
            rules (dictionary): Словарь правил
        Returns:
            List of rules: Список правил (or, and, not)
    """
    rules_not, rules_or, rules_and = [], [], []
    for rule in rules:
        if rule.get('if').get('or') is not None:
            rules_or.extend([[rule.get('if').get('or'), rule.get('then')]])
        if rule.get('if').get('and') is not None:
            rules_and.extend([[rule.get('if').get('and'), rule.get('then')]])
        if rule.get('if').get('not') is not None:
            rules_not.extend([[rule.get('if').get('not'), rule.get('then')]])
    return [rules_or, rules_and, rules_not]

def update_facts(facts):
    """Summary
        Args:
            facts (list): Список фактов
        Returns:
            dict: Словарь фактов
    """
    facts_dict = {}
    for fact in facts:
        if facts_dict.get(fact) is None:
            facts_dict[fact] = True
    return facts_dict


def dumbest_ai(rules_list, facts_dict):
    """Самый тупой искуственный интелект
        Args:
            rules (list of dict): Словарь правил
            facts (list): Список фактов
        Returns:
            list: База знаний
    """
    #OR
    for rule in rules_list[0]:
        for ifor in rule[0]:
            if facts_dict.get(ifor) is True:
                if facts_dict.get(rule[1]) is None:
                    facts_dict[rule[1]] = True
    
    #AND
    for rule in rules_list[1]:
        for ifand in rule[0]:
            if facts_dict.get(ifand) is None:
                break
            if facts_dict.get(rule[1]) is None:
                facts_dict[rule[1]] = True

    #NOT
    for rule in rules_list[2]:
        for ifnot in rule[0]:
            if facts_dict.get(ifnot) is True:
                break
            if facts_dict.get(rule[1]) is None:
                facts_dict[rule[1]] = True
    return ''

def main():
    """Main
    """
    # SIMPLE RULES RAND FACTS
    rules = ge.generate_simple_rules(10000, 100, 100000)
    facts = ge.generate_rand_facts(10000, 10000)
    rules_list = update_rules(rules)
    facts_dict = update_facts(facts)
    print('SIMPLE RULES RAND FACTS:')
    dumbest_ai(rules_list, facts_dict)
    # STAIRWAY RULES, RAND FACTS
    rules = ge.generate_stairway_rules(10000, 100, 100000)
    facts = ge.generate_rand_facts(10000, 10000)
    rules_list = update_rules(rules)
    facts_dict = update_facts(facts)
    print('STAIRWAY RULES RAND FACTS:')
    dumbest_ai(rules_list, facts_dict)
    # RING RULES, RAND FACTS
    rules = ge.generate_ring_rules(10000, 100, 100000)
    facts = ge.generate_rand_facts(10000, 10000)
    rules_list = update_rules(rules)
    facts_dict = update_facts(facts)
    print('RING RULES RAND FACTS:')
    dumbest_ai(rules_list, facts_dict)
    # RANDOM RULES, RAND FACTS
    rules = ge.generate_random_rules(10000, 100, 100000)
    facts = ge.generate_rand_facts(10000, 10000)
    rules_list = update_rules(rules)
    facts_dict = update_facts(facts)
    print('RAND RULES RAND FACTS:')
    dumbest_ai(rules_list, facts_dict)

if __name__ == '__main__':
    main()
