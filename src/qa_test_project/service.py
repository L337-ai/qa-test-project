from qa_test_library.home.test import HomeTest


class LibraryService:
    def get_summary(self, items: list[HomeTest]) -> dict:
        return {
            "count": len(items),
            "names": [item.name for item in items],
            "labels": [item.label for item in items],
        }

    def summarize(self) -> str:
        return "ok"

    def ping(self) -> str:
        return "pong"
