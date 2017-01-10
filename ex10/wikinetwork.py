from ex10.article import Article
from copy import deepcopy

TITLE = 0
NEIGHBOR = 1



def read_article_links(file_name):
    """
    Gets a list of articles
    :param file_name:  a neme of the article list file (withing the foler)
    :return: a list of tuples such as (article, article_link)
    """
    article_list = []
    f = open(file_name, 'r')
    for line in f:
        stripped_line = line.strip()
        tab_index = stripped_line.find('\t')
        tuple_to_add = (stripped_line[0:tab_index],stripped_line[tab_index+1:])
        article_list.append(tuple_to_add)
    return article_list


class WikiNetwork:

    def __init__(self, link_list):
        article_dic = {}
        for link in link_list:
            title = link[TITLE]
            neighbor = link[NEIGHBOR]
            if neighbor not in article_dic:
                article_dic[neighbor] = Article(neighbor)
            elif title not in article_dic:
                new_article = Article(title)
                new_article.add_neighbor(article_dic[neighbor])
                article_dic[title] = new_article
            else:
                article_dic[title].add_neighbor(article_dic[neighbor])
        self.__articles = article_dic

    def __contains__(self, title):
        if title in self.__articles:
            return True
        else:
            return False

    def __len__(self):
        return len(self.__articles)

    def __repr__(self):
        string_dict = {}
        for title in self.__articles:
            # places article repr instead of articles
            string_dict[title] = self.__articles[title]
        return str(string_dict)

    def __getitem__(self, title):
        if title in self:
            return self.__articles[title]

    def update_network(self, link_list):
        for link in link_list:
            if link[TITLE] in self:
                new_article = Article(link[TITLE])
                new_article.add_neighbor(link[NEIGHBOR])
                self.__articles[link[TITLE]] = new_article
            else:
                self.__articles[link[TITLE]].add_neighbor(link[NEIGHBOR])

    def get_titles(self):
        return list(self.__articles.keys())

