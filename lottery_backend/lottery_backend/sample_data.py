data = {
    "performances": [
        {
            "performance_id": 1,
            "performance_name": "Performance 1",
            "date": "2022-01-01",
            "time": "20:00",
            "available_tickets": 10
        },
        {
            "performance_id": 2,
            "performance_name": "Performance 2",
            "date": "2022-01-02",
            "time": "15:00",
            "available_tickets": 5
        },
        {
            "performance_id": 3,
            "performance_name": "Performance 3",
            "date": "2022-01-02",
            "time": "20:00",
            "available_tickets": 10
        }
    ],
    "lottery_entries": [
        {
            "user_id": 123,
            "username": "User 1",
            "performace_name": "Performance 1",
            'no_of_tickets': 10,
            'show_time': '2022-01-05T09:00:00Z',
            "entry_time": "2022-01-01T09:00:00Z"
        },
        {
            "user_id": 456,
            "username": "User 2",
            "performance_id": 3,
            'performace_name': "Performance 3",
            'no_of_tickets': 5,
            'show_time': '2022-01-09T09:00:00Z',
            "entry_time": "2022-01-01T10:00:00Z"
        },
        {
            "user_id": 789,
            "username": "User 3",
            "performance_id": 2,
            'performace_name': "Performance 2",
            'no_of_tickets': 20,
            'show_time': '2022-01-10T09:00:00Z',
            "entry_time": "2022-01-02T09:00:00Z"
        }
    ],
    "winners": [
        {
            "user_id": 123,
            "performance_id": 1,
            "winning_time": "2022-01-01T12:00:00Z"
        },
        {
            "user_id": 456,
            "performance_id": 1,
            "winning_time": "2022-01-01T12:15:00Z"
        }
    ]
}