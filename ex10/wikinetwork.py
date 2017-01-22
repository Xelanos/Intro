from article import Article

TITLE = 0
NEIGHBOR = 1
ARTICLE = 1
MONEY = 0


def read_article_links(file_name):
    """
    Gets a list of articles
    :param file_name:  a name of the article list file (withing the folder)
    :return: a list of tuples such as (article, article_link)
    """
    article_list = []
    f = open(file_name, 'r')
    for line in f:
        stripped_line = line.strip()
        tab_index = stripped_line.find('\t')
        tuple_to_add = (stripped_line[0:tab_index],stripped_line[tab_index+1:])
        article_list.append(tuple_to_add)
    f.close()
    return article_list


class WikiNetwork:
    """
    A class which represents a wiki network of articles and links
    """

    def __init__(self, link_list):
        """
        :param link_list: a link list as described in read_article_links
        self.__collection : a dictionary of network collection
        self.__friends : cache for recursive memorization to follow
        """
        collection = {}
        for link in link_list:
            title = link[TITLE]
            neighbor_title = link[NEIGHBOR]
            if neighbor_title not in collection:
                collection[neighbor_title] = {}
                collection[neighbor_title]['object'] = Article(neighbor_title)
                collection[neighbor_title]['refs'] = set()
                collection[neighbor_title]['money'] = 1
            if title not in collection:
                collection[title] = {}
                collection[title]['object'] = Article(title)
                collection[title]['refs'] = set()
                collection[title]['money'] = 1
            collection[title]['object']\
                .add_neighbor(collection[neighbor_title]['object'])
            collection[neighbor_title]['refs'].add(collection[title]['object'])

        self.__collection = collection
        self.__friends = set()

    def __contains__(self, title):
        if title in self.__collection:
            return True
        else:
            return False

    def __len__(self):
        return len(self.__collection)

    def __repr__(self):
        string_dict = {}
        for title in self.__collection:
            # places article repr instead of articles
            string_dict[title] = self[title]
        return str(string_dict)

    def __getitem__(self, title):
        if title in self:
            return self.__collection[title]['object']

    def update_network(self, link_list):
        """
        method which updates the network according to new link list provided
        :param link_list: a list of links
        """
        for link in link_list:
            title = link[TITLE]
            neighbor_title = link[NEIGHBOR]
            if neighbor_title not in self:
                self.__collection[neighbor_title] = {}
                self.__collection[neighbor_title]['object'] =\
                    Article(neighbor_title)
                self.__collection[neighbor_title]['refs'] = set()
                self.__collection[neighbor_title]['money'] = 1
            if title not in self:
                self.__collection[title] = {}
                self.__collection[title]['object'] = Article(title)
                self.__collection[title]['refs'] = set()
                self.__collection[title]['money'] = 1
            self.__collection[title]['object']\
                .add_neighbor(self[neighbor_title])
            self.__collection[neighbor_title]['refs'].add(self[title])

    def get_articles(self):
        """
        :return: a list of all article objects in network collection
        """
        article_list = []
        for title in self.__collection:
            article_list.append(self.__collection[title]['object'])
        return article_list

    def get_titles(self):
        """
        :return: a list of all the titles(string) of articles in
        network collection
        """
        return list(self.__collection.keys())

    def __list_sorter(self, list_to_sort):
        """
        sorts a list of tuples that follows (float,str)
        :param list_to_sort: a list of tuples that follows (float,str)
        :return: a sorted list first by float value from big to small
        and then by alphabetical order from small to big
        """
        # secondary sorting, by alphabetical, small to big
        alph_sort = sorted(list_to_sort, key=lambda element: element[1])
        # primary sorting, by value, big to small
        value_sort = sorted(alph_sort, key=lambda element: element[0],
                            reverse=True)
        return value_sort

    def __get_references(self, article):
        """
        :param article: article object
        :return: a set of the article references
        """
        title = article.get_title()
        return self.__collection[title]['refs']

    def __get_money(self, article):
        """
        :param article: article object
        :return: articles current money
        """
        title = article.get_title()
        return self.__collection[title]['money']

    def __set_money(self,article_title,amount):
        """
        changes article money to amount
        :param article_title: article title
        :param amount: amount to change money too
        """
        self.__collection[article_title]['money'] = amount


    def page_rank(self, iters, d=0.9):
        """
        runs page rank algorithm on all articles in network
        :param iters: number of iterations the algorithm should do(MUST be int)
        :param d: percentage of money each article gives its outgoing link
        :return: a list of article objects, order by their page rank
        from lowest to highest
        """
        if iters == 0:
            return sorted(self.get_titles())
        for k in range(iters):
            excess = 1 - d
            rank_list = []
            # calculate sum for current iteration
            for article in self.get_articles():
                partial_sum = 0
                # summing all the money gotten from other articles
                if len(self.__get_references(article)) > 0:
                    for reference in self.__get_references(article):
                        partial_sum += \
                            (self.__get_money(reference) / len(reference))
                money_gotten = (d * partial_sum) + excess
                article_rank = (money_gotten, article.get_title())
                rank_list.append(article_rank)
            # updating money for each article in preparation for next iteration
            # must be done AFTER calculation, to not affect it
            for ranking in rank_list:
                self.__set_money(ranking[ARTICLE], ranking[MONEY])
        sorted_rank_list = self.__list_sorter(rank_list)
        return [rank[1] for rank in sorted_rank_list]

    def __jaccard_indexer(self, article_1, article_2):
        """
        :param article_1: Article object
        :param article_2: Article object
        :return: the jaccard index between both articles
        """
        article_1_collection = set(article_1.get_neighbors())
        article_2_collection = set(article_2.get_neighbors())
        intersection = article_1_collection & article_2_collection
        union = article_1_collection | article_2_collection
        jaccard_index = len(intersection) / len(union)
        return jaccard_index

    def jaccard_index(self, article_title):
        """
        index all articles in collection by jaccard index, in relation to
        inputted article title
        :param article_title: a string
        :return: a list of all article titles in collection, ordered by their
        jaccard index in in relation to inputted article title
        """
        if article_title not in self:
            return None
        elif len(self[article_title]) == 0:
            return None
        else:
            jaccard_list = []
            for article in self.get_articles():
                jac_indx = self.__jaccard_indexer(self[article_title], article)
                article_jaccard = (jac_indx, article.get_title())
                jaccard_list.append(article_jaccard)
            sorted_jaccard_list = self.__list_sorter(jaccard_list)
            return [jac[1] for jac in sorted_jaccard_list]

    def travel_path_iterator(self, article_title):
        """
        A generator that travels along legit moves from article to article.
        choosing the next legit move by the node that has the most incoming
        links.
        :param article_title: starting article title
        :return: for each next : the title of the next article in the path
        """
        if article_title not in self:
            return
        else:
            # first title is of course the function parameter
            current_article = self[article_title]
            yield current_article.get_title()
            # generator ends when reaching a node with 0 inc links
            while len(current_article) > 0:
                # now checking which neighbors has the most incoming links
                next_node_candidates = []
                max_links = 0
                for neighbor in current_article.get_neighbors():
                    entry_level = len(self.__get_references(neighbor))
                    if entry_level > max_links:
                        next_node_candidates = []
                        max_links = entry_level
                        next_node_candidates.append(neighbor.get_title())
                    elif entry_level == max_links:
                        next_node_candidates.append(neighbor.get_title())
                    else:
                        continue
                next_node = min(next_node_candidates)
                current_article = self[next_node]
                yield current_article.get_title()

    def ___friends_helper(self, article_title, depth):
        """
        recursion function of freind by depth.
        using self.__friends for memorization
        :param article_title: stating article title
        :param depth: depth required
        :return: a set of article objects
        """
        if depth <= 0:
            self.__friends.add(self[article_title])
        else:
            self.___friends_helper(article_title, depth - 1)
            current_depth_neighbors = set()
            for article in self.__friends:
                current_depth_neighbors |= set(article.get_neighbors())
            self.__friends |= current_depth_neighbors

    def friends_by_depth(self, article_title, depth):
        """
        :param article_title: starting article titles
        :param depth: required depth
        :return: a list of all the titles of friends of 'depth' from
         starting article
        """
        if article_title not in self:
            return
        self.__friends = set()
        self.___friends_helper(article_title, depth)
        return [article.get_title() for article in self.__friends]
