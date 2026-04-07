def get_task(name: str):
    datasets = {
        "easy": {
            "emails": [
                {"id": "1", "subject": "Campus movie night", "body": "Join us Friday at 8PM", "sender": "club@uni.edu", "timestamp": "2026-04-06"},
                {"id": "2", "subject": "Math assignment due", "body": "Submit before April 10 23:59", "sender": "math@uni.edu", "timestamp": "2026-04-06"},
            ]
        },
        "medium": {
            "emails": [
                {"id": "1", "subject": "AI assignment due", "body": "Deadline April 10 23:59", "sender": "ai@uni.edu", "timestamp": "2026-04-06"},
                {"id": "2", "subject": "OS assignment", "body": "Submit before April 12", "sender": "os@uni.edu", "timestamp": "2026-04-06"},
                {"id": "3", "subject": "Internship application deadline", "body": "Apply before April 11", "sender": "career@uni.edu", "timestamp": "2026-04-06"},
                {"id": "4", "subject": "Scholarship renewal form", "body": "Deadline April 15", "sender": "aid@uni.edu", "timestamp": "2026-04-06"},
                {"id": "5", "subject": "Music club event", "body": "Open mic tomorrow night", "sender": "club@uni.edu", "timestamp": "2026-04-06"},
            ]
        },
        "hard": {
            "emails": [
                {"id": "1", "subject": "Networks exam", "body": "April 8 9AM room B12", "sender": "admin@uni.edu", "timestamp": "2026-04-06"},
                {"id": "2", "subject": "Exam moved", "body": "Networks exam moved to April 8 2PM room C3", "sender": "admin@uni.edu", "timestamp": "2026-04-06"},
                {"id": "3", "subject": "Room change", "body": "Final room D5", "sender": "admin@uni.edu", "timestamp": "2026-04-06"},
                {"id": "4", "subject": "AI deadline", "body": "Project due April 8", "sender": "ai@uni.edu", "timestamp": "2026-04-06"},
                {"id": "5", "subject": "OS deadline", "body": "Report due April 8", "sender": "os@uni.edu", "timestamp": "2026-04-06"},
                {"id": "6", "subject": "Fee payment deadline", "body": "Pay before April 9", "sender": "finance@uni.edu", "timestamp": "2026-04-06"},
                {"id": "7", "subject": "Reminder AI deadline", "body": "Same April 8", "sender": "ai@uni.edu", "timestamp": "2026-04-06"},
                {"id": "8", "subject": "Reminder AI deadline", "body": "Same April 8", "sender": "ai@uni.edu", "timestamp": "2026-04-06"},
                {"id": "9", "subject": "Lab slot A", "body": "April 10 10AM", "sender": "lab@uni.edu", "timestamp": "2026-04-06"},
                {"id": "10", "subject": "Lab slot B", "body": "April 10 10AM", "sender": "lab@uni.edu", "timestamp": "2026-04-06"},
            ]
        },
    }
    return datasets[name]