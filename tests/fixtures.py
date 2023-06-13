import pytest


@pytest.fixture
def test_data_1():
    return [
        {
            "length": 100,
            "width": 100,
            "height": 100,
            "weight": 100
        },
        {
            "length": 100,
            "width": 100,
            "height": 100,
            "weight": 100
        },
        {
            "length": 100,
            "width": 100,
            "height": 100,
            "weight": 100
        },
        {
            "length": 100,
            "width": 100,
            "height": 100,
            "weight": 100
        }
    ]


@pytest.fixture
def expected_result_1():
    return {
        "loaded_cargos": [
            {
                "length": 100,
                "width": 100,
                "height": 100,
                "weight": 100,
                "coordinates": [
                    {
                        "x": 0,
                        "y": 0
                    },
                    {
                        "x": 0,
                        "y": 100
                    },
                    {
                        "x": 100,
                        "y": 0
                    },
                    {
                        "x": 100,
                        "y": 100
                    }
                ]
            },
            {
                "length": 100,
                "width": 100,
                "height": 100,
                "weight": 100,
                "coordinates": [
                    {
                        "x": 0,
                        "y": 105
                    },
                    {
                        "x": 0,
                        "y": 205
                    },
                    {
                        "x": 100,
                        "y": 105
                    },
                    {
                        "x": 100,
                        "y": 205
                    }
                ]
            },
            {
                "length": 100,
                "width": 100,
                "height": 100,
                "weight": 100,
                "coordinates": [
                    {
                        "x": 0,
                        "y": 210
                    },
                    {
                        "x": 0,
                        "y": 310
                    },
                    {
                        "x": 100,
                        "y": 210
                    },
                    {
                        "x": 100,
                        "y": 310
                    }
                ]
            },
            {
                "length": 100,
                "width": 100,
                "height": 100,
                "weight": 100,
                "coordinates": [
                    {
                        "x": 0,
                        "y": 315
                    },
                    {
                        "x": 0,
                        "y": 415
                    },
                    {
                        "x": 100,
                        "y": 315
                    },
                    {
                        "x": 100,
                        "y": 415
                    }
                ]
            }
        ],
        "denied": []
    }


@pytest.fixture
def test_data_2():
    return [
        {
            "length": 550,
            "width": 100,
            "height": 100,
            "weight": 100
        },
        {
            "length": 100,
            "width": 550,
            "height": 100,
            "weight": 100
        },
        {
            "length": 100,
            "width": 100,
            "height": 350,
            "weight": 100
        },
        {
            "length": 100,
            "width": 100,
            "height": 100,
            "weight": 1050
        }
    ]


@pytest.fixture
def expected_result_2():
    return {
        "loaded_cargos": [],
        "denied": [
            {
                "length": 100,
                "width": 100,
                "height": 100,
                "weight": 1050
            },
            {
                "length": 550,
                "width": 100,
                "height": 100,
                "weight": 100
            },
            {
                "length": 100,
                "width": 550,
                "height": 100,
                "weight": 100
            },
            {
                "length": 100,
                "width": 100,
                "height": 350,
                "weight": 100
            }
        ]
    }


@pytest.fixture()
def test_data_3():
    return [
        {
            "length": 100,
            "width": 100,
            "height": 100,
            "weight": 320
        },
        {
            "length": 100,
            "width": 100,
            "height": 100,
            "weight": 300
        },
        {
            "length": 100,
            "width": 100,
            "height": 100,
            "weight": 310
        },
        {
            "length": 100,
            "width": 100,
            "height": 100,
            "weight": 350
        }
    ]


@pytest.fixture
def expected_result_3():
    return {
        "loaded_cargos": [
            {
                "length": 100,
                "width": 100,
                "height": 100,
                "weight": 350,
                "coordinates": [
                    {
                        "x": 0,
                        "y": 0
                    },
                    {
                        "x": 0,
                        "y": 100
                    },
                    {
                        "x": 100,
                        "y": 0
                    },
                    {
                        "x": 100,
                        "y": 100
                    }
                ]
            },
            {
                "length": 100,
                "width": 100,
                "height": 100,
                "weight": 320,
                "coordinates": [
                    {
                        "x": 0,
                        "y": 105
                    },
                    {
                        "x": 0,
                        "y": 205
                    },
                    {
                        "x": 100,
                        "y": 105
                    },
                    {
                        "x": 100,
                        "y": 205
                    }
                ]
            },
            {
                "length": 100,
                "width": 100,
                "height": 100,
                "weight": 310,
                "coordinates": [
                    {
                        "x": 0,
                        "y": 210
                    },
                    {
                        "x": 0,
                        "y": 310
                    },
                    {
                        "x": 100,
                        "y": 210
                    },
                    {
                        "x": 100,
                        "y": 310
                    }
                ]
            }
        ],
        "denied": [
            {
                "length": 100,
                "width": 100,
                "height": 100,
                "weight": 300
            }
        ]
    }


@pytest.fixture
def test_data_4():
    return [
        {
            "length": 300,
            "width": 100,
            "height": 100,
            "weight": 100
        },
        {
            "length": 300,
            "width": 100,
            "height": 100,
            "weight": 100
        },
        {
            "length": 300,
            "width": 100,
            "height": 100,
            "weight": 100
        },
        {
            "length": 300,
            "width": 100,
            "height": 100,
            "weight": 100
        }
    ]


@pytest.fixture
def expected_result_4():
    return {
        "loaded_cargos": [
            {
                "length": 300,
                "width": 100,
                "height": 100,
                "weight": 100,
                "coordinates": [
                    {
                        "x": 0,
                        "y": 0
                    },
                    {
                        "x": 0,
                        "y": 300
                    },
                    {
                        "x": 100,
                        "y": 0
                    },
                    {
                        "x": 100,
                        "y": 300
                    }
                ]
            },
            {
                "length": 300,
                "width": 100,
                "height": 100,
                "weight": 100,
                "coordinates": [
                    {
                        "x": 0,
                        "y": 305
                    },
                    {
                        "x": 0,
                        "y": 605
                    },
                    {
                        "x": 100,
                        "y": 305
                    },
                    {
                        "x": 100,
                        "y": 605
                    }
                ]
            },
            {
                "length": 300,
                "width": 100,
                "height": 100,
                "weight": 100,
                "coordinates": [
                    {
                        "x": 0,
                        "y": 610
                    },
                    {
                        "x": 0,
                        "y": 910
                    },
                    {
                        "x": 100,
                        "y": 610
                    },
                    {
                        "x": 100,
                        "y": 910
                    }
                ]
            }
        ],
        "denied": [
            {
                "length": 300,
                "width": 100,
                "height": 100,
                "weight": 100
            }
        ]
    }
