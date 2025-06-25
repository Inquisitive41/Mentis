import networkx as nx
import sympy as sp
from collections import defaultdict
import logging


class NovaMentis:
    """
    Класс NovaMentis реализует парадигму гипотезного мышления для ИИ:
    - Формирует и тестирует гипотезы
    - Корректирует правила на лету
    - Хранит знания в графе понятий
    """

    def __init__(self):
        self.graph = nx.DiGraph()
        self.hypotheses = {}
        self.alpha = 0.01
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s"
        )
        logging.info("NovaMentis инициализирован.")

    def hypothesize(self, data):
        """
        Генерирует гипотезы на основе входных данных.
        """
        n = sp.Symbol("n")
        for x, y in data:
            try:
                hyp = f"n^2 = y"
                score = self._test_hypothesis(n**2 - y, x, y)
                self.hypotheses[hyp] = score
                logging.info(f"Гипотеза: {hyp}, score: {score}")
            except Exception as e:
                logging.error(f"Ошибка при генерации гипотезы: {e}")
        if self.hypotheses:
            return max(self.hypotheses, key=self.hypotheses.get)
        return None

    def _test_hypothesis(self, expr, x, y):
        """
        Тестирует гипотезу на одном примере.
        """
        n = sp.Symbol("n")
        try:
            result = 1.0 if sp.simplify(expr.subs(n, x) - y) == 0 else 0.0
            logging.info(f"Тест гипотезы для x={x}, y={y}: {result}")
            return result
        except Exception as e:
            logging.error(f"Ошибка при тестировании гипотезы: {e}")
            return 0.0

    def update(self, new_data):
        """
        Корректирует веса гипотез на новых данных с учётом вероятности.
        """
        n = sp.Symbol("n")
        for x, y in new_data:
            h = self.hypothesize([(x, y)])
            if h is None:
                continue
            try:
                # P(h|D) = score гипотезы (0 или 1)
                p = self.hypotheses.get(h, 0.0)
                reward = 1.0 if self._test_hypothesis(n**2 - y, x, y) else -1.0
                self.hypotheses[h] = p + self.alpha * (reward - p)
                logging.info(f"Обновление гипотезы {h}: вес={self.hypotheses[h]}")
            except Exception as e:
                logging.error(f"Ошибка при обновлении гипотезы: {e}")

    def build_theory(self, data):
        """
        Строит теорию и граф понятий на основе данных.
        """
        h = self.hypothesize(data)
        if h:
            self.graph.add_node(h)
            for x, y in data:
                self.graph.add_edge(f"{x}^2", h)
                self.graph.add_edge(h, f"{y}")
            logging.info(f"Теория построена: {h}")
        return h, self.graph


# Демо-использование вынесено отдельно
if __name__ == "__main__":
    nm = NovaMentis()
    data = [(1, 1), (2, 4)]
    theory, graph = nm.build_theory(data)
    print(f"Теория: {theory}")
    new_data = [(3, 9)]
    nm.update(new_data)
    print(f"Обновлённая теория: {max(nm.hypotheses, key=nm.hypotheses.get)}")
