def furthest(cache, future_requests):
    furthest = cache[0]

    # find page in cache that's furthest away in future requests
    for i in range(len(cache)):
        if cache[i] in future_requests:
            try:
                if future_requests.index(cache[i]) > future_requests.index(furthest):
                    furthest = cache[i]
            except:
                pass
        else:
            return cache[i]
    return furthest

instances = int(input())
page_faults_list = []
for i in range(instances):
    cache = []
    page_faults = 0
    cache_size = int(input())
    num_page_requests = int(input())
    page_requests = [int(page_request) for page_request in input().split(" ")]
    for i in range(num_page_requests):
        # if cache is full and page request not already in cache, replace furthest page
        if len(cache) == cache_size and page_requests[i] not in cache:
            furthest_page = furthest(cache, page_requests[i:])
            cache[cache.index(furthest_page)] = page_requests[i]
            page_faults += 1

        # if page is not in cache, add it
        elif page_requests[i] not in cache:
            cache.append(page_requests[i])
            page_faults += 1

        # if page is in cache, do nothing
        else:
            pass
    page_faults_list.append(page_faults)
for page_faults in page_faults_list:
    print(str(page_faults))
