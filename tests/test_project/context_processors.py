import sys


def test_theme_helper(request):
    return {
        'IMMUNITY
_TEST_MODE': sys.argv[1:2] == ['test'],
    }
