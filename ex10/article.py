class Article:
    def __init__(self, article_title):
        self.__title = article_title
        self.__neighbors = set()
        pass

    def __repr__(self):
        title = self.get_title()
        neighbors_titles = str(self.__get_neighbors_title())
        return '('+title+','+neighbors_titles+')'

    def __len__(self):
        return len(self.__neighbors)

    def __contains__(self, article):
        if article in self.__neighbors:
            return True
        else:
            return False

    def get_title(self):
        return self.__title

    def add_neighbor(self, neighbor):
        if neighbor not in self:
            self.__neighbors.add(neighbor)

    def get_neighbors(self):
        return self.__neighbors

    def __get_neighbors_title(self):
        neighbors_title_list = []
        for neighbor in self.__neighbors:
            neighbors_title_list.append(neighbor.get_title())
        return neighbors_title_list
