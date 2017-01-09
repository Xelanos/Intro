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



