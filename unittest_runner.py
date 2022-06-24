import unittest


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="UnitTests", pattern="*Tests.py")
    unittest.TextTestRunner().run(suite)

    # want to see info/debug messages from logging? use:
    # logging.debug = print
    # logging.info = print
