from src.sc.pwr.inz.language.components.LogicalOperator import LogicalOperator

"""
Module involves methods essential for establishing tao in Holons.
As it seems this old 500loc module wasn't so necessary after all.
"""


class Grounder:
    @staticmethod
    def determine_fulfilment(dk, formula):
        """
        Method determines fulfilment for SimpleFormula it basically counts appearances of Observations in which
        formula was fulfilled a.e when carpet indeed was red.
        :param dk : DistributedKnowledge: contains most of data which we will seek truth in
        :param formula: Formula : Given formula we'd want to find answer for
        :return int : Number of times given formula was observed
        """
        if (dk.get_formula().get_type() == formula.get_type()) and (formula in dk.get_complementary_formulas()):
            count = 0
            for bp in dk.get_bpset():
                if bp.check_if_observed(formula.get_model().get_identifier(),
                                        formula.get_traits()[0], formula.get_states()[0]):
                    count += 1
            return count
        else:
            raise AttributeError("Either you gave me wrong formula,or Distributed Knowledge which doesn't belong to it")

    @staticmethod
    def determine_fulfilment_cf(dk, formula):
        """
        Method determines fulfilment for ComplexFormula it basically counts appearances of Observations in which
        formula was fulfilled a.e when carpet indeed was red and fluffy.
        :param dk:  DistributedKnowledge: contains most of data which we will seek truth in
        :param formula: Formula : Given formula we'd want to find answer for
        :return int : Number of times given formula was observed
        """
        if (dk.get_formula().get_type() == formula.get_type()) and (formula in dk.get_complementary_formulas()):
            count = 0
            for bp in dk.get_bpset():
                if formula.get_logical_operator() == LogicalOperator.AND:
                    if bp.check_if_observed(formula.get_model().get_identifier(), formula.get_traits()[0],
                                            formula.get_states()[0]) and \
                            bp.check_if_observed(formula.get_model().get_identifier(), formula.get_traits()[1],
                                                 formula.get_states()[1]):
                        count += 1
                if formula.get_logical_operator() == LogicalOperator.OR:
                    if bp.check_if_observed(formula.get_model().get_identifier(), formula.get_traits()[0],
                                            formula.get_states()[0]) or \
                            bp.check_if_observed(formula.get_model().get_identifier(), formula.get_traits()[1],
                                                 formula.get_states()[1]):
                        count += 1
                if formula.get_logical_operator() == LogicalOperator.XOR:
                    if (bp.check_if_observed(formula.get_model().get_identifier(), formula.get_traits()[0],
                                             formula.get_states()[0]) and not
                        bp.check_if_observed(formula.get_model().get_identifier(), formula.get_traits()[1],
                                             formula.get_states()[1])) or (not
                                                                    bp.check_if_observed(
                                                                           formula.get_model().get_identifier(),
                                                                           formula.get_traits()[0],
                                                                           formula.get_states()[0]) and
                                                                           bp.check_if_observed(
                                                                               formula.get_model().get_identifier(),
                                                                               formula.get_traits()[1],
                                                                               formula.get_states()[1])):
                        count += 1
                    return count
            return count
        else:
            raise AttributeError("Either you gave me wrong formula,or Distributed Knowledge "
                                 "which doesn't belong to it")
