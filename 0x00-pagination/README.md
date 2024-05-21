# 0x00-pagination

This project covers how to paginate a dataset with simple page and page_size parameters, how to paginate a dataset with hypermedia metadata, and how to paginate in a deletion-resilient manner.

## How to paginate a dataset with simple page and page_size parameters

To paginate a dataset with simple page and page_size parameters, you can use the `index_range` function from the `utils` module. This function takes the list to paginate, the page number, and the page size as arguments, and returns a tuple containing the start and end indexes for the requested page.

## How to paginate a dataset with hypermedia metadata

To paginate a dataset with hypermedia metadata, you can use the `get_hyper` function from the `utils` module. This function takes the list to paginate, the page number, and the page size as arguments, and returns a dictionary containing the requested page data and metadata such as the total number of pages, the current page, and the next and previous page URLs.

## How to paginate in a deletion-resilient manner

To paginate in a deletion-resilient manner, you can use the `DataSet` class from the `utils` module. This class provides a way to paginate a dataset while ensuring that deleted items are properly handled. It has methods for adding, removing, and retrieving items, as well as for paginating the dataset with hypermedia metadata.
