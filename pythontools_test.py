import python_tools
from python_tools.html_downloader import get_html_content
from python_tools.path_tools import get_absolute_paths, get_sorted_filenames
import unittest


class PythonToolsTest(unittest.TestCase):


    def test_htmldownloader(self):
        html_content = get_html_content("https://www.google.com")
        self.assertTrue(len(html_content) > 50)

    def test_filename(self):
        path = python_tools.__file__
        newpath = path[:-12]
        filenames = get_sorted_filenames(newpath)
        self.assertTrue(any("html_downloader.py" in filename for filename in filenames))

    def test_filenameending(self):
        path = python_tools.__file__
        newpath = path[:-12]
        filenames = get_sorted_filenames(newpath,".jpg")
        self.assertTrue(filenames == [])

    def test_absolutepath(self):
        path = python_tools.__file__
        newpath = path[:-12]
        filenames = get_sorted_filenames(newpath)
        returned_absolute_paths = get_absolute_paths(newpath,["__init__.pyc"])
        self.assertEqual(path,returned_absolute_paths[0])


if __name__ == '__main__':
    unittest.main()
    
