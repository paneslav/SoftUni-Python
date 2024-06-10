from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    def __init__(self, budget):
        super().__init__(budget)

    @property
    def sponsors(self):
        sponsors = {
            'Petronas': {1: 1_000_000, 3: 500_000},
            'Honda': {5: 100_000, 7: 50_000}
        }

        return sponsors

    @property
    def race_expenses(self):
        return 200_000
