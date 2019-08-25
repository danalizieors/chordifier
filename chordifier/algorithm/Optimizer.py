import numpy as np
import random
from deap import base, creator, tools, algorithms

from chordifier.algorithm.Evaluator import Evaluator


class Optimizer:
    def __init__(self, evaluator: Evaluator, parameters):
        self.evaluator = evaluator
        self.parameters = parameters

        self.toolbox = self.setup_toolbox()
        self.winner = tools.HallOfFame(1)
        self.stats = self.setup_stats()

    def setup_toolbox(self):
        if self.parameters["best"]:
            creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
            creator.create("Individual", list, fitness=creator.FitnessMin)
        else:
            creator.create("FitnessMax", base.Fitness, weights=(1.0,))
            creator.create("Individual", list, fitness=creator.FitnessMax)

        characters = self.parameters['characters']

        toolbox = base.Toolbox()
        toolbox.register("indices", random.sample, range(characters),
                         characters)
        toolbox.register("individual", tools.initIterate, creator.Individual,
                         toolbox.indices)
        toolbox.register("population", tools.initRepeat, list,
                         toolbox.individual)

        toolbox.register("mate", tools.cxOrdered)
        toolbox.register("mutate", tools.mutShuffleIndexes,
                         indpb=self.parameters[
                             'mutate_independent_probability'])
        toolbox.register("select", tools.selTournament,
                         tournsize=self.parameters['select_tournament_size'])
        toolbox.register("evaluate", self.evaluator.evaluate)

        return toolbox

    @staticmethod
    def setup_stats():
        stats = tools.Statistics(lambda individual: individual.fitness.values)

        stats.register("average", np.mean)
        stats.register("standard", np.std)
        stats.register("minimum", np.min)
        stats.register("maximum", np.max)

        return stats

    def optimize(self):
        population = self.toolbox.population(self.parameters['population_size'])
        algorithms.eaSimple(population,
                            self.toolbox,
                            self.parameters['mate_probability'],
                            self.parameters['mutate_probability'],
                            self.parameters['generations'],
                            self.stats,
                            self.winner)

        permutation = self.winner.items[0]
        return self.evaluator.retrieve_mapping(permutation)
