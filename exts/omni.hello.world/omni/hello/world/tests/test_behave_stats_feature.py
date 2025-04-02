from behave import __main__ as behave_executable
import omni.kit.test
import omni.kit.test.async_unittest as async_unittest
import subprocess
import unittest


class FeatureTests(omni.kit.test.AsyncTestCase):

    # @unittest.TestCase.subTest
    @omni.kit.test.AsyncTestCase.subTest
    def test_stats_endpoint_should_return_stats(self):
        # Run behave test 1
        result = subprocess.run(['behave', 'features/stats.feature'], capture_output=True)
        self.assertEqual(result.returncode, 0, f"behave test 1 failed:\n{result.stdout.decode()}")


    def test_run_auto_tests(self):
        ts = BehaveTestSuite()
        ts.run()

    # Add more test methods for each behave test

class BehaveTestLoader(unittest.TestLoader):
    def loadTestsFromModule(self, module, pattern=None):
        features = behave_executable.main(
            args=[module.__file__.replace('.py', '')]
        )
        return self.loadTestsFromFeature(features)

    def loadTestsFromFeature(self, features):
        suite = self.suiteClass()
        for feature in features:
            for scenario in feature.scenarios:
                test_case = self.loadTestsFromTestCase(omni.kit.test.AsyncTestCase)[0]
                test_case.feature = feature
                test_case.scenario = scenario
                suite.addTest(test_case)
        return suite


class BehaveTestSuite(omni.kit.test.AsyncTestSuite):
    async def run():
        loader = unittest.TestLoader()
        loader.suiteClass = omni.kit.test.AsyncTestCase
        suite = loader.loadTestsFromTestCase(FeatureTests)

        # Run the tests
        runner = async_unittest.AsyncTextTestRunner()
        runner.run(suite)


        # Alternative method: enumerate the tests
        loader = BehaveTestLoader()
        suite = loader.discover('.')
        runner = async_unittest.AsyncTextTestRunner()
        runner.run(suite)

    
if __name__ == '__main__':
    # Create a test suite
    ts = BehaveTestSuite()
    ts.run()
