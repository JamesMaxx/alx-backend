# Project: 0x00. Pagination

This project covers the implementation of pagination, a technique used in web development to divide large data sets into smaller, more manageable chunks. Pagination helps improve website performance and user experience by loading only a portion of the data at a time.

## Resources

### Read or watch:

- [REST API Design: Pagination](https://intranet.alxswe.com/rltoken/7Kdzi9CH1LdSfNQ4RaJUQw)
- [HATEOAS](https://intranet.alxswe.com/rltoken/tfzcEbTSdMYSYxsspJH_oA)

## Tasks

| Task                                        | File                                                               |
| ------------------------------------------- | ------------------------------------------------------------------ |
| 0. Simple helper function                   | [0-simple_helper_function.py](./0-simple_helper_function.py)       |
| 1. Simple pagination                        | [1-simple_pagination.py](./1-simple_pagination.py)                 |
| 2. Hypermedia pagination                    | [2-hypermedia_pagination.py](./2-hypermedia_pagination.py)         |
| 3. Deletion-resilient hypermedia pagination | [3-hypermedia_del_pagination.py](./3-hypermedia_del_pagination.py) |

### 0. Simple helper function

This task involves implementing a simple helper function to calculate the index range for a given page and page size.

### 1. Simple pagination

In this task, you will implement a simple pagination system using the helper function from the previous task.

### 2. Hypermedia pagination

This task focuses on implementing hypermedia pagination, which involves adding links to the pagination metadata to enable navigation between pages.

### 3. Deletion-resilient hypermedia pagination

Building upon the previous task, this task aims to make the hypermedia pagination system resilient to data deletions by handling the case where the requested page contains fewer items than expected due to deletions.
