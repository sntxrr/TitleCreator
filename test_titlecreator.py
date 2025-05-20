import subprocess
import unittest

class TestTitleCreator(unittest.TestCase):

    def test_title_generator_smoke(self):
        """
        Smoke test for TitleCreator.py.
        Runs the script multiple times and checks basic output structure.
        """
        for i in range(20):
            # Execute TitleCreator.py as a subprocess
            # Ensure using python3, as the script has a shebang for python3
            process = subprocess.run(
                ['python3', 'TitleCreator.py'],
                capture_output=True,
                text=True,  # Decodes stdout and stderr as UTF-8
                check=True  # Raises CalledProcessError if return code is non-zero
            )

            output = process.stdout

            # 1. Assert that the script produces an output
            self.assertTrue(output, msg=f"Run {i+1}: Output was empty")

            # 2. Assert that the output contains the introductory line
            self.assertIn(
                "Congratulations! Your new title is:",
                output,
                msg=f"Run {i+1}: Introductory line not found in output:\n{output}"
            )

            lines = output.strip().split('\n')

            # 3. Assert that there are at least two lines (intro + title)
            self.assertGreaterEqual(
                len(lines),
                2,
                msg=f"Run {i+1}: Expected at least 2 lines, got {len(lines)} in output:\n{output}"
            )

            # 4. Assert that the actual generated title string is not empty
            generated_title = lines[1]
            self.assertTrue(
                generated_title,
                msg=f"Run {i+1}: Generated title string is empty in output:\n{output}"
            )
            # 5. (Implicit) Assert title is a string - already true due to text=True and split
            self.assertIsInstance(
                generated_title,
                str,
                msg=f"Run {i+1}: Generated title is not a string in output:\n{output}"
            )

if __name__ == '__main__':
    unittest.main()
