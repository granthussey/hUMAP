import pandas as pd
import unittest


class TestHumap(unittest.TestCase):
    def setUp(self):
        # Set up test data and hierarchy
        self.data = pd.DataFrame(
            {"A": [0.1, 0.2, 0.3], "B": [0.4, 0.5, 0.6], "C": [0.7, 0.8, 0.9]}
        )
        self.hierarchy = pd.DataFrame(
            {
                "index_column": ["A", "B", "C"],
                "level_1": ["Kingdom", "Phylum", "Class"],
                "level_2": ["Animalia", "Chordata", "Mammalia"],
            }
        )

    def test_df_dominant_level(self):
        # Create an instance of the Humap class
        humap = Humap(self.data, self.hierarchy)

        # Call the df_dominant_level method
        result = humap.df_dominant_level()

        # Assert the expected output
        expected_result = pd.DataFrame(
            {
                "dom_level_1": ["Kingdom", "Kingdom", "Kingdom"],
                "dom_level_2": ["Animalia", "Animalia", "Animalia"],
                "index_column": ["A", "B", "C"],
            }
        ).set_index("index_column")

        pd.testing.assert_frame_equal(result, expected_result)


if __name__ == "__main__":
    unittest.main()
