class Article:
    def __init__(self, article_title):
        self.__title = article_title
        self.__neighbors = []
        pass

    def __repr__(self):
        return '('+str(self.get_title())+','\
               +str(self.get_neighbors_title())+')'

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
            self.__neighbors.append(neighbor)

    def get_neighbors(self):
        return self.__neighbors

    def get_neighbors_title(self):
        neighbors_title_list = []
        for neighbor in self.__neighbors:
            neighbors_title_list.append(neighbor.get_title())
        return neighbors_title_list

