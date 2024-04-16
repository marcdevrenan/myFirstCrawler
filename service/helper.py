class Helper:
    @staticmethod
    def format_categories(categories):
        categories = [category for category in categories if category.lower() not in ["more", "all"]]
        return categories
