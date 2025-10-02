def func():
    test_dict = dict()
    test_dict["1"] = ("101", "2")
    test_dict["2"] = ("202", "3")
    import pdb;pdb.set_trace()
    top_task = max(
            test_dict.items(),
            key=lambda item: (item[1][1], item[0]))
    
    return top_task

func()