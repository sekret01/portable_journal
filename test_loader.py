from journal import Loader


DATA_FOR_TEST_FILE = {
	"last_changes": 1745441116,
	"all_titles": ["TEST TITLE", "ALSO TEST TITLE"], 
	"journal": 
	{
		"23.04.2025":
		[
			{
				"time": 1745441116,
				"title": "TEST TITLE",
				"message": "some text"
			},
			{
				"time": 1745441116,
				"title": "ALSO TEST TITLE",
				"message": "some text second"
			}
		],
		"22.04.2025":
		[
			{
				"time": 1745441116,
				"title": "TEST TITLE",
				"message": "some text"
			},
			{
				"time": 1745441116,
				"title": "ALSO TEST TITLE",
				"message": "some text second"
			}
		]
	}
}


def test_Loader_get_titles():
    loader = Loader()
    res = loader.get_titles()
    assert(res) == ['TEST TITLE', 'ALSO TEST TITLE']

def test_Loader_get_all_journal():
    loader = Loader()
    res = loader.get_journal()
    right_data = {
		"23.04.2025":
		[
			{
				"time": 1745441116.4921274,
				"title": "TEST TITLE",
				"message": "some text"
			},
			{
				"time": 1745441116.4921274,
				"title": "ALSO TEST TITLE",
				"message": "some text second"
			}
		],
		"22.04.2025":
		[
			{
				"time": 1745441116.4921274,
				"title": "TEST TITLE",
				"message": "some text"
			},
			{
				"time": 1745441116.4921274,
				"title": "ALSO TEST TITLE",
				"message": "some text second"
			}
		]
	}
    assert(res) == right_data
    
def test_Loader_get_date_journal():
    loader = Loader()
    res = loader.get_journal(date="23.04.2025")
    right_data = {
		"23.04.2025":
		[
			{
				"time": 1745441116.4921274,
				"title": "TEST TITLE",
				"message": "some text"
			},
			{
				"time": 1745441116.4921274,
				"title": "ALSO TEST TITLE",
				"message": "some text second"
			}
		]
	}
    assert(res) == right_data
    
def test_Loader_get_title_journal():
    loader = Loader()
    res = loader.get_journal(title="TEST TITLE")
    right_data = {
		"23.04.2025":
		[
			{
				"time": 1745441116.4921274,
				"title": "TEST TITLE",
				"message": "some text"
			}
		],
        "22.04.2025":
		[
			{
				"time": 1745441116.4921274,
				"title": "TEST TITLE",
				"message": "some text"
			}
		]
	}
    assert(res) == right_data