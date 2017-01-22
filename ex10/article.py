class Article:
    """
    A class for an article
    """
    def __init__(self, article_title):
        """

        :param article_title: article title
        collection : all articles this article reference TO
        money : starting money for page rank algo
        references : all articles this article has a reference FROM
        """
        self.__title = article_title
        self.__collection = []

    def __repr__(self):
        title = self.get_title()
        neighbors_titles = str(self.__get_neighbors_title())
        return '(\''+title+'\', '+neighbors_titles+')'

    def __len__(self):
        return len(self.__collection)

    def __contains__(self, article):
        if article in self.__collection:
            return True
        else:
            return False

    def get_title(self):
        """
        :return: article title, a string
        """
        return self.__title

    def add_neighbor(self, neighbor):
        """
        Adds a neighbor, if neighbor is there already, does nothing
        :param neighbor: article object to add as neighbor
        """
        if neighbor not in self:
            self.__collection.append(neighbor)

    def get_neighbors(self):
        """
        :return: a list with all of current article neighbors(Article objects)
        """
        return self.__collection

    def __get_neighbors_title(self):
        """
        :return: a list with all the titles(strings) of this article neighbors
        """
        neighbors_title_list = []
        for neighbor in self.__collection:
            neighbors_title_list.append(neighbor.get_title())
        return neighbors_title_list

